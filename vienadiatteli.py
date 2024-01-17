#from cgitb import reset
from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox

gamewindow = Tk()
gamewindow.title("Vienādie attēli")
gamewindow.configure(bg="black")
gamewindow.resizable(1,1)

count = 0
correctAnswer = 0
answers = []
answer_dict = {}
answerCount=0

myImg1 = ImageTk.PhotoImage(Image.open("1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("3.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("4.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("5.jpg"))
myImg6 = ImageTk.PhotoImage(Image.open("6.jpg"))
bgImg = ImageTk.PhotoImage(Image.open("7.jpg"))

ImageList = [myImg1, myImg1, myImg2, myImg2, myImg3, myImg3, myImg4, myImg4, myImg5, myImg5,myImg6, myImg6 ]
myLabel=Label(image=myImg1)

bgImg= ImageTk.PhotoImage(Image.open("7.jpg"))

#pogas
btn0=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn0, 0))
btn1=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn1, 1))
btn2=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn2, 2))
btn3=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn3, 3))
btn4=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn4, 4))
btn5=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn5, 5))
btn6=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn6, 6))
btn7=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn7, 7))
btn8=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn8, 8))
btn9=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn9, 9))
btn10=Button(width=200,height=00, image = bgImg, command = lambda: btnClick(btn10, 10))
btn11=Button(width=200,height=200, image = bgImg, command = lambda: btnClick(btn11, 11))

#pogu novietojums
btn0.grid(row = 1, column = 1)
btn1.grid(row = 2, column = 2)
btn2.grid(row = 3, column = 3)
btn3.grid(row = 1, column = 4)
btn4.grid(row = 2, column = 1)
btn5.grid(row = 3, column = 2)
btn6.grid(row = 1, column = 3)
btn7.grid(row = 2, column = 4)
btn8.grid(row = 3, column = 1)
btn9.grid(row = 1, column = 2)
btn10.grid(row = 2, column = 3)
btn11.grid(row = 3, column = 4)

random.shuffle(ImageList)

count = 0
correctAnswer = 0
answers = []
answer_dict = {}
answerCount=0

def reset():
    global count, correctAnswer, answers, answer_dict, answerCount
    count=0
    answerCount=0
    correctAnswer = 0
    answers=[]
    answer_dict={}
    btn0.config(state=NORMAL)
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)


    btn0["image"]="pyimage7"#bg attēls virs 
    btn1["image"]="pyimage7"
    btn2["image"]="pyimage7"
    btn3["image"]="pyimage7"
    btn4["image"]="pyimage7"
    btn5["image"]="pyimage7"
    btn6["image"]="pyimage7"
    btn7["image"]="pyimage7"
    btn8["image"]="pyimage7"
    btn9["image"]="pyimage7"
    btn10["image"]="pyimage7"
    btn11["image"]="pyimage7"

    random.shuffle(ImageList)

    count=0
    correctAnswers=0
    answers=[]
    answer_dict={}
    answerCount=0

    return 0

def infoLogs():# info logs
    gamewindow=Toplevel()
    gamewindow.title("Info par programmu")
    gamewindow.geometry("500x300")
    apraksts=Label(gamewindow,text="Atmini 2 vienādus attēlus")
    apraksts.grid(row=0,column=0)
       
    return 0

#def btnClick(btn, number):# pogu funkcija lai klikšķinātu
    global count, correctAnswer, answers, answer_dict
    if btn["image"] == "pyImage7" and count < 2:
        btn["image"] = ImageList[number]
        count += 1
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

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict, answerCount
    if btn["image"]=="pyimage7" and count<2:
        btn["image"]=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2:
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers=+2
            if correctAnswers==2:
                messagebox.showinfo("Vienādi attēli", "Esi uzminējis")
                correctAnswers=0
                answerCount+=1
        else:
            messagebox.showinfo("Vienādi attēli","Neuzminēji")
            for key in answer_dict:
                key["image"]="pyimage7"
        count=0
        answers=[]
        answer_dict={}
    if answerCount==6:
        messagebox.showinfo("Vienādi attēli","Tu uzvareji")
        reset()
    return 0


galvenaIzvele=Menu(gamewindow)
gamewindow.config(menu=galvenaIzvele)

opcijas=Menu(galvenaIzvele,tearoff=False)
galvenaIzvele.add_cascade(label="Opcijas",menu=opcijas)
galvenaIzvele.add_command(label="par programmu",command=infoLogs)

#opciajs.add_command(label="Jauna spēle",command=reset)
#opciajs.add_command(label="Iziet",command=gamewindow.quit)


gamewindow.mainloop()