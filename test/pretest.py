"""
    Pre-tests fixtures
"""

import os
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

from airflow_python_sdk import Configuration, ApiClient

API_CLIENT = ApiClient(
    Configuration(
        host=os.environ["API_HOST"],
        username=os.environ["API_USERNAME"],
        password=os.environ["API_PASSWORD"],
    )
)
