from tkinter import *

class drawf:
    board=[["b","0","b","0","b","0","b","0"],["0","b","0","b","0","b","0","b"],["b","0","b","0","b","0","b","0"],["0","1","0","1","0","1","0","1"],["1","0","1","0","1","0","1","0"],["0","w","0","w","0","w","0","w"],["w","0","w","0","w","0","w","0"],["0","w","0","w","0","w","0","w"]]
    def showboard(self):
        for i in self.board:
            print(i)

class checkerbuttons(Button):
    position=None
    name=None
    def setposition(self,x,y):
        self.position=(x,y)

def place(b1,b2,b3):
    if d1.board[b2.position[0]][b2.position[1]]=="b" and b1.position[0]==7:
            d1.board[b2.position[0]][b2.position[1]]="kb"
            b2.config(image=b_king)
    elif d1.board[b2.position[0]][b2.position[1]]=="w" and b1.position[0]==0:
            d1.board[b2.position[0]][b2.position[1]]="kw"
            b2.config(image=w_king)
    if b3==None:
        d1.board[b1.position[0]][b1.position[1]]=d1.board[b2.position[0]][b2.position[1]]
        d1.board[b2.position[0]][b2.position[1]]="1"
        b1.config(image=b2.cget("image"))
        b2.config(image="")
        
        
    else:
        d1.board[b1.position[0]][b1.position[1]]=d1.board[b2.position[0]][b2.position[1]]
        d1.board[b2.position[0]][b2.position[1]]="1"
        d1.board[b3.position[0]][b3.position[1]]="1"
        b1.config(image=b2.cget("image"))
        b2.config(image="")
        b3.config(image="")

    globals()["b00"].config(command=lambda:move(globals()["b00"]),bg="#617905")
    globals()["b02"].config(command=lambda:move(globals()["b02"]),bg="#617905")
    globals()["b04"].config(command=lambda:move(globals()["b04"]),bg="#617905")
    globals()["b06"].config(command=lambda:move(globals()["b06"]),bg="#617905")
    globals()["b11"].config(command=lambda:move(globals()["b11"]),bg="#617905")
    globals()["b13"].config(command=lambda:move(globals()["b13"]),bg="#617905")
    globals()["b15"].config(command=lambda:move(globals()["b15"]),bg="#617905")
    globals()["b17"].config(command=lambda:move(globals()["b17"]),bg="#617905")
    globals()["b20"].config(command=lambda:move(globals()["b20"]),bg="#617905")
    globals()["b22"].config(command=lambda:move(globals()["b22"]),bg="#617905")
    globals()["b24"].config(command=lambda:move(globals()["b24"]),bg="#617905")
    globals()["b26"].config(command=lambda:move(globals()["b26"]),bg="#617905")
    globals()["b31"].config(command=lambda:move(globals()["b31"]),bg="#617905")
    globals()["b33"].config(command=lambda:move(globals()["b33"]),bg="#617905")
    globals()["b35"].config(command=lambda:move(globals()["b35"]),bg="#617905")
    globals()["b37"].config(command=lambda:move(globals()["b37"]),bg="#617905")
    globals()["b40"].config(command=lambda:move(globals()["b40"]),bg="#617905")
    globals()["b42"].config(command=lambda:move(globals()["b42"]),bg="#617905")
    globals()["b44"].config(command=lambda:move(globals()["b44"]),bg="#617905")
    globals()["b46"].config(command=lambda:move(globals()["b46"]),bg="#617905")
    globals()["b51"].config(command=lambda:move(globals()["b51"]),bg="#617905")
    globals()["b53"].config(command=lambda:move(globals()["b53"]),bg="#617905")
    globals()["b55"].config(command=lambda:move(globals()["b55"]),bg="#617905")
    globals()["b57"].config(command=lambda:move(globals()["b57"]),bg="#617905")
    globals()["b60"].config(command=lambda:move(globals()["b60"]),bg="#617905")
    globals()["b62"].config(command=lambda:move(globals()["b62"]),bg="#617905")
    globals()["b64"].config(command=lambda:move(globals()["b64"]),bg="#617905")
    globals()["b66"].config(command=lambda:move(globals()["b66"]),bg="#617905")
    globals()["b71"].config(command=lambda:move(globals()["b71"]),bg="#617905")
    globals()["b73"].config(command=lambda:move(globals()["b73"]),bg="#617905")
    globals()["b75"].config(command=lambda:move(globals()["b75"]),bg="#617905")
    globals()["b77"].config(command=lambda:move(globals()["b77"]),bg="#617905")



