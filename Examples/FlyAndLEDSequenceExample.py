# 5/19/2026
# A sequence lasting ~20 seconds where the drones takeoff, change LED colors (white, red, blue, off), and lands

from codrone_edu.swarm import *

def main():
  swarm = Swarm(enable_color=False, enable_pause=False)
  swarm.reset_trim()
  swarm.connect()
  swarm.takeoff()
  swarm.set_drone_LED(255, 255, 255, 100)
  swarm.hover(3)
  swarm.set_drone_LED(255, 0, 0, 100)
  swarm.hover(3)
  swarm.set_drone_LED(0, 0, 255, 100)
  swarm.hover(3)
  swarm.set_drone_LED(0, 0, 0, 0)
  swarm.hover(3)
  swarm.hover(3)
  swarm.land()
  swarm.disconnect()
