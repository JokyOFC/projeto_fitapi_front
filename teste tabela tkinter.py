from tkinter import *
from  tkinter import ttk


ws  = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

#define our column
 
my_game['columns'] = ('nomes', 'peso', 'cpf', 'contato', 'data nascimento', 'email', 'endereço')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("nomes",anchor=CENTER, width=80)
my_game.column("peso",anchor=CENTER,width=80)
my_game.column("cpf",anchor=CENTER,width=80)
my_game.column("contato",anchor=CENTER,width=80)
my_game.column("data nascimento",anchor=CENTER,width=80)
my_game.column("email",anchor=CENTER,width=80)
my_game.column("endereço",anchor=CENTER,width=80)

#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("nomes",text="nomes",anchor=CENTER)
my_game.heading("peso",text="peso",anchor=CENTER)
my_game.heading("cpf",text="cpf",anchor=CENTER)
my_game.heading("contato",text="contato",anchor=CENTER)
my_game.heading("data nascimento",text="data de nascimento",anchor=CENTER)
my_game.heading("email",text="email",anchor=CENTER)
my_game.heading("endereço",text="endereço",anchor=CENTER)


#add data 
my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore', 'srteco@hotmail.com', 'rua travasso de dentro'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))
my_game.insert(parent='',index='end',iid=6,text='',
values=('7','RayRizzo','107','Colorado' , 'Denver'))
my_game.insert(parent='',index='end',iid=7,text='',
values=('8','Byun','108','Pennsylvania' , 'ORVISTON'))
my_game.insert(parent='',index='end',iid=8,text='',
values=('9','Trink','109','Ohio' , 'Cleveland'))
my_game.insert(parent='',index='end',iid=9,text='',
values=('10','Twitch','110','Georgia' , 'Duluth'))
my_game.insert(parent='',index='end',iid=10,text='',
values=('1','Animus','111', 'Connecticut' , 'Hartford'))
my_game.pack()


ws.mainloop()