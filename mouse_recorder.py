import mouse 
import keyboard
import tkinter as tk
# from PyQt5 import QtGui

class action:
    def __init__(self,name,record):
        self.name=name
        self.content=content

# events = []
# mouse.hook(events.append)
# keyboard.wait("escape")
# mouse.unhook(events.append)
# mouse.play(events)

def delete_selected(index):
    pass

def play_selected(index):
    pass

def add_action(newName,newRecord):
    if newName!='':
        pass

if __name__ == '__main__':
    records=[]
    recordButton='r'
    lastRecord=''
    selectedIndex=-1
    
    win = tk.Tk()
    # win.title("welcome to the mouse control program")
    label = tk.Label(text='welcome to mouse control program')
    label.grid(row=0)

    # position
    windowWidth = win.winfo_reqwidth()
    windowHeight = win.winfo_reqheight()
    positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
    win.geometry("+{}+{}".format(positionRight, positionDown))

    recordsLB=tk.Listbox(win)
    # recordsLB.insert(1, "Python")
    # recordsLB.insert(2, "Perl")
    # recordsLB.insert(3, "C")
    # recordsLB.insert(4, "PHP")
    # recordsLB.insert(5, "JSP")
    # recordsLB.insert(6, "Ruby")    

    # recordsLB.delete(0,1)
    recordsLB.grid(row=1,column=0)

    deleteSelectedB=tk.Button(win,text="delete selected", command=delete_selected(recordsLB.curselection()))
    # deleteSelectedB.pack()
    deleteSelectedB.grid(row=2,column=0)

    playSelecyedB=tk.Button(win,text="play selected", command=play_selected(recordsLB.curselection()))
    # playSelecyedB.pack()
    playSelecyedB.grid(row=1,column=1)

    newNameL=tk.Label(win, text='new name: ').grid(row=3, column=0, sticky='w')
    newNameE=tk.Entry(win).grid(row=3,column=0,sticky='e')

    clickToRecordL=tk.Label(text="click r to record").grid(row=4,column=0, sticky='w')

    addActionB=tk.Button(win,text='add action', command=add_action('a','a')).grid(row=4,sticky='e')
    # selectedIndex=recordsLB.activate('index')
    # tk.Messagebox.showinfo(title=selectedIndex)
    win.mainloop()
    




