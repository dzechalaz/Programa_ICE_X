def Sub_inicio(arm):
    import time

######################################### Posición segura ##############################################      

    while not arm.get_cgpio_digital(13)[1] == 0:
            t1 = time.monotonic()
            arm.set_cgpio_digital(3, 1, delay_sec=0)
                
            interval = time.monotonic() - t1
            if interval < 0.01:
               time.sleep(0.01 - interval)
    arm.set_cgpio_digital(3, 0, delay_sec=0)

    tcp_speed = 20
    angle_speed =20

    pos_acual_tub = ()
    pos_acual_tub = arm.get_servo_angle(servo_id=1,is_radian=False)
    pos_actual_array = pos_acual_tub[1]

    print(pos_actual_array)

    if arm.get_position(is_radian=False) == (0, [262.4151, 2.432852, 570.889648, 178.586934, -0.537205, 1.039804]):
       arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed,  wait=False, radius=0.0)

    else:
       if arm.position[2] < 100:
        pos_actual = arm.position
        pos_actual[2] = 200
        arm.set_position(*pos_actual, speed=tcp_speed, radius=0.0, wait=True)
       arm.set_servo_angle(angle=[pos_acual_tub[1], -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed,  wait=False, radius=0.0)
       arm.set_servo_angle(angle=[-129.4, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed,  wait=False, radius=0.0)
       arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed,  wait=False, radius=0.0)

    
