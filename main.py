#Ask users 3 names as input
#Search the pre-made friends list for the 3 names (names.txt)
#If any common name found store them in new file (nearby.txt)

friend_names = input("Enter the names of friends with comma in between (no spaces please): ").split(',')

names = open('names.txt', 'r')
file_content = [line.strip() for line in names.readlines()]
names.close()

friend_names_set = set(friend_names)
names_set = set(file_content)
nearby_friends = names_set.intersection(friend_names_set)

nearby = open('nearby.txt', 'w')
for friend in nearby_friends:
    print(f"{friend} is nearby! U can meet him/her!!")
    nearby.write(f'{friend}\n')
nearby.close()
