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

f = open("a_example.txt", "r")
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
print(nodes)

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
    for nV in notVisited:
        temp = interest(n, nV)
        if(temp > val):
            temp = val
            ans = nV
    notVisited.remove(nV)
    return nV

print(len(notVisited))


def display(n):
    if n.type == "V":
        print(n.photos[0], n.photos[1])
    else:
        print(n.photos)

currentNode = notVisited.pop()
while len(notVisited) != 0:
    display(currentNode)
    next = computeMaximum(currentNode)
    currentNode = next
   
display(currentNode)

