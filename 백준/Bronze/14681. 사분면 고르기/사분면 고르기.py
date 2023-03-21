quardrant_x=int(input())
quardrant_y=int(input())

if quardrant_x>0 and quardrant_y>0:
    print(1)
elif quardrant_x>0 and quardrant_y<0:
    print(4)
elif quardrant_x<0 and quardrant_y>0:
    print(2)
else:
    print(3)