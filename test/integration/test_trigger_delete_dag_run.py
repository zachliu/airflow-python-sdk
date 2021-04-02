"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

import logging
from datetime import datetime
from time import sleep

from test.integration.conftest import BCOLORS

from airflow_python_sdk.model.dag_run import DAGRun
from dateutil.parser import parse

def test_trigger_delete_dag_run(dag_run_api_setup):
    """Test the /dags/{dag_id}/dagRuns API EP (post) &
    /dags/{dag_id}/dagRuns/{dag_run_id} API EP (delete)"""
    time_now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    dag_run_id = "test2__{}".format(time_now)
    dag_run = DAGRun(
        dag_run_id=dag_run_id,
        execution_date=parse(time_now),
        conf={},
    )
    trigger_resp = dag_run_api_setup.post_dag_run(
        dag_id="example_bash_operator",
        dag_run=dag_run,
    )
    logging.getLogger().info("%s", trigger_resp)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

    sleep(5)

    delete_resp = dag_run_api_setup.delete_dag_run(
        dag_id="example_bash_operator",
        dag_run_id=dag_run_id,
    )
    logging.getLogger().info("%s", delete_resp)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")