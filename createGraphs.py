f = open("a_example.txt", "r")
contents = f.readlines()
a = int(contents[0])
for i in range(a):
    print(contents[i+1])


