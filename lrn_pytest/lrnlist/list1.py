from collections import deque
l = [4,5,0,5,6,5,4,234567,"hello"]
l1= [1,2,3]
def listapi1():
    print(l.index(5))
    print(l.index(5,2))
    l.append((4,5,6))
    l.extend((23,3,4,5))
    print(l)
    d = deque(l)
    print(d)
    d.append(("seb","kela"))
    print(d)
def map_api():
    map1 = map(lambda x: x**2, range(10))
    print(map1)
    lmap = list(map1)
    tmap = tuple(map1)
    print(lmap)
    print(tmap)



if __name__ == '__main__':
    # listapi1()
    map_api()