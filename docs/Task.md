# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_ref** | [**ClassReference**](ClassReference.md) |  | [optional] 
**task_id** | **str** |  | [optional] [readonly] 
**owner** | **str** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**end_date** | **datetime** |  | [optional] [readonly] 
**trigger_rule** | [**TriggerRule**](TriggerRule.md) |  | [optional] 
**extra_links** | [**[TaskExtraLinks]**](TaskExtraLinks.md) |  | [optional] [readonly] 
**depends_on_past** | **bool** |  | [optional] [readonly] 
**wait_for_downstream** | **bool** |  | [optional] [readonly] 
**retries** | **float** |  | [optional] [readonly] 
**queue** | **str** |  | [optional] [readonly] 
**pool** | **str** |  | [optional] [readonly] 
**pool_slots** | **float** |  | [optional] [readonly] 
**execution_timeout** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_delay** | [**TimeDelta**](TimeDelta.md) |  | [optional] 
**retry_exponential_backoff** | **bool** |  | [optional] [readonly] 
**priority_weight** | **float** |  | [optional] [readonly] 
**weight_rule** | [**WeightRule**](WeightRule.md) |  | [optional] 
**ui_color** | [**Color**](Color.md) |  | [optional] 
**ui_fgcolor** | [**Color**](Color.md) |  | [optional] 
**template_fields** | **[str]** |  | [optional] [readonly] 
**sub_dag_id** | **str** |  | [optional] [readonly] 
**downstream_task_ids** | **[str]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


