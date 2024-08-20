def Sub_V_Topping_2(arm):
    import time

    ##############################  MAIN  #######################################

    angle_speed = 30
   
    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-184.8, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
    
    tcp_speed = 70

    arm.set_position(*[-227.7, 82.9, 169.3, -54.0, 88.4, 89.7], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-271.5, 168.9, 143.4, -53.3, 88.4, 81.1], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-271.5, 168.9, 231.2, -53.3, 88.4, 81.1], speed=tcp_speed, radius=0.0, wait=True)
    
   # arm.set_cgpio_digital(8, 1, delay_sec=0)
    
    time.sleep(0.5)
   # arm.set_cgpio_digital(8, 0, delay_sec=0)
    
    arm.set_position(*[-271.5, 168.9, 143.4, -53.3, 88.4, 81.1], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-227.7, 82.9, 169.3, -54.0, 88.4, 89.7], speed=tcp_speed, radius=0.0, wait=False)
    