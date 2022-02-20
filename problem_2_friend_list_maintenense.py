friends_list = input().split(", ")
blacklisted_names = 0
lost_names = 0
commands_line = input()
while not commands_line == "Report":
    commands = commands_line.split(" ")
    command = commands[0]

    if command == "Blacklist":
        name = commands[1]
        if commands[1] in friends_list:
            index_of_name = friends_list.index(commands[1])
            friends_list[index_of_name] = "Blacklisted"
            print(f"{commands[1]} was blacklisted.")
            blacklisted_names += 1
        else:
            print(f"{commands[1]} was not found.")
    elif command == "Error":
        index = int(commands[1])

        if 0 <= index < len(friends_list):
            is_valid = True

        if friends_list[index] != "Blacklisted" and friends_list[index] != "Lost" and 0 <= index < len(friends_list):
            print(f"{friends_list[index]} was lost due to an error.")
            friends_list[index] = "Lost"
            lost_names += 1
    elif command == "Change":
        index = int(commands[1])

        if 0 <= index < len(friends_list):
            print(f"{friends_list[index]} changed his username to {commands[2]}.")
            friends_list[index] = commands[2]
    commands_line = input()
print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(f"{' '.join(friends_list)}")
