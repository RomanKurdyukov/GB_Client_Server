from serv_service_layer import *
import unittest


class ServerLayerTestCase(unittest.TestCase):

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
            "time": time(),
            "type": "status",
            "user": {
                "account_name": 'username',
                "status": "Yep, I am here!"
            }
        }

    def test_get_encoded_decoded_data(self):
        result_encoded = encode_data(self.test_response_ok_dict)
        result_decoded = decode_data(result_encoded)
        self.assertEqual(type(result_encoded), bytes)
        self.assertEqual(type(result_decoded), dict)
        self.assertEqual(result_decoded, self.test_response_ok_dict)

    def test_get_response_ok_msg(self):
        result = decode_data(response_ok_msg())
        self.assertEqual(type(result), dict)

    def test_get_data_from_config(self):
        result = server_config['ACTION'][0]
        self.assertEqual(result, 'probe')

    def test_get_probation_action(self):
        result = decode_data(clients_probation())
        self.assertEqual(type(result), dict)
        self.assertEqual(result['action'], self.test_action_probe_dict['action'])
        self.assertEqual(len(result), len(self.test_action_probe_dict))

    def test_check_probation_data(self):
        result = check_probation_data(self.test_response_probe_dict)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
