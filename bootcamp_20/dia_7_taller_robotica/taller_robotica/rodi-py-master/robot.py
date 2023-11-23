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
distance = 5
lista = (robot.sense())
while True:
    try:
        distance = robot.see()
        print(distance)
        if distance <= 10 && :
            robot.move_stop()
        else:
            robot.move_forward()
    except KeyboardInterrupt:
        robot.move_stop()
        break
#prueba para saber valores
""" while True:
    print(robot.sense())
    lista = robot.sense()
    print("izq", lista[0])
    print('der', lista[1]) """
""" 
    negro 
    izq 917 - 892
    der 480 - 507 """
""" 
    blanco
    izq 681  - 864
    der 48   - 49"""