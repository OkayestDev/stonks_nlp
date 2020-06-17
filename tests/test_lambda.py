from unittest import TestCase
import src.utils as utils


class Test(TestCase):

    @classmethod
    def setup_class(cls):
        print('\r\nSetting up the class')
        utils.create_lambda('lambda')

    @classmethod
    def teardown_class(cls):
        print('\r\nTearing down the class')
        utils.delete_lambda('lambda')

    def test_that_lambda_returns_correct_message(self):
        payload = {"tweet": "howdy"}
        response = utils.invoke_function_and_get_message('lambda', payload)
        self.assertEqual(response['message'], 'Hello pytest!')
        self.assertEqual(response['tweet'], "howdy")
