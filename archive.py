from tkinter import * #imports everything
import tkinter as tk

#pack(side=tk.TOP) --> stacks top to bottom
#pack(side=tk.BOTTOM) --> stacks bottom to top
#pack(side=tk.LEFT) --> stacks left to right (if label is blank, will resize once filled) - no built in gray boundries
#padx=40 --> 40 pixels 
#place allows more control on programmer(fine control), pack gives more control on 'puter 
# relief styles = flat, raised, sunken, groove, ridge

class MyApp:
    def __init__(self, root):
      root.title("To-Do")
      root.geometry("500x400") #sets initial size
      root.maxsize(1000,800)

      frame = Frame(root, width=200, height=100, borderwidth=2, relief="ridge")
      frame.place(x=0,y=0)

      self.label_text = StringVar()
      label = Label(root, text="some label text", textvariable=self.label_text)
     # label.pack(side=tk.TOP, padx=10, pady=5)
      #label['text'] = "New stuff"
      #label['font']= ("Courier", 40)
      label.configure(text="New", font= ('Courier', 40)) #shorthand of two above lines
     # label.grid(column=1, row=1)

      self.entry_text = StringVar() #updates when Entry changes
      entry = Entry(root, textvariable= self.entry_text)
    #  entry.pack() #by default goes top to bottom
    #  entry.place(x=100, y=40)
     # entry.grid(column=2, row=2)

      
      button = Button(root, text="Button text", command=self.press_button)
     # button.place(x=0, y=0)
    #  button.pack()
     # button.grid(column=1,row=2, sticky=(S,W,E))
     # button.configure(width=30, height=5, font=("Courier", 10))

      self.list_item_strings = ["Hello", "Hi", "Greetings", "Konbonwa"]
      list_items = StringVar(value=self.list_item_strings)
      listbox = Listbox(root, listvariable=list_items, height=3)
    #  listbox.pack()
      listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection())) #passes currently selected item index into select_item to pass to index. Index is a tuple as [index]: blank
      
    
    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
    
    def select_item(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)


root = Tk()
MyApp(root)
root.mainloop()