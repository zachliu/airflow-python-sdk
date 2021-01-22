# airflow_python_sdk.ImportErrorApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_import_error**](ImportErrorApi.md#delete_import_error) | **DELETE** /importErrors/{import_error_id} | Delete an import error
[**get_import_error**](ImportErrorApi.md#get_import_error) | **GET** /importErrors/{import_error_id} | Get an import errors
[**get_import_errors**](ImportErrorApi.md#get_import_errors) | **GET** /importErrors | Get all import errors


# **delete_import_error**
> delete_import_error(import_error_id)

Delete an import error

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import import_error_api
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
    api_instance = import_error_api.ImportErrorApi(api_client)
    import_error_id = 1 # int | The Import Error ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete an import error
        api_instance.delete_import_error(import_error_id)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ImportErrorApi->delete_import_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_error_id** | **int**| The Import Error ID. |

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

# **get_import_error**
> ImportError get_import_error(import_error_id)

Get an import errors

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import import_error_api
from airflow_python_sdk.model.import_error import ImportError
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
    api_instance = import_error_api.ImportErrorApi(api_client)
    import_error_id = 1 # int | The Import Error ID.

    # example passing only required values which don't have defaults set
    try:
        # Get an import errors
        api_response = api_instance.get_import_error(import_error_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ImportErrorApi->get_import_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_error_id** | **int**| The Import Error ID. |

### Return type

[**ImportError**](ImportError.md)

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

# **get_import_errors**
> ImportErrorCollection get_import_errors()

Get all import errors

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import import_error_api
from airflow_python_sdk.model.import_error_collection import ImportErrorCollection
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
    api_instance = import_error_api.ImportErrorApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all import errors
        api_response = api_instance.get_import_errors(limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ImportErrorApi->get_import_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**ImportErrorCollection**](ImportErrorCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of import errors. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

