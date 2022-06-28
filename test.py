# pylint: disable=missing-module-docstring
# pylint: disable=consider-using-f-string
# pylint: disable=line-too-long
from random import choices, randint, sample, shuffle
from sys import byteorder
zoids = [
    [0],
    [46,47,74,80,82,83,84,85,87,89,90,91,92,93,97,98,99,107],
    [16,33,37,51,72,75,81,94,100,108,113,114,137],
    [34,56,73,76,78,102,109,119,120,121,122,123,124,125,126],
    [35,36,38,77,88,96,104,105,110,111,143],
    [1,7,10,11,12,13,14,15,17,18,19,20,22,39,49,50,52,53,95,101,142],
    [3,21,40,42,70,106,127,131,141,151],
    [4,5,8,9,23,24,25,26,27,29,30,43,54,55,71,79,144],
    [2,28,45,58,61,63,138,139],
    [6,31,32,44,59,62,68,69,103,112,115,128,129,132,133,134,135],
    [60,64,65,66,67,86,116,118,130,136],
    [41,48,57,117,140,145,146]
]

zcp = [
    0,50,60,45,55,70,60,40,70,50,40,40,50,40,40,40,20,30,
    25,40,30,40,40,50,45,40,30,30,30,40,30,30,25,30,25,
    30,30,30,25,35,45,70,50,60,60,55,18,20,200,60,20,35,
    50,45,55,50,40,90,40,40,50,40,35,30,45,40,40,50,35,
    30,50,60,20,10,15,20,10,5,20,40,15,25,18,15,20,15,60,
    18,40,20,15,12,12,20,18,30,15,20,20,13,20,30,25,50,
    30,25,35,15,20,20,10,10,30,20,20,60,30,60,50,30,30,
    30,20,20,30,20,30,30,40,40,60,30,40,20,60,45,60,20,
    55,50,180,30,30,25,30,70,150,0,0,0,0,25
]

eqp = [
    0,12,25,27,35,30,50,40,50,60,80,5,11,23,26,6,15,20,25,8,12,15,23,14,12,25,32,35,40,
    15,18,25,28,30,8,12,18,20,23,21,18,35,40,20,23,25,27,30,4,5,7,10,3,3,8,8,10,12,13,
    15,10,15,18,20,26,10,15,22,27,15,18,10,30,80,30,25,10,15,20,23,15,23,25,12,13,14,99,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    5,10,15,20,25,30,20,30,40,5,10,30,15,20,30,50,15,3,5,10,1,3,5,10,5,5,5,5,0,3,5,6,8,5,
    8,3,2,2,4,6,8,5,3,10,5,7,10,12,5,10,5,5,10,10,3,3,3,12,15,15,10,20,20,14,10,10,5
]

ast5 = [
    121,137,138,118,122,130,136,143,155,156,157,139,101,110,
    119,123,125,126,127,128,131,134,142,145,149,151,152,167
]

wep = [*range(1,88),*range(101,129),*range(130,168)]

with open('zoids.gba','rb') as rf, open('randomized.gba','wb') as wf:
    A = rf.read()
    for addr in range(0x0,0x7a21c0):
        wf.write(A[addr].to_bytes(1, byteorder='little'))

with open('randomized.gba','ab') as wf:
    shop = [*sample(wep,40),*sample(wep,152)] #weapon shop item
    for itm in shop:
        wf.write(itm.to_bytes(1, byteorder='little'))
        wf.write(0x00.to_bytes(1, byteorder='little'))

with open('zoids.gba','rb') as rf, open('randomized.gba','ab') as wf:
    A = rf.read()
    for addr in range(0x7a2340,0x7a2394):
        wf.write(A[addr].to_bytes(1, byteorder='little'))

with open('randomized.gba','ab') as wf:
    ww = []
    for a in range(1, 168): #weapon shop price
        pr = (eqp[a] + 1) * a * randint(1,500)
        ww.append(pr - pr%100 + 100)
    shuffle(ww)
    for www in ww:
        wf.write(www.to_bytes(4, byteorder='little'))

with open('zoids.gba','rb') as rf, open('randomized.gba','ab') as wf:
    A = rf.read()
    for addr in range(0x7a2630,0x7b9c28):
        wf.write(A[addr].to_bytes(1, byteorder='little'))

with open('randomized.gba','ab') as wf:
    for a in range(1, 181): #random battles
        limit = a // 3 + 4
        p = []
        # print(limit)
        i = 0
        while i < limit: #random parties
            if len(p) == 96:
                p.append(23)
                p.append(0)
                p.append(0)
                p.append(0)
                break
            r = randint(0,10)
            if limit < 11:
                r = randint(1,limit)
                z = 0
            if i + r < limit:
                i += r
                z = choices(zoids[r])[0]
            p.append(z) #choosing zoids
            p.append(randint(0,7)) #choosing colors
            p.append(100) #health
            p.append(0) #hidden health bar
            j = zcp[z]
            u = randint(101, 167)
            if j < 9:
                u = choices(ast5)[0]
            p.append(u) #choosing top equipment
            j-=eqp[u]
            u = randint(0,86)
            if j - eqp[u] < 0:
                u = 0
            if j > 10:
                while eqp[u] >= j:
                    u = randint(0,86)
            p.append(u) #choosing left equipment
            j-=eqp[u]
            u = randint(0,86)
            if j - eqp[u] < 0:
                u = 0
            p.append(u) #choosing right equipment
            j-=eqp[u]
            u = randint(101,167)
            if j - eqp[u] < 0:
                u = 0
            p.append(u) #choosing bottom equipment
            
            maxe = a*3+r*10
            e = randint(1,maxe)
            e1 = e % 256
            e2 = e // 256
            p.append(e1)
            p.append(e2)
            p.append(0)
            p.append(0)
            maxm = 100*r*r
            m = randint(0,maxm)
            m += 500
            m1 = m % 256
            m2 = m // 256
            p.append(m1)
            p.append(m2)
            p.append(0)
            p.append(0)
        for pp in p:
            # print(pp)
            wf.write(pp.to_bytes(1, byteorder='little'))



with open('zoids.gba','rb') as rf, open('randomized.gba','ab') as wf:
    A = rf.read()
    for addr in range(0x7BE278,0x800000):
        wf.write(A[addr].to_bytes(1, byteorder='little'))
