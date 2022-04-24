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
