from tkinter import *
import os

#----------------------------------------------
# Part 1 = Konfigurasi Awal

#main window
root = Tk()
#window title
root.title("Implementasi Undo Redo Sederhana")
#height and width of the window
root.geometry("300x150")

#----------------------------------------------
#Part 2 = Class Stack

#class stack to store data text
class Stack:
    def __init__(self):
        self.text = []

    def push(self, new_text):
        self.text.append(new_text)

    def pop(self):
        if self.text == []:
            print("ERROR. File is Empty.")
            return
        else:
            return self.text.pop()
    
    def erase_all(self):
        self.text.clear()

    def get_list(self):
        return self.text


#----------------------------------------------
#Part 3 = Generate Objek

#our stack
stack = Stack()
simpan = Stack()

#apakah sebelumnya di undo?
isUndo = False

#banyak undo, redo, dan add_text (untuk history), serta history
undo_banyak = 0
redo_banyak = 0
add_text_banyak = 0
undo_limit = 0
history_urutan = []


#----------------------------------------------
#Part 4 = File Handling

#ambil data dari file.txt dan di store di stack
#ubah data di file.txt menjadi list
with open("file.txt", 'r') as line:
	lines = line.readlines()
#hapus '\n' dan push ke stack
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", '')
    stack.push(lines[i])


#----------------------------------------------
#Part 5 = Method yang dibutuhkan

#add text to file.txt
def add_text_to_file(new_text):
    file_write_a = open("file.txt", 'a')
    file_write_a.write(new_text + '\n')

#remove text from file.txt
def remove_text_from_file():
    file_read = open("file.txt", 'r')
    with file_read as line_:
        lines_ = line_.readlines()
    if lines_ == []:
        print("ERROR. File is empty.")
    else:
        lines_.pop()
        file_write_w = open("file.txt", 'w')
        file_write_w.write("".join(lines_))

#add_text method
def add_text(): #button method
    global isUndo, history_urutan, add_text_banyak, undo_limit
    new_text = entri.get()
    stack.push(new_text)
    if isUndo:
        simpan.erase_all()
        isUndo = False
    entri.delete(0, 'end')
    add_text_banyak += 1
    add_text_to_file(new_text)
    undo_limit += 1
    history_urutan.append("Add text : " + new_text)

    
#undo method
def undo():
    global isUndo, undo_banyak, history_urutan, undo_limit
    erase_from_stack = stack.pop()
    if undo_limit == 0:
        print("ERROR. You can't Undo.")
        undo_text = "ERROR. You can't Undo."
    else:
        if erase_from_stack == None:
            print("ERROR. stack is empty.")
            undo_text = "ERROR. stack is empty."
        else:
            simpan.push(erase_from_stack)
            undo_text = "erase '" + erase_from_stack + "'"
            isUndo = True
            undo_banyak += 1
        remove_text_from_file()
        undo_limit -= 1
    history_urutan.append("Undo : " + undo_text)
    
#redo method
def redo():
    global isUndo, redo_banyak, history_urutan, undo_limit
    if isUndo:
        recover_from_stack = simpan.pop()
        if recover_from_stack is None:
            print("ERROR. Redo is reaching limit.")
            redo_text = "ERROR. Redo is reaching limit."
        else:
            stack.push(recover_from_stack)
            redo_text = "recover '" + recover_from_stack + "'"
            redo_banyak += 1
            add_text_to_file(recover_from_stack)
            undo_limit += 1
    else:
        print("ERROR. Undo is undetected.") #untuk bisa redo, maka harus undo dulu.
        redo_text = "ERROR. Undo is undetected."
    history_urutan.append("Redo : " + redo_text)

#show text method
def show_text(): #menampilkan text di new window
    show_window = Tk()
    show_window.title("File")
    show_text_list = stack.get_list()
    show_text_list = "\n".join(show_text_list)
    show_label = Label(show_window, text=show_text_list)
    show_label.pack()

    show_window.mainloop()

#history method
def history():
    history_window = Tk()
    history_window.title("History Undo Redo")
    history_text = "\n".join(history_urutan)
    history_label = Label(history_window, text=history_text)
    history_label.pack()

    show_label_undo_text = "Undo : " + str(undo_banyak)
    show_label_undo = Label(history_window, text=show_label_undo_text)
    show_label_undo.pack()

    show_label_redo_text = "Redo : " + str(redo_banyak)
    show_label_redo = Label(history_window, text=show_label_redo_text)
    show_label_redo.pack()

    show_label_add_text = "Add Text : " + str(add_text_banyak)
    show_label_add = Label(history_window, text=show_label_add_text)
    show_label_add.pack()

    history_window.mainloop()

# to open readme.txt
def readme():
    os.startfile("README.txt")


#----------------------------------------------
#Part 6 = Konfigurasi GUI

#form to insert data text
entri = Entry(root, width=35)
entri.grid(row=0, column=0, columnspan=4)

#button to add text
btn_add_text = Button(root, text="Add to File", command=add_text)
btn_add_text.grid(row=0, column=4, columnspan=2)

#Undo Redo Button
btn_undo = Button(root, text="Undo", command=undo)
btn_undo.grid(row=1, column=0)
btn_redo = Button(root, text="Redo", command=redo)
btn_redo.grid(row=1, column=1)

#button to show text in new window
btn_show_text = Button(root, text="Show in New Window", command=show_text)
btn_show_text.grid(row=1, column=2, columnspan=2)

#button to show history
btn_history = Button(root, text="Show History", command=history)
btn_history.grid(row=2, column=0, columnspan=2)

#readme file (instruction)
readme_btn = Button(root, text="Instruction", command=readme)
readme_btn.grid(row=3, column=0, columnspan=2)

#credit
credit_text = "Kelompok 2"
credit_label = Label(root, text=credit_text)
credit_label.grid(row=5, column=1, columnspan=4)

#loop the window
root.mainloop()
