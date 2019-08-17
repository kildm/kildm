#!/usr/bin/env python3


print('input ip and mask')
ip, mask = input().split('/')



print('\n'+'-'*30)

ip = ip.split('.')
#print(type(mask))


ip = [int(item) for item in ip]
mask = int(mask)
maskbin = (mask*'1'+('0'*(32-mask)))
formats = '''
	 {0:<8} {1:<8} {2:<8} {3:<8}
	 {0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''


binlist = [maskbin[0:8],maskbin[8:16],maskbin[16:24],maskbin[24:32]]

binlist = [int(item,2) for item in binlist]



mask = binlist


print(formats.format(ip[0],ip[1],ip[2],ip[3]))
print(formats.format(mask[0],mask[1],mask[2],mask[3]))