def move(button):
    x=int(button.position[0])
    y=int(button.position[1])
    buttonlist=["b00","b02","b04","b06","b11","b13","b15","b17","b20","b22","b24","b26","b31","b33","b35","b37","b40","b42","b44","b46","b51","b53","b55","b57","b60","b62","b64","b66","b71","b73","b75","b77"]
    if "k" in d1.board[x][y]:
        m=(d1.board[x][y])[1]
        if m=="b":n="w"
        elif m=="w":n="b"
        if 0<=x+1<=7 and 0<=y-1<=7:
            if d1.board[x+1][y-1]=="1":
                globals()[f"b{x+1}{y-1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+1}{y-1}"],button,None))
                buttonlist.remove(f"b{x+1}{y-1}")
            elif n in d1.board[x+1][y-1] and 0<=x+2<=7 and 0<=y-2<=7 and d1.board[x+2][y-2]=="1":
                globals()[f"b{x+2}{y-2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+2}{y-2}"],button,globals()[f"b{x+1}{y-1}"]))
                buttonlist.remove(f"b{x+2}{y-2}")

        if 0<=x+1<=7 and 0<=y+1<=7:
            if d1.board[x+1][y+1]=="1":
                globals()[f"b{x+1}{y+1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+1}{y+1}"],button,None))
                buttonlist.remove(f"b{x+1}{y+1}")
            elif n in d1.board[x+1][y+1] and 0<=x+2<=7 and 0<=y+2<=7 and d1.board[x+2][y+2]=="1":
                globals()[f"b{x+2}{y+2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+2}{y+2}"],button,globals()[f"b{x+1}{y+1}"]))
                buttonlist.remove(f"b{x+2}{y+2}")

        if 0<=x-1<=7 and 0<=y-1<=7:
            if d1.board[x-1][y-1]=="1":
                globals()[f"b{x-1}{y-1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-1}{y-1}"],button,None))
                buttonlist.remove(f"b{x-1}{y-1}")
            elif n in d1.board[x-1][y-1] and 0<=x-2<=7 and 0<=y-2<=7 and d1.board[x-2][y-2]=="1":
                globals()[f"b{x-2}{y-2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-2}{y-2}"],button,globals()[f"b{x-1}{y-1}"]))
                buttonlist.remove(f"b{x-2}{y-2}")

        if 0<=x-1<=7 and 0<=y+1<=7:
            if d1.board[x-1][y+1]=="1":
                globals()[f"b{x-1}{y+1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-1}{y+1}"],button,None))
                buttonlist.remove(f"b{x-1}{y+1}")
            elif n in d1.board[x-1][y+1] and 0<=x-2<=7 and 0<=y+2<=7 and d1.board[x-2][y+2]=="1":
                globals()[f"b{x-2}{y+2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-2}{y+2}"],button,globals()[f"b{x-1}{y+1}"]))
                buttonlist.remove(f"b{x-2}{y+2}")

    
    elif "b" in d1.board[x][y]:
        if 0<=x+1<=7 and 0<=y-1<=7:
            if d1.board[x+1][y-1]=="1":
                globals()[f"b{x+1}{y-1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+1}{y-1}"],button,None))
                buttonlist.remove(f"b{x+1}{y-1}")
            elif "w" in d1.board[x+1][y-1] and 0<=x+2<=7 and 0<=y-2<=7 and d1.board[x+2][y-2]=="1":
                globals()[f"b{x+2}{y-2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+2}{y-2}"],button,globals()[f"b{x+1}{y-1}"]))
                buttonlist.remove(f"b{x+2}{y-2}")

        if 0<=x+1<=7 and 0<=y+1<=7:
            if d1.board[x+1][y+1]=="1":
                globals()[f"b{x+1}{y+1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+1}{y+1}"],button,None))
                buttonlist.remove(f"b{x+1}{y+1}")
            elif "w" in d1.board[x+1][y+1] and 0<=x+2<=7 and 0<=y+2<=7 and d1.board[x+2][y+2]=="1":
                globals()[f"b{x+2}{y+2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x+2}{y+2}"],button,globals()[f"b{x+1}{y+1}"]))
                buttonlist.remove(f"b{x+2}{y+2}")

    elif "w" in d1.board[x][y]:
        if 0<=x-1<=7 and 0<=y-1<=7:
            if d1.board[x-1][y-1]=="1":
                globals()[f"b{x-1}{y-1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-1}{y-1}"],button,None))
                buttonlist.remove(f"b{x-1}{y-1}")
            elif "b" in d1.board[x-1][y-1] and 0<=x-2<=7 and 0<=y-2<=7 and d1.board[x-2][y-2]=="1":
                globals()[f"b{x-2}{y-2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-2}{y-2}"],button,globals()[f"b{x-1}{y-1}"]))
                buttonlist.remove(f"b{x-2}{y-2}")

        if 0<=x-1<=7 and 0<=y+1<=7:
            if d1.board[x-1][y+1]=="1":
                globals()[f"b{x-1}{y+1}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-1}{y+1}"],button,None))
                buttonlist.remove(f"b{x-1}{y+1}")
            elif "b" in d1.board[x-1][y+1] and 0<=x-2<=7 and 0<=y+2<=7 and d1.board[x-2][y+2]=="1":
                globals()[f"b{x-2}{y+2}"].config(bg="lightblue",command=lambda:place(globals()[f"b{x-2}{y+2}"],button,globals()[f"b{x-1}{y+1}"]))
                buttonlist.remove(f"b{x-2}{y+2}")
    if "b00" in buttonlist:
        globals()["b00"].config(command=lambda:move(globals()["b00"]),bg="#617905")
    if "b02" in buttonlist:
        globals()["b02"].config(command=lambda:move(globals()["b02"]),bg="#617905")
    if "b04" in buttonlist:
        globals()["b04"].config(command=lambda:move(globals()["b04"]),bg="#617905")
    if "b06" in buttonlist:
        globals()["b06"].config(command=lambda:move(globals()["b06"]),bg="#617905")
    if "b11" in buttonlist:
        globals()["b11"].config(command=lambda:move(globals()["b11"]),bg="#617905")
    if "b13" in buttonlist:
        globals()["b13"].config(command=lambda:move(globals()["b13"]),bg="#617905")
    if "b15" in buttonlist:
        globals()["b15"].config(command=lambda:move(globals()["b15"]),bg="#617905")
    if "b17" in buttonlist:
        globals()["b17"].config(command=lambda:move(globals()["b17"]),bg="#617905")
    if "b20" in buttonlist:
        globals()["b20"].config(command=lambda:move(globals()["b20"]),bg="#617905")
    if "b22" in buttonlist:
        globals()["b22"].config(command=lambda:move(globals()["b22"]),bg="#617905")
    if "b24" in buttonlist:
        globals()["b24"].config(command=lambda:move(globals()["b24"]),bg="#617905")
    if "b26" in buttonlist:
        globals()["b26"].config(command=lambda:move(globals()["b26"]),bg="#617905")
    if "b31" in buttonlist:
        globals()["b31"].config(command=lambda:move(globals()["b31"]),bg="#617905")
    if "b33" in buttonlist:
        globals()["b33"].config(command=lambda:move(globals()["b33"]),bg="#617905")
    if "b35" in buttonlist:
        globals()["b35"].config(command=lambda:move(globals()["b35"]),bg="#617905")
    if "b37" in buttonlist:
        globals()["b37"].config(command=lambda:move(globals()["b37"]),bg="#617905")
    if "b40" in buttonlist:
        globals()["b40"].config(command=lambda:move(globals()["b40"]),bg="#617905")
    if "b42" in buttonlist:
        globals()["b42"].config(command=lambda:move(globals()["b42"]),bg="#617905")
    if "b44" in buttonlist:
        globals()["b44"].config(command=lambda:move(globals()["b44"]),bg="#617905")
    if "b46" in buttonlist:
        globals()["b46"].config(command=lambda:move(globals()["b46"]),bg="#617905")
    if "b51" in buttonlist:
        globals()["b51"].config(command=lambda:move(globals()["b51"]),bg="#617905")
    if "b53" in buttonlist:
        globals()["b53"].config(command=lambda:move(globals()["b53"]),bg="#617905")
    if "b55" in buttonlist:
        globals()["b55"].config(command=lambda:move(globals()["b55"]),bg="#617905")
    if "b57" in buttonlist:
        globals()["b57"].config(command=lambda:move(globals()["b57"]),bg="#617905")
    if "b60" in buttonlist:
        globals()["b60"].config(command=lambda:move(globals()["b60"]),bg="#617905")
    if "b62" in buttonlist:
        globals()["b62"].config(command=lambda:move(globals()["b62"]),bg="#617905")
    if "b64" in buttonlist:
        globals()["b64"].config(command=lambda:move(globals()["b64"]),bg="#617905")
    if "b66" in buttonlist:
        globals()["b66"].config(command=lambda:move(globals()["b66"]),bg="#617905")
    if "b71" in buttonlist:
        globals()["b71"].config(command=lambda:move(globals()["b71"]),bg="#617905")
    if "b73" in buttonlist:
        globals()["b73"].config(command=lambda:move(globals()["b73"]),bg="#617905")
    if "b75" in buttonlist:
        globals()["b75"].config(command=lambda:move(globals()["b75"]),bg="#617905")
    if "b77" in buttonlist:
        globals()["b77"].config(command=lambda:move(globals()["b77"]),bg="#617905")

