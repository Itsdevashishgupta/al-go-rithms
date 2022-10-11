import random


def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='g':
            return True
        elif you=='w':
            return False
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False
    elif  comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
comp=print("computer's turn:snake(s), water(w), gun(g)")
randno=random.randint(1,3)
if randno==1:
    comp='g'
elif randno==2:
    comp='w'
else:
    comp='s'
you=input("your's turn:")
a=game(comp,you)
print(f"computer choose:{comp}")
print(f"your turn:{you}")
if a==None:
    print("tie")
elif a:
    print("you win")
else:
    print("you lose")