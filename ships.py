import random

with open("end_citys.txt", "r") as file:
    lines = file.readlines()

lines = lines[6:]

def generate_waypoint(name, index, x, z, size=0):
    random_number = random.randint(0, 15)
    
    waypoint_name = f"{index}_{name}_{size.replace('size', 's')}"
    
    return f"waypoint:{waypoint_name}:E:{x}:74:{z}:{random_number}:false:0:gui.xaero_default:false:0:0:false\n"

all_waypoints = []
ships = []
without_ships = []

index = 0
index_ships = 0
index_without_ships  = 0
name_ship = "CITY_SHIP"
name_without_ship= "CITY"
for line in lines:
    parts = line.strip().split(";")
    
    x = parts[2]
    z = parts[3]
    
    details = parts[4] if len(parts) > 4 else ""
    if "ship" in details:
        ships.append(generate_waypoint(name_ship, index_ships, x, z, details.replace(':ship', '')))
        index_ships += 1

        all_waypoints.append(generate_waypoint(name_ship, index, x, z, details.replace(':ship', '')))
        index += 1
    else:
        without_ships.append(generate_waypoint(name_without_ship, index_without_ships, x, z, details))
        index_without_ships += 1

        all_waypoints.append(generate_waypoint(name_without_ship, index, x, z, details))
        index += 1
    

with open("all.txt", "w") as file:
    file.writelines(all_waypoints)

with open("ships.txt", "w") as file:
    file.writelines(ships)

with open("without_ships.txt", "w") as file:
    file.writelines(without_ships)

print("El archivo ha sido procesado y guardado como 'waypoints.txt', 'ships.txt' y 'without_ships.txt'.")
