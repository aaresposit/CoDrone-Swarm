from codrone_edu.swarm import *

swarm = Swarm(enable_pause=False)
swarm.connect() #drones will take off at the same time
print(f'get_address_data returns: {swarm.get_address_data()}')
print(f'get_address_data returns: {swarm.get_cpu_id_data()}')

identifiers = []
addresses = []
for item in swarm:
    while True:
        id = item.get_cpu_id_data()[0][1]
        if len(id)>0:
            print(id)
            identifiers.append(id)
            break
        else:
            pass
    while True:
        addr = item.get_address_data()[0][1]
        if len(addr)>0:
            print(addr)
            addresses.append(addr)
            break
        else:
            pass

print(identifiers)
print(addresses)

with open('drones.txt','r') as file:
    contents = file.read()
with open('drones.txt', 'a') as file:
    for id, addr, count in zip(identifiers,addresses,range(len(identifiers))):
        desired = f"id: {id} | addr: {addr}"
        if desired not in contents:
            file.write(f"Drone 00{count} | id: {id} | addr: {addr}\n")
        if desired in contents:
            print("Already present.")
        elif id in contents and addr in contents:
            print("Error: Found both id and addr, but could not find standard wording.")
        elif id not in contents or addr not in contents:
            print("Error: One item of the pair is missing or is incorrectly paired.")
        else:
            print(f"Drone {count} | id: {id} | addr: {addr} is already a part of the list!")
with open('drones.txt','r') as file:
    contents = file.read()
    print("Updated version: ", contents)

swarm.disconnect()





