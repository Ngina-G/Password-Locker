import unittest
from credential import Account
import pyperclip

class TestCredentails(unittest.TestCase):
    '''
        Test class that defines test cases for the accounts class behaviors
    
        Args:
            unittest.testCase; TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_account = Account("Netflix", "Annet", "janet@gmail.com", "Hb(9Mnn!05n")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Netflix")
        self.assertEqual(self.new_account.account_user,"Annet")
        self.assertEqual(self.new_account.email,"janet@gmail.com")
        self.assertEqual(self.new_account.password,"Hb(9Mnn!05n")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.account_list= []

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into the account list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):
        '''
        Test to check if app can save multiple account objects to the account_list
        '''

        self.new_account.save_account()
        test_account = Account("Application", "John Doe", "johndoe@gmail.com", "pass1234")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
        '''
        Test to check whether the app can delete an account object
        '''

        self.new_account.save_account()
        test_account = Account("Application", "John Doe", "johndoe@gmail.com", "pass1234")
        test_account.save_account()
        
        self.new_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_find_by_account_name(self):
        '''
        Test to check if we can find an account object by its name
        '''

        self.new_account.save_account()
        test_account = Account("Application", "John Doe", "johndoe@gmail.com", "pass1234")
        test_account.save_account()

        found_account = Account.find_by_account_name("Application")
        self.assertEqual(found_account.account_user, test_account.account_user)

    def test_if_account_exists(self):
        '''
        Test to check if we can return a boolean when checking to find if an account exists by an account name
        '''

        self.new_account.save_account()
        test_account = Account("Application", "John Doe", "johndoe@gmail.com", "pass1234")
        test_account.save_account()

        account_exists = Account.account_exists("Application")
        self.assertTrue(account_exists)

    def test_display_account(self):
        '''
        Test that returns a list of all the accounts
        '''

        self.assertEqual(Account.display_accounts(), Account.account_list)
if __name__ == '__main__':
    unittest.main()