from codrone_edu.swarm import *
swarm = Swarm()

swarm.connect()
swarm.set_drone_LED(255, 0, 0, 100)
swarm.hover(1)
swarm.set_drone_LED(0, 0, 255, 100)
swarm.hover(1)
swarm.set_drone_LED(255, 0, 0, 100)
swarm.hover(1)
swarm.takeoff()
swarm.hover(1)
swarm.land()
swarm.disconnect()
