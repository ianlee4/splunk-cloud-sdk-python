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
    SDC Service: Splunk Search service

    Use the Search service in Splunk Cloud Services to dispatch, review, and manage searches and search jobs. You can finalize or cancel jobs, retrieve search results, and request search-related configurations from the Metadata Catalog service in Splunk Cloud Services.

    OpenAPI spec version: v3alpha1 
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.search.v3alpha1.gen_models import Dataset
from splunk_sdk.search.v3alpha1.gen_models import DatasetPATCH
from splunk_sdk.search.v3alpha1.gen_models import DatasetPOST
from splunk_sdk.search.v3alpha1.gen_models import DeleteSearchJob
from splunk_sdk.search.v3alpha1.gen_models import FederatedConnection
from splunk_sdk.search.v3alpha1.gen_models import FederatedConnectionInput
from splunk_sdk.search.v3alpha1.gen_models import FieldsSummary
from splunk_sdk.search.v3alpha1.gen_models import ListDatasets
from splunk_sdk.search.v3alpha1.gen_models import ListModules
from splunk_sdk.search.v3alpha1.gen_models import ListPreviewResultsResponse
from splunk_sdk.search.v3alpha1.gen_models import ListSearchResultsResponse
from splunk_sdk.search.v3alpha1.gen_models import Module
from splunk_sdk.search.v3alpha1.gen_models import SearchJob
from splunk_sdk.search.v3alpha1.gen_models import SearchModule
from splunk_sdk.search.v3alpha1.gen_models import SearchStatus
from splunk_sdk.search.v3alpha1.gen_models import TimeBucketsSummary
from splunk_sdk.search.v3alpha1.gen_models import UpdateJob


