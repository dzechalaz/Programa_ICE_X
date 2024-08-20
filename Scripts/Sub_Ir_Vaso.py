def Sub_Ir_Vaso(arm):
    import time
    import Scripts.Sub_inicio as Sub_inicio
 ####################################### Posición segura ##################################   
    Sub_inicio.Sub_inicio(arm)
    
#############################################  MAIN  ##################################################33

    time.sleep(1)
    
    angle_speed = 85
    arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed,  wait=False, radius=0.0)
       
    arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)
       
    arm.set_servo_angle(angle=[-129.4, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed,  wait=False, radius=0.0)
            
    arm.set_servo_angle(angle=[-214.5, -45.0, -30.0, -180.0, -45.0, -180.0], speed=angle_speed,  wait=False, radius=0.0)
    
    arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -192.9], speed=angle_speed,  wait=False, radius=0.0)
            
    angle_speed = 35
    arm.set_servo_angle(angle=[-196.0, 22.7, -34.7, -86.6, 89.6, -194.3], speed=angle_speed,  wait=False, radius=0.0)
    
    tcp_speed = 55
    arm.set_position(*[-278.3, 180.4, 43.5, 107.4, -87.2, 145.1], speed=tcp_speed,  radius=0.0, wait=True)
    
    arm.set_gripper_position(670, wait=True, speed=2000, auto_enable=True)
    
    arm.set_position(*[-278.3, 180.4, 147.7, 107.4, -87.2, 145.1], speed=tcp_speed,  radius=0.0, wait=True)
    
    tcp_speed = 100

    arm.set_position(*[-227.9, 137.5, 237.7, 66.4, -87.5, -95.0], speed=tcp_speed,  radius=0.0, wait=True)
    
    time.sleep(0.5)
    if arm.get_cgpio_digital(15)[1] == 0:
                angle_speed = 110
                arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed,  wait=False, radius=0.0)
                
    else:
                while not arm.get_cgpio_digital(15)[1] == 0:
                    t1 = time.monotonic()
                    arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)
                    
                    arm.set_servo_angle(angle=[-196.0, 22.7, -34.7, -86.6, 89.6, -194.3], speed=angle_speed,  wait=False, radius=0.0)
                    
                    arm.set_position(*[-278.3, 180.4, 43.5, 107.4, -87.2, 145.1], speed=tcp_speed,  radius=0.0, wait=True)
                    
                    arm.set_position(z=-4, radius=-1, speed=tcp_speed,  relative=True, wait=True)
                    
                    arm.set_gripper_position(665, wait=True, speed=2000, auto_enable=True)
                    
                    arm.set_position(*[-278.3, 180.4, 147.7, 107.4, -87.2, 145.1], speed=tcp_speed,  radius=0.0, wait=True)
                    
                    arm.set_position(*[-227.9, 137.5, 237.7, 66.4, -87.5, -95.0], speed=tcp_speed,  radius=0.0, wait=True)
                    
                    time.sleep(0.5)
                    interval = time.monotonic() - t1
                    if interval < 0.01:
                        time.sleep(0.01 - interval)
                arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed,  wait=False, radius=0.0)
               