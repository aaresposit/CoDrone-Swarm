# this will be the file used by the server.py and client.py files.
# for now, code will intentionally not run on its own; it requires server and client files to execute code

from codrone_edu.swarm import *
swarm = Swarm(enable_color=False, enable_print=False)

def main():
    swarm.connect()
    # enter code here
    swarm.disconnect()

# uncommenting the following line will allow the code to run on its own, but may also give issues with the server/client files

# main()
