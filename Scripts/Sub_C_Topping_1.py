def Sub_C_Topping_1(arm):
    import time

    #########################################  MAIN  #########################################

    angle_speed = 30
    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-184.8, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-191.3, -12.4, -1.6, -152.6, 78.5, -7.6], speed=angle_speed, wait=False, radius=0.0)
    
    tcp_speed = 70
    arm.set_position(*[-362.4, -20.0, 169.3, -53.3, 88.4, 94.5], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-362.4, -20.0, 235, -53.3, 88.4, 94.5], speed=tcp_speed, radius=0.0, wait=True)
    
    arm.set_cgpio_digital(13, 1, delay_sec=0)
    
    time.sleep(0.2)
    arm.set_cgpio_digital(13, 0, delay_sec=0)
    
    arm.set_position(*[-362.4, -20.0, 156.7, -53.3, 88.4, 94.5], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-227.7, 82.9, 169.3, -54.0, 88.4, 89.7], speed=tcp_speed, radius=0.0, wait=False)
