from Lab10.application.controller import Plane
from Lab10.infrastructure.repositories import Airport
from Lab10.domain.person import Passenger

"""
The function which displays the menu
"""


def printmenu():
    # Displays the menu
    msg = "Menu:\n"
    msg += "\t 1 ADD PASSENGER\n"
    msg += "\t 2 GET PASSENGER\n"
    msg += "\t 3 UPDATE PASSENGER\n"
    msg += "\t 4 DELETE PASSENGER\n"
    msg += "\t 5 ADD PLANE\n"
    msg += "\t 6 GET PLANE\n"
    msg += "\t 7 UPDATE PLANE\n"
    msg += "\t 8 DELETE PLANE\n"
    msg += "\t 9 SORT PASSENGERS BY LAST NAME\n"
    msg += "\t 10 SORT PLANES BY NUMBER OF PASSENGERS\n"
    msg += "\t 11 SORT PLANES BY THE NUMBER OF PASSENGER WITH FIRST NAME STARTING WITH A SUBSTRING\n"
    msg += "\t 12 SORT PLANES BY CONCATENATION OF DESTINATION AND NUMBER OF PASSENGER\n"
    msg += "\t 13 IDENTIFY PLANES THAT HAVE PASSENGERS WITH THE SAME 3 LETTERS IN PNC\n"
    msg += "\t 14 IDENTIFY PASSENGERS WHOSE NAME CONTAIN A GIVEN STRING\n"
    msg += "\t 15 IDENTIFY PLANES WHICH HAVE A CERTAIN PERSON IN\n"
    msg += "\t 16 FORM GROUPS OF K PASSENGERS FROM SAME PLANE BUT DIFFERENT LAST NAMES\n"
    msg += "\t 17 FORM GROUPS OF K PLANES WITH THE SAME DESTINATION BUT DIFFERENT AIRLINES\n"
    msg += "\t 0 Exit\n"
    print(msg)


'''
The function which starts the app
'''


def main():
    # Initialization of the planes in the airport
    my_airport = Airport([Plane(1,"sky",12,"Romania",[Passenger("Ion","Pop",1551012447778)])])
    option = 1
    while option != 0:
        printmenu()
        try:
            option = int(input("Enter option:"))
        except ValueError:
            print("Wrong input. Please enter a number...")
        if option == 0:
            print("BYE")
            break
        elif option == 1:
            print("Give the index of the plane, the first name, last name and the PNC of the passenger")
            try:
                index = int(input("Index="))
                first = str(input("First="))
                last = str(input("Last="))
                pnc = int(input("PNC="))
                my_airport.get_plane(index).add_passenger(first,last,pnc)
            except ValueError:
                print("The name should be a string and the PNC and the index integers")
        elif option == 2:
            print("Give the index of the plane and the index of the passenger")
            try:
                index1 = int(input("INDEX PLANE="))
                index2 = int(input("INDEX PASSENGER="))
                print(my_airport.get_plane(index1).get_passenger(index2))
            except IndexError:
                print("The index should be integer")
        elif option == 3:
            my_airport.get_plane(0).sort_by_last_name()
        else:
            print("Invalid option. Please enter a number between 0 and 16")
            printmenu()
            try:
                option = int(input("Enter option:"))
            except ValueError:
                print("The option must be an integer")

# Calling the main function


main()

