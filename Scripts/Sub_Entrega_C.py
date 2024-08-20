def Sub_Entrega_C(arm):
    import time

    ################################################  MAIN  #####################################################

    angle_speed = 50
    arm.set_servo_angle(angle=[-191.3, -12.4, -1.6, -152.6, 78.5, -7.6], speed=angle_speed, wait=False, radius=0.0)
            
    tcp_speed = 85
    arm.set_position(*[-217.0, 53.5, 213.7, 72.1, 89.3, 152.2], speed=tcp_speed, radius=0.0, wait=False)
            
    arm.set_servo_angle(angle=[-317.0, 15.9, -41.6, -62.1, 103.9, -21.6], speed=angle_speed, wait=False, radius=0.0)
            
    arm.set_position(*[302.4, 144.8, 85.0, 17.2, 88.2, -58.9], speed=tcp_speed, radius=0.0, wait=False)
            
    arm.set_gripper_position(850, wait=True, speed=1000, auto_enable=True)
            
    arm.set_position(*[280.1, 192.7, 82.0, 22.3, 88.2, -53.8], speed=tcp_speed, radius=0.0, wait=True)
            
    arm.set_servo_angle(angle=[-271.8, 15.3, -26.7, -57.5, 97.7, -8.4], speed=angle_speed, wait=False, radius=0.0)
            
    arm.set_servo_angle(angle=[-288.2, -26.3, -5.8, -119.4, 50.1, -18.0], speed=angle_speed, wait=False, radius=0.0)
            
    arm.set_servo_angle(angle=[-290.5, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=True, radius=0.0)
            
    if arm.get_cgpio_digital(9)[1] == 0 and arm.get_cgpio_digital(13)[1] == 0:
        while not arm.get_cgpio_digital(12)[1] == 0:
         t1 = time.monotonic()
         arm.set_cgpio_digital(1, 1, delay_sec=0)
    
         interval = time.monotonic() - t1
         if interval < 0.01:
             time.sleep(0.01 - interval)
        arm.set_cgpio_digital(1, 0, delay_sec=0)
        
        arm.set_servo_angle(angle=[-129.4, -45.0, -30.0, -180.0, -45.0, 0.0], speed=angle_speed, wait=False, radius=0.0)
        
        arm.set_servo_angle(angle=[0.9, -37.9, -63.5, 0.3, 100.9, 0.2], speed=angle_speed, wait=True, radius=0.0)
        
        while not arm.get_cgpio_digital(9)[1] == 1:
          t1 = time.monotonic()
          arm.set_cgpio_digital(3, 0, delay_sec=0)
        
          interval = time.monotonic() - t1
          if interval < 0.01:
              time.sleep(0.01 - interval)
        time.sleep(0.5)
        while not arm.get_cgpio_digital(13)[1] == 0:
            t1 = time.monotonic()
            arm.set_cgpio_digital(3, 1, delay_sec=0)
    
            interval = time.monotonic() - t1
            if interval < 0.01:
               time.sleep(0.01 - interval)
        arm.set_cgpio_digital(3, 0, delay_sec=0)
        
    else:
        arm.set_state(4)