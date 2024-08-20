def Sub_C_Helado_2(arm):
    import time   
 
    ######################################################  MAIN  ###############################################################

    angle_speed = 75
   # arm.set_cgpio_digital(10, 1, delay_sec=0)
           
    arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed, wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-184.8, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
           
    arm.set_cgpio_digital(4, 1, delay_sec=0)
    
    arm.set_servo_angle(angle=[-135.7, -56.6, -0.2, -179.9, 31.1, 0.0], speed=angle_speed, wait=False, radius=0.0)
           
    tcp_speed = 85
    arm.set_position(*[-202.3, -304.5, 318, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)
           
    tcp_speed = 45
    arm.set_position(*[-202.3, -304.5, 338.4, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=True)
        
    arm.set_cgpio_digital(10, 0, delay_sec=0)
           
    time.sleep(1)
    tcp_speed = 20
    arm.set_position(*[-202.3, -304.5, 301.0, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
           
    arm.set_cgpio_digital(4, 0, delay_sec=0)
    
    arm.set_cgpio_digital(9, 1, delay_sec=0)
    
    arm.set_position(*[-202.3, -304.5, 318.3, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
    
    arm.set_position(*[-202.3, -304.5, 235.8, -76.6, 87.8, 106.0], speed=tcp_speed, radius=0.0, wait=False)
    
    tcp_speed = 75
    arm.set_position(*[-154.0, -148.4, 266.0, 176.1, 87.9, 41.7], speed=tcp_speed, radius=0.0, wait=False)
           
    arm.set_cgpio_digital(9, 0, delay_sec=0)
