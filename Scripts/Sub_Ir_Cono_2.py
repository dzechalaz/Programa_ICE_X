def Sub_Ir_Cono_2(arm):
   import time
   import Scripts.Sub_inicio as Sub_inicio
####################################### Posición segura ##################################   
   Sub_inicio.Sub_inicio(arm)        

   ###################################  MAIN  #################################################




   time.sleep(1)
   angle_speed = 60
            
   arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed, wait=False, radius=0.0)
            
   arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)
            
   arm.set_servo_angle(angle=[-129.4, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=False, radius=0.0)          
   arm.set_servo_angle(angle=[-214.5, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=False, radius=0.0)
   arm.set_servo_angle(angle=[-193.5, -24.7, -0.8, -153.4, 67.8, -12.3], speed=angle_speed, wait=False, radius=0.0)
  
   tcp_speed = 55
   arm.set_position(*[-174.6, 169.6, 173.5, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=False)
           
   
           
   arm.set_position(*[-171.3, 172.2, 288, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=False)
            
   arm.set_gripper_position(55, wait=True, speed=1500, auto_enable=True)
            
   arm.set_position(*[-168.3, 175.2, 121.3, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=False)
   arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)
          
   angle_speed = 30
   time.sleep(1)


   if arm.get_cgpio_digital(15)[1] == 0:
           arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)
              
   else:
          while  not arm.get_cgpio_digital(15)[1] == 0:
             t1 = time.monotonic()
             arm.set_gripper_position(850, wait=True, speed=5000, auto_enable=True)
             
             arm.set_position(*[-168.3, 175.2, 121.3, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=True)       
             arm.set_position(*[-171.3, 172.2, 295, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=False)
                
             arm.set_gripper_position(55, wait=True, speed=1500, auto_enable=True)
                    
             arm.set_position(*[-168.3, 175.2, 121.3, -10.7, 89.1, 110.9], speed=tcp_speed, radius=0.0, wait=False)

             arm.set_position(*[-227.9, 82.9, 155.8, -53.3, 88.4, 90.4], speed=tcp_speed, radius=0.0, wait=True)

             time.sleep(0.5)
             interval = time.monotonic() - t1
             if interval < 0.01:
                   time.sleep(0.01 - interval)
          arm.set_servo_angle(angle=[-190.2, -6.5, -2.4, -151.9, 83.2, -5.4], speed=angle_speed, wait=False, radius=0.0)
                
