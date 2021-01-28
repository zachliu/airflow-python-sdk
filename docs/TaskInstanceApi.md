# airflow_python_sdk.TaskInstanceApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task_instance**](TaskInstanceApi.md#delete_task_instance) | **DELETE** /dags/{dag_id}/taskInstances/{task_id}/{execution_date} | Delete DAG Run
[**get_extra_links**](TaskInstanceApi.md#get_extra_links) | **GET** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/links | Get extra links for task instance
[**get_logs**](TaskInstanceApi.md#get_logs) | **GET** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/logs/{task_try_number} | Get logs for specific task instance
[**get_task_instance**](TaskInstanceApi.md#get_task_instance) | **GET** /dags/{dag_id}/taskInstances/{task_id}/{execution_date} | Get a task instance
[**update_task_instance**](TaskInstanceApi.md#update_task_instance) | **PATCH** /dags/{dag_id}/taskInstances/{task_id}/{execution_date} | Update a task instance


# **delete_task_instance**
> delete_task_instance(dag_id, task_id, execution_date)

Delete DAG Run

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import task_instance_api
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
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

    # example passing only required values which don't have defaults set
    try:
        # Delete DAG Run
        api_instance.delete_task_instance(dag_id, task_id, execution_date)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->delete_task_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |

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

# **get_extra_links**
> ExtraLinkCollection get_extra_links(dag_id, task_id, execution_date)

Get extra links for task instance

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import task_instance_api
from airflow_python_sdk.model.extra_link_collection import ExtraLinkCollection
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
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

    # example passing only required values which don't have defaults set
    try:
        # Get extra links for task instance
        api_response = api_instance.get_extra_links(dag_id, task_id, execution_date)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_extra_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |

### Return type

[**ExtraLinkCollection**](ExtraLinkCollection.md)

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

# **get_logs**
> InlineResponse200 get_logs(dag_id, task_id, execution_date, task_try_number)

Get logs for specific task instance

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import task_instance_api
from airflow_python_sdk.model.inline_response200 import InlineResponse200
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
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    task_try_number = 1 # int | The Task Try Number.
    full_content = True # bool | A full reply will be returned. By default, only the first fragment will be returned.  (optional)
    token = True # bool | A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get logs for specific task instance
        api_response = api_instance.get_logs(dag_id, task_id, execution_date, task_try_number)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get logs for specific task instance
        api_response = api_instance.get_logs(dag_id, task_id, execution_date, task_try_number, full_content=full_content, token=token)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **task_try_number** | **int**| The Task Try Number. |
 **full_content** | **bool**| A full reply will be returned. By default, only the first fragment will be returned.  | [optional]
 **token** | **bool**| A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content of logs. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |
**404** | A specified resource is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_instance**
> TaskInstance get_task_instance(dag_id, task_id, execution_date)

Get a task instance

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import task_instance_api
from airflow_python_sdk.model.task_instance import TaskInstance
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
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

    # example passing only required values which don't have defaults set
    try:
        # Get a task instance
        api_response = api_instance.get_task_instance(dag_id, task_id, execution_date)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->get_task_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |

### Return type

[**TaskInstance**](TaskInstance.md)

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

# **update_task_instance**
> TaskInstance update_task_instance(dag_id, task_id, execution_date, task_instance)

Update a task instance

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import task_instance_api
from airflow_python_sdk.model.task_instance import TaskInstance
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
    api_instance = task_instance_api.TaskInstanceApi(api_client)
    dag_id = "dag_id_example" # str | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    task_instance = TaskInstance(
        task_id="task_id_example",
        dag_id="dag_id_example",
        execution_date="execution_date_example",
        start_date="start_date_example",
        end_date="end_date_example",
        duration=3.14,
        state=TaskState("success"),
        try_number=1,
        max_tries=1,
        hostname="hostname_example",
        unixname="unixname_example",
        job_id=1,
        pool="pool_example",
        pool_slots=1,
        queue="queue_example",
        priority_weight=1,
        operator="operator_example",
        queued_dttm="queued_dttm_example",
        pid=1,
        executor_config="executor_config_example",
        sla_miss=SLAMiss(
            task_id="task_id_example",
            dag_id="dag_id_example",
            execution_date="execution_date_example",
            email_sent=True,
            timestamp="timestamp_example",
            description="description_example",
            notification_sent=True,
        ),
    ) # TaskInstance | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a task instance
        api_response = api_instance.update_task_instance(dag_id, task_id, execution_date, task_instance)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->update_task_instance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a task instance
        api_response = api_instance.update_task_instance(dag_id, task_id, execution_date, task_instance, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling TaskInstanceApi->update_task_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **str**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **task_instance** | [**TaskInstance**](TaskInstance.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**TaskInstance**](TaskInstance.md)

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

