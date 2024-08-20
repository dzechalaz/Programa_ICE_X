import serial
import time

# Mapeo de los valores de monedas en pesos según las posiciones del string de respuesta
MONEDA_VALORES = {
    '2': 1,   # 52 representa 1 peso
    '3': 2,   # 53 representa 2 pesos
    '4': 5,   # 54 representa 5 pesos
    '5': 10   # 55 representa 10 pesos
}

# Configuración global y funciones auxiliares
class GlobalConfig:
    def __init__(self):
        self.coin_alternative_payout = True  # Configuración según sea necesario
        self.coin_scaling_factor = .5         # Ajustar según sea necesario
        self.coin_timeout = 1
        self.total_money = 0  # Agregamos un total de dinero aquí
        self.previous_state = None  # Para guardar el estado anterior del monedero
        self.mdb_com_buffer = ""  # Buffer serial del puerto serial al cual se conecta el dispositivo MDB
        self.mdb_status = 255  # No hay mensaje MDB
        self.monedero_mdb_ispolled = False  # El monedero MDB no ha sido polleado

g = GlobalConfig()

def mdb_add_crc(_linput):
    _lcrc = 0
    for _li in range(0, len(_linput)):
        _lcrc += _linput[_li]
    _lcrc_lo = _lcrc & 0xFF
    return _lcrc_lo

def mdb_hex_dump(_lstring):
    print(" ".join(f"{byte:02x}" for byte in _lstring))

def mdb_send_command(command, timeout, response_length):
    ser.timeout = timeout
    ser.write(command)
    response = ser.read(response_length)
    return response != b'', response

def mdb_coin_change(change_value):
    if not g.coin_alternative_payout:
        print("Cambio alternativo deshabilitado")
        return False

    try:
        change_value = int(change_value)
        change_value = int(change_value / g.coin_scaling_factor)
        change_value = change_value & 0xFF
        command = [0x0F, 0x02, change_value]
        command.append(mdb_add_crc(command))
        print("Mensaje al dispositivo")
        mdb_hex_dump(command)
        result, response = mdb_send_command(command, g.coin_timeout, 40)
        if result:
            print("Respuesta del dispositivo")
            mdb_hex_dump(response)
            if response[0] == 0x00:
                print("Cambio exitoso")
                return True
            else:
                print("Error al dar cambio")
                return False
        else:
            print("No se recibió respuesta")
            return False
    except ValueError:
        print("Valor no numérico para el cambio")
        return False

# Función para enviar comando y recibir respuesta
def send_command(ser, command, expected_response_length=10):
    ser.write(command)
    time.sleep(0.1)
    response = ser.read(expected_response_length)
    return response

# Función para habilitar el aceptador de monedas
def enable_coin_acceptor(ser):
    enable_command = bytes([0x0C, 0xFF, 0xFF, 0xFF, 0xFF])
    response = send_command(ser, enable_command, expected_response_length=1)
    print(f"Comando enviado: {enable_command.hex()}")
    print(f"Respuesta recibida: {response.hex()}")
    return response

# Función para deshabilitar el aceptador de monedas
def disable_coin_acceptor(ser):
    disable_command = bytes([0x0C, 0x00, 0x00, 0x00, 0x00])
    response = send_command(ser, disable_command, expected_response_length=1)
    print(f"Comando enviado: {disable_command.hex()}")
    print(f"Respuesta recibida: {response.hex()}")
    return response

# Función para hacer poll del aceptador de monedas
def poll_coin_acceptor(ser):
    poll_command = bytes([0x0B])
    response = send_command(ser, poll_command, expected_response_length=40)  # Leer más bytes para obtener toda la respuesta
    return response

# Función para analizar los datos del buffer y actualizar el estado del monedero
def parse_mdb_buffer():
    print(f"Parsing buffer: {g.mdb_com_buffer}")
    while True:
        if len(g.mdb_com_buffer) == 0:
            return
        
        if g.mdb_com_buffer.startswith("00 ") and g.mdb_com_buffer[3:5] == chr(0x0D) + chr(0x0A):
            g.monedero_mdb_ispolled = True
            g.mdb_com_buffer = g.mdb_com_buffer[5:]
        
        elif g.mdb_com_buffer.startswith("08") and len(g.mdb_com_buffer) >= 10:
            if g.mdb_com_buffer[8:10] == chr(0x0D) + chr(0x0A):
                coin_type = g.mdb_com_buffer[4]
                print(f"Coin type detected: {coin_type}")
                if coin_type in MONEDA_VALORES:
                    g.total_money += MONEDA_VALORES[coin_type]
                    print(f"Moneda aceptada: {MONEDA_VALORES[coin_type]} peso(s)")
                    print(f"Total dinero en el monedero: {g.total_money} pesos")
                else:
                    print(f"Coin type {coin_type} no reconocido en MONEDA_VALORES.")
                g.mdb_com_buffer = g.mdb_com_buffer[10:]
            else:
                break
        else:
            g.mdb_com_buffer = g.mdb_com_buffer[1:]

def mdb_read_and_parse():
    while True:
        if ser.in_waiting > 0:
            g.mdb_com_buffer += ser.read(ser.in_waiting).decode('ascii', errors='ignore')
            parse_mdb_buffer()
        time.sleep(0.1)

# Funciones para cashless

def mdb_cashless_vend_request(amount):
    amount_high = (amount >> 8) & 0xFF
    amount_low = amount & 0xFF
    command = [0x13, 0x00, amount_high, amount_low, 0x00]
    command.append(mdb_add_crc(command))
    print("Solicitud de venta cashless al dispositivo")
    mdb_hex_dump(command)
    result, response = mdb_send_command(command, g.coin_timeout, 40)
    if result:
        print("Respuesta del dispositivo")
        mdb_hex_dump(response)
        if response[0] == 0x00:
            print("Venta cashless solicitada exitosamente")
            return True
        else:
            print("Error al solicitar venta cashless")
            return False
    else:
        print("No se recibió respuesta")
        return False

def mdb_cashless_vend_cancel():
    command = [0x13, 0x01]
    command.append(mdb_add_crc(command))
    print("Cancelación de venta cashless al dispositivo")
    mdb_hex_dump(command)
    result, response = mdb_send_command(command, g.coin_timeout, 40)
    if result:
        print("Respuesta del dispositivo")
        mdb_hex_dump(response)
        if response[0] == 0x00:
            print("Venta cashless cancelada exitosamente")
            return True
        else:
            print("Error al cancelar venta cashless")
            return False
    else:
        print("No se recibió respuesta")
        return False

def mdb_cashless_vend_complete():
    command = [0x13, 0x02]
    command.append(mdb_add_crc(command))
    print("Completar venta cashless al dispositivo")
    mdb_hex_dump(command)
    result, response = mdb_send_command(command, g.coin_timeout, 40)
    if result:
        print("Respuesta del dispositivo")
        mdb_hex_dump(response)
        if response[0] == 0x00:
            print("Venta cashless completada exitosamente")
            return True
        else:
            print("Error al completar venta cashless")
            return False
    else:
        print("No se recibió respuesta")
        return False

def connect_to_mdb_rs232(port, baudrate=9600, timeout=1):
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Conectado al puerto {port} a {baudrate} baudios.")
        return ser
    except serial.SerialException as e:
        print(f"No se pudo conectar al puerto {port}: {e}")
        return None
