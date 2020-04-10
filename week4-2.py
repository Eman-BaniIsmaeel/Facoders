name = input("Enter student's name: ")
s1=['Ahmad',18,17,19.5,8,25]
s2=['Sami',20,20,19,9,28]
s3=['Faris',14.5,16,13,7,23]
while True:
    if name in s1:
        a=s1[1:]
        print(name ,sum(a))
        break
    elif name in s2:
        b=s2[1:]
        print(name ,sum(b))
        break
    elif name in s3:
        c=s3[1:]
        print(name ,sum(c))
        break
    else:
        print('Student is not recorded',0)
        break
