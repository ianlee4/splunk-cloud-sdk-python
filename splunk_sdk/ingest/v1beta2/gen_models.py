# Copyright © 2020 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# [http://www.apache.org/licenses/LICENSE-2.0]
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Ingest API

    Use the Ingest service in Splunk Cloud Services to send event and metrics data, or upload a static file, to Splunk Cloud Services.

    OpenAPI spec version: v1beta2.3 (recommended default)
    Generated by: https://openapi-generator.tech
"""


from datetime import datetime
from typing import List, Dict
from splunk_sdk.common.sscmodel import SSCModel
from splunk_sdk.base_client import dictify, inflate
from enum import Enum



class Error(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "Error":
        instance = Error.__new__(Error)
        instance._attrs = model
        return instance

    def __init__(self, code: "str" = None, details: "object" = None, message: "str" = None, **extra):
        """Error"""

        self._attrs = dict()
        if code is not None:
            self._attrs["code"] = code
        if details is not None:
            self._attrs["details"] = details
        if message is not None:
            self._attrs["message"] = message
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def code(self) -> "str":
        """ Gets the code of this Error.
        """
        return self._attrs.get("code")

    @code.setter
    def code(self, code: "str"):
        """Sets the code of this Error.


        :param code: The code of this Error.
        :type: str
        """
        self._attrs["code"] = code

    @property
    def details(self) -> "dict":
        """ Gets the details of this Error.
        """
        return self._attrs.get("details")

    @details.setter
    def details(self, details: "dict"):
        """Sets the details of this Error.


        :param details: The details of this Error.
        :type: object
        """
        self._attrs["details"] = details

    @property
    def message(self) -> "str":
        """ Gets the message of this Error.
        """
        return self._attrs.get("message")

    @message.setter
    def message(self, message: "str"):
        """Sets the message of this Error.


        :param message: The message of this Error.
        :type: str
        """
        self._attrs["message"] = message

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class Event(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "Event":
        instance = Event.__new__(Event)
        instance._attrs = model
        return instance

    def __init__(self, body: "object", attributes: "Dict[str, object]" = None, host: "str" = None, id: "str" = None, nanos: "int" = None, source: "str" = None, sourcetype: "str" = None, timestamp: "int" = None, **extra):
        """Event"""

        self._attrs = dict()
        if body is not None:
            self._attrs["body"] = body
        if attributes is not None:
            self._attrs["attributes"] = attributes
        if host is not None:
            self._attrs["host"] = host
        if id is not None:
            self._attrs["id"] = id
        if nanos is not None:
            self._attrs["nanos"] = nanos
        if source is not None:
            self._attrs["source"] = source
        if sourcetype is not None:
            self._attrs["sourcetype"] = sourcetype
        if timestamp is not None:
            self._attrs["timestamp"] = timestamp
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def body(self) -> "object":
        """ Gets the body of this Event.
        JSON object for the event.
        """
        return self._attrs.get("body")

    @body.setter
    def body(self, body: "object"):
        """Sets the body of this Event.

        JSON object for the event.

        :param body: The body of this Event.
        :type: object
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")
        self._attrs["body"] = body

    @property
    def attributes(self) -> "dict":
        """ Gets the attributes of this Event.
        Specifies a JSON object that contains explicit custom fields to be defined at index time.
        """
        return self._attrs.get("attributes")

    @attributes.setter
    def attributes(self, attributes: "dict"):
        """Sets the attributes of this Event.

        Specifies a JSON object that contains explicit custom fields to be defined at index time.

        :param attributes: The attributes of this Event.
        :type: Dict[str, object]
        """
        self._attrs["attributes"] = attributes

    @property
    def host(self) -> "str":
        """ Gets the host of this Event.
        The host value assigned to the event data. Typically, this is the hostname of the client from which you are sending data.
        """
        return self._attrs.get("host")

    @host.setter
    def host(self, host: "str"):
        """Sets the host of this Event.

        The host value assigned to the event data. Typically, this is the hostname of the client from which you are sending data.

        :param host: The host of this Event.
        :type: str
        """
        self._attrs["host"] = host

    @property
    def id(self) -> "str":
        """ Gets the id of this Event.
        An optional ID that uniquely identifies the event data. It is used to deduplicate the data if same data is set multiple times. If ID is not specified, it will be assigned by the system.
        """
        return self._attrs.get("id")

    @id.setter
    def id(self, id: "str"):
        """Sets the id of this Event.

        An optional ID that uniquely identifies the event data. It is used to deduplicate the data if same data is set multiple times. If ID is not specified, it will be assigned by the system.

        :param id: The id of this Event.
        :type: str
        """
        self._attrs["id"] = id

    @property
    def nanos(self) -> "int":
        """ Gets the nanos of this Event.
        Optional nanoseconds part of the timestamp.
        """
        return self._attrs.get("nanos")

    @nanos.setter
    def nanos(self, nanos: "int"):
        """Sets the nanos of this Event.

        Optional nanoseconds part of the timestamp.

        :param nanos: The nanos of this Event.
        :type: int
        """
        self._attrs["nanos"] = nanos

    @property
    def source(self) -> "str":
        """ Gets the source of this Event.
        The source value to assign to the event data. For example, if you are sending data from an app that you are developing, set this key to the name of the app.
        """
        return self._attrs.get("source")

    @source.setter
    def source(self, source: "str"):
        """Sets the source of this Event.

        The source value to assign to the event data. For example, if you are sending data from an app that you are developing, set this key to the name of the app.

        :param source: The source of this Event.
        :type: str
        """
        self._attrs["source"] = source

    @property
    def sourcetype(self) -> "str":
        """ Gets the sourcetype of this Event.
        The sourcetype value assigned to the event data.
        """
        return self._attrs.get("sourcetype")

    @sourcetype.setter
    def sourcetype(self, sourcetype: "str"):
        """Sets the sourcetype of this Event.

        The sourcetype value assigned to the event data.

        :param sourcetype: The sourcetype of this Event.
        :type: str
        """
        self._attrs["sourcetype"] = sourcetype

    @property
    def timestamp(self) -> "int":
        """ Gets the timestamp of this Event.
        Epoch time in milliseconds.
        """
        return self._attrs.get("timestamp")

    @timestamp.setter
    def timestamp(self, timestamp: "int"):
        """Sets the timestamp of this Event.

        Epoch time in milliseconds.

        :param timestamp: The timestamp of this Event.
        :type: int
        """
        self._attrs["timestamp"] = timestamp

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class HTTPResponse(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "HTTPResponse":
        instance = HTTPResponse.__new__(HTTPResponse)
        instance._attrs = model
        return instance

    def __init__(self, code: "str" = None, details: "object" = None, message: "str" = None, **extra):
        """HTTPResponse"""

        self._attrs = dict()
        if code is not None:
            self._attrs["code"] = code
        if details is not None:
            self._attrs["details"] = details
        if message is not None:
            self._attrs["message"] = message
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def code(self) -> "str":
        """ Gets the code of this HTTPResponse.
        """
        return self._attrs.get("code")

    @code.setter
    def code(self, code: "str"):
        """Sets the code of this HTTPResponse.


        :param code: The code of this HTTPResponse.
        :type: str
        """
        self._attrs["code"] = code

    @property
    def details(self) -> "dict":
        """ Gets the details of this HTTPResponse.
        """
        return self._attrs.get("details")

    @details.setter
    def details(self, details: "dict"):
        """Sets the details of this HTTPResponse.


        :param details: The details of this HTTPResponse.
        :type: object
        """
        self._attrs["details"] = details

    @property
    def message(self) -> "str":
        """ Gets the message of this HTTPResponse.
        """
        return self._attrs.get("message")

    @message.setter
    def message(self, message: "str"):
        """Sets the message of this HTTPResponse.


        :param message: The message of this HTTPResponse.
        :type: str
        """
        self._attrs["message"] = message

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class Metric(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "Metric":
        instance = Metric.__new__(Metric)
        instance._attrs = model
        return instance

    def __init__(self, name: "str", dimensions: "Dict[str, str]" = None, type: "str" = None, unit: "str" = None, value: "float" = None, **extra):
        """Metric"""

        self._attrs = dict()
        if name is not None:
            self._attrs["name"] = name
        if dimensions is not None:
            self._attrs["dimensions"] = dimensions
        if type is not None:
            self._attrs["type"] = type
        if unit is not None:
            self._attrs["unit"] = unit
        if value is not None:
            self._attrs["value"] = value
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def name(self) -> "str":
        """ Gets the name of this Metric.
        Name of the metric e.g. CPU, Memory etc.
        """
        return self._attrs.get("name")

    @name.setter
    def name(self, name: "str"):
        """Sets the name of this Metric.

        Name of the metric e.g. CPU, Memory etc.

        :param name: The name of this Metric.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._attrs["name"] = name

    @property
    def dimensions(self) -> "Dict[str, str]":
        """ Gets the dimensions of this Metric.
        Dimensions allow metrics to be classified e.g. {\"Server\":\"nginx\", \"Region\":\"us-west-1\", ...}
        """
        return self._attrs.get("dimensions")

    @dimensions.setter
    def dimensions(self, dimensions: "Dict[str, str]"):
        """Sets the dimensions of this Metric.

        Dimensions allow metrics to be classified e.g. {\"Server\":\"nginx\", \"Region\":\"us-west-1\", ...}

        :param dimensions: The dimensions of this Metric.
        :type: Dict[str, str]
        """
        self._attrs["dimensions"] = dimensions

    @property
    def type(self) -> "str":
        """ Gets the type of this Metric.
        Type of metric. Default is g for gauge.
        """
        return self._attrs.get("type")

    @type.setter
    def type(self, type: "str"):
        """Sets the type of this Metric.

        Type of metric. Default is g for gauge.

        :param type: The type of this Metric.
        :type: str
        """
        self._attrs["type"] = type

    @property
    def unit(self) -> "str":
        """ Gets the unit of this Metric.
        Unit of the metric e.g. percent, megabytes, seconds etc.
        """
        return self._attrs.get("unit")

    @unit.setter
    def unit(self, unit: "str"):
        """Sets the unit of this Metric.

        Unit of the metric e.g. percent, megabytes, seconds etc.

        :param unit: The unit of this Metric.
        :type: str
        """
        self._attrs["unit"] = unit

    @property
    def value(self) -> "float":
        """ Gets the value of this Metric.
        Value of the metric. If not specified, it will be defaulted to 0.
        """
        return self._attrs.get("value")

    @value.setter
    def value(self, value: "float"):
        """Sets the value of this Metric.

        Value of the metric. If not specified, it will be defaulted to 0.

        :param value: The value of this Metric.
        :type: float
        """
        self._attrs["value"] = value

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class MetricAttribute(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "MetricAttribute":
        instance = MetricAttribute.__new__(MetricAttribute)
        instance._attrs = model
        return instance

    def __init__(self, default_dimensions: "Dict[str, str]" = None, default_type: "str" = None, default_unit: "str" = None, **extra):
        """MetricAttribute"""

        self._attrs = dict()
        if default_dimensions is not None:
            self._attrs["defaultDimensions"] = default_dimensions
        if default_type is not None:
            self._attrs["defaultType"] = default_type
        if default_unit is not None:
            self._attrs["defaultUnit"] = default_unit
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def default_dimensions(self) -> "Dict[str, str]":
        """ Gets the default_dimensions of this MetricAttribute.
        Optional. If set, individual metrics inherit these dimensions and can override any and/or all of them.
        """
        return self._attrs.get("defaultDimensions")

    @default_dimensions.setter
    def default_dimensions(self, default_dimensions: "Dict[str, str]"):
        """Sets the default_dimensions of this MetricAttribute.

        Optional. If set, individual metrics inherit these dimensions and can override any and/or all of them.

        :param default_dimensions: The default_dimensions of this MetricAttribute.
        :type: Dict[str, str]
        """
        self._attrs["defaultDimensions"] = default_dimensions

    @property
    def default_type(self) -> "str":
        """ Gets the default_type of this MetricAttribute.
        Optional. If set, individual metrics inherit this type and can optionally override.
        """
        return self._attrs.get("defaultType")

    @default_type.setter
    def default_type(self, default_type: "str"):
        """Sets the default_type of this MetricAttribute.

        Optional. If set, individual metrics inherit this type and can optionally override.

        :param default_type: The default_type of this MetricAttribute.
        :type: str
        """
        self._attrs["defaultType"] = default_type

    @property
    def default_unit(self) -> "str":
        """ Gets the default_unit of this MetricAttribute.
        Optional. If set, individual metrics inherit this unit and can optionally override.
        """
        return self._attrs.get("defaultUnit")

    @default_unit.setter
    def default_unit(self, default_unit: "str"):
        """Sets the default_unit of this MetricAttribute.

        Optional. If set, individual metrics inherit this unit and can optionally override.

        :param default_unit: The default_unit of this MetricAttribute.
        :type: str
        """
        self._attrs["defaultUnit"] = default_unit

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class MetricEvent(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "MetricEvent":
        instance = MetricEvent.__new__(MetricEvent)
        instance._attrs = model
        return instance

    def __init__(self, body: "List[Metric]", attributes: "MetricAttribute" = None, host: "str" = None, id: "str" = None, nanos: "int" = None, source: "str" = None, sourcetype: "str" = None, timestamp: "int" = None, **extra):
        """MetricEvent"""

        self._attrs = dict()
        if body is not None:
            self._attrs["body"] = body
        if attributes is not None:
            self._attrs["attributes"] = attributes.to_dict()
        if host is not None:
            self._attrs["host"] = host
        if id is not None:
            self._attrs["id"] = id
        if nanos is not None:
            self._attrs["nanos"] = nanos
        if source is not None:
            self._attrs["source"] = source
        if sourcetype is not None:
            self._attrs["sourcetype"] = sourcetype
        if timestamp is not None:
            self._attrs["timestamp"] = timestamp
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def body(self) -> "List[Metric]":
        """ Gets the body of this MetricEvent.
        Specifies multiple related metrics e.g. Memory, CPU etc.
        """
        return [Metric._from_dict(i) for i in self._attrs.get("body")]

    @body.setter
    def body(self, body: "List[Metric]"):
        """Sets the body of this MetricEvent.

        Specifies multiple related metrics e.g. Memory, CPU etc.

        :param body: The body of this MetricEvent.
        :type: List[Metric]
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")
        self._attrs["body"] = body

    @property
    def attributes(self) -> "MetricAttribute":
        """ Gets the attributes of this MetricEvent.
        """
        return MetricAttribute._from_dict(self._attrs["attributes"])

    @attributes.setter
    def attributes(self, attributes: "MetricAttribute"):
        """Sets the attributes of this MetricEvent.


        :param attributes: The attributes of this MetricEvent.
        :type: MetricAttribute
        """
        self._attrs["attributes"] = attributes.to_dict()

    @property
    def host(self) -> "str":
        """ Gets the host of this MetricEvent.
        The host value assigned to the event data. Typically, this is the hostname of the client from which you are sending data.
        """
        return self._attrs.get("host")

    @host.setter
    def host(self, host: "str"):
        """Sets the host of this MetricEvent.

        The host value assigned to the event data. Typically, this is the hostname of the client from which you are sending data.

        :param host: The host of this MetricEvent.
        :type: str
        """
        self._attrs["host"] = host

    @property
    def id(self) -> "str":
        """ Gets the id of this MetricEvent.
        An optional ID that uniquely identifies the metric data. It is used to deduplicate the data if same data is set multiple times. If ID is not specified, it will be assigned by the system.
        """
        return self._attrs.get("id")

    @id.setter
    def id(self, id: "str"):
        """Sets the id of this MetricEvent.

        An optional ID that uniquely identifies the metric data. It is used to deduplicate the data if same data is set multiple times. If ID is not specified, it will be assigned by the system.

        :param id: The id of this MetricEvent.
        :type: str
        """
        self._attrs["id"] = id

    @property
    def nanos(self) -> "int":
        """ Gets the nanos of this MetricEvent.
        Optional nanoseconds part of the timestamp.
        """
        return self._attrs.get("nanos")

    @nanos.setter
    def nanos(self, nanos: "int"):
        """Sets the nanos of this MetricEvent.

        Optional nanoseconds part of the timestamp.

        :param nanos: The nanos of this MetricEvent.
        :type: int
        """
        self._attrs["nanos"] = nanos

    @property
    def source(self) -> "str":
        """ Gets the source of this MetricEvent.
        The source value to assign to the event data. For example, if you are sending data from an app that you are developing, set this key to the name of the app.
        """
        return self._attrs.get("source")

    @source.setter
    def source(self, source: "str"):
        """Sets the source of this MetricEvent.

        The source value to assign to the event data. For example, if you are sending data from an app that you are developing, set this key to the name of the app.

        :param source: The source of this MetricEvent.
        :type: str
        """
        self._attrs["source"] = source

    @property
    def sourcetype(self) -> "str":
        """ Gets the sourcetype of this MetricEvent.
        The sourcetype value assigned to the event data.
        """
        return self._attrs.get("sourcetype")

    @sourcetype.setter
    def sourcetype(self, sourcetype: "str"):
        """Sets the sourcetype of this MetricEvent.

        The sourcetype value assigned to the event data.

        :param sourcetype: The sourcetype of this MetricEvent.
        :type: str
        """
        self._attrs["sourcetype"] = sourcetype

    @property
    def timestamp(self) -> "int":
        """ Gets the timestamp of this MetricEvent.
        Epoch time in milliseconds.
        """
        return self._attrs.get("timestamp")

    @timestamp.setter
    def timestamp(self, timestamp: "int"):
        """Sets the timestamp of this MetricEvent.

        Epoch time in milliseconds.

        :param timestamp: The timestamp of this MetricEvent.
        :type: int
        """
        self._attrs["timestamp"] = timestamp

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}
