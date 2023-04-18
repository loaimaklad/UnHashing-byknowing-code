#app is made by loai khalid by tkinter/python !-- Loay Copyright 2022 - 2023
#WAIT FOR GUI BUILT
while True :
    x=int(input('Whatis UR CODE : '))
    try :
        as1 = int(2009*80) #CODE THATIS IS USEING HASH CODE
        y=x-as1
        print(chr(y))
    except Exception as ex :
        print(ex)
