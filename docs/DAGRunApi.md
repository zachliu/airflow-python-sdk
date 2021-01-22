# airflow_python_sdk.DAGRunApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dag_run**](DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG Run
[**get_dag_run**](DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG Run
[**get_dag_runs**](DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | Get all DAG Runs
[**update_dag_run**](DAGRunApi.md#update_dag_run) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id} | Update a DAG Run


# **delete_dag_run**
> delete_dag_run(dag_id, dag_run_id)

Delete a DAG Run

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import dag_run_api
from airflow_python_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_python_sdk.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = airflow_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = 1 # int | The DAG ID.
    dag_run_id = 1 # int | The DAG Run ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a DAG Run
        api_instance.delete_dag_run(dag_id, dag_run_id)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->delete_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **dag_run_id** | **int**| The DAG Run ID. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_run**
> DAGRun get_dag_run(dag_id, dag_run_id)

Get a DAG Run

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import dag_run_api
from airflow_python_sdk.model.dag_run import DAGRun
from airflow_python_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_python_sdk.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = airflow_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = 1 # int | The DAG ID.
    dag_run_id = 1 # int | The DAG Run ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a DAG Run
        api_response = api_instance.get_dag_run(dag_id, dag_run_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **dag_run_id** | **int**| The DAG Run ID. |

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dag_runs**
> DAGRunCollection get_dag_runs(dag_id)

Get all DAG Runs

This endpoint support reading resources across multiple DAGs by specifying a \"-\" as a dag_id. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import dag_run_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.dag_run_collection import DAGRunCollection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_python_sdk.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = airflow_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = 1 # int | The DAG ID.
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all DAG Runs
        api_response = api_instance.get_dag_runs(dag_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all DAG Runs
        api_response = api_instance.get_dag_runs(dag_id, limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->get_dag_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DAG Runs. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dag_run**
> DAGRun update_dag_run(dag_id, dag_run_id, dag_run)

Update a DAG Run

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import dag_run_api
from airflow_python_sdk.model.dag_run import DAGRun
from airflow_python_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = airflow_python_sdk.Configuration(
    host = "http://localhost/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = airflow_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dag_run_api.DAGRunApi(api_client)
    dag_id = 1 # int | The DAG ID.
    dag_run_id = 1 # int | The DAG Run ID.
    dag_run = DAGRun(
        dag_id="dag_id_example",
        execution_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        state=TaskState("success"),
        run_id="run_id_example",
        external_trigger=True,
    ) # DAGRun | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a DAG Run
        api_response = api_instance.update_dag_run(dag_id, dag_run_id, dag_run)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->update_dag_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a DAG Run
        api_response = api_instance.update_dag_run(dag_id, dag_run_id, dag_run, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling DAGRunApi->update_dag_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **dag_run_id** | **int**| The DAG Run ID. |
 **dag_run** | [**DAGRun**](DAGRun.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

