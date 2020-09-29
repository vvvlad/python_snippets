import unittest
import os
from aws_unittest.lambdas import extract_lambda
from moto import mock_s3
import boto3
import json


@mock_s3
class TestExtract(unittest.TestCase):
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))

    SOURCE_BUCKET = "source_bucket"
    DEST_BUCKET = "destination_bucket"
    DEST_KEY = "s3/key/"

    ENV_DEST_KEY = "DEST_KEY"
    ENV_DEST_BUCKET = "DEST_BUCKET"

    def setUp(self):
        os.environ[TestExtract.ENV_DEST_KEY] = TestExtract.DEST_KEY
        os.environ[TestExtract.ENV_DEST_BUCKET] = TestExtract.DEST_BUCKET

        conn = boto3.resource('s3')
        conn.create_bucket(Bucket=TestExtract.SOURCE_BUCKET)
        conn.create_bucket(Bucket=TestExtract.DEST_BUCKET)

    def tearDown(self):
        del os.environ[TestExtract.ENV_DEST_KEY]
        del os.environ[TestExtract.ENV_DEST_BUCKET]

        self.remove_bucket(TestExtract.SOURCE_BUCKET)
        self.remove_bucket(TestExtract.DEST_BUCKET)

    """
    helper functions are removed because they are not discussed in the article. 
    you can find the original test file here
    https://github.com/vincentclaes/serverless_data_pipeline_example/blob/master/serverless_data_pipeline_tests/lambda_function/test_extract.py
    """

    def test_extract_the_contents_of_an_email_successfully(self):
        # arrange
        email_name = 'test_extract_the_contents_of_an_email_successfully.eml'
        test_email_path = os.path.join(self.DIR_PATH, 'resources', email_name)
        self.put_email_to_s3(test_email_path, email_name)

        event = self.get_s3_event(TestExtract.SOURCE_BUCKET, email_name)

        # act
        s3_key_extracted_message = extract.handler(event, None)

        # assert
        email_as_json = self.read_s3_object(TestExtract.DEST_BUCKET, s3_key_extracted_message)
        expected_json = {'id': 'test_extract_the_contents_of_an_email_successfully.eml',
                         'from': 'vclaes1986@gmail.com',
                         'to': 'vincent.v.claes@gmail.com',
                         'cc': '', 'subject': 'Hey how are you doing',
                         'date': '2019-07-09 13:42:54+02:00',
                         'body': '\nCash Me Outside How Bout Dah'}
        self.assertDictEqual(json.loads(email_as_json), expected_json)


if __name__ == '__main__':
    unittest.main()
