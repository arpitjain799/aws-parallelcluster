# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


import re

from pcluster.api import util
from pcluster.api.models.base_model_ import Model


class CreateClusterRequestContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cluster_name=None, cluster_configuration=None):
        """CreateClusterRequestContent - a model defined in OpenAPI

        :param cluster_name: The cluster_name of this CreateClusterRequestContent.  # noqa: E501
        :type cluster_name: str
        :param cluster_configuration: The cluster_configuration of this CreateClusterRequestContent.  # noqa: E501
        :type cluster_configuration: str
        """
        self.openapi_types = {"cluster_name": str, "cluster_configuration": str}

        self.attribute_map = {"cluster_name": "clusterName", "cluster_configuration": "clusterConfiguration"}

        self._cluster_name = cluster_name
        self._cluster_configuration = cluster_configuration

    @classmethod
    def from_dict(cls, dikt) -> "CreateClusterRequestContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClusterRequestContent of this CreateClusterRequestContent.
        :rtype: CreateClusterRequestContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateClusterRequestContent.

        Name of the cluster that will be created.  # noqa: E501

        :return: The name of this CreateClusterRequestContent.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateClusterRequestContent.

        Name of the cluster

        :param cluster_name: The name of this CreateClusterRequestContent.
        :type cluster_name: str
        """
        if cluster_name is None:
            raise ValueError("Invalid value for `cluster_name`, must not be `None`")
        if cluster_name is not None and not re.search(r"^[a-zA-Z][a-zA-Z0-9-]+$", cluster_name):
            raise ValueError(
                "Invalid value for `cluster_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-]+$/`"
            )

        self._cluster_name = cluster_name

    @property
    def cluster_configuration(self):
        """Gets the cluster_configuration of this CreateClusterRequestContent.

        Cluster configuration as a YAML document

        :return: The cluster_configuration of this CreateClusterRequestContent.
        :rtype: str
        """
        return self._cluster_configuration

    @cluster_configuration.setter
    def cluster_configuration(self, cluster_configuration):
        """Sets the cluster_configuration of this CreateClusterRequestContent.

        Cluster configuration as a YAML document

        :param cluster_configuration: The cluster_configuration of this CreateClusterRequestContent.
        :type cluster_configuration: str
        """
        if cluster_configuration is None:
            raise ValueError("Invalid value for `cluster_configuration`, must not be `None`")

        self._cluster_configuration = cluster_configuration