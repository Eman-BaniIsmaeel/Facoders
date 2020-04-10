print('Numbers from 1 to 10')
num=5
i=int(input('Guess the number: '))
while i>=1 and i<=10:
    if i==num:
        print('Great you did it')
        break
    else:
        i=int(input('Guess the number: '))
        continue
else:
    print('Number should be between 1 and 10')            
