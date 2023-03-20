from Lab10.application.controller import Plane
from Lab10.functions.functions import *


class Airport:

    """
    initialization method
    """
    def __init__(self,data):
        for i in range(len(data)):
            for j in range(i+1,len(data)):
                if data[i].get_id() == data[j].get_id():
                    raise ValueError("The id cannot be the same")
                else:
                    self.__data = data[:]

    '''
    CRUD - create, read, update, delete methods on planes
    '''

    def add_plane(self, id, airline, nrseats, destination, lst):
        for i in range(len(self.__data)):
            if self.__data[i].get_id() == id:
                raise ValueError("The id cannot be the same")
            else:
                p = Plane(id,airline,nrseats,destination,lst)
                self.__data.append(p)

    def get_plane(self,index):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            return self.__data[index]

    def update_plane(self, index, id, airline, nrseats, destination, lst):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            for i in range(len(self.__data)):
                if self.__data[i].get_id == id:
                    raise ValueError("The id cannot be the same")
                else:
                    self.__data[index].set_id(id)
                    self.__data[index].set_airline(airline)
                    self.__data[index].set_nrseats(nrseats)
                    self.__data[index].set_destination(destination)
                    self.__data[index].set_lst(lst)

    def del_plane(self,index):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            del self.__data[index]

    '''
    method that sorts the planes by their number of passengers
    '''
    def sort_by_nr_pass(self):
        return sorted(self.__data, key=lambda data: len(data.get_list()))

    '''
    method that sorts the planes by the number of the passengers in each plane whose first name
    starts with a given string
    '''
    def sort_by_nr_pass_substring(self,substring):
        return sorted(self.__data, key=lambda data: sum(1 for passenger in data.get_list() if passenger.get_firstname().startswith(substring)))

    '''
    method that sorts the planes by the concatenation of their number of passengers and the planes' destination
    '''
    def sort_by_concatenation(self):
        return sorted(self.__data, key=lambda data: str(len(self.__data.get_list())) + self.__data.get_destination())

    '''
    method that identifies the planes which have passengers whose PNC start with a string given as 3 letters
    '''
    def identify_planes_by_pnc(self,substring):
        list_of_planes = []
        for plane in self.__data:
            for passengers in self.__data.get_list():
                if str(passengers.get_passnr()).startswith(substring):
                    list_of_planes.append(plane)
        return list_of_planes[:]

    '''
    method that identifies passengers in a given plane whose first name or last name
    starts with a given substring
    '''
    def identify_pass_from_given_plane(self, substring, index):
        list_of_pass = []
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("The index is not well defined")
        else:
            for passenger in self.__data[index].get_list():
                if passenger.get_firstname().starswith(substring) or passenger.get_lastname().startswith(substring):
                    list_of_pass.append(passenger)
        return list_of_pass[:]

    '''
    method that identifies planes who have a passenger with a given name
    '''
    def identify_plane_with_pass_name(self,first,last):
        list_of_planes = []
        for plane in self.__data:
            for passengers in self.__data.get_list():
                if passengers.get_firstname() == first and passengers.get_lastname() == last:
                    list_of_planes.append(plane)
        return list_of_planes[:]

    def call_bt(self, n, start):
        for sol in back_rec(n, [], start):
            print(sol)



