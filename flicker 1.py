from codrone_edu.swarm import *
swarm = Swarm(enable_color=False, enable_print=False)
swarm.connect()

def blinking(n):
    hover_time = 3
    while(n>0):
        swarm.set_drone_LED(r=255, g=0, b=0, brightness=255)
        swarm.hover(hover_time)
        swarm.set_drone_LED(r=255, g=255, b=255, brightness=255)
        swarm.hover(hover_time)
        swarm.set_drone_LED(r=0, g=0, b=255, brightness=255)
        swarm.hover(hover_time)
        n=n-1

def main():
    #swarm.takeoff()
    #swarm.hover()
    blinking(5)
    #swarm.land()

try:
    main()
except KeyboardInterrupt:
    swarm.land()

swarm.disconnect()
