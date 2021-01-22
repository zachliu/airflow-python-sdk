# airflow_python_sdk.XComApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_x_com_value**](XComApi.md#delete_x_com_value) | **DELETE** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/xcomValues/{key} | Delete an XCom entry
[**get_x_com_value**](XComApi.md#get_x_com_value) | **GET** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/xcomValues/{key} | Get an XCom entry
[**get_x_com_values**](XComApi.md#get_x_com_values) | **GET** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/xcomValues | Get all XCom values
[**update_x_com_value**](XComApi.md#update_x_com_value) | **PATCH** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/xcomValues/{key} | Update an XCom entry
[**update_x_com_values**](XComApi.md#update_x_com_values) | **POST** /dags/{dag_id}/taskInstances/{task_id}/{execution_date}/xcomValues | Create an XCom entry


# **delete_x_com_value**
> delete_x_com_value(dag_id, task_id, execution_date, key)

Delete an XCom entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import x_com_api
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
    api_instance = x_com_api.XComApi(api_client)
    dag_id = 1 # int | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    key = "key_example" # str | The XCom Key.

    # example passing only required values which don't have defaults set
    try:
        # Delete an XCom entry
        api_instance.delete_x_com_value(dag_id, task_id, execution_date, key)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->delete_x_com_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **key** | **str**| The XCom Key. |

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

# **get_x_com_value**
> XCom get_x_com_value(dag_id, task_id, execution_date, key)

Get an XCom entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import x_com_api
from airflow_python_sdk.model.x_com import XCom
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
    api_instance = x_com_api.XComApi(api_client)
    dag_id = 1 # int | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    key = "key_example" # str | The XCom Key.

    # example passing only required values which don't have defaults set
    try:
        # Get an XCom entry
        api_response = api_instance.get_x_com_value(dag_id, task_id, execution_date, key)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->get_x_com_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **key** | **str**| The XCom Key. |

### Return type

[**XCom**](XCom.md)

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

# **get_x_com_values**
> XComCollection get_x_com_values(dag_id, task_id, execution_date)

Get all XCom values

This endpoint support reading resources across multiple Task Instances by specifying a \"-\" as a `dag_id`, `task_id` and `execution_date`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import x_com_api
from airflow_python_sdk.model.x_com_collection import XComCollection
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
    api_instance = x_com_api.XComApi(api_client)
    dag_id = 1 # int | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all XCom values
        api_response = api_instance.get_x_com_values(dag_id, task_id, execution_date)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->get_x_com_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all XCom values
        api_response = api_instance.get_x_com_values(dag_id, task_id, execution_date, limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->get_x_com_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**XComCollection**](XComCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of XCom values. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_x_com_value**
> XCom update_x_com_value(dag_id, task_id, execution_date, key, x_com)

Update an XCom entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import x_com_api
from airflow_python_sdk.model.x_com import XCom
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
    api_instance = x_com_api.XComApi(api_client)
    dag_id = 1 # int | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    key = "key_example" # str | The XCom Key.
    x_com = XCom() # XCom | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an XCom entry
        api_response = api_instance.update_x_com_value(dag_id, task_id, execution_date, key, x_com)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->update_x_com_value: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an XCom entry
        api_response = api_instance.update_x_com_value(dag_id, task_id, execution_date, key, x_com, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->update_x_com_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **key** | **str**| The XCom Key. |
 **x_com** | [**XCom**](XCom.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**XCom**](XCom.md)

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

# **update_x_com_values**
> XCom update_x_com_values(dag_id, task_id, execution_date, x_com)

Create an XCom entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import x_com_api
from airflow_python_sdk.model.x_com import XCom
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
    api_instance = x_com_api.XComApi(api_client)
    dag_id = 1 # int | The DAG ID.
    task_id = 1 # int | The Task ID.
    execution_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
    x_com = XCom() # XCom | 

    # example passing only required values which don't have defaults set
    try:
        # Create an XCom entry
        api_response = api_instance.update_x_com_values(dag_id, task_id, execution_date, x_com)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling XComApi->update_x_com_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dag_id** | **int**| The DAG ID. |
 **task_id** | **int**| The Task ID. |
 **execution_date** | **datetime**| The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. &#x60;2017-07-21T17:32:28Z&#x60;  |
 **x_com** | [**XCom**](XCom.md)|  |

### Return type

[**XCom**](XCom.md)

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

