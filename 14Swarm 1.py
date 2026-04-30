import drone
from codrone_edu.swarm import *
swarm = Swarm(enable_color=False, enable_print=False)
cycle_num = 0

def color_cycle():
    global r
    global g
    global b
    global cycle_num
    if cycle_num%2:
        r,g,b = 255,0,0
    else:
        r,g,b = 0,0,255
    cycle_num += 1
    # Code that detects whether "cycle_num" is odd or even and switches between red and blue

def try_change_colors():
    drone_count = 0
    while True:
        try:
            color_cycle()
            swarm.run_drone(drone_count, "set_drone_LED", r, g, b, brightness=255)
            drone_count += 1
        except:
            print(f"There are {drone_count} drones connected")
            break

def move_drones():
    drone.send_absolute_position(0.5, 0, 1, 0.5, 0, 0)

def main():
    swarm.connect()
    #swarm.takeoff()
    #swarm.hover()
    try_change_colors()
    #swarm.land()
    swarm.disconnect()


try:
    main()
except KeyboardInterrupt:
    print("Program stopped via PyCharm")
    swarm.land()
    swarm.disconnect()
