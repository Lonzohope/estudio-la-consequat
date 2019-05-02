import unittest
from models import photo

Photo = photos.Photo

class PhotoTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Photo class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
      

    def test_instance(self):
        self.assertTrue(isinstance(self.photo_photo,Photo))


if __name__ == '__main__':
    unittest.main()