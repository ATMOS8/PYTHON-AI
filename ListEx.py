x = [1,2,3,4,5,6,7]
print(x)
print(x[0])
print(x[-1])
print(x[0:3])
print(x[-3:])
print(x[2:])
print(x[:-2])
print(x[::-2])

users = ["Smith", "James", "Kang", "Mathew", "Eliz"]

print(users)

print("using index number in for loop")
for i in range(0,len(users)) : 
    print(users[i])

print("using item object in for loop")
for item in users :
    print(item)

colors = list()

colors.append("Black")
colors.append("Blue")
colors.append("Red")

print(colors)

favcolors = ["White","Orange","Purple"]
colors.extend(favcolors)

print(colors)

colors.insert(5,"Yellow")

print(colors)

colors[4] = "Grey"

print(colors)

colors.pop()

print(colors)

colors.remove("White")

print(colors)

del colors[2]

print(colors)