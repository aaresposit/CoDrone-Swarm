from codrone_edu.swarm import *
import random
import time
swarm = Swarm(enable_color=False, enable_print=False, enable_pause=False)
swarm.connect()
swarm.takeoff()
try:
    #RED
    swarm.set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm.hover(1)
    #WHITE
    swarm.set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm.hover(1)
    #RED
    swarm.set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm.hover(1)
    #WHITE
    swarm.set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm.hover(1)
    #BLUE
    swarm.set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm.hover(1)
    #RED,WHITE
    swarm.set_drone_LED(r=255, g=0, b=0, brightness=100)

    swarm.hover(1)
    #WHITE, RED
    swarm[:4].set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm[4:].set_drone_LED(r=255, g=0, b=0, brightness=100)

    swarm.hover(1)
    #BLUE,WHITE
    swarm[:4].set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm[4:].set_drone_LED(r=255, g=255, b=255, brightness=100)

    swarm.hover(1)
    #WHITE, BLUE
    swarm[:4].set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm[4:].set_drone_LED(r=0, g=0, b=255, brightness=100)

    swarm.hover(1)
    #RED, BLUE
    swarm[:4].set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm[4:].set_drone_LED(r=0, g=0, b=255, brightness=100)

    swarm.hover(1)
    #BLUE, RED
    swarm[:4].set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm[4:].set_drone_LED(r=255, g=0, b=0, brightness=100)

    swarm.hover(1)
    #RED, BLUE
    swarm[:4].set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm[4:].set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm.hover(1)
    #BLUE,RED
    swarm[:4].set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm[4:].set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm.hover(1)
    #RED
    swarm.set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm.hover(1)
    #WHITE
    swarm.set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm.hover(1)
    #BLUE
    swarm.set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm.hover(1)
    #RED
    swarm.set_drone_LED(r=255, g=0, b=0, brightness=100)
    swarm.hover(1)
    #WHITE
    swarm.set_drone_LED(r=255, g=255, b=255, brightness=100)
    swarm.hover(1)
    #BLUE
    swarm.set_drone_LED(r=0, g=0, b=255, brightness=100)
    swarm.hover(1)
except KeyboardInterrupt:
    swarm.land()
    swarm.disconnect()
finally:
    swarm.land()

indexes = [i for i in range(8)]
print(indexes)
for i in range(8):
    ind = random.choice(indexes)
    swarm.run_drone(ind, "set_drone_LED", r=255, g=255, b=255, brightness=100)
    swarm.hover(0.25)
    swarm.run_drone(ind,"set_drone_LED", r=0, g=0, b=0, brightness=100)
    swarm.hover(0.5)
    swarm.run_drone(ind, "set_drone_LED", r=0, g=0, b=0, brightness=100)
    indexes.remove(ind)

swarm.disconnect()
