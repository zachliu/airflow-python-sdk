# DAGRun

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dag_id** | **str** |  | [optional] [readonly] 
**execution_date** | **datetime** |  | [optional] 
**start_date** | **datetime** |  | [optional] [readonly] 
**end_date** | **datetime, none_type** |  | [optional] [readonly] 
**state** | [**TaskState**](TaskState.md) |  | [optional] 
**dag_run_id** | **str, none_type** |  | [optional] 
**external_trigger** | **bool** |  | [optional] [readonly]  if omitted the server will use the default value of True
**conf** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | JSON object describing additional configuration parameters.  The value of this field can be set only when creating the object. If you try to modify the field of an existing object, the request fails with an BAD_REQUEST error.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


