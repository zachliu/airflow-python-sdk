"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from airflow_python_sdk.api_client import ApiClient, Endpoint
from airflow_python_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.extra_link_collection import ExtraLinkCollection
from airflow_python_sdk.model.inline_response200 import InlineResponse200
from airflow_python_sdk.model.task_instance import TaskInstance


class TaskInstanceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_task_instance(
            self,
            dag_id,
            task_id,
            execution_date,
            **kwargs
        ):
            """Delete DAG Run  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_task_instance(dag_id, task_id, execution_date, async_req=True)
            >>> result = thread.get()

            Args:
                dag_id (int): The DAG ID.
                task_id (int): The Task ID.
                execution_date (datetime): The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dag_id'] = \
                dag_id
            kwargs['task_id'] = \
                task_id
            kwargs['execution_date'] = \
                execution_date
            return self.call_with_http_info(**kwargs)

        self.delete_task_instance = Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/dags/{dag_id}/taskInstances/{task_id}/{execution_date}',
                'operation_id': 'delete_task_instance',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'required': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (int,),
                    'task_id':
                        (int,),
                    'execution_date':
                        (datetime,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                    'execution_date': 'execution_date',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
                    'execution_date': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_task_instance
        )

        def __get_extra_links(
            self,
            dag_id,
            task_id,
            execution_date,
            **kwargs
        ):
            """Get extra links for task instance  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_extra_links(dag_id, task_id, execution_date, async_req=True)
            >>> result = thread.get()

            Args:
                dag_id (int): The DAG ID.
                task_id (int): The Task ID.
                execution_date (datetime): The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ExtraLinkCollection
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dag_id'] = \
                dag_id
            kwargs['task_id'] = \
                task_id
            kwargs['execution_date'] = \
                execution_date
            return self.call_with_http_info(**kwargs)

        self.get_extra_links = Endpoint(
            settings={
                'response_type': (ExtraLinkCollection,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/dags/{dag_id}/taskInstances/{task_id}/{execution_date}/links',
                'operation_id': 'get_extra_links',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'required': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (int,),
                    'task_id':
                        (int,),
                    'execution_date':
                        (datetime,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                    'execution_date': 'execution_date',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
                    'execution_date': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_extra_links
        )

        def __get_logs(
            self,
            dag_id,
            task_id,
            execution_date,
            task_try_number,
            **kwargs
        ):
            """Get logs for specific task instance  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_logs(dag_id, task_id, execution_date, task_try_number, async_req=True)
            >>> result = thread.get()

            Args:
                dag_id (int): The DAG ID.
                task_id (int): The Task ID.
                execution_date (datetime): The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
                task_try_number (int): The Task Try Number.

            Keyword Args:
                full_content (bool): A full reply will be returned. By default, only the first fragment will be returned. . [optional]
                token (bool): A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued. . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse200
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dag_id'] = \
                dag_id
            kwargs['task_id'] = \
                task_id
            kwargs['execution_date'] = \
                execution_date
            kwargs['task_try_number'] = \
                task_try_number
            return self.call_with_http_info(**kwargs)

        self.get_logs = Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/dags/{dag_id}/taskInstances/{task_id}/{execution_date}/logs/{task_try_number}',
                'operation_id': 'get_logs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                    'task_try_number',
                    'full_content',
                    'token',
                ],
                'required': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                    'task_try_number',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (int,),
                    'task_id':
                        (int,),
                    'execution_date':
                        (datetime,),
                    'task_try_number':
                        (int,),
                    'full_content':
                        (bool,),
                    'token':
                        (bool,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                    'execution_date': 'execution_date',
                    'task_try_number': 'task_try_number',
                    'full_content': 'full_content',
                    'token': 'token',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
                    'execution_date': 'path',
                    'task_try_number': 'path',
                    'full_content': 'query',
                    'token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_logs
        )

        def __get_task_instance(
            self,
            dag_id,
            task_id,
            execution_date,
            **kwargs
        ):
            """Get a task instance  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_task_instance(dag_id, task_id, execution_date, async_req=True)
            >>> result = thread.get()

            Args:
                dag_id (int): The DAG ID.
                task_id (int): The Task ID.
                execution_date (datetime): The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TaskInstance
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dag_id'] = \
                dag_id
            kwargs['task_id'] = \
                task_id
            kwargs['execution_date'] = \
                execution_date
            return self.call_with_http_info(**kwargs)

        self.get_task_instance = Endpoint(
            settings={
                'response_type': (TaskInstance,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/dags/{dag_id}/taskInstances/{task_id}/{execution_date}',
                'operation_id': 'get_task_instance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'required': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (int,),
                    'task_id':
                        (int,),
                    'execution_date':
                        (datetime,),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                    'execution_date': 'execution_date',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
                    'execution_date': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_task_instance
        )

        def __update_task_instance(
            self,
            dag_id,
            task_id,
            execution_date,
            task_instance,
            **kwargs
        ):
            """Update a task instance  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_task_instance(dag_id, task_id, execution_date, task_instance, async_req=True)
            >>> result = thread.get()

            Args:
                dag_id (int): The DAG ID.
                task_id (int): The Task ID.
                execution_date (datetime): The date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), E.G. `2017-07-21T17:32:28Z` 
                task_instance (TaskInstance):

            Keyword Args:
                update_mask ([str]): The fields to update on the connection (connection, pool etc). If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TaskInstance
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['dag_id'] = \
                dag_id
            kwargs['task_id'] = \
                task_id
            kwargs['execution_date'] = \
                execution_date
            kwargs['task_instance'] = \
                task_instance
            return self.call_with_http_info(**kwargs)

        self.update_task_instance = Endpoint(
            settings={
                'response_type': (TaskInstance,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/dags/{dag_id}/taskInstances/{task_id}/{execution_date}',
                'operation_id': 'update_task_instance',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                    'task_instance',
                    'update_mask',
                ],
                'required': [
                    'dag_id',
                    'task_id',
                    'execution_date',
                    'task_instance',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dag_id':
                        (int,),
                    'task_id':
                        (int,),
                    'execution_date':
                        (datetime,),
                    'task_instance':
                        (TaskInstance,),
                    'update_mask':
                        ([str],),
                },
                'attribute_map': {
                    'dag_id': 'dag_id',
                    'task_id': 'task_id',
                    'execution_date': 'execution_date',
                    'update_mask': 'update_mask',
                },
                'location_map': {
                    'dag_id': 'path',
                    'task_id': 'path',
                    'execution_date': 'path',
                    'task_instance': 'body',
                    'update_mask': 'query',
                },
                'collection_format_map': {
                    'update_mask': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_task_instance
        )