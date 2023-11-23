import rodi
import time

robot = rodi.RoDI()

while True:
    try:
        robot.move_forward()

        distance = robot.see()
        print(distance)
        color= robot.sense()

            #""" 
            #blanco
                            #izq 681  - 864   der 48   - 49"""
        if distance <= 5 and color[0] < 600 and color[1] < 50:
            robot.move_forward()
                #""" 
                #negro 
                #izq 917 - 892   der 480 - 507 """
        elif color[0] > 800 and color[1] < 550:
            robot.move_backward()
            robot.sleep(1.5)  # Back up for 1 second
            robot.move_stop()
            robot.move_left()
            time.sleep(0.50)

    except KeyboardInterrupt:
        robot.move_stop()
        break




