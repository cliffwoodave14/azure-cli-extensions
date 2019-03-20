# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ElasticPoolPerDatabaseMinPerformanceLevelCapability(Model):
    """The minimum per-database performance level capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar limit: The minimum performance level per database.
    :vartype limit: float
    :ivar unit: Unit type used to measure performance level. Possible values
     include: 'DTU', 'VCores'
    :vartype unit: str or ~azure.mgmt.sql.models.PerformanceLevelUnit
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'limit': {'readonly': True},
        'unit': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'float'},
        'unit': {'key': 'unit', 'type': 'str'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str=None, **kwargs) -> None:
        super(ElasticPoolPerDatabaseMinPerformanceLevelCapability, self).__init__(**kwargs)
        self.limit = None
        self.unit = None
        self.status = None
        self.reason = reason
