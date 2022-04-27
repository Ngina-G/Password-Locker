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

    def test_save_multiple_user(self):
        '''
        Test to check if app can save multiple account objects to the user_list
        '''

        self.new_user.save_user()
        test_user = User("John Doe", "johndoe@gmail.com", "pass1234")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_account(self):
        '''
        Test to check whether the app can delete an account object
        '''

        self.new_user.save_user()
        test_user = User("John Doe", "johndoe@gmail.com", "pass1234")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_find_by_user_email(self):
        '''
        Test to check if we can find an user object by its email
        '''

        self.new_user.save_user()
        test_user = User("John Doe", "johndoe@gmail.com", "pass1234")
        test_user.save_user()

        found_user = User.find_by_user_email("johndoe@gmail.com")
        self.assertEqual(found_user.user, test_user.user)

    def test_if_user_exists(self):
        '''
        Test to check if we can find an user object by its email
        '''

        self.new_user.save_user()
        test_user = User("John Doe", "johndoe@gmail.com", "pass1234")
        test_user.save_user()

        user_exists = User.user_exists("johndoe@gmail.com", "pass1234")
        self.assertFalse(user_exists)

    def test_display_user(self):
        '''
        Test that returns a list of all the users
        '''

        self.assertEqual(User.display_users(), User.user_list)

    # def test_copy_users(self):
    #     '''
    #     Test to confirm that we are copying the user details from a found contact
    #     '''
    #     self.new_user.save_user()
    #     User.copy_user("janedoe@gmail.com")

    #     self.assertEqual(self.new_user.user,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()