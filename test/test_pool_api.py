"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: dev@airflow.apache.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.pool_api import PoolApi  # noqa: E501


class TestPoolApi(unittest.TestCase):
    """PoolApi unit test stubs"""

    def setUp(self):
        self.api = PoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pool(self):
        """Test case for create_pool

        Create aa pool  # noqa: E501
        """
        pass

    def test_delete_pool(self):
        """Test case for delete_pool

        Delete a pool  # noqa: E501
        """
        pass

    def test_get_pool(self):
        """Test case for get_pool

        Get a pool  # noqa: E501
        """
        pass

    def test_get_pools(self):
        """Test case for get_pools

        Get all pools  # noqa: E501
        """
        pass

    def test_get_task_instances(self):
        """Test case for get_task_instances

        Get list of task instance of DAG.  # noqa: E501
        """
        pass

    def test_upadte_pool(self):
        """Test case for upadte_pool

        Update a pool  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
