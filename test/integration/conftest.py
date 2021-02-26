"""
    Pre-tests fixtures
"""

import os

import pytest

from airflow_python_sdk.api.dag_api import DAGApi  # noqa: E501
from airflow_python_sdk.api.dag_run_api import DAGRunApi  # noqa: E501
from airflow_python_sdk.api.config_api import ConfigApi  # noqa: E501
from airflow_python_sdk.api.monitoring_api import MonitoringApi  # noqa: E501
from airflow_python_sdk.api.connection_api import ConnectionApi  # noqa: E501
from airflow_python_sdk.api.event_log_api import EventLogApi
from airflow_python_sdk.api.import_error_api import ImportErrorApi
from airflow_python_sdk.api.pool_api import PoolApi
from airflow_python_sdk.api.task_instance_api import TaskInstanceApi
from airflow_python_sdk.api.variable_api import VariableApi
from airflow_python_sdk.api.x_com_api import XComApi
from airflow_python_sdk import Configuration, ApiClient

if "API_HOST" not in os.environ or \
        "API_USERNAME" not in os.environ or \
        "API_PASSWORD" not in os.environ or \
        not os.environ["API_HOST"] or \
        not os.environ["API_USERNAME"] or \
        not os.environ["API_PASSWORD"]:
    raise EnvironmentError(
        "Must use API_HOST, API_USERNAME, API_PASSWORD "
        "as environment variables"
    )

API_CLIENT = ApiClient(
    Configuration(
        host=os.environ["API_HOST"],
        username=os.environ["API_USERNAME"],
        password=os.environ["API_PASSWORD"],
    )
)

class BCOLORS:
    """Color constants"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@pytest.fixture
def config_api_setup():
    """Instantiate api"""
    return ConfigApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def dag_api_setup():
    """Instantiate api"""
    return DAGApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def dag_run_api_setup():
    """Instantiate api"""
    return DAGRunApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def monitoring_api_setup():
    """Instantiate api"""
    return MonitoringApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def connection_api_setup():
    """Instantiate api"""
    return ConnectionApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def event_log_api_setup():
    """Instantiate api"""
    return EventLogApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def import_error_api_setup():
    """Instantiate api"""
    return ImportErrorApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def pool_api_setup():
    """Instantiate api"""
    return PoolApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def task_instance_api_setup():
    """Instantiate api"""
    return TaskInstanceApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def variable_api_setup():
    """Instantiate api"""
    return VariableApi(API_CLIENT)  # noqa: E501

@pytest.fixture
def xcom_api_setup():
    """Instantiate api"""
    return XComApi(API_CLIENT)  # noqa: E501
