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
    SDC Service: Data Stream Processing REST API

    Use the Streams service to perform create, read, update, and delete (CRUD) operations on your data pipeline. The Streams service also has metrics and preview session endpoints and gives you full control over your data pipeline.

    OpenAPI spec version: v3beta1.1 (recommended default)
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.streams.v3beta1.gen_models import ActivatePipelineRequest
from splunk_sdk.streams.v3beta1.gen_models import ConnectionPatchRequest
from splunk_sdk.streams.v3beta1.gen_models import ConnectionPutRequest
from splunk_sdk.streams.v3beta1.gen_models import ConnectionRequest
from splunk_sdk.streams.v3beta1.gen_models import ConnectionSaveResponse
from splunk_sdk.streams.v3beta1.gen_models import DeactivatePipelineRequest
from splunk_sdk.streams.v3beta1.gen_models import DecompileRequest
from splunk_sdk.streams.v3beta1.gen_models import DecompileResponse
from splunk_sdk.streams.v3beta1.gen_models import ErrorResponse
from splunk_sdk.streams.v3beta1.gen_models import FilesMetaDataResponse
from splunk_sdk.streams.v3beta1.gen_models import GetInputSchemaRequest
from splunk_sdk.streams.v3beta1.gen_models import GetOutputSchemaRequest
from splunk_sdk.streams.v3beta1.gen_models import LookupTableResponse
from splunk_sdk.streams.v3beta1.gen_models import MetricsResponse
from splunk_sdk.streams.v3beta1.gen_models import PaginatedResponseOfConnectionResponse
from splunk_sdk.streams.v3beta1.gen_models import PaginatedResponseOfConnectorResponse
from splunk_sdk.streams.v3beta1.gen_models import PaginatedResponseOfPipelineJobStatus
from splunk_sdk.streams.v3beta1.gen_models import PaginatedResponseOfPipelineResponse
from splunk_sdk.streams.v3beta1.gen_models import PaginatedResponseOfTemplateResponse
from splunk_sdk.streams.v3beta1.gen_models import Pipeline
from splunk_sdk.streams.v3beta1.gen_models import PipelinePatchRequest
from splunk_sdk.streams.v3beta1.gen_models import PipelineReactivateResponse
from splunk_sdk.streams.v3beta1.gen_models import PipelineReactivateResponseAsync
from splunk_sdk.streams.v3beta1.gen_models import PipelineReactivationStatus
from splunk_sdk.streams.v3beta1.gen_models import PipelineRequest
from splunk_sdk.streams.v3beta1.gen_models import PipelineResponse
from splunk_sdk.streams.v3beta1.gen_models import PreviewData
from splunk_sdk.streams.v3beta1.gen_models import PreviewSessionStartRequest
from splunk_sdk.streams.v3beta1.gen_models import PreviewStartResponse
from splunk_sdk.streams.v3beta1.gen_models import PreviewState
from splunk_sdk.streams.v3beta1.gen_models import ReactivatePipelineRequest
from splunk_sdk.streams.v3beta1.gen_models import RegistryModel
from splunk_sdk.streams.v3beta1.gen_models import Response
from splunk_sdk.streams.v3beta1.gen_models import SplCompileRequest
from splunk_sdk.streams.v3beta1.gen_models import TemplatePatchRequest
from splunk_sdk.streams.v3beta1.gen_models import TemplatePutRequest
from splunk_sdk.streams.v3beta1.gen_models import TemplateRequest
from splunk_sdk.streams.v3beta1.gen_models import TemplateResponse
from splunk_sdk.streams.v3beta1.gen_models import UpgradePipelineRequest
from splunk_sdk.streams.v3beta1.gen_models import UplType
from splunk_sdk.streams.v3beta1.gen_models import UploadFileResponse
from splunk_sdk.streams.v3beta1.gen_models import ValidateConnectionRequest
from splunk_sdk.streams.v3beta1.gen_models import ValidateRequest
from splunk_sdk.streams.v3beta1.gen_models import ValidateResponse


