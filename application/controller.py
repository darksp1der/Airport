from Lab10.domain.person import Passenger


class Plane:
    """
    initialization method
    """

    def __init__(self, id, airline, nrseats, destination, lst):
        self.__id = id
        self.__airline = airline
        if nrseats < 1 or nrseats < len(lst):
            raise ValueError("The nr of the seats must be greater or equal to the nr of passengers")
        else:
            self.__nrseats = nrseats

        self.__destination = destination

        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                if lst[i].get_passnr() == lst[j].get_passnr():
                    raise ValueError("Ids cannot be the same")

        self.__lst = lst[:]

    '''
    getters and setters
    '''
    def get_id(self):
        return self.__id

    def get_airline(self):
        return self.__airline

    def get_nrseats(self):
        return self.__nrseats

    def get_destination(self):
        return self.__destination

    def get_list(self):
        return self.__lst[:]

    def set_id(self,id):
        self.__id = id

    def set_airline(self,airline):
        self.__airline = airline

    def set_nrseats(self,nr):
        if nr < 1 or nr < len(self.__lst):
            raise ValueError("The nr must be greater or equal to the nr of passengers")
        else:
            self.__nrseats = nr

    def set_destination(self,destination):
        self.__destination = destination

    def set_lst(self,lst):
        if self.__nrseats < len(lst):
            raise ValueError("The nr must be greater or equal to the nr of passengers")
        else:
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    if lst[i].get_passnr() == lst[j].get_passnr():
                        raise ValueError("Ids cannot be the same")
                    else:
                        self.__lst = lst[:]

    '''
    CRUD - create, read, update, delete methods on passengers
    '''

    def add_passenger(self,first,last,number):
        for i in range(len(self.__lst)):
            if self.__lst[i].get_passnr() == number:
                raise ValueError("The PNC should be unique")
            else:
                passenger = Passenger(first,last,number)
                self.__lst.append(passenger)

    def get_passenger(self,index):
        if index < 0 or index > len(self.__lst) - 1:
            raise IndexError("The index is not well defined")
        else:
            return self.__lst[index]

    def update_passenger(self,index,first,last,number):
        if index < 0 or index > len(self.__lst) - 1:
            raise IndexError("The index is not well defined")
        else:
            for i in range(len(self.__lst)):
                if self.__lst[i].get_passnr() == number:
                    raise ValueError("The PNC should be unique")

            self.__lst[index].set_firstname(first)
            self.__lst[index].set_lastname(last)
            self.__lst[index].set_passnr(number)

    def del_passenger(self,index):
        if index < 0 or index > len(self.__lst) - 1:
            raise IndexError("The index is not well defined")
        else:
            del self.__lst[index]

    '''
    method that sorts the passengers in the plane by their last name
    '''

    def sort_by_last_name(self):
        return sorted(self.__lst, key=lambda lst: lst.get_lastname())







