# airflow_python_sdk.EventLogApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_log**](EventLogApi.md#create_event_log) | **POST** /eventLogs | Create event log
[**delete_event_log_entry**](EventLogApi.md#delete_event_log_entry) | **DELETE** /eventLogs/{event_log_id} | Delete a log entry
[**get_event_log**](EventLogApi.md#get_event_log) | **GET** /eventLogs | Get all log entries from event log
[**get_event_log_entry**](EventLogApi.md#get_event_log_entry) | **GET** /eventLogs/{event_log_id} | Get a log entry
[**update_event_log_entry**](EventLogApi.md#update_event_log_entry) | **PATCH** /eventLogs/{event_log_id} | Update a log entry


# **create_event_log**
> EventLog create_event_log(event_log)

Create event log

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import event_log_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.event_log import EventLog
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
    api_instance = event_log_api.EventLogApi(api_client)
    event_log = EventLog(
        id=1,
        dttm="dttm_example",
        dag_id="dag_id_example",
        task_id="task_id_example",
        event="event_example",
        execution_date="execution_date_example",
        owner="owner_example",
        extra="extra_example",
    ) # EventLog | 

    # example passing only required values which don't have defaults set
    try:
        # Create event log
        api_response = api_instance.create_event_log(event_log)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->create_event_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log** | [**EventLog**](EventLog.md)|  |

### Return type

[**EventLog**](EventLog.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_log_entry**
> delete_event_log_entry(event_log_id)

Delete a log entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import event_log_api
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
    api_instance = event_log_api.EventLogApi(api_client)
    event_log_id = 1 # int | The Import Error ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a log entry
        api_instance.delete_event_log_entry(event_log_id)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->delete_event_log_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The Import Error ID. |

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

# **get_event_log**
> EventLogCollection get_event_log()

Get all log entries from event log

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import event_log_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.event_log_collection import EventLogCollection
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
    api_instance = event_log_api.EventLogApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all log entries from event log
        api_response = api_instance.get_event_log(limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->get_event_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**EventLogCollection**](EventLogCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of log entries. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_log_entry**
> EventLog get_event_log_entry(event_log_id)

Get a log entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import event_log_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.event_log import EventLog
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
    api_instance = event_log_api.EventLogApi(api_client)
    event_log_id = 1 # int | The Import Error ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a log entry
        api_response = api_instance.get_event_log_entry(event_log_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->get_event_log_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The Import Error ID. |

### Return type

[**EventLog**](EventLog.md)

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

# **update_event_log_entry**
> EventLog update_event_log_entry(event_log_id, event_log)

Update a log entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import event_log_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.event_log import EventLog
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
    api_instance = event_log_api.EventLogApi(api_client)
    event_log_id = 1 # int | The Import Error ID.
    event_log = EventLog(
        id=1,
        dttm="dttm_example",
        dag_id="dag_id_example",
        task_id="task_id_example",
        event="event_example",
        execution_date="execution_date_example",
        owner="owner_example",
        extra="extra_example",
    ) # EventLog | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a log entry
        api_response = api_instance.update_event_log_entry(event_log_id, event_log)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->update_event_log_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a log entry
        api_response = api_instance.update_event_log_entry(event_log_id, event_log, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling EventLogApi->update_event_log_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_log_id** | **int**| The Import Error ID. |
 **event_log** | [**EventLog**](EventLog.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**EventLog**](EventLog.md)

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

