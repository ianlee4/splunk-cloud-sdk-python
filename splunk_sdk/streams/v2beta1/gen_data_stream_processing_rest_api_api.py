# coding: utf-8

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
    SDC Service: Data Stream Processing REST API

    Use the Streams service to perform create, read, update, and delete (CRUD) operations on your data pipeline. The Streams service also has metrics and preview session endpoints and gives you full control over your data pipeline.

    OpenAPI spec version: v2beta1.4 
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.streams.v2beta1.gen_models import ActivatePipelineRequest
from splunk_sdk.streams.v2beta1.gen_models import ConnectionPatchRequest
from splunk_sdk.streams.v2beta1.gen_models import ConnectionPutRequest
from splunk_sdk.streams.v2beta1.gen_models import ConnectionRequest
from splunk_sdk.streams.v2beta1.gen_models import ConnectionSaveResponse
from splunk_sdk.streams.v2beta1.gen_models import DeactivatePipelineRequest
from splunk_sdk.streams.v2beta1.gen_models import DslCompilationRequest
from splunk_sdk.streams.v2beta1.gen_models import GetInputSchemaRequest
from splunk_sdk.streams.v2beta1.gen_models import GetOutputSchemaRequest
from splunk_sdk.streams.v2beta1.gen_models import GroupExpandRequest
from splunk_sdk.streams.v2beta1.gen_models import GroupPatchRequest
from splunk_sdk.streams.v2beta1.gen_models import GroupPutRequest
from splunk_sdk.streams.v2beta1.gen_models import GroupRequest
from splunk_sdk.streams.v2beta1.gen_models import GroupResponse
from splunk_sdk.streams.v2beta1.gen_models import MetricsResponse
from splunk_sdk.streams.v2beta1.gen_models import PaginatedResponseOfConnectionResponse
from splunk_sdk.streams.v2beta1.gen_models import PaginatedResponseOfConnectorResponse
from splunk_sdk.streams.v2beta1.gen_models import PaginatedResponseOfPipelineJobStatus
from splunk_sdk.streams.v2beta1.gen_models import PaginatedResponseOfPipelineResponse
from splunk_sdk.streams.v2beta1.gen_models import PaginatedResponseOfTemplateResponse
from splunk_sdk.streams.v2beta1.gen_models import PipelineDeleteResponse
from splunk_sdk.streams.v2beta1.gen_models import PipelinePatchRequest
from splunk_sdk.streams.v2beta1.gen_models import PipelineReactivateResponse
from splunk_sdk.streams.v2beta1.gen_models import PipelineRequest
from splunk_sdk.streams.v2beta1.gen_models import PipelineResponse
from splunk_sdk.streams.v2beta1.gen_models import PipelinesMergeRequest
from splunk_sdk.streams.v2beta1.gen_models import PreviewData
from splunk_sdk.streams.v2beta1.gen_models import PreviewSessionStartRequest
from splunk_sdk.streams.v2beta1.gen_models import PreviewStartResponse
from splunk_sdk.streams.v2beta1.gen_models import PreviewState
from splunk_sdk.streams.v2beta1.gen_models import Response
from splunk_sdk.streams.v2beta1.gen_models import SplCompileRequest
from splunk_sdk.streams.v2beta1.gen_models import TemplatePatchRequest
from splunk_sdk.streams.v2beta1.gen_models import TemplatePutRequest
from splunk_sdk.streams.v2beta1.gen_models import TemplateRequest
from splunk_sdk.streams.v2beta1.gen_models import TemplateResponse
from splunk_sdk.streams.v2beta1.gen_models import UplPipeline
from splunk_sdk.streams.v2beta1.gen_models import UplRegistry
from splunk_sdk.streams.v2beta1.gen_models import UplType
from splunk_sdk.streams.v2beta1.gen_models import ValidateRequest
from splunk_sdk.streams.v2beta1.gen_models import ValidateResponse


