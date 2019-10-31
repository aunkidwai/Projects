import tkinter as tk

class TicTacToeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default = "")
        tk.Tk.wm_title(self, "Tic Tac Toe")
        tk.Tk.wm_resizable(self, 0, 0)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #menubar = tk.Menu(container)

        #aboutmenu = tk.Menu(menubar, tearoff=0)
        #aboutmenu.add_command(label="The Game")
        #aboutmenu.add_command(label="The Developer")
        #menubar.add_cascade(label="About", menu=aboutmenu)

        #tk.Tk.config(self, menu = menubar)

        self.frames = {}

        for F in (StartPage, GamePage, ResultPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "white")

        #title
        label = tk.Label(self, text = "Tic Tac Toe", font = "Times 30 bold", bg = "white", padx = 20, pady = 50)
        label.pack()

        name1 = tk.Label(self, text="Player 1", bg="white", pady = 20)
        player1 = tk.Entry(self)
        name1.pack()
        player1.pack()

        name2 = tk.Label(self, text="Player 2", bg="white", pady = 20)
        player2 = tk.Entry(self)
        name2.pack()
        player2.pack()

        def play():
            n1 = player1.get()
            n2 = player2.get()
            var1.set(n1)
            var2.set(n2)
            controller.show_frame(GamePage)

        global var1
        global var2
        var1 = tk.StringVar()
        var2 = tk.StringVar()

        button1 = tk.Button(self, text = "Play", command = play)
        button1.pack(pady = 40)

class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg = "white")

        label = tk.Label(self, text="Tic Tac Toe", font="Times 30 bold", bg="white", padx=20, pady=50)
        label.pack()

        frame2 = tk.Frame(self, width=500, height=200, relief="flat", highlightthickness=0)
        frame2.pack()

        global turn
        turn = 1

        def clicked1():
            global turn
            if btn1["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn1["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn1["text"] = "O"
                check()

        def clicked2():
            global turn
            if btn2["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn2["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn2["text"] = "O"
                check()

        def clicked3():
            global turn
            if btn3["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn3["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn3["text"] = "O"
                check()

        def clicked4():
            global turn
            if btn4["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn4["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn4["text"] = "O"
                check()

        def clicked5():
            global turn
            if btn5["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn5["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn5["text"] = "O"
                check()

        def clicked6():
            global turn
            if btn6["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn6["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn6["text"] = "O"
                check()

        def clicked7():
            global turn
            if btn7["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn7["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn7["text"] = "O"
                check()

        def clicked8():
            global turn
            if btn8["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn8["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn8["text"] = "O"
                check()

        def clicked9():
            global turn
            if btn9["text"] == " ":  # For getting the text of a button
                if turn == 1:
                    turn = 2
                    btn9["text"] = "X"
                elif turn == 2:
                    turn = 1
                    btn9["text"] = "O"
                check()

        global flag
        flag = 1

        def check():
            global flag
            b1 = btn1["text"]
            b2 = btn2["text"]
            b3 = btn3["text"]
            b4 = btn4["text"]
            b5 = btn5["text"]
            b6 = btn6["text"]
            b7 = btn7["text"]
            b8 = btn8["text"]
            b9 = btn9["text"]

            flag = flag + 1

            if (b1 == b2  == b3  == "O") or (b4 == b5  == b6  == "O") or (b7 == b8  == b9  == "O") or \
               (b1 == b4  == b7  == "O") or (b2 == b5  == b8  == "O") or (b3 == b6  == b9  == "O") or \
               (b1 == b5  == b9  == "O") or (b3 == b5  == b7  == "O"):
                win("Player 2")

            elif (b1 == b2  == b3  == "X") or (b4 == b5  == b6  == "X") or (b7 == b8  == b9  == "X") or \
               (b1 == b4  == b7  == "X") or (b2 == b5  == b8  == "X") or (b3 == b6  == b9  == "X") or \
               (b1 == b5  == b9  == "X") or (b3 == b5  == b7  == "X"):
                win("Player 1")

            elif (flag == 10):
                draw()

        def win(player):
            wins.set(player + " wins the game")
            controller.show_frame(ResultPage)

        global wins
        wins = tk.StringVar()

        def draw():
            draws.set("Game Draw")
            controller.show_frame(ResultPage)

        global draws
        draws = tk.StringVar()

        btn1 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked1)
        btn1.grid(row=0, column=0)
        btn2 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked2)
        btn2.grid(row=0, column=1)
        btn3 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked3)
        btn3.grid(row=0, column=2)
        btn4 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked4)
        btn4.grid(row=1, column=0)
        btn5 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked5)
        btn5.grid(row=1, column=1)
        btn6 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked6)
        btn6.grid(row=1, column=2)
        btn7 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked7)
        btn7.grid(row=2, column=0)
        btn8 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked8)
        btn8.grid(row=2, column=1)
        btn9 = tk.Button(frame2, text=" ", bg="white", fg="Black", width=4, height=2, relief="flat", font="Times 30 bold",command=clicked9)
        btn9.grid(row=2, column=2)

        frame1 = tk.Frame(self, width = 500, height = 200, bg = "white", relief="ridge", highlightthickness = 0)
        frame1.pack()

        global playername1
        global playername2

        text1 = tk.Label(frame1, text = "{ X } Player 1: ", bg = "white")
        playername1 = tk.Label(frame1, textvariable=var1, bg = "white")

        text2 = tk.Label(frame1, text="{ O } Player 2: ", bg = "white")
        playername2 = tk.Label(frame1, textvariable=var2, bg = "white")

        text1.grid(row = 0, column = 0, pady = 20)
        playername1.grid(row = 0, column = 1)

        text2.grid(row = 1, column = 0)
        playername2.grid(row = 1, column = 1)

        #button2 = tk.Button(self, text="Home", command=lambda: controller.show_frame(ResultPage))
        #button2.pack()

class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg="white")

        label = tk.Label(self, text="Tic Tac Toe", font="Times 30 bold", bg="white", padx=20, pady=50)
        label.pack()

        result = tk.Label(self, textvariable = wins, font="Times 20 bold", bg="white", padx=20, pady=50)
        result.pack()
        result = tk.Label(self, textvariable = draws, font="Times 30 bold", bg="white", padx=20, pady=50)
        result.pack()

        button2 = tk.Button(self, text="Exit", command=quit)
        button2.pack()

app = TicTacToeApp()
app.geometry("500x600")
app.mainloop()