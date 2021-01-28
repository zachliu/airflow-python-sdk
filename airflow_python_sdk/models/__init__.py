# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from airflow_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from airflow_python_sdk.model.class_reference import ClassReference
from airflow_python_sdk.model.clear_task_instance import ClearTaskInstance
from airflow_python_sdk.model.collection_info import CollectionInfo
from airflow_python_sdk.model.color import Color
from airflow_python_sdk.model.config import Config
from airflow_python_sdk.model.config_option import ConfigOption
from airflow_python_sdk.model.config_section import ConfigSection
from airflow_python_sdk.model.connection import Connection
from airflow_python_sdk.model.connection_all_of import ConnectionAllOf
from airflow_python_sdk.model.connection_collection import ConnectionCollection
from airflow_python_sdk.model.connection_collection_item import ConnectionCollectionItem
from airflow_python_sdk.model.cron_expression import CronExpression
from airflow_python_sdk.model.dag import DAG
from airflow_python_sdk.model.dag_collection import DAGCollection
from airflow_python_sdk.model.dag_run import DAGRun
from airflow_python_sdk.model.dag_run_collection import DAGRunCollection
from airflow_python_sdk.model.dag_state import DagState
from airflow_python_sdk.model.dag_structure import DagStructure
from airflow_python_sdk.model.dag_structure_collection import DagStructureCollection
from airflow_python_sdk.model.error import Error
from airflow_python_sdk.model.event_log import EventLog
from airflow_python_sdk.model.event_log_collection import EventLogCollection
from airflow_python_sdk.model.extra_link import ExtraLink
from airflow_python_sdk.model.extra_link_collection import ExtraLinkCollection
from airflow_python_sdk.model.import_error import ImportError
from airflow_python_sdk.model.import_error_collection import ImportErrorCollection
from airflow_python_sdk.model.inline_response200 import InlineResponse200
from airflow_python_sdk.model.inline_response2001 import InlineResponse2001
from airflow_python_sdk.model.pool import Pool
from airflow_python_sdk.model.pool_collection import PoolCollection
from airflow_python_sdk.model.relative_delta import RelativeDelta
from airflow_python_sdk.model.sla_miss import SLAMiss
from airflow_python_sdk.model.sla_miss_collection import SLAMissCollection
from airflow_python_sdk.model.schedule_interval import ScheduleInterval
from airflow_python_sdk.model.tag import Tag
from airflow_python_sdk.model.task import Task
from airflow_python_sdk.model.task_collection import TaskCollection
from airflow_python_sdk.model.task_extra_links import TaskExtraLinks
from airflow_python_sdk.model.task_fail import TaskFail
from airflow_python_sdk.model.task_instance import TaskInstance
from airflow_python_sdk.model.task_instance_collection import TaskInstanceCollection
from airflow_python_sdk.model.task_instance_reference import TaskInstanceReference
from airflow_python_sdk.model.task_instance_reference_collection import TaskInstanceReferenceCollection
from airflow_python_sdk.model.task_state import TaskState
from airflow_python_sdk.model.time_delta import TimeDelta
from airflow_python_sdk.model.trigger_rule import TriggerRule
from airflow_python_sdk.model.update_task_instances_state import UpdateTaskInstancesState
from airflow_python_sdk.model.variable import Variable
from airflow_python_sdk.model.variable_all_of import VariableAllOf
from airflow_python_sdk.model.variable_collection import VariableCollection
from airflow_python_sdk.model.variable_collection_item import VariableCollectionItem
from airflow_python_sdk.model.weight_rule import WeightRule
from airflow_python_sdk.model.x_com import XCom
from airflow_python_sdk.model.x_com_collection import XComCollection
from airflow_python_sdk.model.x_com_collection_item import XComCollectionItem
