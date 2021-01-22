"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import airflow_python_sdk
from airflow_python_sdk.api.connection_api import ConnectionApi  # noqa: E501


class TestConnectionApi(unittest.TestCase):
    """ConnectionApi unit test stubs"""

    def setUp(self):
        self.api = ConnectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_connection(self):
        """Test case for create_connection

        Create connection entry  # noqa: E501
        """
        pass

    def test_delete_connection(self):
        """Test case for delete_connection

        Delete a connection entry  # noqa: E501
        """
        pass

    def test_get_connection(self):
        """Test case for get_connection

        Get a connection entry  # noqa: E501
        """
        pass

    def test_get_connections(self):
        """Test case for get_connections

        Get all connection entries  # noqa: E501
        """
        pass

    def test_patch_connection(self):
        """Test case for patch_connection

        Update a connection entry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()