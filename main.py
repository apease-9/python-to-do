from tkinter import * #imports everything

class ToDoItem:
    def __init__(self, name, description):
        self.name=name
        self.description = description

class ToDo:
    def __init__(self, root):
      root.title("To-Do")
      frame = Frame(root, borderwidth=2, relief="sunken")
      frame.grid(column=1, row=1, sticky=(N,E,S,W))
      root.columnconfigure(1, weight=1) #makes any future grid configure within it
      root.rowconfigure(1, weight=1)

      list_title = Label(frame, text="To-Do Items")
      list_title.grid(column=1, row=1, sticky=(S,W))


      self.to_do_items = [
          ToDoItem("Housework", "Vaccuum, sweep, dishes"),
          ToDoItem("Workout", "Push ups, pull ups, squats"),
          ToDoItem("Groceries", "Flour, Sugar, eggs")
      ]
      self.to_do_names= StringVar(value=list(map(lambda x: x.name, self.to_do_items))) #takes every item of function and returns item ex. takes "Meal Plan" and passes it to list
      self.list_items = Listbox(frame, listvariable=self.to_do_names, bd=0, fg="#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
      self.list_items.bind("<<ListboxSelect>>", lambda s: self.select_item(self.list_items.curselection()))
      self.list_items.grid(column=1, row=2, sticky=(E,W), rowspan=4)
      

      item_scrollbar = Scrollbar(frame)
      item_scrollbar.grid(column=1, row=2, sticky=(N,S,E), rowspan=4)

      self.list_items.config(yscrollcommand=item_scrollbar.set)
      item_scrollbar.config(command=self.list_items.yview)

      self.selected_description=StringVar()
      self.selected_description_label = Label(frame, textvariable=self.selected_description, wraplength=200)
      self.selected_description_label.grid(column=1, row=6, sticky=(E,W))
      

      new_item_label = Label(frame, text="New Item")
      new_item_label.grid(column=2, row=1, sticky= (SW))

      name_label = Label(frame, text="Item name")
      name_label.grid(column=2, row=2, sticky= (SW))

      self.name=StringVar()
      self.name_entry=Entry(frame, textvariable=self.name)
      self.name_entry.grid(column=2, row=3, sticky=(N,E,W))

      description_label = Label(frame, text="Description of Item")
      description_label.grid(column=2, row=4, sticky= (SW))

      self.description=StringVar()
      self.description_entry=Entry(frame, textvariable=self.description)
      self.description_entry.grid(column=2, row=5, sticky=(N,E,W))

      save_button = Button(frame, text="Save to To-Do List", command=self.press_button)
      save_button.grid(column=2,row=6, sticky=(E))

      remove_button=Button(frame, text="Remove from To-Do", command=self.remove_item)
      remove_button.grid(column=1, row=7, sticky=(EW))

      for child in frame.winfo_children(): #gets all children in frame widget
          child.grid_configure(padx=10, pady=5)

     
    def remove_item(self):
        name= self.list_items.curselection()
        remove= name[0]
        del self.to_do_items[remove]
        self.list_items.delete(ANCHOR)
        
    def press_button(self):
        name = self.name.get()
        description= self.description.get()
        newItem= ToDoItem(name, description)
        self.to_do_items.append(newItem)
        self.to_do_names.set(list(map(lambda x: x.name, self.to_do_items)))
        self.name_entry.delete(0,END)
        self.description_entry.delete(0,END)
    
    def select_item(self, index):
        selected_des= self.to_do_items[index[0]]
        self.selected_description.set(selected_des.description)


root = Tk()
ToDo(root)
root.mainloop()