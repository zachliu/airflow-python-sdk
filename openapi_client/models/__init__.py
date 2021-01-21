# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.class_reference import ClassReference
from openapi_client.model.collection_info import CollectionInfo
from openapi_client.model.color import Color
from openapi_client.model.config import Config
from openapi_client.model.config_option import ConfigOption
from openapi_client.model.config_section import ConfigSection
from openapi_client.model.connection import Connection
from openapi_client.model.connection_all_of import ConnectionAllOf
from openapi_client.model.connection_collection import ConnectionCollection
from openapi_client.model.connection_collection_item import ConnectionCollectionItem
from openapi_client.model.cron_expression import CronExpression
from openapi_client.model.dag import DAG
from openapi_client.model.dag_collection import DAGCollection
from openapi_client.model.dag_run import DAGRun
from openapi_client.model.dag_run_collection import DAGRunCollection
from openapi_client.model.dag_state import DagState
from openapi_client.model.dag_structure import DagStructure
from openapi_client.model.dag_structure_collection import DagStructureCollection
from openapi_client.model.error import Error
from openapi_client.model.event_log import EventLog
from openapi_client.model.event_log_collection import EventLogCollection
from openapi_client.model.extra_link import ExtraLink
from openapi_client.model.extra_link_collection import ExtraLinkCollection
from openapi_client.model.import_error import ImportError
from openapi_client.model.import_error_collection import ImportErrorCollection
from openapi_client.model.inline_response200 import InlineResponse200
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.pool import Pool
from openapi_client.model.pool_collection import PoolCollection
from openapi_client.model.relative_delta import RelativeDelta
from openapi_client.model.sla_miss import SLAMiss
from openapi_client.model.sla_miss_collection import SLAMissCollection
from openapi_client.model.schedule_interval import ScheduleInterval
from openapi_client.model.tag import Tag
from openapi_client.model.task import Task
from openapi_client.model.task_collection import TaskCollection
from openapi_client.model.task_extra_links import TaskExtraLinks
from openapi_client.model.task_fail import TaskFail
from openapi_client.model.task_instance import TaskInstance
from openapi_client.model.task_instance_collection import TaskInstanceCollection
from openapi_client.model.task_state import TaskState
from openapi_client.model.time_delta import TimeDelta
from openapi_client.model.trigger_rule import TriggerRule
from openapi_client.model.variable import Variable
from openapi_client.model.variable_all_of import VariableAllOf
from openapi_client.model.variable_collection import VariableCollection
from openapi_client.model.variable_collection_item import VariableCollectionItem
from openapi_client.model.weight_rule import WeightRule
from openapi_client.model.x_com import XCom
from openapi_client.model.x_com_collection import XComCollection
from openapi_client.model.x_com_collection_item import XComCollectionItem
