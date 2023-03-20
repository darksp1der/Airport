import unittest
from Lab10.infrastructure.repositories import Airport
from Lab10.domain.person import Passenger
from Lab10.application.controller import Plane

"""
 TEST FUNCTIONS
"""


class TestFunctions(unittest.TestCase):

    def test_sort_by_last_name(self):
        test = Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)])
        self.assertEqual(Plane.sort_by_last_name(test),[Passenger("Marius","Dan",2111111111112), Passenger("Ion","Pop",1111111111111)],"Sorted wrong")

    def test_sort_by_nr_pass(self):
        test = Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)]))
        self.assertEqual(Airport.get_plane(test,0),Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111),Passenger("Marius","Dan",2111111111112)])),"Sorted wrong")

    def test_sort_by_nr_pass_substring(self):
        test = Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)]))
        self.assertEqual(Airport.get_plane(test, 0),Airport(Plane(1, "sky", 32, "Paris", [Passenger("Ion", "Pop", 1111111111111),Passenger("Marius","Dan",2111111111112)])),"Sorted wrong")

    def test_sort_by_concatenation(self):
        test = Plane(1, "sky", 32, "Paris",[Passenger("Ion", "Pop", 1111111111111), Passenger("Marius", "Dan", 2111111111112)])
        self.assertEqual(Plane.sort_by_last_name(test),[Passenger("Marius", "Dan", 2111111111112), Passenger("Ion", "Pop", 1111111111111)],"Sorted wrong")

    def test_identify_planes_by_pnc(self, string):
        test = test = Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)]))
        self.assertEqual(Airport.identify_planes_by_pnc(test,111),Airport(Plane(1, "sky", 32, "Paris", [Passenger("Ion", "Pop", 1111111111111)])),"Sorted wrong")
    def identify_pass_from_given_plane(self, substring, index):
        test = Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)]))
        self.assertEqual(Airport.identify_pass_from_given_plane(test,"Ion",0), Airport(Plane(1, "sky", 32, "Paris", [Passenger("Ion", "Pop", 1111111111111)])), "Sorted wrong")

    def identify_plane_with_pass_name(self, first, last):
        test = Airport(Plane(1,"sky",32,"Paris",[Passenger("Ion","Pop",1111111111111), Passenger("Marius","Dan",2111111111112)]))
        self.assertEqual(Airport.identify_plane_with_pass_name(test,"Marius","Dan"), Airport(Plane(1, "sky", 32, "Paris", [Passenger("Marius", "Dan", 2111111111112)])), "Sorted wrong")


