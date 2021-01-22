# airflow_python_sdk.VariableApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variable**](VariableApi.md#create_variable) | **POST** /variables | Create a variables
[**delete_variable**](VariableApi.md#delete_variable) | **DELETE** /variables/{variable_id} | Delete variable
[**get_variable**](VariableApi.md#get_variable) | **GET** /variables/{variable_id} | Get a variables by id
[**get_variables**](VariableApi.md#get_variables) | **GET** /variables | Get all variables
[**lookup_variable**](VariableApi.md#lookup_variable) | **GET** /variables/lookup | Get variable using its key.
[**update_variable**](VariableApi.md#update_variable) | **PATCH** /variables/{variable_id} | Update a variable by id


# **create_variable**
> Variable create_variable(variable)

Create a variables

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
from airflow_python_sdk.model.variable import Variable
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
    api_instance = variable_api.VariableApi(api_client)
    variable = Variable() # Variable | 

    # example passing only required values which don't have defaults set
    try:
        # Create a variables
        api_response = api_instance.create_variable(variable)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->create_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable** | [**Variable**](Variable.md)|  |

### Return type

[**Variable**](Variable.md)

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

# **delete_variable**
> delete_variable(variable_id)

Delete variable

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
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
    api_instance = variable_api.VariableApi(api_client)
    variable_id = "variable_id_example" # str | The Variable ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete variable
        api_instance.delete_variable(variable_id)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->delete_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The Variable ID. |

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

# **get_variable**
> Variable get_variable(variable_id)

Get a variables by id

The collection does not contain data. To get data, you must get a single entity.

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
from airflow_python_sdk.model.variable import Variable
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
    api_instance = variable_api.VariableApi(api_client)
    variable_id = "variable_id_example" # str | The Variable ID.

    # example passing only required values which don't have defaults set
    try:
        # Get a variables by id
        api_response = api_instance.get_variable(variable_id)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->get_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The Variable ID. |

### Return type

[**Variable**](Variable.md)

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

# **get_variables**
> VariableCollection get_variables()

Get all variables

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.variable_collection import VariableCollection
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
    api_instance = variable_api.VariableApi(api_client)
    limit = 100 # int | The numbers of items to return. (optional) if omitted the server will use the default value of 100
    offset = 0 # int | The number of items to skip before starting to collect the result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all variables
        api_response = api_instance.get_variables(limit=limit, offset=offset)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->get_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The numbers of items to return. | [optional] if omitted the server will use the default value of 100
 **offset** | **int**| The number of items to skip before starting to collect the result set. | [optional]

### Return type

[**VariableCollection**](VariableCollection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of variables. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_variable**
> Variable lookup_variable(variable_key)

Get variable using its key.

The response contains all fields, including data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
from airflow_python_sdk.model.variable import Variable
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
    api_instance = variable_api.VariableApi(api_client)
    variable_key = "variable_key_example" # str | The Variable Key.

    # example passing only required values which don't have defaults set
    try:
        # Get variable using its key.
        api_response = api_instance.lookup_variable(variable_key)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->lookup_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_key** | **str**| The Variable Key. |

### Return type

[**Variable**](Variable.md)

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

# **update_variable**
> Variable update_variable(variable_id, variable)

Update a variable by id

### Example

* Basic Authentication (basicAuth):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import variable_api
from airflow_python_sdk.model.variable import Variable
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
    api_instance = variable_api.VariableApi(api_client)
    variable_id = "variable_id_example" # str | The Variable ID.
    variable = Variable() # Variable | 
    update_mask = [
        "update_mask_example",
    ] # [str] | The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a variable by id
        api_response = api_instance.update_variable(variable_id, variable)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->update_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a variable by id
        api_response = api_instance.update_variable(variable_id, variable, update_mask=update_mask)
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling VariableApi->update_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| The Variable ID. |
 **variable** | [**Variable**](Variable.md)|  |
 **update_mask** | **[str]**| The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional]

### Return type

[**Variable**](Variable.md)

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

