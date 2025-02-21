import unittest

def add(n1,n2):
        return n1+n2

class ExampleCase(unittest.TestCase):
    
    def test_description(self):
        # TODO: write code...
        self.assertEquals(10,add(5,5))
        print("true")
    
   

if __name__ =='__main':
    unittest.main()