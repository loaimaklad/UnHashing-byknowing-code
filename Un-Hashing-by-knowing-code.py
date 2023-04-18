#gui-built :
from tkinter import *
root=Tk()
root.title('simp-unencrypt')
root.geometry('300x300')
x=Entry()
def Lo13I():
    try :
        as1 = int(2009*80)
        y=x-as1
        print(chr(y))
    except Exception as ex :
        print('An err was detected /\\')
root.mainloop()
