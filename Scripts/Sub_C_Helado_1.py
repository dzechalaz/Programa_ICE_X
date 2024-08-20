def Sub_C_Helado_1(arm):
    import time

    #########################################  MAIN  ###########################################################

    angle_speed = 75
   # arm.set_cgpio_digital(14, 1, delay_sec=0)
            
    arm.set_cgpio_digital(4, 1, delay_sec=0)
            
    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
            
    tcp_speed = 85
    arm.set_position(*[-202.3, -371.4, 312.5, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)
           
    tcp_speed = 40
    arm.set_position(*[-202.3, -373.4, 318, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)
           
    arm.set_cgpio_digital(14, 0, delay_sec=0)
            
    time.sleep(4)
    tcp_speed = 20
    arm.set_position(*[-202.3, -373.4, 270, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
            
    arm.set_cgpio_digital(4, 0, delay_sec=0)
           
    arm.set_cgpio_digital(15, 1, delay_sec=0)
            
    arm.set_position(*[-202.3, -373.4, 320, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
            
    arm.set_position(*[-202.3, -373.4, 235.8, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
           
    tcp_speed = 75
    arm.set_position(*[-154.0, -148.4, 266.0, 176.1, 87.9, 41.7], speed=tcp_speed, radius=0.0, wait=False)
            
    arm.set_cgpio_digital(15, 0, delay_sec=0)