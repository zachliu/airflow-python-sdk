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
from airflow_python_sdk.model.cron_expression import CronExpression
from airflow_python_sdk.model.relative_delta import RelativeDelta
from airflow_python_sdk.model.time_delta import TimeDelta
globals()['CronExpression'] = CronExpression
globals()['RelativeDelta'] = RelativeDelta
globals()['TimeDelta'] = TimeDelta
from airflow_python_sdk.model.schedule_interval import ScheduleInterval


class TestScheduleInterval(unittest.TestCase):
    """ScheduleInterval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduleInterval(self):
        """Test ScheduleInterval"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScheduleInterval()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
