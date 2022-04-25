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
    SDC Service: Splunk Forwarder Service

    Send data from a Splunk forwarder to the Splunk Forwarder service in Splunk Cloud Services.

    OpenAPI spec version: v2beta1.4 (recommended default)
    Generated by: https://openapi-generator.tech
"""


from datetime import datetime
from typing import List, Dict
from splunk_sdk.common.sscmodel import SSCModel
from splunk_sdk.base_client import dictify, inflate
from enum import Enum



class Certificate(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "Certificate":
        instance = Certificate.__new__(Certificate)
        instance._attrs = model
        return instance

    def __init__(self, pem: "str", **extra):
        """Certificate"""

        self._attrs = dict()
        if pem is not None:
            self._attrs["pem"] = pem
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def pem(self) -> "str":
        """ Gets the pem of this Certificate.
        """
        return self._attrs.get("pem")

    @pem.setter
    def pem(self, pem: "str"):
        """Sets the pem of this Certificate.


        :param pem: The pem of this Certificate.
        :type: str
        """
        if pem is None:
            raise ValueError("Invalid value for `pem`, must not be `None`")
        self._attrs["pem"] = pem

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


class CertificateInfo(SSCModel):

    @staticmethod
    def _from_dict(model: dict) -> "CertificateInfo":
        instance = CertificateInfo.__new__(CertificateInfo)
        instance._attrs = model
        return instance

    def __init__(self, content: "str" = None, hash: "str" = None, issuer: "str" = None, last_update: "datetime" = None, not_after: "datetime" = None, not_before: "datetime" = None, slot: "int" = None, subject: "str" = None, **extra):
        """CertificateInfo"""

        self._attrs = dict()
        if content is not None:
            self._attrs["content"] = content
        if hash is not None:
            self._attrs["hash"] = hash
        if issuer is not None:
            self._attrs["issuer"] = issuer
        if last_update is not None:
            self._attrs["lastUpdate"] = last_update
        if not_after is not None:
            self._attrs["notAfter"] = not_after
        if not_before is not None:
            self._attrs["notBefore"] = not_before
        if slot is not None:
            self._attrs["slot"] = slot
        if subject is not None:
            self._attrs["subject"] = subject
        for k, v in extra.items():
            self._attrs[k] = v

    @property
    def content(self) -> "str":
        """ Gets the content of this CertificateInfo.
        """
        return self._attrs.get("content")

    @content.setter
    def content(self, content: "str"):
        """Sets the content of this CertificateInfo.


        :param content: The content of this CertificateInfo.
        :type: str
        """
        self._attrs["content"] = content

    @property
    def hash(self) -> "str":
        """ Gets the hash of this CertificateInfo.
        """
        return self._attrs.get("hash")

    @hash.setter
    def hash(self, hash: "str"):
        """Sets the hash of this CertificateInfo.


        :param hash: The hash of this CertificateInfo.
        :type: str
        """
        self._attrs["hash"] = hash

    @property
    def issuer(self) -> "str":
        """ Gets the issuer of this CertificateInfo.
        """
        return self._attrs.get("issuer")

    @issuer.setter
    def issuer(self, issuer: "str"):
        """Sets the issuer of this CertificateInfo.


        :param issuer: The issuer of this CertificateInfo.
        :type: str
        """
        self._attrs["issuer"] = issuer

    @property
    def last_update(self) -> "datetime":
        """ Gets the last_update of this CertificateInfo.
        """
        return self._attrs.get("lastUpdate")

    @last_update.setter
    def last_update(self, last_update: "datetime"):
        """Sets the last_update of this CertificateInfo.


        :param last_update: The last_update of this CertificateInfo.
        :type: datetime
        """
        self._attrs["lastUpdate"] = last_update

    @property
    def not_after(self) -> "datetime":
        """ Gets the not_after of this CertificateInfo.
        """
        return self._attrs.get("notAfter")

    @not_after.setter
    def not_after(self, not_after: "datetime"):
        """Sets the not_after of this CertificateInfo.


        :param not_after: The not_after of this CertificateInfo.
        :type: datetime
        """
        self._attrs["notAfter"] = not_after

    @property
    def not_before(self) -> "datetime":
        """ Gets the not_before of this CertificateInfo.
        """
        return self._attrs.get("notBefore")

    @not_before.setter
    def not_before(self, not_before: "datetime"):
        """Sets the not_before of this CertificateInfo.


        :param not_before: The not_before of this CertificateInfo.
        :type: datetime
        """
        self._attrs["notBefore"] = not_before

    @property
    def slot(self) -> "int":
        """ Gets the slot of this CertificateInfo.
        """
        return self._attrs.get("slot")

    @slot.setter
    def slot(self, slot: "int"):
        """Sets the slot of this CertificateInfo.


        :param slot: The slot of this CertificateInfo.
        :type: int
        """
        self._attrs["slot"] = slot

    @property
    def subject(self) -> "str":
        """ Gets the subject of this CertificateInfo.
        """
        return self._attrs.get("subject")

    @subject.setter
    def subject(self, subject: "str"):
        """Sets the subject of this CertificateInfo.


        :param subject: The subject of this CertificateInfo.
        :type: str
        """
        self._attrs["subject"] = subject

    def to_dict(self):
        return {k: v for (k, v) in self._attrs.items() if v is not None}


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
