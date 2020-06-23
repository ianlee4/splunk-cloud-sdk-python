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
    SDC Service: Provisioner

    With the Provisioner service in Splunk Cloud Services, you can provision and manage tenants.

    OpenAPI spec version: v1beta1.4 (recommended default)
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.provisioner.v1beta1.gen_provisioner_api import Provisioner

# import models into sdk package
from splunk_sdk.provisioner.v1beta1.gen_models import CreateProvisionJobBody, \
    Error, \
    InviteBody, \
    InviteInfoErrorsItems, \
    InviteInfo, \
    ProvisionJobInfoErrorsItems, \
    ProvisionJobInfo, \
    TenantInfo, \
    UpdateInviteBody
