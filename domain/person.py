from datetime import date


class Passenger:
    """
    initialization method for passenger
    """
    def __init__(self,first,last,number):
        self.__firstname = first
        self.__lastname = last
        self.__passnr = number

    '''
    getters and setters for passenger
    '''
    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_passnr(self):
        return self.__passnr

    def set_firstname(self,name):
        self.__firstname = name

    def set_lastname(self,name):
        self.__lastname = name

    def set_passnr(self,nr):
        self.__passnr = nr

    '''
    Representation method for passenger
    '''
    def __repr__(self):
        r = "Passenger(" + str(self.__firstname) + ", " + str(self.__lastname)
        r += ", " + str(self.__passnr) + ")"
        return r
    '''
    method which calculates the passenger's age using the PNC
    '''
    def age(self):
        c = str(self.__passnr)
        s = int(c[0])
        if s < 1 or s > 6:
            raise ValueError("The pass nr is not well defined")
        else:
            aa = 1800 + int(c[1]+c[2])
            ll = int(c[3]+c[4])
            zz = int(c[5]+c[6])
            if ll < 0 or ll > 12:
                raise ValueError("The pass nr is not well defined")
            else:
                if s == 1 or s == 2:
                    aa += 100
                elif s == 5 or s == 6:
                    aa += 200
                today = date.today()
                birth = date(aa,ll,zz)
                return int(abs(today - birth).days / 365)
