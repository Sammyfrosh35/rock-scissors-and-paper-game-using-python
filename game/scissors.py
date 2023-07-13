from tkinter import *
from PIL import Image,ImageTk
from random import randint


#main window
root = Tk()
root.title("rock scissors paper")
root.configure(background="grey")

#pictures
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#inser pictures
user_label= Label(root,image=scissors_img, bg="grey")
comp_label= Label(root,image=scissors_img_comp, bg="grey")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


#scores
playerscore = Label(root,text=0,font=100,fg="white",bg="grey")
computerscore= Label(root,text=0,font=100,fg="white", bg="grey")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicator
user_indicator = Label(root,font=50,text="USER"
                       ,bg="grey").grid(row=0,column=3,)
computer_indicator = Label(root,font=50,text="COMPUTER"
                           ,bg="grey").grid(row=0,column=1)

#messages
msg =Label(root, font=50, bg="grey",
           fg="white").grid(row=3, column=2)

#updatemessage
def updatemessage(x):
    msg['text']= x 


#update user score
def updateusescore():
    score = int(playerscore["text"])
    score +=1
    playerscore["text"] = str(score)

#updatecomputer score
def updatecompscore():
    score = int(computerscore["text"])
    score +=1
    computerscore["text"] = str(score)

#check winner
def checkwinner(player,computer):
    if player == computer:
        updatemessage("its a tie")
    elif player == "rock":
        if computer == "paper":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateusescore()
    elif player=="paper":
        if computer == "scissors":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateusescore()

    elif player == "scissors":
        if computer == "rock":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateusescore()
    else:
        pass


     



#update choices
choices = ["rock", "paper" , "scissors"]
def updatechoices(x):
#for computer 
    compchoice = choices[randint(0,2)]
    if  compchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)




#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
   
    checkwinner(x, compchoice)





#button
rock =Button(root,width=20,height=2,text='ROCK',bg="red",
             fg="white", command= lambda:updatechoices("rock")).grid(row=2,column=1)
paper =Button(root,width=20,height=2,text='PAPER',bg="yellow",
              fg="white",command= lambda:updatechoices("paper")).grid(row=2,column=2)
scissors =Button(root,width=20,height=2,text='SCISSORS',bg="blue",
                 fg="white",command= lambda:updatechoices("scissors")).grid(row=2,column=3)




root.mainloop()