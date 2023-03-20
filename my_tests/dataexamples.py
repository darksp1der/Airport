from Lab10.infrastructure.repositories import Airport
from Lab10.domain.person import Passenger
from Lab10.application.controller import Plane

"""
 DATA EXAMPLES
"""


def data_examples():
    test = Airport(Plane(1, "sky", 32, "Paris",[Passenger("Ion", "Pop", 1111111111111), Passenger("Marius", "Dan", 2111111111112)]))
    Airport.add_plane(test,3,"sky",64,"Romania",[Passenger("George","Ioan", 3111111549322)])
    print(test)
    # Airport([Plane(1, "sky", 32, "Paris",[Passenger("Ion", "Pop", 1111111111111),
    # Passenger("Marius", "Dan", 2111111111112)])]),
    # Plane(3,"sky",64,"Romania",[Passenger("George", "Ioan", 3111111549322)])

    Airport.get_plane(test,0)
    print(test)
    # Plane(1, "sky", 32, "Paris",[Passenger("Ion", "Pop", 1111111111111), Passenger("Marius", "Dan", 2111111111112)]))

    Airport.update_plane(test,0,5,"nova",10,"France",[Passenger("Nick","Helston", 1111115483951)])
    print(test)
    # Plane(5, "nova", 10, "France", [Passenger("Nick", "Helston", 1111115483951)])

    Airport.del_plane(test,0)
    print(test)
    # Airport([Plane(3,"sky",64,"Romania",[Passenger("George", "Ioan", 3111111549322)])])

    Airport.del_plane(test,0)
    print(test)
    # Airport([])

