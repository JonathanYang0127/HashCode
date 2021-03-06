nodes = []
class Node:
    def __init__(self, inputTags, p):
        self.tags = set()
        a = inputTags.split()
        self.type = a[0]
        self.photos = p
        for i in range(len(a)-2):
            self.tags.add(a[i+2])
            
                
    def combine(self, other):
        for i in other.tags:
            self.tags.add(i)
        self.photos = (self.photos, other.photos)
        return self

f = open("b_lovely_landscapes.txt", "r")
w = open("output.txt", "w+")
contents = f.readlines()
a = int(contents[0])
horizontal = []
vertical = []

for i in range(a):
    k = contents[i+1][0]
    if k[0] == 'H':
        horizontal.append(Node(contents[i+1], i))
    else:
        vertical.append(Node(contents[i+1], i))   

#pair the v nodes
verticalCombined = []

for i in range(0, len(vertical), 2):
    if(i < len(vertical) - 1):
       verticalCombined.append(vertical[i].combine(vertical[i+1]))

vertical = verticalCombined 
  
nodes = horizontal + vertical

#compute greedy path
notVisited = set()

for i in nodes:
    notVisited.add(i)

def interest(a, b):
    k1 = len(a.tags)
    k2 = len(b.tags)
    k3 = len(b.tags.intersection(a.tags))
    return min(k1 - k3, k2 - k3, k3)

def computeMaximum(n):
    ans, val = None, -1
    i = 0
    for nV in notVisited:
        #if(i > 1000):
            #break
        temp = interest(n, nV)
        if(temp > val):
            val = temp
            ans = nV
        #if val >= 3:
            #break;
        i = i + 1
    print(val)
    notVisited.remove(nV)
    return nV

w.write(str(len(notVisited))+"\n")


def display(n):
    if n.type == "V":
        w.write(str(n.photos[0])+" "+str( n.photos[1])+"\n")
    else:
        w.write(str(n.photos)+"\n")

currentNode = notVisited.pop()
while len(notVisited) != 0:
    if(len(notVisited) % 1000  == 0):
        print(len(notVisited))
    #print(len(notVisited))
    display(currentNode)
    next = computeMaximum(currentNode)
    currentNode = next
     
display(currentNode)

