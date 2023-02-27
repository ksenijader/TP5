'''Code allowing to link GUI and model script'''
from vue import Application
from model import Model


class Controller():
    '''Class controlling the GUI'''
    def __init__(self):
        '''Defining initial class parameters'''
        # Specifying the file that should be passed to
        # the model
        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()

    def display(self, value):
        '''Display all the information about searched animal'''
        # Get the animal object specified in
        # search field from the dico_animaux in model and pass
        # it as an argument to display_label function in vue
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        '''Add animal from the entries'''
        # Pass the dict_animal dictionary
        # created from the GUI entries as
        # an argument for save method in model
        self.model.save(dict_animal)
        # Rewrite the file
        self.model.rewrite_file()
        # Update the listbox
        self.view.update_list()

    def get_model_entries(self):
        '''Get class entries from model script'''
        return self.model.get_attributes()

    def get_model_info(self):
        '''Get object information from model script'''
        return self.model.get_info()

    def delete_model_animal(self):
        '''Delete animal from the animal list'''
        # Get the animal selected from the listbox
        selected_animal = self.view.selected_animal()
        # Pass it as argument to delete_animal method
        # in model
        self.model.delete_animal(selected_animal)
        # Update the file
        self.model.rewrite_file()
        # Update the listbox
        self.view.update_list()
        # Show the pop-up message
        self.view.show_delete_message()

    def get_model_things(self):
        '''Get all information for selected animal'''
        # Get the animal selected from the listbox
        value = self.view.selected_animal()
        # Get all the information for selected animal
        # from model
        return self.model.get_entries(value)

    def quit_window(self):
        '''Close the application window'''
        print("close app")
        self.model.close()
        self.view.destroy()


if __name__ == "__main__":
    C = Controller()
