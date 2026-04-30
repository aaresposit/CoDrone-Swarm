import drone
from codrone_edu.swarm import *
swarm = Swarm(enable_color=False, enable_print=False)
cycle_num = 0

def color_cycle():
    # Code that alternates between red and blue everytime it is called
    # Can be changed to different colors
    global r
    global g
    global b
    global cycle_num
    if cycle_num%2:
        r,g,b = 255,0,0 # red
    else:
        r,g,b = 0,0,255 # blue
    cycle_num += 1
    

def setup_drones():
    # Counts the number of drones and assigns colors
    drone_count = 0
    while True:
        try:
            color_cycle()
            swarm.run_drone(drone_count, "set_drone_LED", r, g, b, brightness=255)
            drone_count += 1
        except:
            print(f"There are {drone_count} drones connected")
            return drone_count
            break

def move_drones(*drone_count):
    # tries to move the drones. prints error if fails.
    try:
        swarm.send_absolute_position(0.5, 0, 0.5, 0.5, 0, 0)
        swarm.hover(1)
        swarm.send_absolute_position(0, 0, 0.1, 0.5, 0, 0)
        swarm.hover(1)
    except Exception as e:
        print(f"Could not move. Error: {e}")

def main():
    swarm.connect()
    swarm.takeoff()
    swarm.hover()
    drone_count = setup_drones()
    print(drone_count)
    swarm.land()
    swarm.disconnect()


try:
    main()
except KeyboardInterrupt:
    print("Program stopped via PyCharm")
    swarm.land()
    swarm.disconnect()
