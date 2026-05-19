# 5/6/26
# Example of a flowing pattern through drones

from codrone_edu.swarm import *
swarm = Swarm()

def drone_count(): # returns number of drones
    drone_index = 0
    try:
        while True:
            print(swarm.run_drone(drone_index, "get_position_data"))
            drone_index += 1
    except:
        return drone_index

def flowing_pattern(loops, r, g, b, brightness): # creates a flowing pattern
    total = drone_count()
    print("Starting flowing pattern for", total, "drones.")
    delay = 1.5 # this changes delay between each light
    for i in range(loops):
        print(loops)
        for index in range(total):
            swarm.run_drone(index, 'set_drone_LED', r, g, b, brightness)
            print(f"{index} on and ",end="")
            index = (index + total//2) % total
            swarm.run_drone(index, 'set_drone_LED', r, g, b, 0)
            print(f"{index} off.")
            swarm.hover(delay)
    print("Flowing pattern finished.")
    swarm.set_drone_LED(0, 0, 0, 0)

def main():
    swarm.connect()
    swarm.takeoff
    swarm.connect()
    flowing_pattern(2, 0, 255, 0, 100)
    swarm.disconnect()
    swarm.land()
