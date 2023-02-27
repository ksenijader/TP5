'''Creates the GUI '''
from tkinter import *
from tkinter import messagebox


class Application(Tk):
    '''Application class inherits Tkinter class'''
    def __init__(self, controller):
        '''Creating the window using controller.
        Controller connects it to the model'''
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.creer_widgets()

    def creer_widgets(self):
        '''Creating widgets in GUI'''
        # All the labels
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.label_search = Label(self, text="Recherche")
        # All the buttons
        self.bouton_display = Button(self, text="Afficher",
                                     command=self.display_something)
        self.bouton = Button(self, text="Quitter",
                             command=self.quit_window)
        self.bouton_add_animal = Button(self, text="Add/save changes",
                                        command=self.add_animal)
        self.btn = Button(self, text = "Delete selection",
                          command=self.controller.delete_model_animal)
        self.but = Button(self,text="Edit", command=self.edit_animal)


        # Entries
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        # Listbox
        self.animal_list = Listbox(self)
        self.animal_list.insert(0, *self.controller.get_model_info())
        # Adding everything in order
        self.label.pack()
        self.label1.pack()
        self.label_search.pack()
        self.search.pack()
        self.bouton_display.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.bouton_add_animal.pack()
        self.animal_list.pack()
        self.btn.pack()
        self.but.pack()
        self.bouton.pack()


    def quit_window(self):
        '''To close the created GUI window'''
        self.controller.quit_window()

    def display_something(self):
        '''To display the information that controller
        found in module about animal specified
        in 'search' field'''
        self.controller.display(self.search.get())

    def display_label(self, value):
        '''To get the information entered by user as
        dictionary key'''
        self.label1['text'] = value

    def add_animal(self):
        '''Add animal from the entries to the dictionary'''
        # Create empty dictionary
        dict_animal = {}
        # For each entry provided by user
        for att in self.entries:
            # Add the key and the value to the dictionary
            dict_animal[att] = self.entries[att].get()
            # Clear the entry fields
            self.entries[att].delete(0, END)
        # Execute 'add_animal' function
        # from controller, take
        # created dictionary as argument
        self.controller.add_animal(dict_animal)
        # Display pop up message
        messagebox.showinfo("Saved!", "Animal is saved!")

    def selected_animal(self):
        '''To get the animal selected from the list'''
        for animal in self.animal_list.curselection():
            # Return the animal chosen from the listbox
            return self.animal_list.get(animal)

    def edit_animal(self):
        '''To create a pop up window
        allowing to edit information
        about an already existing animal'''
        # In entries_dict stock information
        # from the model for chosen animal
        entries_dict = self.controller.get_model_things()
        for k in entries_dict:
            for att in self.attributes:
                # if the key in entries_dict is the same
                # as the key in self.attributes
                if k == att:
                    # Fill the entry field with information
                    # stocked in entries_dict
                    self.entries[att].insert(1, entries_dict[k])

    def update_list(self):
        '''To update the list displayed in the window'''
        # Delete animal list from listbox
        self.animal_list.delete(0, END)
        # Add the current animal list to listbox
        self.animal_list.insert(0, *self.controller.get_model_info())

    def show_delete_message(self):
        '''To get pop up message once animal is deleted
        from the list'''
        messagebox.showinfo("Deleted!", "Animal deleted!")

    def view_window(self):
        '''To display the window'''
        self.title("Ma Première App :-)")
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.view_window()
