dial_starting_value = 50

dial_range = [0,99]

dial_position = dial_starting_value

password = 0

directional_dictionary = {"L": int(-1),
                          "R": int(1)}
with open("../input.txt", 'r') as f:
    directions = f.readlines()
for direction in directions:
    dial_position += (int(direction[1:]) * directional_dictionary[direction[0]])
    dial_position %= 100
    if dial_position == 0:
        password += 1
print(password)

