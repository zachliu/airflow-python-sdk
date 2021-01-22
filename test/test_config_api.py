"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import airflow_python_sdk
from airflow_python_sdk.api.config_api import ConfigApi  # noqa: E501


class TestConfigApi(unittest.TestCase):
    """ConfigApi unit test stubs"""

    def setUp(self):
        self.api = ConfigApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config(self):
        """Test case for get_config

        Get current configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
