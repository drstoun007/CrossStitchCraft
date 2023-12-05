from PIL import EpsImagePlugin
import tkinter 
import turtle
import math
import sys
import os
from tkinter import *
from PIL import Image
import tkinter.messagebox
from tkinter import filedialog as fd 
print(os.getcwd())
EpsImagePlugin.gs_windows_binary =  r'gswin64c.exe'
name =''
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
kolonka_x = 0
kolonka_y = 0
set_y_setki=19
set_x_setki=19
set_color='red'
color_pattern=1
schema = []
color_lib = {1: 'red', 2: 'darkgreen', 3: 'blue', 4: 'yellow', 5: 'green', 6: 'white'}
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

def mathematic(c,d,new_x0,new_y0,step):
    a,b = (c * step,d * step)
    k =b/2
    l =a/2
    x0 = (new_x0 - b/2)#-(step/2)
    y0 = (new_y0 + a/2)#-(step/2)
    return x0,y0,a,b

def select(event):#функія яка вичисляє де потрібно поставити хрестик 
    widget = event.widget                     
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    x0, y0, a, b = mathematic(set_x_setki,set_y_setki,new_x0,new_y0,step)
    otstup_x=(razmer_x-b)/2
    otstup_y=(razmer_y-a)/2
    kolonka_x = ((event.x-otstup_x)//step)
    kolonka_y = ((event.y-otstup_y)//step)
    if kolonka_y < 0:
        kolonka_y=0
    if kolonka_y > set_x_setki-1:
        kolonka_y = set_x_setki-1
    if kolonka_x < 0:
        kolonka_x=0
    if kolonka_x > set_y_setki-1:
        kolonka_x = set_y_setki-1
    kolonka_x=int(kolonka_x)
    kolonka_y=int(kolonka_y)
    print(kolonka_x,kolonka_y)
    schema[kolonka_y][kolonka_x] = color_pattern
    krestik_new(kolonka_x,kolonka_y,step,color_pattern,x0,y0)
    
canvas.bind("<Button-1>",select)

def callback():#функція яка визиває вікно в якому можно вибрати файл і путь до ноьго записуєтся у змінну name
    global set_y_setki,set_x_setki,schema
    name= fd.askopenfilename() 
    print(name)
    f = open(name, 'r')
    schema= []
    set_y_setki,set_x_setki = map(int, f.readline().split())#d=y c=x
    for i in range(set_x_setki):
        s = list(map(int, f.readline().split()))
        schema.append(s)

def setka(step,set_x_setki,set_y_setki):#функція яка малює сітку
    x0, y0, a, b = mathematic(set_x_setki,set_y_setki,new_x0,new_y0,step)
    draw.color('Light gray')
    draw.speed(0)
    draw.up()
    draw.goto(x0,y0+step)
    draw.setheading(270)
    kolichestvo_x = a + step
    kolichestvo_y = b + step
    for j in range(set_y_setki):
            draw.down()
            draw.fd(kolichestvo_x)
            draw.up()
            draw.setheading(0)
            draw.fd(step)
            if j % 2 !=0:
               draw.setheading(270) 
            else:
                draw.setheading(90)
            draw.up()    
    draw.goto(x0-step,y0)
    draw.setheading(0)
    for i in range(set_x_setki):
        draw.down()
        draw.fd(kolichestvo_y)
        draw.up()
        draw.setheading(270)
        draw.fd(step)
        if i % 2!=0:
               draw.setheading(0) 
        else:
            draw.setheading(180)

def krestik(n):#функція яка малює хрестік
    draw.speed(0)
    draw.down()
    draw.width(1)
    draw.setheading(45)
    draw.fd(n*math.sqrt(2))
    draw.up()
    draw.setheading(270)
    draw.fd(n)
    draw.setheading(135)
    draw.down()
    draw.fd(n*math.sqrt(2))
    draw.up()

    
def vushuvka(schema2,step,set_x_setki,set_y_setki):#функція яка малює хрестик згідно з шаблоном
    x0, y0, a, b = mathematic(set_x_setki,set_y_setki,new_x0,new_y0,step)
    for indexrow, row in enumerate(schema2):
        for indexi, color in enumerate(row):
            if color != 0:
                krestik_new(indexi,indexrow,step,color,x0,y0)

def krestik_new(x,y,step,color,x0,y0):
    cordinat_x=x0+step*x-step/2
    cordinat_y=y0-step*y-step/2
    draw.goto(cordinat_x,cordinat_y)
    draw.color(color_lib[color])
    draw.down()
    krestik(step)
    draw.up()

def Board2():#ця функція малює сітку потім хрестики
    draw.reset() 
    setka(step,set_x_setki,set_y_setki)
    vushuvka(schema,step,set_x_setki,set_y_setki)

def exit():#кнопка вийти 
    sys.exit()

def my_file():
    with open("Pattern.txt", 'w') as file:
        file.write(f"{set_y_setki} {set_x_setki}\n")
        for row in schema:
            file.write(" ".join(map(str, row)) + '\n')

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

def save_image():#збереження зображення
    canvas.postscript(file="my_dram.ps", colormode="color")
    img = Image.open("my_dram.ps")
    img.save("my_dram.png", "png")

def clear():#кнопка очистити холст
    draw.reset()

def draw_setka():#намалювати тільки сітку 
    draw.reset()
    setka(step,set_x_setki,set_y_setki)

def colorR():
    global color_pattern
    global set_color
    krestik_color.config(bg="Red")
    set_color="Red"
    color_pattern=1

def colordG():
    global color_pattern
    global set_color
    krestik_color.config(bg="darkgreen")
    set_color="darkgreen"
    color_pattern=2

def colorB():
    global color_pattern
    global set_color
    krestik_color.config(bg="Blue")
    set_color="Blue"
    color_pattern=3

def colorY():
    global color_pattern
    global set_color
    krestik_color.config(bg="Yellow")
    set_color="Yellow"
    color_pattern=4

def colorG():
    global color_pattern
    global set_color
    krestik_color.config(bg="Green")
    set_color="Green"
    color_pattern=5

def colorW():
    global color_pattern
    global set_color
    krestik_color.config(bg="White")
    set_color="White"
    color_pattern=6

def save_size_setki():#ввести власні розміри сітки 
   global set_y_setki
   global set_x_setki
   global schema
   set_y_setki = int(Entry_X_setki.get())
   set_x_setki = int(Entry_Y_setki.get())
   schema = [[0 for _ in range(set_y_setki)] for _ in range(set_x_setki)]
   draw.reset()

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
Entry_X = tkinter.Entry(window)
Entry_X.grid(padx=0, pady=0, row=0, column=3, sticky='nsew')
#
Entry_X_setki = tkinter.Entry(window)
Entry_X_setki.grid(padx=0, pady=0, row=1, column=3, sticky='nsew')
#
height_label = tkinter.Label(window, text ="Висота")
height_label.grid(padx=0, pady=0, row=0, column=4, sticky='nsew')
#
height_setki_label = tkinter.Label(window, text ="Висота сітки")
height_setki_label.grid(padx=0, pady=0, row=1, column=4, sticky='nsew')
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
krestik_color.grid(padx=0, pady=0, row=0,column=8, sticky='nsew')
#
save_pattern = tkinter.Button(window, text ="Зберегти шаблон",command = my_file)
save_pattern.config(bg="lightgreen",fg="black")
save_pattern.grid(padx=0, pady=0, row=1,column=8, sticky='nsew')
#
cm = Menu(m)
m.add_cascade(label="Колір", menu=cm)
cm.add_command(label="Червоний", command=colorR)
cm.add_command(label="Темно-зелений", command=colordG)
cm.add_command(label="Синій", command=colorB)
cm.add_command(label="Жовтий", command=colorY)
cm.add_command(label="Зелений", command=colorG)
cm.add_command(label="Білий", command=colorW)
#
mc = Menu(m)
m.add_cascade(label="Довідка", menu=mc)
mc.add_command(label="Путівник Користувача", command=click)
#
window.mainloop()
