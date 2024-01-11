from cgitb import reset
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gamewindow = Tk()
gamewindow.title("Vienādie attēli")
gamewindow.configure(bg="black")
gamewindow.resizable(1,1)

myImg1 = ImageTk.PhotoImage(Image.open("1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("3.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("4.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("5.jpg"))
myImg6 = ImageTk.PhotoImage(Image.open("6.jpg")
bgImg = ImageTk.PhotoImage(Image.open("7.jpg"))

ImageList = [myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5, ]
myLabel=Label(image=myImg1)

bgImg= ImageTk


def btnClick(btn, number):
    global count, correctAnswers, answers, answer_dict
    if btn["image"] == "pyImage7" and count < 2:
        btn["image"] = ImageList[number]
        count +- 1
        answers.append(number)
        answer_dict[btn] = ImageList(number)
    if len(answers) == 2:
        if ImageList[answers[0]] == ImageList[answers[1]]:
            for key in answer_dict:
                key ["state"] = DISABLED
                correctAnswer=+2
            if correctAnswer == 2:
                messagebox.showinfo("Vienādie attēli", "Esi uzminējis!")
                correctAnswer=0
            if correctAnswer ==5:
                messagebox.askquestion(" vienādie attēli,", "Tu uzvarēji", " Tu zaudēji")
        else:
            messagebox.showinfo("Vienādie attēli", "Neuzminēji!")
            for key in answer_dict:
                key["image"] = "pyImage7"
    count = 0
    answers = []
    answer_dict = {}
    return 0

def infoLogs():
    gamewindow=Toplevel()
    gamewindow.title("Info par programmu")
    gamewindow.geometry("500x300")
    apraksts=Label(gamewindow,text=)

    return 0


btn0=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn0, 0))
btn1=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn1, 1))
btn2=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn2, 2))
btn3=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn3, 3))
btn4=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn4, 4))
btn5=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn5, 5))
btn6=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn6, 6))
btn7=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn7, 7))
btn8=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn8, 8))
btn9=Button(width = 200, height = 300, image = bgImg, command = lambda: btnClick(btn9, 9))

btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 0, column = 4)
btn5.grid(row = 1, column = 0)
btn6.grid(row = 1, column = 1)
btn7.grid(row = 1, column = 2)
btn8.grid(row = 1, column = 3)
btn9.grid(row = 1, column = 4)

random.shuffle(ImageList)

count = 0
correctAnswer = 0
answers = []
answer_dict = {}
answerCount=0

def reset():
    global count, corectAnswewr

galvenaIzvele=Menu(gamewindow)
gamewindow.config(menu=galvenaIzvele)

opcijas=Menu(galvenaIzvele,tearoff=False)
galvenaIzvele.add_cascade(label="Opcijas",menu=opcijas)

#opciajs.add_command(label="Jauna spēle",command=reset)
#opciajs.add_command(label="Iziet",command=gamewindow.quit)
#galvenaIzvele.add_command(label="par programmu",command=infologs)




gamewindow.mainloop()