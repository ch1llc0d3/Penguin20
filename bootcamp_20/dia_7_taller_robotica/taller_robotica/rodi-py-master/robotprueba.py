import rodi
import time

robot = rodi.RoDI() 
#creamos nuestro objeto dentro de la variable robot utilizando
#la clase RoDI desde nuestra librearia rodi.

""" robot.move_forward()
time.sleep(3)
robot.move_stop(3) """

#Desafio: Utilizando el sensor de distancia de RoDI hacer que
#nuestro robot avance libremente evitando chocar de frente
#contra un obstaculo a menos de 10 centimetros.
"""# ... (código existente)

""" class rodi(object):
    # ... (código existente)

    def avoid_obstacle(self):
        '''
        Moves the robot forward, avoiding obstacles in the path
        '''
        while True:
            distance = self.see()
            if distance is not None and distance < 10:
                # Obstacle detected, stop and change direction
                self.move_stop()
                self.move_backward()
                self.sleep(1)  # Back up for 1 second
                self.move_stop()
                self.move_left()  # Turn left
                self.sleep(1)  # Turn for 1 second
            else:
                # No obstacle, move forward
                self.move_forward()

    # ... (código existente)

if __name__ == '__main__':
    ROBOT = RoDI()
    ROBOT.avoid_obstacle()""" """
""" 
import rodi
import time
 """
""" robot = rodi.RoDI()
class RoDI(object):
    # ... (código existente)

    def avoid_obstacle(self):
        '''
        Moves the robot forward, avoiding obstacles in the path
        '''
        while True:
            distance = self.see()
            x = distance < 10 
            if distance is not None and x:
                # Obstacle detected, stop and change direction
                self.move_stop()
                self.move_backward()
                self.sleep(1)  # Back up for 1 second
                self.move_stop()
                self.move_left()  # Turn left
                self.sleep(1)  # Turn for 1 second
            elif:
                # No obstacle, move forward
                self.move_forward()
            elif:
 """

""" 
while True:
    try:
        robot.move_forward()

        distance = robot.see()
        print(distance)
        color= robot.sense()

        if distance <= 10 and color[0] < 500:
            robot.move_forward()
        elif color[0] > 500:
            robot.move_left()
            time.sleep(0.50)

    except KeyboardInterrupt:
        robot.move_stop()
        break
 """