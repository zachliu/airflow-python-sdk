"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import airflow_python_sdk
from airflow_python_sdk.model.connection_all_of import ConnectionAllOf
from airflow_python_sdk.model.connection_collection_item import ConnectionCollectionItem
globals()['ConnectionAllOf'] = ConnectionAllOf
globals()['ConnectionCollectionItem'] = ConnectionCollectionItem
from airflow_python_sdk.model.connection import Connection


class TestConnection(unittest.TestCase):
    """Connection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnection(self):
        """Test Connection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Connection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()