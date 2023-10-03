number =  0 

while  number < 101:
    if number % 15 == 0:
        print('физбаз')
    elif number % 5 == 0:
        print('баз')
    elif number % 3 == 0:
        print('физ')
    else:
        print(number)
    number += 1
