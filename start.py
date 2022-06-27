# pylint: disable=missing-module-docstring
# a
# import mmap


with open('test.gba','rb') as f, open('test','wb') as wf:
    A = f.read()
    i,j = 0,0
    for addr in range(0x7b9c28, 0x7BE273):
        # if len(a)==16:
        #     print('{:04x}:{:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x} {:02x}'.format(addr,*a))
        #     a = []
        
        if i % 100 == 0:
            j = 0
        if j % 16 == 0 and i % 100 != 96:
            print('{:04x}:{:02x} {}:{}'.format(addr,A[addr],i,j))
            wf.write(A[addr].to_bytes(1, byteorder='little'))
        j += 1
        i += 1

    f.close()
    wf.close()

    
