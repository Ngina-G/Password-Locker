import unittest
from user import User
import pyperclip

class TestUser(unittest.TestCase):
    '''
        Test class that defines test cases for the users class behaviors
    
        Args:
            unittest.testCase; TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user = User("Annet", "annet@gmial.com", "annet.4000")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user,"Annet")
        self.assertEqual(self.new_user.user_email,"annet@gmial.com")
        self.assertEqual(self.new_user.user_pass,"annet.4000")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()