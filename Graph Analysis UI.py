from tkinter import *
window = Tk()

l5 = Label(window,text = "Agents : ")
l5.grid(row = 0, column = 0,columnspan = 2,pady = 5,padx = 20)
list2 = Listbox(window,width = 40,height = 5)
list2.grid(row = 0,column = 2,columnspan=2,pady = 5,padx = 20)
#sb2 = Scrollbar(topFrame)
#sb2.grid(row = 2,column = 9, rowspan = 5,pady = 5)


l6 = Label(window,text = "Integrators : ")
l6.grid(row = 1, column = 0,columnspan = 2,pady = 5,padx = 20)
list3 = Listbox(window,width = 40,height = 5)
list3.grid(row = 1,column = 2,columnspan=2,pady = 5,padx = 20)
#sb3 = Scrollbar(topFrame)
#sb3.grid(row = 3,column = 9, rowspan = 5,pady = 5)

l7 = Label(window,text = "Graph Analysis Result : ")
l7.grid(row = 2, column = 0,columnspan = 2,pady = 5,padx = 20)
list4 = Listbox(window,width = 40,height = 5)
list4.grid(row = 2,column = 2,columnspan=2,pady = 5,padx = 20)

button1 = Button(window, text = "Get Graph Analysis Result")
button1.grid(row = 3,column = 2,columnspan = 2,pady = 5,padx = 20)

window.title("Graph Analysis")
window.mainloop()