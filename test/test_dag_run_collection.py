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
from openapi_client.model.dag_run import DAGRun
globals()['DAGRun'] = DAGRun
from openapi_client.model.dag_run_collection import DAGRunCollection


class TestDAGRunCollection(unittest.TestCase):
    """DAGRunCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDAGRunCollection(self):
        """Test DAGRunCollection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DAGRunCollection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
