'''Code allowing to manipulate animal class objects'''
from Animal import Animal

class Model():
    '''Class model allowing to stock animal class information'''
    def __init__(self, filename):
        '''Defining initials class attributes'''
        self.filename = filename
        self.file = open(self.filename, "r+")
        self.dico_animaux = {}

    def read_file(self):
        '''Method allowing to read file line by line'''
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
            self.dico_animaux[a.name] = a

    def save(self, dict_animal):
        '''Method allowing to save animal from GUI entries'''
        # Create a list of all animal names
        all_animals = self.dico_animaux.keys()
        # If the name provided in entry by user
        # is not in the list of names
        if dict_animal["name"] not in all_animals:
            # Create a new animal using entries
            # provided by user as attributes
            new_animal = Animal(dict_animal["species"],
                                dict_animal["age"],
                                dict_animal["diet"],
                                dict_animal["foot"],
                                dict_animal["name"])
            # Add the new animal to the dictionary
            self.dico_animaux[new_animal.name] = new_animal
            # Update the text file
            self.rewrite_file()
        else:  # Otherwise
            # Delete the already existing animal from the list
            self.delete_animal(dict_animal["name"])
            # Repeat the method to add modified animal to the list
            self.save(dict_animal)

    def close(self):
        '''Method to close the opened file'''
        self.file.close()

    def get_attributes(self) -> []:
        '''Method to get attributes from the dictionary'''
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def get_info(self) -> []:
        '''Method allowing to get information from the dictionary'''
        # Create a list to stock information
        animal_list = self.dico_animaux
        return animal_list

    def delete_animal(self, selected_animal):
        '''Method allowing to delete animal'''
        # Delete the animal that was selected
        # from the dictionary
        del self.dico_animaux[selected_animal]
        # Update the text file
        self.rewrite_file()

    def rewrite_file(self):
        '''Method allowing to update the text file'''
        # Starting from the first line
        self.file.seek(0)
        self.file.truncate()
        # For each animal in dictionary
        for animal in self.dico_animaux.values():
            # Write information about animal
            self.file.write(animal.species+","+animal.age+","+animal.diet+","
                            + animal.foot+","+animal.name+"\n")
        # Close the file to apply changes
        self.close()
        # Reopen file to continue working with it
        self.file = open(self.filename, "r+")

    def get_entries(self, name):
        '''Method allowing to get a dictionary with only
        "non-inbuilt" information from
        the Animal class object'''
        # Create an empty dictionary to
        # stock information about animal
        entries_dict = {}
        # Stock in animal the animal class object
        animal = self.dico_animaux.get(name)
        # Using inbuilt dir function to
        # access object information
        for attr in dir(animal):
            # If dictionary key doesn't start with "_",
            # it is object attribute that we defined
            if not attr.startswith("_"):
                # Get the attribute's value
                value = getattr(animal, attr)
                # Add it to the entries_dict
                entries_dict[attr] = value
        # Return the created dictionary
        return entries_dict


if __name__ == "__main__":
    model = Model("a.txt")
    model.read_file()
    model.close()
