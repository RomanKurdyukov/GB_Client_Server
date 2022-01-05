from cli_service_layer import *
# from l3_task_client import check_response
import unittest


class ClientLayerTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.test_response_ok_dict = {
            'response': '200',
            'time': time(),
            'alert': 'OK'
        }

        self.test_action_probe_dict = {
            'action': 'probe',
            'time': time()
        }

        self.test_response_probe_dict = {
            "action": "presence",
            "type": "status",
            "user": {
                "account_name": 'username',
                "status": "Yep, I am here!"
            }
        }

    def test_get_encoded_decoded_data(self):
        result_encoded = encode_data(self.test_response_probe_dict)
        result_decoded = decode_data(result_encoded)
        self.assertEqual(type(result_encoded), bytes)
        self.assertEqual(type(result_decoded), dict)
        self.assertEqual(result_decoded, self.test_response_probe_dict)

    def test_check_presence_msg_create(self):

        result = presence_msg_create('username')
        del result['time']
        self.assertEqual(result, self.test_response_probe_dict)


if __name__ == '__main__':
    unittest.main()
