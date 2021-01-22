# airflow_python_sdk.ConnectionApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionApi.md#create_connection) | **POST** /connections | Create connection entry
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connections/{connection_id} | Delete a connection entry
[**get_connection**](ConnectionApi.md#get_connection) | **GET** /connections/{connection_id} | Get a connection entry
[**get_connections**](ConnectionApi.md#get_connections) | **GET** /connections | Get all connection entries
[**patch_connection**](ConnectionApi.md#patch_connection) | **PATCH** /connections/{connection_id} | Update a connection entry


# **create_connection**
> Connection create_connection(connection)

Create connection entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import connection_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.connection import Connection
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
    api_instance = connection_api.ConnectionApi(api_client)
    connection = Connection() # Connection | 

    # example passing only required values which don't have defaults set
    try:
        # Create connection entry
        api_response = api_instance.create_connection(connection)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->create_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | [**Connection**](Connection.md)|  |

### Return type

[**Connection**](Connection.md)

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

# **delete_connection**
> delete_connection(connection_id)

Delete a connection entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import connection_api
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
    api_instance = connection_api.ConnectionApi(api_client)
    connection_id = 1 # int | The Connection ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete a connection entry
        api_instance.delete_connection(connection_id)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| The Connection ID. |

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

# **get_connection**
> Connection get_connection(connection_id)

Get a connection entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import connection_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.connection import Connection
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
    api_instance = connection_api.ConnectionApi(api_client)
    connection_id = 1 # int | The Connection ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a connection entry
        api_response = api_instance.get_connection(connection_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->get_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| The Connection ID. |

### Return type

[**Connection**](Connection.md)

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

# **get_connections**
> ConnectionCollection get_connections()

Get all connection entries

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import connection_api
from airflow_python_sdk.model.connection_collection import ConnectionCollection
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
    api_instance = connection_api.ConnectionApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all connection entries
        api_response = api_instance.get_connections(limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->get_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**ConnectionCollection**](ConnectionCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of connection entry. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_connection**
> Connection patch_connection(connection_id, connection)

Update a connection entry

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import connection_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.connection import Connection
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
    api_instance = connection_api.ConnectionApi(api_client)
    connection_id = 1 # int | The Connection ID.
    connection = Connection() # Connection | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a connection entry
        api_response = api_instance.patch_connection(connection_id, connection)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->patch_connection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a connection entry
        api_response = api_instance.patch_connection(connection_id, connection, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->patch_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| The Connection ID. |
 **connection** | [**Connection**](Connection.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**Connection**](Connection.md)

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

