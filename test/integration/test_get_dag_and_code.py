"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

import logging

from test.integration.conftest import BCOLORS


def test_get_dag(dag_api_setup):
    """Test the /dags/{dag_id} API EP"""
    api_response = dag_api_setup.get_dag(dag_id="example_bash_operator")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

def test_get_dag_code(dag_api_setup):
    """Test the /dagSources/{file_token} API EP"""
    api_response = dag_api_setup.get_dag(dag_id="example_bash_operator")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

    file_token = api_response.file_token

    api_response = dag_api_setup.get_dag_source(file_token=file_token)
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")