from PIL import EpsImagePlugin
import tkinter 
import turtle
import math
import sys
import os
from tkinter import *
from PIL import Image
import tkinter.messagebox as mb
from tkinter import filedialog as fd 
print(os.getcwd())
EpsImagePlugin.gs_windows_binary =  r'gswin64c.exe'
name =''
x0=0
y0=0
a=0
b=0
original_x=1200
original_y=900
popravka_x=0
popravka_y=0
razmer_x=original_x
razmer_y=original_y
new_x0=0
new_y0=0
otstup_x=0
otstup_y=0
step = 10
kolonka_x=0
kolonka_y=0
proverka_setki = False
name_proverka = False
set_y_setki=19
set_x_setki=19
proverka_setki1=0
set_color="Red"
window = tkinter.Tk()
window.title("Хрестики української вишивки")
window.resizable(False, False) 
window["bg"] = "gray70"
window.iconphoto(False, tkinter.PhotoImage(file='vishivka.png'))
canvas = tkinter.Canvas(master = window, width = razmer_x, height = razmer_y)
canvas.grid(padx=2, pady=2, row=2, column=0, rowspan=9, columnspan=9)
draw = turtle.RawTurtle(canvas)
m = Menu(window)
window.config(menu=m)

def select(event):#функія яка вичисляє де потрібно поставити хрестик 
    global kolonka_x
    global kolonka_y
    if proverka_setki1 != True:
        f = open(name, 'r')
        c,d = map(int, f.readline().split())#d=x c=y
    else:
        c=set_y_setki
        d=set_x_setki
    a,b = (c * step,d * step)
    otstup_x=(razmer_x-b)/2
    otstup_y=(razmer_y-a)/2
    #print(otstup_x,otstup_y)
    widget = event.widget                     
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    #print(event.x,event.y)
    kolonka_x = ((event.x-otstup_x)//step)
    kolonka_y = ((event.y-otstup_y)//step)
    if kolonka_x < 0:
        kolonka_x=0
    if kolonka_x > d:
        kolonka_x = d+1
    if kolonka_y < 0:
        kolonka_y=0
    if kolonka_y > c:
        kolonka_y = c+1
    #print(kolonka_x,kolonka_y)
    krestik_x=(new_x0 - b/2)+(kolonka_x*step)-(step/2)
    krestik_y=(new_y0 + a/2)-(kolonka_y*step)-(step/2)
    draw.color(set_color)
    draw.goto(krestik_x,krestik_y)
    draw.down()
    krestik(step)
    draw.up()
    
canvas.bind("<Button-1>",select)

def callback():#функція яка визиває вікно в якому можно вибрати файл і путь до ноьго записуєтся у змінну name
    global name
    global proverka_setki1
    global name_proverka
    name= fd.askopenfilename() 
    proverka_setki1 = False
    name_proverka = True

    print(name)

def setka(step):#функція яка малює сітку
    if proverka_setki1 != True:
        f = open(name, 'r')
        c,d = map(int, f.readline().split())
    else :
        c=set_y_setki
        d=set_x_setki
    a,b = (c * step,d * step)
    kolichestvo_x = a + (3 * step)
    kolichestvo_y = b + (3 * step)
    f=(d // 2) + 1
    b1= new_x0 - b/2
    a1= new_y0 + a/2
    draw.color('Light gray')
    draw.speed(0)
    draw.up()
    draw.goto(b1,a1+step)
    draw.setheading(0)
    for j in range((d // 2)+1):
        draw.rt(90)
        draw.down()
        draw.fd(kolichestvo_x)
        draw.up()
        draw.setheading(0)
        draw.fd(step)
        draw.down()
        draw.lt(90)
        draw.down()
        draw.fd(kolichestvo_x)
        draw.up()
        draw.setheading(0)
        draw.fd(step)
    if d % 2  == 0:
        draw.up()
    else:
        draw.rt(90)
        draw.down()
        draw.fd(a + (3 * step))    
        draw.up()
        
    draw.goto((b1-step),a1)
    draw.setheading(0)
    for i in range(c // 2 + 1):
        draw.down()
        draw.fd(kolichestvo_y)
        draw.up()
        draw.setheading(270)
        draw.fd(step)
        draw.rt(90)
        draw.down()
        draw.fd(kolichestvo_y)
        draw.up()
        draw.setheading(270)
        draw.fd(step)
        draw.lt(90)
    if c % 2 == 0:
        draw.up()
    else:
        draw.down()
        draw.fd(b + (3 * step))
        draw.up()

def krestik(n):#функція яка малює хрестік
    draw.speed(0)
    draw.down()
    draw.width(1)
    draw.lt(45)
    draw.fd(n*math.sqrt(2))
    draw.up()
    draw.lt(135)
    draw.fd(n)
    draw.lt(135)
    draw.down()
    draw.fd(n*math.sqrt(2))
    draw.lt(45)
    draw.speed(0)
    
def vushuvka(schema2,step,color=1):#функція яка малює хрестик згідно з шаблоном
    f = open(name, 'r')
    c,d = map(int, f.readline().split())
    a,b = (c * step,d * step)
    x0 = new_x0 - b/2
    y0 = new_y0 + a/2 - step
    x = x0
    y = y0
    n = 0
    s = True
    for row  in schema2:
        m = 0
        if s == True:
            x = x0
        for i in row:
            if i == color:
                draw.goto(x + (step/2),y - (step/2))
                draw.down()

                krestik(step)
                
            if i != color:
                draw.up()
                
            m += 1
            if s == True:
                x += step
            else:
                x -= step
        n += 1
        draw.up()
        if s == True:
            draw.setheading(180)
            s = False
        else:
            draw.setheading(0)
            y -= 2*step
            draw.goto(x0 ,y0 -( n )* step)
            s = True


        
def Board2():#ця функція малює сітку потім хрестики
    draw.reset() 
    setka(step)
    draw_click()
    
def draw_click ():#
    k = 0
    schema2 = []
    schema = []
    f = open(name, 'r')
    c,d = map(int, f.readline().split())
    a,b = (c * step,d * step)
    x0 = new_x0 - b/2
    y0 = new_y0 + a/2 - step
    #print(x0,y0)
    for i in range(c):
        s = list(map(int, f.readline().split()))
        schema.append(s)
    for i in range(1, len(schema), 2):
        schema2.append(schema[i-1])
        schema2.append(schema[i][::-1])
        k+=1
 
    draw.goto(x0,y0)
    draw.color('red')  
    vushuvka(schema2,step)

    draw.goto(x0,y0)
    draw.color('darkgreen')
    vushuvka(schema2,step,2)

    draw.goto(x0,y0)
    draw.color('blue')
    vushuvka(schema2,step,3)

    draw.goto(x0,y0)
    draw.color('yellow')
    vushuvka(schema2,step,4)

    draw.goto(x0,y0)
    draw.color('green')
    vushuvka(schema2,step,5)
    
    draw.goto(x0,y0)
    draw.color('white')
    vushuvka(schema2,step,6) 

def exit():#кнопка вийти 
    sys.exit()

def save_size():#змінює розмір холста canva
   global new_y0
   global new_x0
   global razmer_x
   global razmer_y
   set_x = int(Entry_X.get())
   set_y = int(Entry_Y.get())
   canvas.config(width=set_x, height=set_y)
   new_x0 = (original_x-set_x)/2*(-1)
   new_y0 =(original_y-set_y)/2
   razmer_x=set_x
   razmer_y=set_y
   draw.reset() 
   #print(set_x,set_y)

def save_image():#збереження зображення
    canvas.postscript(file="my_dram.ps", colormode="color")
    img = Image.open("my_dram.ps")
    img.save("my_dram.png", "png")

def clear():#кнопка очистити холст
    draw.reset()

def draw_setka():#намалювати тільки сітку 
    draw.reset()
    setka(step)

def colorY():
    global set_color
    krestik_color.config(bg="Yellow")
    set_color="Yellow"

def colorG():
    global set_color
    krestik_color.config(bg="Green")
    set_color="Green"

def colorB():
    global set_color
    krestik_color.config(bg="Blue")
    set_color="Blue"

def colorW():
    global set_color
    krestik_color.config(bg="White")
    set_color="White"

def colorR():
    global set_color
    krestik_color.config(bg="Red")
    set_color="Red"

def save_size_setki():#ввести власні розміри сітки 
   global set_y_setki
   global set_x_setki
   global proverka_setki1
   set_x_setki = int(Entry_X_setki.get())
   set_y_setki = int(Entry_Y_setki.get())
   draw.reset()
   proverka_setki1=True
   #print(set_x_setki,set_y_setki)

def click():#довідка
    dovidka = Tk()
    dovidka.title("Довідка")
    text = """Увага! Під час виконання рапорту НЕ робіть ніяких дій! 
    Режими роботи:
    1. Створення рапорту за готовим шаблоном. 
    Для цього потрібно:
    1) натиснути кнопку "Вибрати файл"(вибрати заздалегідь заготовлений візерунок);
    2) натиснути кнопку "Малювати" і чекати закінчення малювання.
    2. Редагування рапорту, створеного за готовим шаблоном.
    Дотримуйтесь інструкції:
    1) натиснути кнопку "Вибрати файл"(вибрати заздалегідь заготовлений візерунок);
    2) натиснути кнопку "Малювати" і чекати результату;
    3) додати хрестики в потрібній позиції за лівим кліком миші.
    3.Створення власного рапорту.
    Алгоритм роботи:
    1) ввести розміри сітки (ширину та висоту) у  відповідне тестове поле;
    2) натиснути кнопку "Зберегти розмір сітки";
    3) натиснути кнопку "Намалювати сітку";
    4) додати хрестики в потрібній позиції за лівим кліком миші;
    5) для зміни кольору хрестиків натиснути на кнопку "Колір", у випадаючому списку вибрати потрібний колір.
    Бажаємо наснаги та насолоди від реалізації творчих задумів під час вишивання!
    Додаткові функції:
    - Збереження готового рапорту у вигляді графічного зображення з розширенням *.png у папку з кодом, натиснувши на кнопку "Зберегти зображення".
    - Зміна розмірів вікна введенням  його розмірів у текстові поля "Ширина" і "Висота" (у пікселях), натиснувши кнопку "Зберегти розмір".
    - Очищення холста натисканням на кнопку "Очистити вікно".
    """
    text_label = tkinter .Label(dovidka, text=text, justify=tkinter.LEFT)
    text_label.pack()

#
Board_Button = tkinter.Button(window, text ="Малювати", command = Board2)
Board_Button.config(bg="lightgreen",fg="black")
Board_Button.grid(padx=0, pady=0, row=0, column=0, sticky='nsew')
#
Select_Button = tkinter.Button(window, text ="Вибрати файл", command = callback)
Select_Button.config(bg="lightgreen",fg="black")
Select_Button.grid(padx=0, pady=0, row=1, column=0, sticky='nsew')
#
Exit_Button = tkinter.Button(window, text ="Вийти", command = exit)
Exit_Button.config(bg="lightgreen",fg="black")
Exit_Button.grid(padx=0, pady=0, row=0, column=1, sticky='nsew')
#
Save_Image = tkinter.Button(window, text ="Зберегти зображення", command = save_image)
Save_Image.config(bg="lightgreen",fg="black")
Save_Image.grid(padx=0, pady=0, row=1, column=1, sticky='nsew')
#
width_label = tkinter.Label(window, text ="Ширина")
width_label.grid(padx=0, pady=0, row=0, column=2, sticky='nsew')
#
width_setki_label = tkinter.Label(window, text ="Ширина сітки")
width_setki_label.grid(padx=0, pady=0, row=1, column=2, sticky='nsew')
#
height_label = tkinter.Label(window, text ="Висота")
height_label.grid(padx=0, pady=0, row=0, column=4, sticky='nsew')
#
height_setki_label = tkinter.Label(window, text ="Висота сітки")
height_setki_label.grid(padx=0, pady=0, row=1, column=4, sticky='nsew')
#
Entry_X = tkinter.Entry(window)
Entry_X.grid(padx=0, pady=0, row=0, column=3, sticky='nsew')
#
Entry_X_setki = tkinter.Entry(window)
Entry_X_setki.grid(padx=0, pady=0, row=1, column=3, sticky='nsew')
#
Entry_Y = tkinter.Entry(window)
Entry_Y.grid(padx=0, pady=0, row=0, column=5, sticky='nsew')
#
Entry_Y_setki = tkinter.Entry(window)
Entry_Y_setki.grid(padx=0, pady=0, row=1, column=5, sticky='nsew')
#
Save_size = tkinter.Button(window, text ="Зберегти розмір", command = save_size)
Save_size.config(bg="lightgreen",fg="black")
Save_size.grid(padx=0, pady=0, row=0, column=6, sticky='nsew')
#
Save_size_setki = tkinter.Button(window, text ="Зберегти розмір сітки", command = save_size_setki)
Save_size_setki.config(bg="lightgreen",fg="black")
Save_size_setki.grid(padx=0, pady=0, row=1, column=6, sticky='nsew')
#
Clear_window = tkinter.Button(window, text ="Очистити вікно", command = clear)
Clear_window.config(bg="lightgreen",fg="black")
Clear_window.grid(padx=0, pady=0,row=1, column=7, sticky='nsew')
#
Draw_setka = tkinter.Button(window, text ="Намалювати сітку", command = draw_setka)
Draw_setka.config(bg="lightgreen",fg="black")
Draw_setka.grid(padx=0, pady=0,row=0, column=7, sticky='nsew')
#
krestik_color = tkinter.Label(window, text ="Колір Хрестиків")
krestik_color.config(bg=set_color,fg="black")
krestik_color.grid(padx=0, pady=0, row=0, rowspan=2,column=8, sticky='nsew')
#
cm = Menu(m)
m.add_cascade(label="Колір", menu=cm)
cm.add_command(label="Жовтий", command=colorY)
cm.add_command(label="Зелений", command=colorG)
cm.add_command(label="Синій", command=colorB)
cm.add_command(label="Червоний", command=colorR)
cm.add_command(label="Білий", command=colorW)

mc = Menu(m)
m.add_cascade(label="Довідка", menu=mc)
mc.add_command(label="Путівник Користувача", command=click)
#
window.mainloop()
