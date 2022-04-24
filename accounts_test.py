import unittest
from accounts import Account
import pyperclip

class TestAccount(unittest.TestCase):
    '''
        Test class that defines test cases for the accounts class behaviors
    
        Args:
            unittest.testCase; TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_account = Account("Netflix", "Annet", "janet@gmial.com", "Hb(9Mnn!05n")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account,"Netflix")
        self.assertEqual(self.new_account.account_user,"Annet")
        self.assertEqual(self.new_account.email,"janet@gmial.com")
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
        test_account = Account("Application", "John Doe", "johndoe@gmial.com", "pass1234")
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)



if __name__ == '__main__':
    unittest.main()