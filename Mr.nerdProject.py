from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as tts;
from tkinter import *



my_bot = ChatBot(name='Mr.Nerd', read_only=True,
          logic_adapters=
['chatterbot.logic.MathematicalEvaluation',
          'chatterbot.logic.BestMatch'])
small_talk = ['hi!',
          'hello!',
          'how do you do?',
          'how are you?',
          'i\'m cool.',
          'fine, you?',
          'always cool.',
          'i\'m ok',
          'glad to hear that.',
          'i\'m fine',
          'glad to hear that.',
          'i feel awesome',
          'excellent, glad to hear that.',
          'not so good',
          'sorry to hear that.',
          'what\'s your name?',
          'i\'m Mr.Nerd. ask me a math question, please.',
              'bye',
              'good bye it was nice talk']
math_talk_5 = ['sum of angles',
               'sin(A + B) = sin(A).cos(B) + cos(A)sin(B)']
math_talk_6 = ['area of triangle',
               'Area = ½ × base × height']
math_talk_7 = ['sine',
               'a/sin A = b/sin B = c/sin C']  
math_talk_4 =['calculating the percentage',
              'Percentage= (Value/Total Value)×100']
list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk_5, math_talk_6 ,math_talk_7 ,math_talk_4):
          list_trainer.train(item)


engine=tts.init()
engine.setProperty('rate',125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def ask_bot():
    query=user_input.get()
    answer=my_bot.get_response(query)
    ChatBox.insert(END,"You :"+query)
    ChatBox.insert(END,"Mr.Nerd :"+str(answer))
    engine.say(str(answer))
    user_input.delete(0,END)
    ChatBox.yview(END)
    engine.runAndWait()







root = Tk()

root.geometry('500x600')
root.title('Mr.Nerd')
#Background
bgimage = PhotoImage(file='AQ.png')
bgLabel = Label(root,image=bgimage)
bgLabel.place(x=0,y=0)
root.resizable(False,False)
#small pic
smlimage = PhotoImage(file="Uu.png")
smlLabel=Label(root, image=smlimage,bd=0)
smlLabel.place(x=0, y=72)

#Entry Label
enterlaw1 = Label(root,text='Welcome To Mr.Nerd!',font=('castellar',19,'bold'),foreground='white',background='#001E1F')
enterlaw1.place(x=125,y=115)

#ChatBox + ScrollBar
frame=Frame(root)
SC=Scrollbar(frame)
ChatBox=Listbox(frame,width=45,heigh=7,font=('times new roman',16),yscrollcommand=SC.set)
SC.config(command=ChatBox.yview)
SC.pack(side=RIGHT,fill=Y)
ChatBox.place(x=0,y=200)
frame.pack(pady=200)
ChatBox.pack(pady=15)

#user intery
user_input = Entry(root,font=('times new roman',15),width= 50, bd=1,relief=GROOVE)
user_input.place(x=0, y=450)
#Button
askButton = Button(root,bg='#00A79D',fg='white',text='Ask Mr.Nerd', font=('times new roman',16),command=ask_bot, cursor='hand2',activebackground='#E8D989')
askButton.place(x=187,y=500)

#EF982F

enterlaw = Label(root,text='Enter the name of the law',font=('times new roman',18,'bold'),foreground='white',background='#001E1F')
enterlaw.place(x=123,y=405)

#Icon
root.iconbitmap(r"C:\Users\96650\Desktop\LRChatbot\iconfinder-10-avatar-2754575_120521.ico")

root.mainloop()
