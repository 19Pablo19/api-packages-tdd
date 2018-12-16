import unittest
from package.api import *



class TestPrueba(unittest.TestCase):

    def test_listUsers(self):
        result = ListUsers().get()
        self.assertEqual(result, {"Listado de usuarios":users})






if __name__ == "__main__":
    unittest.main()