d1=drawf()
root=Tk()
root.title("CHECKERS GAME")
root.minsize(width=800,height=800)
root.config(bg="#2B3035")
icon=PhotoImage(file="icon.png")
root.iconphoto(False,icon)
background=PhotoImage(file="background.png")

f1=Frame(root,bg="black",padx=5,pady=5)
f1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
canvas=Canvas(f1,width=1500,height=1800)
canvas.create_image(0,0,image=background)
canvas.pack()
board=Frame(f1,bg="#E1FEE0")
board.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.8 )
l1=Label(f1,bg="#617905",fg="white",text="CHECKERS GAME",font=("times",15,"bold"))
l1.place(rely=0.05,relx=0.39)
l2=Label(f1,bg="#617905",fg="white",text="made by yasoob raza",font=("calibri",10))
l2.place(relx=0.43,rely=0.1)

black=PhotoImage(file="black.png")
white=PhotoImage(file="white.png")
b_king=PhotoImage(file="black king.png")
w_king=PhotoImage(file="white king.png")


#BOARD ROW 1
b00=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b00))
b00.place(relx=0,rely=0,relwidth=0.125,relheight=0.125)
b00.setposition(0,0)

b02=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b02))
b02.place(relx=0.25,rely=0,relwidth=0.125,relheight=0.125)
b02.setposition(0,2)

