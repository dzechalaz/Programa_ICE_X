def Sub_Ir_Cono_1(arm):
    import time
    import Scripts.Sub_inicio as Sub_inicio
 ####################################### Posición segura ##################################   
    Sub_inicio.Sub_inicio(arm)
       
   ######################################  MAIN  ############################################################
 


    time.sleep(1)
    angle_speed = 60

    arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed, wait=False, radius=0.0)
            
    arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)

    arm.set_servo_angle(angle=[-129.4, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-214.5, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed, wait=False, radius=0.0)
    arm.set_servo_angle(angle=[-184.8, -0.9, -15.0, -146.1, 78.9, -10.0], speed=angle_speed, wait=False, radius=0.0)
            
    tcp_speed = 55
            
    arm.set_position(*[-303.0, 72.9, 288, -31.3, 87.3, 112.3], speed=tcp_speed, radius=0.0, wait=False)
           
    arm.set_gripper_position(55, wait=True, speed=1500, auto_enable=True)
            
    arm.set_position(*[-303.0, 72.9, 145, -31.3, 87.3, 112.3], speed=tcp_speed, radius=0.0, wait=True)
    arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)

    time.sleep(0.5)

    if arm.get_cgpio_digital(15)[1] == 0:
                angle_speed = 85
                arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)
                
    else:
           while not arm.get_cgpio_digital(14)[1] == 0:
               t1 = time.monotonic()
               arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)
              
               
               arm.set_position(*[-303.0, 72.9, 145, -31.3, 87.3, 112.3], speed=tcp_speed, radius=0.0, wait=True)
               arm.set_position(*[-303.0, 72.9, 295, -31.3, 87.3, 112.3], speed=tcp_speed, radius=0.0, wait=True)
               
               arm.set_gripper_position(55, wait=True, speed=1500, auto_enable=True)
              
               arm.set_position(*[-303.0, 72.9, 155.3, -31.3, 87.3, 112.3], speed=tcp_speed, radius=0.0, wait=True)

               arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)
               
               time.sleep(0.5)
               interval = time.monotonic() - t1
               if interval < 0.01:
                   time.sleep(0.01 - interval)
           arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=False)
