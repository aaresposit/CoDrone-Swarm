# updated 5/1/2026
# test code to be used with three drones, demonstrating independent flight / actions
# uncomment movement once verified this works

from codrone_edu.swarm import *

seq_0 = Sequence(0)
# seq_0.add('takeoff')
# seq_0.add('send_absolute_position', 0.5, 0, 0, 0.5, 0, 0)
# seq_0.add('hover', 0.5)
seq_0.add('set_drone_LED', 255, 25, 255, 255) # purple

seq_1 = Sequence(1)
# seq_1.add('takeoff')
# seq_1.add('set_yaw', 50)
# seq_1.add('move', 1)
# seq_1.add('hover', 0.5)
seq_1.add('set_drone_LED', 25, 255, 255, 255) # cyan

seq_2 = Sequence(0)
# seq_2.add('send_absolute_position', -0.5, 0, 0, 0.5, 0, 0)
# seq_2.add('hover', 0.5)
# seq_2.add('land')
seq_2.add('set_drone_LED', 25, 255, 255, 255) # cyan

seq_3 = Sequence(1)
# seq_3.add('set_yaw', -50)
# seq_3.add('move', 1)
# seq_3.add('hover', 0.5)
# seq_3.add('land')
seq_3.add('set_drone_LED', 255, 25, 255, 255) # purple

seq_4 = Sequence(3)
seq_4.add('set_drone_LED', 255, 0, 0, 255) # red
seq_4.add('set_controller_LED', 255, 0, 0, 255)
seq_4.add('drone_buzzer', 200, 300)
seq_4.add('set_drone_LED', 255, 255, 0, 255) # yellow
seq_4.add('set_controller_LED', 255, 255, 0, 255)
seq_4.add('drone_buzzer', 250, 300)
seq_4.add('set_drone_LED', 0, 255, 0, 255) # green
seq_4.add('set_controller_LED', 0, 255, 0, 255)
seq_4.add('drone_buzzer', 265, 300)

seq_actions = Sync(seq_0, seq_1, seq_2, seq_3)
seq_actions.add(seq_4) # will this work? what is the purpose of this command?

# drones begin to move here
swarm = Swarm()
swarm.connect()
try:
    swarm.run(seq_actions, 'sequential', delay=None, order=None)
except Exception as e:
    print(f"Error: {e}")
swarm.land()
swarm.disconnect()
