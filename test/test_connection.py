"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.connection_all_of import ConnectionAllOf
from openapi_client.model.connection_collection_item import ConnectionCollectionItem
globals()['ConnectionAllOf'] = ConnectionAllOf
globals()['ConnectionCollectionItem'] = ConnectionCollectionItem
from openapi_client.model.connection import Connection


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