class DataStreamProcessingRESTAPI(BaseService):
    """
    Data Stream Processing REST API
    Version: v2beta1.4
    Use the Streams service to perform create, read, update, and delete (CRUD) operations on your data pipeline. The Streams service also has metrics and preview session endpoints and gives you full control over your data pipeline.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def activate_pipeline(self, id: str, activate_pipeline_request: ActivatePipelineRequest, query_params: Dict[str, object] = None) -> Response:
        """
        Activates an existing pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}/activate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = activate_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Response)

    def compile_dsl(self, dsl_compilation_request: DslCompilationRequest, query_params: Dict[str, object] = None) -> UplPipeline:
        """
        Compiles the Streams DSL and returns Streams JSON.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/compile-dsl").substitute(path_params)
        url = self.base_client.build_url(path)
        data = dsl_compilation_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplPipeline)

    def compile_spl(self, spl_compile_request: SplCompileRequest, query_params: Dict[str, object] = None) -> UplPipeline:
        """
        Compiles SPL2 and returns Streams JSON.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/compile-spl").substitute(path_params)
        url = self.base_client.build_url(path)
        data = spl_compile_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplPipeline)

    def create_connection(self, connection_request: ConnectionRequest, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Create a new DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/connections").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def create_group(self, group_request: GroupRequest, query_params: Dict[str, object] = None) -> GroupResponse:
        """
        Create a new group function by combining the Streams JSON of two or more functions.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/groups").substitute(path_params)
        url = self.base_client.build_url(path)
        data = group_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, GroupResponse)

    def create_pipeline(self, pipeline_request: PipelineRequest, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Creates a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines").substitute(path_params)
        url = self.base_client.build_url(path)
        data = pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, PipelineResponse)

    def create_template(self, template_request: TemplateRequest, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Creates a template for a tenant.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/templates").substitute(path_params)
        url = self.base_client.build_url(path)
        data = template_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, TemplateResponse)

    def deactivate_pipeline(self, id: str, deactivate_pipeline_request: DeactivatePipelineRequest, query_params: Dict[str, object] = None) -> Response:
        """
        Deactivates an existing pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}/deactivate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = deactivate_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Response)

    def delete_connection(self, connection_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Delete all versions of a connection by its id.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v2beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_group(self, group_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Removes an existing group.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "groupId": group_id,
        }

        path = Template("/streams/v2beta1/groups/${groupId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_pipeline(self, id: str, query_params: Dict[str, object] = None) -> PipelineDeleteResponse:
        """
        Removes a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, PipelineDeleteResponse)

    def delete_template(self, template_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Removes a template with a specific ID.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v2beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def expand_group(self, group_id: str, group_expand_request: GroupExpandRequest, query_params: Dict[str, object] = None) -> UplPipeline:
        """
        Creates and returns the expanded version of a group.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "groupId": group_id,
        }

        path = Template("/streams/v2beta1/groups/${groupId}/expand").substitute(path_params)
        url = self.base_client.build_url(path)
        data = group_expand_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplPipeline)

    def expand_pipeline(self, upl_pipeline: UplPipeline, query_params: Dict[str, object] = None) -> UplPipeline:
        """
        Returns the entire Streams JSON, including the expanded Streams JSON of any group functions in the pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/expand").substitute(path_params)
        url = self.base_client.build_url(path)
        data = upl_pipeline.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplPipeline)

    def get_group(self, group_id: str, query_params: Dict[str, object] = None) -> GroupResponse:
        """
        Returns the full Streams JSON of a group.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "groupId": group_id,
        }

        path = Template("/streams/v2beta1/groups/${groupId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, GroupResponse)

    def get_input_schema(self, get_input_schema_request: GetInputSchemaRequest, query_params: Dict[str, object] = None) -> UplType:
        """
        Returns the input schema for a function in a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/input-schema").substitute(path_params)
        url = self.base_client.build_url(path)
        data = get_input_schema_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplType)

    def get_output_schema(self, get_output_schema_request: GetOutputSchemaRequest, query_params: Dict[str, object] = None) -> Dict[str, UplType]:
        """
        Returns the output schema for a specified function in a pipeline. If no function ID is  specified, the request returns the output schema for all functions in a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/output-schema").substitute(path_params)
        url = self.base_client.build_url(path)
        data = get_output_schema_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplType)

    def get_pipeline(self, id: str, version: str = None, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Returns an individual pipeline by version.
        """
        if query_params is None:
            query_params = {}
        if version is not None:
            query_params['version'] = version

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PipelineResponse)

    def get_pipeline_latest_metrics(self, id: str, query_params: Dict[str, object] = None) -> MetricsResponse:
        """
        Returns the latest metrics for a single pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}/metrics/latest").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, MetricsResponse)

    def get_pipelines_status(self, activated: bool = None, create_user_id: str = None, name: str = None, offset: int = None, page_size: int = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfPipelineJobStatus:
        """
        Returns the status of pipelines from the underlying streaming system.
        """
        if query_params is None:
            query_params = {}
        if activated is not None:
            query_params['activated'] = activated
        if create_user_id is not None:
            query_params['createUserId'] = create_user_id
        if name is not None:
            query_params['name'] = name
        if offset is not None:
            query_params['offset'] = offset
        if page_size is not None:
            query_params['pageSize'] = page_size
        if sort_dir is not None:
            query_params['sortDir'] = sort_dir
        if sort_field is not None:
            query_params['sortField'] = sort_field

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/status").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfPipelineJobStatus)

    def get_preview_data(self, preview_session_id: str, query_params: Dict[str, object] = None) -> PreviewData:
        """
        Returns the preview data for a session.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "previewSessionId": preview_session_id,
        }

        path = Template("/streams/v2beta1/preview-data/${previewSessionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PreviewData)

    def get_preview_session(self, preview_session_id: str, query_params: Dict[str, object] = None) -> PreviewState:
        """
        Returns information from a preview session.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "previewSessionId": preview_session_id,
        }

        path = Template("/streams/v2beta1/preview-session/${previewSessionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PreviewState)

    def get_preview_session_latest_metrics(self, preview_session_id: str, query_params: Dict[str, object] = None) -> MetricsResponse:
        """
        Returns the latest metrics for a preview session.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "previewSessionId": preview_session_id,
        }

        path = Template("/streams/v2beta1/preview-session/${previewSessionId}/metrics/latest").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, MetricsResponse)

    def get_registry(self, local: bool = None, query_params: Dict[str, object] = None) -> UplRegistry:
        """
        Returns all functions in JSON format.
        """
        if query_params is None:
            query_params = {}
        if local is not None:
            query_params['local'] = local

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/registry").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, UplRegistry)

    def get_template(self, template_id: str, version: int = None, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Returns an individual template by version.
        """
        if query_params is None:
            query_params = {}
        if version is not None:
            query_params['version'] = version

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v2beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TemplateResponse)

    def list_connections(self, connector_id: str = None, create_user_id: str = None, function_id: str = None, name: str = None, offset: int = None, page_size: int = None, show_secret_names: str = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfConnectionResponse:
        """
        Returns a list of connections (latest versions only) by tenant ID.
        """
        if query_params is None:
            query_params = {}
        if connector_id is not None:
            query_params['connectorId'] = connector_id
        if create_user_id is not None:
            query_params['createUserId'] = create_user_id
        if function_id is not None:
            query_params['functionId'] = function_id
        if name is not None:
            query_params['name'] = name
        if offset is not None:
            query_params['offset'] = offset
        if page_size is not None:
            query_params['pageSize'] = page_size
        if show_secret_names is not None:
            query_params['showSecretNames'] = show_secret_names
        if sort_dir is not None:
            query_params['sortDir'] = sort_dir
        if sort_field is not None:
            query_params['sortField'] = sort_field

        path_params = {
        }

        path = Template("/streams/v2beta1/connections").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfConnectionResponse)

    def list_connectors(self, query_params: Dict[str, object] = None) -> PaginatedResponseOfConnectorResponse:
        """
        Returns a list of the available connectors.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/connectors").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfConnectorResponse)

    def list_pipelines(self, activated: bool = None, create_user_id: str = None, include_data: bool = None, name: str = None, offset: int = None, page_size: int = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfPipelineResponse:
        """
        Returns all pipelines.
        """
        if query_params is None:
            query_params = {}
        if activated is not None:
            query_params['activated'] = activated
        if create_user_id is not None:
            query_params['createUserId'] = create_user_id
        if include_data is not None:
            query_params['includeData'] = include_data
        if name is not None:
            query_params['name'] = name
        if offset is not None:
            query_params['offset'] = offset
        if page_size is not None:
            query_params['pageSize'] = page_size
        if sort_dir is not None:
            query_params['sortDir'] = sort_dir
        if sort_field is not None:
            query_params['sortField'] = sort_field

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfPipelineResponse)

    def list_templates(self, offset: int = None, page_size: int = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfTemplateResponse:
        """
        Returns a list of all templates.
        """
        if query_params is None:
            query_params = {}
        if offset is not None:
            query_params['offset'] = offset
        if page_size is not None:
            query_params['pageSize'] = page_size
        if sort_dir is not None:
            query_params['sortDir'] = sort_dir
        if sort_field is not None:
            query_params['sortField'] = sort_field

        path_params = {
        }

        path = Template("/streams/v2beta1/templates").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfTemplateResponse)

    def merge_pipelines(self, pipelines_merge_request: PipelinesMergeRequest, query_params: Dict[str, object] = None) -> UplPipeline:
        """
        Combines two Streams JSON programs.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/merge").substitute(path_params)
        url = self.base_client.build_url(path)
        data = pipelines_merge_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplPipeline)

    def put_connection(self, connection_id: str, connection_put_request: ConnectionPutRequest, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Modifies an existing DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v2beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_put_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def put_group(self, group_id: str, group_put_request: GroupPutRequest, query_params: Dict[str, object] = None) -> GroupResponse:
        """
        Update a group function combining the Streams JSON of two or more functions.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "groupId": group_id,
        }

        path = Template("/streams/v2beta1/groups/${groupId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = group_put_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, GroupResponse)

    def put_template(self, template_id: str, template_put_request: TemplatePutRequest, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Updates an existing template.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v2beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = template_put_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, TemplateResponse)

    def reactivate_pipeline(self, id: str, query_params: Dict[str, object] = None) -> PipelineReactivateResponse:
        """
        Reactivate a pipeline
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}/reactivate").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.post(url, params=query_params)
        return handle_response(response, PipelineReactivateResponse)

    def start_preview(self, preview_session_start_request: PreviewSessionStartRequest, query_params: Dict[str, object] = None) -> PreviewStartResponse:
        """
        Creates a preview session for a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/preview-session").substitute(path_params)
        url = self.base_client.build_url(path)
        data = preview_session_start_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, PreviewStartResponse)

    def stop_preview(self, preview_session_id: str, query_params: Dict[str, object] = None) -> str:
        """
        Stops a preview session.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "previewSessionId": preview_session_id,
        }

        path = Template("/streams/v2beta1/preview-session/${previewSessionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, str)

    def update_connection(self, connection_id: str, connection_patch_request: ConnectionPatchRequest, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Partially modifies an existing DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v2beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def update_group(self, group_id: str, group_patch_request: GroupPatchRequest, query_params: Dict[str, object] = None) -> GroupResponse:
        """
        Modify a group function by combining the Streams JSON of two or more functions.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "groupId": group_id,
        }

        path = Template("/streams/v2beta1/groups/${groupId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = group_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, GroupResponse)

    def update_pipeline(self, id: str, pipeline_patch_request: PipelinePatchRequest, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Partially modifies an existing pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v2beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = pipeline_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, PipelineResponse)

    def update_template(self, template_id: str, template_patch_request: TemplatePatchRequest, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Partially modifies an existing template.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v2beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = template_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, TemplateResponse)

    def validate_pipeline(self, validate_request: ValidateRequest, query_params: Dict[str, object] = None) -> ValidateResponse:
        """
        Verifies whether the Streams JSON is valid.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v2beta1/pipelines/validate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = validate_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, ValidateResponse)


