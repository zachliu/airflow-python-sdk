"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""

import logging

from test.integration.conftest import BCOLORS

from airflow_python_sdk.model.pool import Pool

POOL_DICT = {
    "name": "test_pool",
    "slots": 1,
}

INIT_POOL = Pool(**POOL_DICT)

def test_create_pool(pool_api_setup):
    """Test the post /pools API EP"""
    api_response = pool_api_setup.post_pool(INIT_POOL)
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

def test_update_pool(pool_api_setup):
    """Test the patch /pools/{pool_id} API EP"""
    POOL_DICT["slots"] = 2
    updated_pool = Pool(**POOL_DICT)
    api_response = pool_api_setup.patch_pool(
        "test_pool",
        updated_pool,
    )
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")

def test_get_pool(pool_api_setup):
    """Test the get /pools/{pool_id} API EP"""
    POOL_DICT["occupied_slots"] = 0
    POOL_DICT["open_slots"] = POOL_DICT["slots"]
    POOL_DICT["queued_slots"] = 0
    POOL_DICT["running_slots"] = 0
    updated_pool = Pool(**POOL_DICT)
    api_response = pool_api_setup.get_pool("test_pool")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")
    assert api_response == updated_pool

def test_delete_pool(pool_api_setup):
    """Test the delete /pools/{pool_id} API EP"""
    api_response = pool_api_setup.delete_pool("test_pool")
    logging.getLogger().info("%s", api_response)
    print(f"{BCOLORS.OKGREEN}OK{BCOLORS.ENDC}")