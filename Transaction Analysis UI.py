from tkinter import *

window = Tk()
window.geometry("650x1000")

topFrame = Frame(window)
topFrame.pack(side = LEFT)

rightFrame = Frame(window)
rightFrame.pack(side = LEFT)

l1 = Label(topFrame,text = "Select Excel Sheet")
l1.grid(row = 0, column = 0,columnspan = 2,pady = 10)

t1 = StringVar()
e1 = Entry(topFrame,textvariable=t1)
e1.grid(row = 0,column = 2,pady = 10,padx = 10)

button1 = Button(topFrame, text = "Create Database")
button1.grid(row = 0,column = 3,pady = 10)


# Frequent Transaction Frame first row
l2 = Label(topFrame,text = "Bucket count threshold:")
l2.grid(row = 2, column = 0,columnspan = 2,pady = 5)
t2 = StringVar()
e2 = Entry(topFrame,textvariable=t2)
e2.grid(row = 2,column = 2,pady = 5)


# Frequent Transaction Frame second row
l3 = Label(topFrame,text = "Transaction frequency threshold : ")
l3.grid(row = 3, column = 0,columnspan = 2,pady = 5)
t3 = StringVar()
e3 = Entry(topFrame,textvariable=t3)
e3.grid(row = 3,column = 2,pady = 5)

#Get Frequent Transactions
button1 = Button(topFrame, text = "Get frequent transactions")
button1.grid(row = 4,column = 2,pady = 5)

l3 = Label(topFrame,text = "Number of filtered Transactions from Bucket : ")
l3.grid(row = 5, column = 0,columnspan = 2,pady = 5)
t4 = StringVar()
e4 = Entry(topFrame,textvariable=t4)
e4.grid(row = 5,column = 2,pady = 5)

l4 = Label(topFrame,text = "Number of filtered Transactions based on actual count : ")
l4.grid(row = 6, column = 0,columnspan = 2,pady = 5)
t5 = StringVar()
e5 = Entry(topFrame,textvariable=t5)
e5.grid(row = 6,column = 2,pady = 5)


l4 = Label(topFrame,text = "List of Frequent Transactions:")
l4.grid(row = 7, column = 0,columnspan = 2,pady = 5)
list1 = Listbox(topFrame,width = 40,height = 15)
list1.grid(row = 7,column = 2,columnspan=2)

sb1 = Scrollbar(topFrame)
sb1.grid(row = 7,column = 3, rowspan = 15)
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)


l5 = Label(topFrame,text = "Agents : ")
l5.grid(row = 9, column = 0,columnspan = 2,pady = 5)
list2 = Listbox(topFrame,width = 40,height = 5)
list2.grid(row = 9,column = 2,columnspan=2,pady = 5)
#sb2 = Scrollbar(topFrame)
#sb2.grid(row = 2,column = 9, rowspan = 5,pady = 5)


l6 = Label(topFrame,text = "Integrators : ")
l6.grid(row = 10, column = 0,columnspan = 2,pady = 5)
list3 = Listbox(topFrame,width = 40,height = 5)
list3.grid(row = 10,column = 2,columnspan=2,pady = 5)
#sb3 = Scrollbar(topFrame)
#sb3.grid(row = 3,column = 9, rowspan = 5,pady = 5)

l7 = Label(topFrame,text = "Link Analysis Result : ")
l7.grid(row = 11, column = 0,columnspan = 2,pady = 5)
list4 = Listbox(topFrame,width = 40,height = 5)
list4.grid(row = 11,column = 2,columnspan=2,pady = 5)

window.title("Transaction Analysis")
window.mainloop()