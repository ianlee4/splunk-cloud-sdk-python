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
    SDC Service: Splunk Search service

    Use the Search service in Splunk Cloud Services to dispatch, review, and manage searches and search jobs. You can finalize or cancel jobs, retrieve search results, and request search-related configurations from the Metadata Catalog service in Splunk Cloud Services.

    OpenAPI spec version: v2beta1.1 (recommended default)
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.search.v2beta1.gen_models import DeleteSearchJob
from splunk_sdk.search.v2beta1.gen_models import FieldsSummary
from splunk_sdk.search.v2beta1.gen_models import ListPreviewResultsResponse
from splunk_sdk.search.v2beta1.gen_models import ListSearchResultsResponse
from splunk_sdk.search.v2beta1.gen_models import SearchJob
from splunk_sdk.search.v2beta1.gen_models import SearchStatus
from splunk_sdk.search.v2beta1.gen_models import TimeBucketsSummary
from splunk_sdk.search.v2beta1.gen_models import UpdateJob


class SplunkSearchService(BaseService):
    """
    Splunk Search service
    Version: v2beta1.1
    Use the Search service in Splunk Cloud Services to dispatch, review, and manage searches and search jobs. You can finalize or cancel jobs, retrieve search results, and request search-related configurations from the Metadata Catalog service in Splunk Cloud Services.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_job(self, search_job: SearchJob = None, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Creates a search job.
        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v2beta1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        data = search_job.to_dict()
        response = self.base_client.post(url, json=data, params=query_params)
        return handle_response(response, SearchJob)

    def delete_job(self, query_params: Dict[str, object] = None) -> DeleteSearchJob:
        """
        Creates a search job that deletes events from an index. The events are deleted from the index in the specified module, based on the search criteria as specified by the predicate.

        """
        if query_params is None:
            query_params = {}

        path_params = {
        }

        path = Template("/search/v2beta1/jobs/delete").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.post(url, params=query_params)
        return handle_response(response, DeleteSearchJob)

    def get_job(self, sid: str, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Return the search job with the specified search ID (SID).
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, SearchJob)

    def list_events_summary(self, sid: str, count: float = None, earliest: str = None, field: str = None, latest: str = None, offset: float = None, query_params: Dict[str, object] = None) -> ListSearchResultsResponse:
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

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/events-summary").substitute(path_params)
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

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/fields-summary").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, FieldsSummary)

    def list_jobs(self, count: float = None, filter: str = None, status: SearchStatus = None, query_params: Dict[str, object] = None) -> List[SearchJob]:
        """
        Return the matching list of search jobs.
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

        path = Template("/search/v2beta1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, SearchJob)

    def list_preview_results(self, sid: str, count: float = None, offset: float = None, query_params: Dict[str, object] = None) -> ListPreviewResultsResponse:
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

        path = Template("/search/v2beta1/jobs/${sid}/results-preview").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListPreviewResultsResponse)

    def list_results(self, sid: str, count: float = None, field: str = None, offset: float = None, query_params: Dict[str, object] = None) -> ListSearchResultsResponse:
        """
        Return the search results for the job with the specified search ID (SID).
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

        path = Template("/search/v2beta1/jobs/${sid}/results").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, ListSearchResultsResponse)

    def list_time_buckets(self, sid: str, query_params: Dict[str, object] = None) -> TimeBucketsSummary:
        """
        Return event distribution over time of the untransformed events read to-date, for search ID(SID) search.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/time-buckets").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, params=query_params)
        return handle_response(response, TimeBucketsSummary)

    def update_job(self, sid: str, update_job: UpdateJob = None, query_params: Dict[str, object] = None) -> SearchJob:
        """
        Update the search job with the specified search ID (SID) with an action.
        """
        if query_params is None:
            query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = update_job.to_dict()
        response = self.base_client.patch(url, json=data, params=query_params)
        return handle_response(response, SearchJob)