b04=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b04))
b04.place(relx=0.5,rely=0,relwidth=0.125,relheight=0.125)
b04.setposition(0,4)

b06=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b06))
b06.place(relx=0.75,rely=0,relwidth=0.125,relheight=0.125)
b06.setposition(0,6)

#BOARD ROW 2
b11=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b11))
b11.place(relx=0.125,rely=0.125,relwidth=0.125,relheight=0.125)
b11.setposition(1,1)

b13=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b13))
b13.place(relx=0.375,rely=0.125,relwidth=0.125,relheight=0.125)
b13.setposition(1,3)

b15=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b15))
b15.place(relx=0.625,rely=0.125,relwidth=0.125,relheight=0.125)
b15.setposition(1,5)

b17=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b17))
b17.place(relx=0.875,rely=0.125,relwidth=0.125,relheight=0.125)
b17.setposition(1,7)


#BOARD ROW 3
b20=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b20))
b20.place(relx=0,rely=0.25,relwidth=0.125,relheight=0.125)
b20.setposition(2,0)

b22=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b22))
b22.place(relx=0.25,rely=0.25,relwidth=0.125,relheight=0.125)
b22.setposition(2,2)

b24=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b24))
b24.place(relx=0.5,rely=0.25,relwidth=0.125,relheight=0.125)
b24.setposition(2,4)

