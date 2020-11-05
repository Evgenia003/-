a = int(input (' введите колличество элементов'))
b = []
for i in range (0, a):
    print ('введите ', i, 'элемент ')
    c = int(input(''))
    b.append(c)
print('четные числа в этом списке: ')
for i in b:
    if  i%2 == 0:
        print(i)
        
