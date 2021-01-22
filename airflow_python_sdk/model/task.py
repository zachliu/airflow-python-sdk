"""
    Airflow API (Stable)

    Apache Airflow management API.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: zach.z.liu@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from airflow_python_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from airflow_python_sdk.model.class_reference import ClassReference
    from airflow_python_sdk.model.color import Color
    from airflow_python_sdk.model.task_extra_links import TaskExtraLinks
    from airflow_python_sdk.model.time_delta import TimeDelta
    from airflow_python_sdk.model.trigger_rule import TriggerRule
    from airflow_python_sdk.model.weight_rule import WeightRule
    globals()['ClassReference'] = ClassReference
    globals()['Color'] = Color
    globals()['TaskExtraLinks'] = TaskExtraLinks
    globals()['TimeDelta'] = TimeDelta
    globals()['TriggerRule'] = TriggerRule
    globals()['WeightRule'] = WeightRule


class Task(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'class_ref': (ClassReference,),  # noqa: E501
            'task_id': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'start_date': (datetime,),  # noqa: E501
            'end_date': (datetime,),  # noqa: E501
            'trigger_rule': (TriggerRule,),  # noqa: E501
            'extra_links': ([TaskExtraLinks],),  # noqa: E501
            'depends_on_past': (bool,),  # noqa: E501
            'wait_for_downstream': (bool,),  # noqa: E501
            'retries': (float,),  # noqa: E501
            'queue': (str,),  # noqa: E501
            'pool': (str,),  # noqa: E501
            'pool_slots': (float,),  # noqa: E501
            'execution_timeout': (TimeDelta,),  # noqa: E501
            'retry_delay': (TimeDelta,),  # noqa: E501
            'retry_exponential_backoff': (bool,),  # noqa: E501
            'priority_weight': (float,),  # noqa: E501
            'weight_rule': (WeightRule,),  # noqa: E501
            'ui_color': (Color,),  # noqa: E501
            'ui_fgcolor': (Color,),  # noqa: E501
            'template_fields': ([str],),  # noqa: E501
            'sub_dag_id': (str,),  # noqa: E501
            'downstream_task_ids': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_ref': 'class_ref',  # noqa: E501
        'task_id': 'task_id',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'trigger_rule': 'trigger_rule',  # noqa: E501
        'extra_links': 'extra_links',  # noqa: E501
        'depends_on_past': 'depends_on_past',  # noqa: E501
        'wait_for_downstream': 'wait_for_downstream',  # noqa: E501
        'retries': 'retries',  # noqa: E501
        'queue': 'queue',  # noqa: E501
        'pool': 'pool',  # noqa: E501
        'pool_slots': 'pool_slots',  # noqa: E501
        'execution_timeout': 'execution_timeout',  # noqa: E501
        'retry_delay': 'retry_delay',  # noqa: E501
        'retry_exponential_backoff': 'retry_exponential_backoff',  # noqa: E501
        'priority_weight': 'priority_weight',  # noqa: E501
        'weight_rule': 'weight_rule',  # noqa: E501
        'ui_color': 'ui_color',  # noqa: E501
        'ui_fgcolor': 'ui_fgcolor',  # noqa: E501
        'template_fields': 'template_fields',  # noqa: E501
        'sub_dag_id': 'sub_dag_id',  # noqa: E501
        'downstream_task_ids': 'downstream_task_ids',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Task - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            class_ref (ClassReference): [optional]  # noqa: E501
            task_id (str): [optional]  # noqa: E501
            owner (str): [optional]  # noqa: E501
            start_date (datetime): [optional]  # noqa: E501
            end_date (datetime): [optional]  # noqa: E501
            trigger_rule (TriggerRule): [optional]  # noqa: E501
            extra_links ([TaskExtraLinks]): [optional]  # noqa: E501
            depends_on_past (bool): [optional]  # noqa: E501
            wait_for_downstream (bool): [optional]  # noqa: E501
            retries (float): [optional]  # noqa: E501
            queue (str): [optional]  # noqa: E501
            pool (str): [optional]  # noqa: E501
            pool_slots (float): [optional]  # noqa: E501
            execution_timeout (TimeDelta): [optional]  # noqa: E501
            retry_delay (TimeDelta): [optional]  # noqa: E501
            retry_exponential_backoff (bool): [optional]  # noqa: E501
            priority_weight (float): [optional]  # noqa: E501
            weight_rule (WeightRule): [optional]  # noqa: E501
            ui_color (Color): [optional]  # noqa: E501
            ui_fgcolor (Color): [optional]  # noqa: E501
            template_fields ([str]): [optional]  # noqa: E501
            sub_dag_id (str): [optional]  # noqa: E501
            downstream_task_ids ([str]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)