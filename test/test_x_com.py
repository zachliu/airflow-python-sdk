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
from airflow_python_sdk.model.variable_all_of import VariableAllOf
from airflow_python_sdk.model.x_com_collection_item import XComCollectionItem
globals()['VariableAllOf'] = VariableAllOf
globals()['XComCollectionItem'] = XComCollectionItem
from airflow_python_sdk.model.x_com import XCom


class TestXCom(unittest.TestCase):
    """XCom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testXCom(self):
        """Test XCom"""
        # FIXME: construct object with mandatory attributes with example values
        # model = XCom()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
