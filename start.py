# pylint: disable=missing-module-docstring
# a
# import mmap

with open('zoids.gba','rb') as f:
    A = f.read()
    a = []
    for addr in range(0x7b9c28, 0x7BE273):
        a.append(A[addr])
        if len(a)==8:
            print('{:04x}:{:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x}'.format(addr,a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
            a = []
