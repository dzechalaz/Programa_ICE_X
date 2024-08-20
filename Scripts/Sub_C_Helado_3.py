def Sub_C_Helado_3(arm):
    import time    

    ##################################  MAIN  ###################################################

    angle_speed = 75
    arm.set_cgpio_digital(11, 1, delay_sec=0)

    arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed, wait=False, radius=0.0)

    arm.set_servo_angle(angle=[-184.8, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)

    arm.set_cgpio_digital(4, 1, delay_sec=0)

    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed,  wait=False, radius=0.0)

    tcp_speed = 85
    arm.set_position(*[-202.3, -239.3, 312.5, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)

    tcp_speed = 40
    arm.set_position(*[-202.3, -239.3, 318, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)

    arm.set_cgpio_digital(11, 0, delay_sec=0)

    time.sleep(4)
    tcp_speed = 20
    arm.set_position(*[-202.3, -239.3, 290, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)

    arm.set_cgpio_digital(4, 0, delay_sec=0)

    arm.set_cgpio_digital(12, 1, delay_sec=0)

    arm.set_position(*[-202.3, -239.3, 320, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)

    time.sleep(2)
    arm.set_position(*[-202.3, -239.3, 265, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
    
    tcp_speed = 50

    arm.set_position(*[-202.3, -239.3, 300, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)

    tcp_speed = 75
    arm.set_position(*[-154.0, -148.4, 266.0, 176.1, 87.9, 41.7], speed=tcp_speed, radius=0.0, wait=False)

    arm.set_cgpio_digital(12, 0, delay_sec=0)