b26=checkerbuttons(board,bg="#617905",relief="flat",image=black,command=lambda:move(b26))
b26.place(relx=0.75,rely=0.25,relwidth=0.125,relheight=0.125)
b26.setposition(2,6)

#BOARD ROW 4
b31=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b31))
b31.place(relx=0.125,rely=0.375,relwidth=0.125,relheight=0.125)
b31.setposition(3,1)

b33=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b33))
b33.place(relx=0.375,rely=0.375,relwidth=0.125,relheight=0.125)
b33.setposition(3,3)

b35=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b35))
b35.place(relx=0.625,rely=0.375,relwidth=0.125,relheight=0.125)
b35.setposition(3,5)

b37=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b37))
b37.place(relx=0.875,rely=0.375,relwidth=0.125,relheight=0.125)
b37.setposition(3,7)



#BOARD ROW 5
b40=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b40))
b40.place(relx=0,rely=0.5,relwidth=0.125,relheight=0.125)
b40.setposition(4,0)

b42=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b42))
b42.place(relx=0.25,rely=0.5,relwidth=0.125,relheight=0.125)
b42.setposition(4,2)

b44=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b44))
b44.place(relx=0.5,rely=0.5,relwidth=0.125,relheight=0.125)
b44.setposition(4,4)

b46=checkerbuttons(board,bg="#617905",relief="flat",command=lambda:move(b46))
b46.place(relx=0.75,rely=0.5,relwidth=0.125,relheight=0.125)
b46.setposition(4,6)


#BOARD ROW 6
b51=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b51))
b51.place(relx=0.125,rely=0.625,relwidth=0.125,relheight=0.125)
b51.setposition(5,1)
b51.name="b51"

b53=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b53))
b53.place(relx=0.375,rely=0.625,relwidth=0.125,relheight=0.125)
b53.setposition(5,3)
b53.name="b53"

b55=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b55))
b55.place(relx=0.625,rely=0.625,relwidth=0.125,relheight=0.125)
b55.setposition(5,5)
b55.name="b55"

b57=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b57))
b57.place(relx=0.875,rely=0.625,relwidth=0.125,relheight=0.125)
b57.setposition(5,7)
b57.name="b57"

#BOARD ROW 7
b60=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b60))
b60.place(relx=0,rely=0.75,relwidth=0.125,relheight=0.125)
b60.setposition(6,0)
b60.name="b60"

b62=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b62))
b62.place(relx=0.25,rely=0.75,relwidth=0.125,relheight=0.125)
b62.setposition(6,2)
b62.name="b62"

b64=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b64))
b64.place(relx=0.5,rely=0.75,relwidth=0.125,relheight=0.125)
b64.setposition(6,4)
b64.name="b64"

b66=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b66))
b66.place(relx=0.75,rely=0.75,relwidth=0.125,relheight=0.125)
b66.setposition(6,6)
b66.name="b66"

#BOARD ROW 8
b71=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b71))
b71.place(relx=0.125,rely=0.875,relwidth=0.125,relheight=0.125)
b71.setposition(7,1)

b73=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b73))
b73.place(relx=0.375,rely=0.875,relwidth=0.125,relheight=0.125)
b73.setposition(7,3)

b75=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b75))
b75.place(relx=0.625,rely=0.875,relwidth=0.125,relheight=0.125)
b75.setposition(7,5)

b77=checkerbuttons(board,bg="#617905",relief="flat",image=white,command=lambda:move(b77))
b77.place(relx=0.875,rely=0.875,relwidth=0.125,relheight=0.125)
b77.setposition(7,7)


mainloop()