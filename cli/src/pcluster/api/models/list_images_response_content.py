# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


from typing import List

from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.image_info_summary import ImageInfoSummary


class ListImagesResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, images=None, next_token=None):
        """ListImagesResponseContent - a model defined in OpenAPI

        :param images: The images of this ListImagesResponseContent.
        :type images: List[ImageInfoSummary]
        :param next_token: The next_token of this ListImagesResponseContent.
        :type next_token: str
        """
        self.openapi_types = {"images": List[ImageInfoSummary], "next_token": str}

        self.attribute_map = {"images": "images", "next_token": "nextToken"}

        self._images = images
        self._next_token = next_token

    @classmethod
    def from_dict(cls, dikt) -> "ListImagesResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListImagesResponseContent of this ListImagesResponseContent.
        :rtype: ListImagesResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def images(self):
        """Gets the images of this ListImagesResponseContent.


        :return: The images of this ListImagesResponseContent.
        :rtype: List[ImageInfoSummary]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ListImagesResponseContent.


        :param images: The images of this ListImagesResponseContent.
        :type images: List[ImageInfoSummary]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")

        self._images = images

    @property
    def next_token(self):
        """Gets the next_token of this ListImagesResponseContent.

        Token to use for paginated requests.

        :return: The next_token of this ListImagesResponseContent.
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListImagesResponseContent.

        Token to use for paginated requests.

        :param next_token: The next_token of this ListImagesResponseContent.
        :type next_token: str
        """

        self._next_token = next_token