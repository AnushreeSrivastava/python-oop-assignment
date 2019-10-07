# Author : Anushree Srivastava
# Student ID: 801084977
# ITCS 6112 - Assignment: Programming - 1
# Question 1


class House:
    def __init__(self, name, sigil, motto, current_head):
        """
        Constructor for class House.
        It takes name, sigit , motto and current head of the house as arguments
        """
        self.name = name
        self.sigil = sigil
        self.motto = motto
        self.current_head = current_head

    def get_name(self):
        """
        Function to retrieve name
        """
        return self.name

    def get_sigil(self):
        """
        Function to retrieve Sigil
        """
        return self.sigil

    def get_motto(self):
        """
        Function to retrieve Motto
        """
        return self.motto

    def get_current_head(self):
        """
        Function to retrieve Current Head of the House
        """
        return self.current_head

    def update_current_head(self, new_head):
        """
        Function to update the Head of the House
        """
        self.current_head = new_head


def print_all_characteristics(house):
    """
   Function to print all the characteristics of the House created
   :param house:
   :return:
   """
    print("The name of House Lannister is:", house.get_name())
    print("The sigil of House Lannister is:", house.get_sigil())
    print("The motto of House Lannister is:", house.get_motto())
    print("The current Head of House Lannister is:", house.get_current_head())


def main():
    # (i) Creating new object lannister of House class
    lannisterHouse = House("Lannister", "Lion", "Hear me Roar!", "Tywin Lannister")

    # (ii) Retrieving and displaying all the characteristics of House Lannister
    print_all_characteristics(lannisterHouse)

    # (iii)Update the Current Head of house Lannister since Tywin Lannister is killed
    lannisterHouse.update_current_head("Jamie Lannister")

    # (iv) Retrieving and displaying updated all the characteristics of House Lannister
    print("\nThe Updated Characterstics are:")
    print_all_characteristics(lannisterHouse)


main()
