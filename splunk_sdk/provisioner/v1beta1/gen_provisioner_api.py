# coding: utf-8

# Copyright © 2021 Splunk, Inc.
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


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.provisioner.v1beta1.gen_models import Error
from splunk_sdk.provisioner.v1beta1.gen_models import InviteBody
from splunk_sdk.provisioner.v1beta1.gen_models import InviteInfo
from splunk_sdk.provisioner.v1beta1.gen_models import TenantInfo
from splunk_sdk.provisioner.v1beta1.gen_models import UpdateInviteBody


class Provisioner(BaseService):
    """
    Provisioner
    Version: v1beta1.4
    With the Provisioner service in Splunk Cloud Services, you can provision and manage tenants.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_invite(self, invite_body: InviteBody, query_params: Dict[str, object] = None) -> InviteInfo:
        """
        Creates an invitation for a person to join the tenant using their email address.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/provisioner/v1beta1/invites").substitute(path_params)
        url = self.base_client.build_url(path)
        data = invite_body.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, InviteInfo)

    def delete_invite(self, invite_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Removes an invitation in the given tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "inviteId": invite_id,
        }

        path = Template("/provisioner/v1beta1/invites/${inviteId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def get_invite(self, invite_id: str, query_params: Dict[str, object] = None) -> InviteInfo:
        """
        Returns an invitation in the given tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "inviteId": invite_id,
        }

        path = Template("/provisioner/v1beta1/invites/${inviteId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, InviteInfo)

    def get_tenant(self, tenant_name: str, query_params: Dict[str, object] = None) -> TenantInfo:
        """
        Returns a specific tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "tenantName": tenant_name,
        }

        path = Template("/system/provisioner/v1beta1/tenants/${tenantName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TenantInfo)

    def list_invites(self, query_params: Dict[str, object] = None) -> List[InviteInfo]:
        """
        Returns a list of invitations in a given tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/provisioner/v1beta1/invites").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, InviteInfo)

    def list_tenants(self, query_params: Dict[str, object] = None) -> List[TenantInfo]:
        """
        Returns all tenants that the user can read.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/system/provisioner/v1beta1/tenants").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TenantInfo)

    def update_invite(self, invite_id: str, update_invite_body: UpdateInviteBody, query_params: Dict[str, object] = None) -> InviteInfo:
        """
        Modifies an invitation in the given tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "inviteId": invite_id,
        }

        path = Template("/provisioner/v1beta1/invites/${inviteId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = update_invite_body.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, InviteInfo)


