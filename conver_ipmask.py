#!/usr/bin/env python3


print('input ip and mask')
ip, mask = input().split('/')



print('\n'+'-'*30)

ip = ip.split('.') #Делим строку по точке
#print(type(mask))


ip = [int(item) for item in ip] # Переводим в список
mask = int(mask) # Переводим в число
maskbin = (mask*'1'+('0'*(32-mask)))# получаем 32 битную строку маски
formats = '''
	 {0:<8} {1:<8} {2:<8} {3:<8}
	 {0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''
#создаем шаблон


binlist = [maskbin[0:8],maskbin[8:16],maskbin[16:24],maskbin[24:32]] #получаем список октетов маски 

binlist = [int(item,2) for item in binlist] # Переводим строки в числа



mask = binlist


print(formats.format(ip[0],ip[1],ip[2],ip[3]))
print(formats.format(mask[0],mask[1],mask[2],mask[3]))
