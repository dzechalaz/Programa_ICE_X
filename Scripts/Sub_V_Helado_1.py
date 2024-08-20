def Sub_V_Helado_1(arm):
    import time

###################################################  MAIN  #############################################################3

    angle_speed = 75
    arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed,  wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-184.8, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed,  wait=False, radius=0.0)
    
    arm.set_cgpio_digital(14, 1, delay_sec=0)
    
    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed,  wait=False, radius=0.0)
    tcp_speed = 100
    
    arm.set_position(*[-255.0, -372.8, 286.4, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    tcp_speed = 40

    arm.set_position(*[-261.2, -372.8, 337.9, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_cgpio_digital(14, 0, delay_sec=0)
    
    arm.set_position(*[-261.2, -372.8, 335.9, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_cgpio_digital(4, 1, delay_sec=0)
    
    arm.set_cgpio_digital(14, 1, delay_sec=0)
    
    tcp_speed = 45
    arm.set_position(*[-255.0, -372.8, 300.0, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_cgpio_digital(14, 0, delay_sec=0)
    
    arm.set_position(*[-255.0, -372.8, 302.0, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    # remark
    arm.set_cgpio_digital(15, 1, delay_sec=0)
    
    tcp_speed = 5
    arm.set_position(*[-261.2, -372.8, 280.0, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_position(*[-261.2, -372.8, 305.0, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_cgpio_digital(4, 0, delay_sec=0)
    
    tcp_speed = 35
    arm.set_position(*[-261.2, -372.8, 250.0, -76.6, 87.8, 106.0], speed=tcp_speed,  radius=0.0, wait=False)
    
    tcp_speed = 80
    arm.set_position(*[-154.0, -148.4, 266.0, 176.1, 87.9, 41.7], speed=tcp_speed,  radius=0.0, wait=False)
    
    time.sleep(4)
    arm.set_cgpio_digital(15, 0, delay_sec=0)