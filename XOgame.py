from tkinter import *

class startWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome to X O game")
        self.window.geometry("500x500")
        self.window.minsize(500,500)
        self.window.maxsize(500,500)
        self.window.config(background='black')
        
        startLabel = Label(self.window,text = "Don't forget to save your choice",bg='black',fg='white',font=("Arial", 10))
        startLabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        
        self.startEntryVariable = StringVar()
        self.startEntryVariable.set('type x or o')
        startEntry = Entry(self.window,textvariable=self.startEntryVariable)
        startEntry.place(relx=0.5,rely=0.4,anchor=CENTER)
        
        saveChoice = Button(self.window,text='Save Choice',command = self.getChoice)
        saveChoice.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        startButton = Button(self.window,text='Start',command = lambda: self.letsPlay(self.window)) 
        '''
        if called directly, it would immediately call the letsPlay method with self.window as an argument when the button is created, rather than waiting for the button to be clicked.
        This is because in Python, the function is called immediately when it's passed as an argument like this.
        Using Lambda to Delay Execution: To delay the execution of self.letsPlay(self.window) until the button is clicked,we use a lambda function.
        The lambda function acts as a wrapper around self.letsPlay(self.window), ensuring that self.letsPlay(self.window) is only called when the button is clicked.
        '''
        startButton.place(relx=0.5,rely=0.6,anchor=CENTER)
        
        quitButton = Button(self.window,text='Quit',command = self.window.destroy)
        quitButton.place(relx=0.5,rely=0.7,anchor=CENTER)
        
        self.startShape = 1
        self.matrix = [['','',''],['','',''],['','','']]
        self.message = 'You Won !!'
        
    
    def getChoice(self):
        userInput = self.startEntryVariable.get()
        self.startShapeMethode(userInput)
    
    def createFrames(self,window):
        frames = []
        j = 0
        for i in range(0,9):
            if(i%3==0 and i!=0):
                j+=1
            frames.append(Frame(window,background='white',height=155,width=155))
            frames[i].grid(column=i%3,row=j,padx=5,pady=5)
        return frames
    
    
    def startShapeMethode(self,startEntry):
        if(startEntry == 'x'):
            self.startShape = 1
        else:
            self.startShape = 0
    
    def winLoseTest(self,matrix,window):
        if(''.join(matrix[0]) == 'xxx' or ''.join(matrix[0]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join(matrix[1]) == 'xxx' or ''.join(matrix[1]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join(matrix[2]) == 'xxx' or ''.join(matrix[2]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join([matrix[0][0],matrix[1][0],matrix[2][0]]) == 'xxx' or ''.join([matrix[0][0],matrix[1][0],matrix[2][0]]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join([matrix[0][1],matrix[1][1],matrix[2][1]]) == 'xxx' or ''.join([matrix[0][1],matrix[1][1],matrix[2][1]]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join([matrix[0][2],matrix[1][2],matrix[2][2]]) == 'xxx' or ''.join([matrix[0][2],matrix[1][2],matrix[2][2]]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join([matrix[0][0],matrix[1][1],matrix[2][2]]) == 'xxx' or ''.join([matrix[0][0],matrix[1][1],matrix[2][2]]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(''.join([matrix[0][2],matrix[1][1],matrix[2][0]]) == 'xxx' or ''.join([matrix[0][2],matrix[1][1],matrix[2][0]]) == 'ooo'):
            self.endGame(window,self.message)
            return
        if(all(cell != '' for row in matrix for cell in row)):
            self.message = 'Draw'
            self.endGame(window,self.message)
    
    def returnHomeWin(self):
        self.window.deiconify()
        self.playWindow.destroy()
        self.matrix = [['','',''],['','',''],['','','']]
    
    def endGame(self,window,message):
        for widgets in window.winfo_children():
            widgets.destroy()
        
        winLabel = Label(window,text=message,bg='white', fg='black',font=("Arial", 20))
        winLabel.place(relx=0.5,rely=0.4,anchor=CENTER)
        
        homeButton = Button(self.playWindow,text='Home',command = self.returnHomeWin) 
        homeButton.place(relx=0.5,rely=0.5,anchor=CENTER)
        window.config(background='white')
    
    def showCanvas_SaveStats(self,frame,window):
        
        canva = Canvas(frame,height=155,width=155)
        canva.pack()
        
        if(str(frame).split('e')[1]==''):
            i=0
        else:
            i = int(str(frame).split('e')[1]) - 1
        
        
        if(self.startShape % 2 != 0): #x
            canva.create_line(10,10,145,145,fill='blue',width=10)
            canva.create_line(10,145,145,10,fill='blue',width=10)
            self.matrix[i//3][i%3] = 'x'
        else: #o
            canva.create_oval(5,5,150,150,width=10,outline='red')
            self.matrix[i//3][i%3] = 'o'
        
        self.winLoseTest(self.matrix,window)
        self.startShape = self.startShape + 1
        
        
    
    def letsPlay(self,window):
        
        window.withdraw()
        
        self.playWindow = Tk()
        self.playWindow.title("X/O")
        self.playWindow.geometry("500x500")
        self.playWindow.minsize(500,500)
        self.playWindow.maxsize(500,500)
        self.playWindow.config(background='black')
        
        framesList = self.createFrames(self.playWindow)
        
        for frame in framesList:
            frame.bind('<Button-1>',lambda event ,f=frame : self.showCanvas_SaveStats(f,window = self.playWindow))
        
        '''
        used this to capture the iterable and its value 
        <caus lambda in an iterable state it just keeps its form (kay b9aw fiha les variable)
        mli kat sali l iteration 3ad kay t3awdo dok les variables bl value lekhra dyal l iterable argument 
        dakchi 3lach u must change the argument name when calling lambda f iteration
        
        kholasa hh
        In Python, using a lambda function in a loop can lead to unexpected behavior due to late binding.
        This means the lambda function captures the variable, not the value.
        So, if the lambda uses loop variables, it will use the final value of the variable, not the value it had when the function was defined.
        
        event : This is the event object that Tkinter passes automatically when the event occurs. 
        You don't need to explicitly pass it, but it will be received by the lambda function as the first argument.
        ''' 
                    
        self.playWindow.mainloop()
    
    def startGame(self,window):
        window.mainloop()
    

XO_game = startWindow()

XO_game.startGame(XO_game.window)