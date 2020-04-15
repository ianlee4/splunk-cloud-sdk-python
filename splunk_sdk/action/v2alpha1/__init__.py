# coding: utf-8

# flake8: noqa

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
    SDC Service: Action Service

    With the Splunk Cloud Action service, you can receive incoming trigger events and use pre-defined action templates to turn these events into meaningful actions. 

    OpenAPI spec version: v2alpha1.12 
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.action.v2alpha1.gen_action_service_api import ActionService

# import models into sdk package
from splunk_sdk.action.v2alpha1.gen_models import Action, \
    ActionKind, \
    ActionMutable, \
    AppMessageAction, \
    EmailAction, \
    EmailActionMutable, \
    PublicWebhookKey, \
    ServiceError, \
    WebhookAction, \
    WebhookActionMutable