class DataStreamProcessingRESTAPI(BaseService):
    """
    Data Stream Processing REST API
    Version: v3beta1.1
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

        path = Template("/streams/v3beta1/pipelines/${id}/activate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = activate_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Response)

    def compile(self, spl_compile_request: SplCompileRequest, query_params: Dict[str, object] = None) -> Pipeline:
        """
        Compiles SPL2 and returns streams JSON.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/compile").substitute(path_params)
        url = self.base_client.build_url(path)
        data = spl_compile_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Pipeline)

    def create_connection(self, connection_request: ConnectionRequest, skip_validation: bool = None, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Create a new DSP connection.
        """
        if query_params is None:
            query_params = {}
        if skip_validation is not None:
            query_params['skipValidation'] = skip_validation

        path_params = {
        }

        path = Template("/streams/v3beta1/connections").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def create_pipeline(self, pipeline_request: PipelineRequest, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Creates a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines").substitute(path_params)
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

        path = Template("/streams/v3beta1/templates").substitute(path_params)
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

        path = Template("/streams/v3beta1/pipelines/${id}/deactivate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = deactivate_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Response)

    def decompile(self, decompile_request: DecompileRequest, query_params: Dict[str, object] = None) -> DecompileResponse:
        """
        Decompiles UPL and returns SPL.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/decompile").substitute(path_params)
        url = self.base_client.build_url(path)
        data = decompile_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, DecompileResponse)

    def delete_connection(self, connection_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Delete all versions of a connection by its id.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v3beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_file(self, file_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Delete file.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "fileId": file_id,
        }

        path = Template("/streams/v3beta1/files/${fileId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_lookup_file(self, file_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Delete lookup file.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "fileId": file_id,
        }

        path = Template("/streams/v3beta1/lookups/files/${fileId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_pipeline(self, id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Removes a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_source(self, id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Delete a source.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/sources/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_template(self, template_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Removes a template with a specific ID.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v3beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def get_file_metadata(self, file_id: str, query_params: Dict[str, object] = None) -> UploadFileResponse:
        """
        Get file metadata.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "fileId": file_id,
        }

        path = Template("/streams/v3beta1/files/${fileId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, UploadFileResponse)

    def get_files_metadata(self, query_params: Dict[str, object] = None) -> FilesMetaDataResponse:
        """
        Returns files metadata.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/files").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, FilesMetaDataResponse)

    def get_input_schema(self, get_input_schema_request: GetInputSchemaRequest, query_params: Dict[str, object] = None) -> UplType:
        """
        Returns the input schema for a function in a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/input-schema").substitute(path_params)
        url = self.base_client.build_url(path)
        data = get_input_schema_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, UplType)

    def get_lookup_file_metadata(self, file_id: str, query_params: Dict[str, object] = None) -> UploadFileResponse:
        """
        Get lookup file metadata.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "fileId": file_id,
        }

        path = Template("/streams/v3beta1/lookups/files/${fileId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, UploadFileResponse)

    def get_lookup_files_metadata(self, query_params: Dict[str, object] = None) -> FilesMetaDataResponse:
        """
        Returns lookup files metadata.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/lookups/files").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, FilesMetaDataResponse)

    def get_lookup_table(self, connection_id: str, offset: int, size: int, query_params: Dict[str, object] = None) -> LookupTableResponse:
        """
        Returns lookup table results.
        """
        if query_params is None:
            query_params = {}
        if offset is not None:
            query_params['offset'] = offset
        if size is not None:
            query_params['size'] = size

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v3beta1/lookups/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, LookupTableResponse)

    def get_output_schema(self, get_output_schema_request: GetOutputSchemaRequest, query_params: Dict[str, object] = None) -> Dict[str, UplType]:
        """
        Returns the output schema for a specified function in a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/output-schema").substitute(path_params)
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

        path = Template("/streams/v3beta1/pipelines/${id}").substitute(path_params)
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

        path = Template("/streams/v3beta1/pipelines/${id}/metrics/latest").substitute(path_params)
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

        path = Template("/streams/v3beta1/pipelines/status").substitute(path_params)
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

        path = Template("/streams/v3beta1/preview-data/${previewSessionId}").substitute(path_params)
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

        path = Template("/streams/v3beta1/preview-session/${previewSessionId}").substitute(path_params)
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

        path = Template("/streams/v3beta1/preview-session/${previewSessionId}/metrics/latest").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, MetricsResponse)

    def get_registry(self, local: bool = None, query_params: Dict[str, object] = None) -> RegistryModel:
        """
        Returns all functions in JSON format.
        """
        if query_params is None:
            query_params = {}
        if local is not None:
            query_params['local'] = local

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/registry").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, RegistryModel)

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

        path = Template("/streams/v3beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TemplateResponse)

    def list_connections(self, connector_id: List[str] = None, create_user_id: str = None, function_id: str = None, function_op: str = None, name: str = None, offset: int = None, page_size: int = None, show_secret_names: str = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfConnectionResponse:
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
        if function_op is not None:
            query_params['functionOp'] = function_op
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

        path = Template("/streams/v3beta1/connections").substitute(path_params)
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

        path = Template("/streams/v3beta1/connectors").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfConnectorResponse)

    def list_pipelines(self, activated: bool = None, create_user_id: str = None, include_data: bool = None, include_status: bool = None, name: str = None, offset: int = None, page_size: int = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfPipelineResponse:
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
        if include_status is not None:
            query_params['includeStatus'] = include_status
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

        path = Template("/streams/v3beta1/pipelines").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfPipelineResponse)

    def list_templates(self, create_user_id: str = None, offset: int = None, page_size: int = None, sort_dir: str = None, sort_field: str = None, query_params: Dict[str, object] = None) -> PaginatedResponseOfTemplateResponse:
        """
        Returns a list of all templates.
        """
        if query_params is None:
            query_params = {}
        if create_user_id is not None:
            query_params['createUserId'] = create_user_id
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

        path = Template("/streams/v3beta1/templates").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PaginatedResponseOfTemplateResponse)

    def patch_pipeline(self, id: str, pipeline_patch_request: PipelinePatchRequest, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Patches an existing pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = pipeline_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, PipelineResponse)

    def put_connection(self, connection_id: str, connection_put_request: ConnectionPutRequest, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Updates an existing DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v3beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_put_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def put_template(self, template_id: str, template_put_request: TemplatePutRequest, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Updates an existing template.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v3beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = template_put_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, TemplateResponse)

    def reactivate_pipeline(self, id: str, reactivate_pipeline_request: ReactivatePipelineRequest = None, query_params: Dict[str, object] = None) -> PipelineReactivateResponse:
        """
        Reactivate a pipeline
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}/reactivate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = reactivate_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, PipelineReactivateResponse)

    def reactivation_status(self, id: str, upgrade_id: str, query_params: Dict[str, object] = None) -> PipelineReactivationStatus:
        """
        Get pipeline reactivation status
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
            "upgradeId": upgrade_id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}/upgrade/${upgradeId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, PipelineReactivationStatus)

    def start_preview(self, preview_session_start_request: PreviewSessionStartRequest, query_params: Dict[str, object] = None) -> PreviewStartResponse:
        """
        Creates a preview session for a pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/preview-session").substitute(path_params)
        url = self.base_client.build_url(path)
        data = preview_session_start_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, PreviewStartResponse)

    def stop_preview(self, preview_session_id: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Stops a preview session.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "previewSessionId": preview_session_id,
        }

        path = Template("/streams/v3beta1/preview-session/${previewSessionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def update_connection(self, connection_id: str, connection_patch_request: ConnectionPatchRequest, query_params: Dict[str, object] = None) -> ConnectionSaveResponse:
        """
        Patches an existing DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionId": connection_id,
        }

        path = Template("/streams/v3beta1/connections/${connectionId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = connection_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, ConnectionSaveResponse)

    def update_pipeline(self, id: str, pipeline_request: PipelineRequest, query_params: Dict[str, object] = None) -> PipelineResponse:
        """
        Updates an existing pipeline.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = pipeline_request.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, PipelineResponse)

    def update_template(self, template_id: str, template_patch_request: TemplatePatchRequest, query_params: Dict[str, object] = None) -> TemplateResponse:
        """
        Patches an existing template.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "templateId": template_id,
        }

        path = Template("/streams/v3beta1/templates/${templateId}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = template_patch_request.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, TemplateResponse)

    def upgrade_pipeline(self, id: str, upgrade_pipeline_request: UpgradePipelineRequest = None, query_params: Dict[str, object] = None) -> PipelineReactivateResponseAsync:
        """
        Upgrades a pipeline async
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "id": id,
        }

        path = Template("/streams/v3beta1/pipelines/${id}/upgrade").substitute(path_params)
        url = self.base_client.build_url(path)
        data = upgrade_pipeline_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, PipelineReactivateResponseAsync)

    def upload_file(self, filename: str = None) -> UploadFileResponse:
        """
        Upload new file.
        """
        path_params = {
        }

        path = Template("/streams/v3beta1/files").substitute(path_params)
        url = self.base_client.build_url(path)

        # handle file
        files = {'upfile': open(filename, 'rb')}
        response = self.base_client.post(url, files=files)
        return handle_response(response, UploadFileResponse)

    def upload_lookup_file(self, filename: str = None) -> UploadFileResponse:
        """
        Upload new lookup file.
        """
        path_params = {
        }

        path = Template("/streams/v3beta1/lookups/files").substitute(path_params)
        url = self.base_client.build_url(path)

        # handle file
        files = {'upfile': open(filename, 'rb')}
        response = self.base_client.post(url, files=files)
        return handle_response(response, UploadFileResponse)

    def validate_connection(self, validate_connection_request: ValidateConnectionRequest, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Validates the configuration of a DSP connection.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/connections/validate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = validate_connection_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, )

    def validate_pipeline(self, validate_request: ValidateRequest, query_params: Dict[str, object] = None) -> ValidateResponse:
        """
        Verifies whether the Streams JSON is valid.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/streams/v3beta1/pipelines/validate").substitute(path_params)
        url = self.base_client.build_url(path)
        data = validate_request.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, ValidateResponse)


