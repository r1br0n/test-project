from tkinter import*

root=Tk()
root.title('Калькулятор')
root.geometry('500x500')
root.resizable(width=False,height=False)

def summa():
    a=float(ent.get())
    b=float(ent2.get())
    s=a+b
    lab3['text']=str(s)

def dil():
    a=float(ent.get())
    b=float(ent2.get())
    s=a/b
    lab3['text']=str(s)

lab=Label(text='Введіть число a')
lab.pack(pady=10)

ent=Entry()
ent.pack(pady=10)

lab2=Label(text='Введіть число b')
lab2.pack(pady=10)

ent2=Entry()
ent2.pack(pady=10)

lab3=Label(text='Результат')
lab3.pack(pady=10)

btn=Button(text='+',command=summa)
btn.pack(pady=10)

btn1=Button(text='/',command=dil)
btn1.pack(pady=10)



    
