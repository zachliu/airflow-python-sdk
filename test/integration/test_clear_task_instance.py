"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

from test.integration.conftest import BCOLORS

import pytest

from airflow_python_sdk.model.clear_task_instance import ClearTaskInstance
from airflow_python_sdk.exceptions import ApiException


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([True, True], 400),
        ([False, False], None),
        ([True, False], None),
        ([False, True], None),
    ],
)
def test_post_clear_task_instance(dag_api_setup, test_input, expected):
    """Test the /dags/{dag_id}/clearTaskInstances API EP
    """
    dag_id = "test_glue_partitions_sensor"
    start_date = "2020-01-01T00:00:00.00Z"
    end_date = "2021-01-24T23:59:59.00Z"
    only_failed, only_running = test_input
    clear_task_instance = ClearTaskInstance(
        dry_run=True,
        start_date=start_date,
        end_date=end_date,
        include_parentdag=False,
        include_subdags=False,
        only_failed=only_failed,
        only_running=only_running,
        reset_dag_runs=True,
    )
    try:
        api_response = dag_api_setup.post_clear_task_instances(
            dag_id, clear_task_instance
        )
        print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")
    except ApiException as error:
        assert str(expected) in str(error)
