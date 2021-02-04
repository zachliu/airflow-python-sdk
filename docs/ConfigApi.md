# airflow_python_sdk.ConfigApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigApi.md#get_config) | **GET** /config | Get current configuration


# **get_config**
> Config get_config()

Get current configuration

### Example

* Basic Authentication (Basic):
```python
import time
import airflow_python_sdk
from airflow_python_sdk.api import config_api
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.config import Config
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

# Configure HTTP basic authorization: Basic
configuration = airflow_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = config_api.ConfigApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get current configuration
        api_response = api_instance.get_config()
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Config**](Config.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

