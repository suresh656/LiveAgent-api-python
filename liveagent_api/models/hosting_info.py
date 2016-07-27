# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class HostingInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HostingInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_hosted': 'bool',
            'system': 'str'
        }

        self.attribute_map = {
            'is_hosted': 'is_hosted',
            'system': 'system'
        }

        self._is_hosted = None
        self._system = None

    @property
    def is_hosted(self):
        """
        Gets the is_hosted of this HostingInfo.


        :return: The is_hosted of this HostingInfo.
        :rtype: bool
        """
        return self._is_hosted

    @is_hosted.setter
    def is_hosted(self, is_hosted):
        """
        Sets the is_hosted of this HostingInfo.


        :param is_hosted: The is_hosted of this HostingInfo.
        :type: bool
        """
        self._is_hosted = is_hosted

    @property
    def system(self):
        """
        Gets the system of this HostingInfo.


        :return: The system of this HostingInfo.
        :rtype: str
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this HostingInfo.


        :param system: The system of this HostingInfo.
        :type: str
        """
        allowed_values = ["dp", "crm"]
        if system not in allowed_values:
            raise ValueError(
                "Invalid value for `system`, must be one of {0}"
                .format(allowed_values)
            )
        self._system = system

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
