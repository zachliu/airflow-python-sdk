"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import airflow_python_sdk
from airflow_python_sdk.api.task_instance_api import TaskInstanceApi  # noqa: E501


class TestTaskInstanceApi(unittest.TestCase):
    """TaskInstanceApi unit test stubs"""

    def setUp(self):
        self.api = TaskInstanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_task_instance(self):
        """Test case for delete_task_instance

        Delete DAG Run  # noqa: E501
        """
        pass

    def test_get_extra_links(self):
        """Test case for get_extra_links

        Get extra links for task instance  # noqa: E501
        """
        pass

    def test_get_logs(self):
        """Test case for get_logs

        Get logs for specific task instance  # noqa: E501
        """
        pass

    def test_get_task_instance(self):
        """Test case for get_task_instance

        Get a task instance  # noqa: E501
        """
        pass

    def test_update_task_instance(self):
        """Test case for update_task_instance

        Update a task instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