class SplunkSearchService(BaseService):
    """
    Splunk Search service
    Version: v3alpha1
    Use the Search service in Splunk Cloud Services to dispatch, review, and manage searches and search jobs. You can finalize or cancel jobs, retrieve search results, and request search-related configurations from the Metadata Catalog service in Splunk Cloud Services.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_dataset(self, dataset_post: DatasetPOST = None, query_params: Dict[str, object] = None) -> Dataset:
        """
        Creates a dataset.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/datasets").substitute(path_params)
        url = self.base_client.build_url(path)
        data = dataset_post.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, Dataset)

    def create_federated_connection(self, federated_connection_input: FederatedConnectionInput = None, query_params: Dict[str, object] = None) -> FederatedConnection:
        """
        Creates a new federated connection with information about how to connect to a remote index.

        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/connections").substitute(path_params)
        url = self.base_client.build_url(path)
        data = federated_connection_input.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, FederatedConnection)

    def create_job(self, search_job: SearchJob = None, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Creates a search job.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        data = search_job.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, SearchJob)

    def create_search_statements(self, search_module: SearchModule = None, query_params: Dict[str, object] = None) -> SearchModule:
        """
        Create a multi-statement module with inter-dependencies between statements.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/dispatch").substitute(path_params)
        url = self.base_client.build_url(path)
        data = search_module.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, SearchModule)

    def create_spl2_module(self, resource_name: str, module: Module = None, query_params: Dict[str, object] = None) -> Module:
        """
        Modifies/Creates a module with a specified resource name (resourceName).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "resourceName": resource_name,
        }

        path = Template("/search/v3alpha1/spl2-modules/${resourceName}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = module.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, Module)

    def delete_dataset_by_id(self, datasetid: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Deletes a dataset with a specified dataset ID (datasetid).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "datasetid": datasetid,
        }

        path = Template("/search/v3alpha1/datasets/${datasetid}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_federated_connection(self, connection_name: str, query_params: Dict[str, object] = None) -> SSCVoidModel:
        """
        Deletes a federated connection with the specified name (connectionName)

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionName": connection_name,
        }

        path = Template("/search/v3alpha1/connections/${connectionName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, )

    def delete_job(self, delete_search_job: DeleteSearchJob = None, query_params: Dict[str, object] = None) -> DeleteSearchJob:
        """
        Creates a search job that deletes events from an index. The events are deleted from the index in the specified module, based on the search criteria as specified by the predicate.

        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/jobs/delete").substitute(path_params)
        url = self.base_client.build_url(path)
        data = delete_search_job.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, DeleteSearchJob)

    def delete_spl2_module_by_resource_name(self, resource_name: str, query_params: Dict[str, object] = None) -> Module:
        """
        Deletes a module with a specified resource name (resourceName).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "resourceName": resource_name,
        }

        path = Template("/search/v3alpha1/spl2-modules/${resourceName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, params=query_params)
        return handle_response(response, Module)

    def export_results(self, sid: str, count: int = None, filename: str = None, output_mode: str = None, query_params: Dict[str, object] = None) -> object:
        """
        Export the search results for the job with the specified search ID (SID). Export the results as a csv file or json file.
        """
        if query_params is None:
            query_params = {}
        if count is not None:
            query_params['count'] = count
        if filename is not None:
            query_params['filename'] = filename
        if output_mode is not None:
            query_params['outputMode'] = output_mode

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/export").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, object)

    def get_dataset_by_id(self, datasetid: str, query_params: Dict[str, object] = None) -> Dataset:
        """
        Returns a dataset with a specified dataset ID (datasetid).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "datasetid": datasetid,
        }

        path = Template("/search/v3alpha1/datasets/${datasetid}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, Dataset)

    def get_federated_connection_by_name(self, connection_name: str, query_params: Dict[str, object] = None) -> FederatedConnection:
        """
        Returns the federated connection with the specified name (connectionName).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionName": connection_name,
        }

        path = Template("/search/v3alpha1/connections/${connectionName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, FederatedConnection)

    def get_job(self, sid: str, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Returns a search job with a specified search ID (sid).
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, SearchJob)

    def get_spl2_module_by_resource_name(self, resource_name: str, query_params: Dict[str, object] = None) -> Module:
        """
        Returns a module with a specified  resource name (resourceName).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "resourceName": resource_name,
        }

        path = Template("/search/v3alpha1/spl2-modules/${resourceName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, Module)

    def list_datasets(self, query_params: Dict[str, object] = None) -> ListDatasets:
        """
        Returns a list of all datasets.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/datasets").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListDatasets)

    def list_events_summary(self, sid: str, count: int = None, earliest: str = None, field: str = None, latest: str = None, offset: int = None, query_params: Dict[str, object] = None) -> ListSearchResultsResponse:
        """
        Return events summary, for search ID (SID) search.
        """
        if query_params is None:
            query_params = {}
        if count is not None:
            query_params['count'] = count
        if earliest is not None:
            query_params['earliest'] = earliest
        if field is not None:
            query_params['field'] = field
        if latest is not None:
            query_params['latest'] = latest
        if offset is not None:
            query_params['offset'] = offset

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}/timeline-metadata/auto/events-summary").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListSearchResultsResponse)

    def list_fields_summary(self, sid: str, earliest: str = None, latest: str = None, query_params: Dict[str, object] = None) -> FieldsSummary:
        """
        Return fields stats summary of the events to-date, for search ID (SID) search.
        """
        if query_params is None:
            query_params = {}
        if earliest is not None:
            query_params['earliest'] = earliest
        if latest is not None:
            query_params['latest'] = latest

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}/timeline-metadata/auto/fields-summary").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, FieldsSummary)

    def list_jobs(self, count: int = None, filter: str = None, status: SearchStatus = None, query_params: Dict[str, object] = None) -> List[SearchJob]:
        """
        Returns a matching list of search jobs.
        """
        if query_params is None:
            query_params = {}
        if count is not None:
            query_params['count'] = count
        if filter is not None:
            query_params['filter'] = filter
        if status is not None:
            query_params['status'] = status

        path_params = {
        }

        path = Template("/search/v3alpha1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, SearchJob)

    def list_preview_results(self, sid: str, count: int = None, offset: int = None, query_params: Dict[str, object] = None) -> ListPreviewResultsResponse:
        """
        Return the preview search results for the job with the specified search ID (SID). Can be used when a job is running to return interim results.
        """
        if query_params is None:
            query_params = {}
        if count is not None:
            query_params['count'] = count
        if offset is not None:
            query_params['offset'] = offset

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}/results-preview").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListPreviewResultsResponse)

    def list_results(self, sid: str, count: int = None, field: str = None, offset: int = None, query_params: Dict[str, object] = None) -> ListSearchResultsResponse:
        """
        Returns search results for a job with a specified search ID (sid).
        """
        if query_params is None:
            query_params = {}
        if count is not None:
            query_params['count'] = count
        if field is not None:
            query_params['field'] = field
        if offset is not None:
            query_params['offset'] = offset

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}/results").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListSearchResultsResponse)

    def list_spl2_modules(self, query_params: Dict[str, object] = None) -> ListModules:
        """
        gets a list of modules.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v3alpha1/spl2-modules").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListModules)

    def list_time_buckets(self, sid: str, query_params: Dict[str, object] = None) -> TimeBucketsSummary:
        """
        Returns an event distribution over time of the untransformed events that are read to-date for a job with a specified search ID (sid).
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}/timeline-metadata/auto/time-buckets").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TimeBucketsSummary)

    def put_federated_connection_by_name(self, connection_name: str, federated_connection_input: FederatedConnectionInput = None, query_params: Dict[str, object] = None) -> FederatedConnection:
        """
        Creates or updates a federated connection with a specified name (connectionName).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "connectionName": connection_name,
        }

        path = Template("/search/v3alpha1/connections/${connectionName}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = federated_connection_input.to_dict()
        response = self.base_client.put(url, json=data, params=query_params)
        return handle_response(response, FederatedConnection)

    def update_dataset_by_id(self, datasetid: str, dataset_patch: DatasetPATCH = None, query_params: Dict[str, object] = None) -> Dataset:
        """
        Modifies a dataset with a specified dataset ID (datasetid).

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "datasetid": datasetid,
        }

        path = Template("/search/v3alpha1/datasets/${datasetid}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = dataset_patch.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, Dataset)

    def update_job(self, sid: str, update_job: UpdateJob = None, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Modifies a search job with a specified search ID (sid) with an action.

        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v3alpha1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = update_job.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, SearchJob)


