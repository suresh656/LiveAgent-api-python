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


class Call(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Call - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'ticket_id': 'str',
            'online_status': 'str',
            'online_settings': 'list[CallCommand]',
            'offline_settings': 'list[CallCommand]',
            'queue_settings': 'list[CallCommand]'
        }

        self.attribute_map = {
            'id': 'id',
            'ticket_id': 'ticket_id',
            'online_status': 'online_status',
            'online_settings': 'online_settings',
            'offline_settings': 'offline_settings',
            'queue_settings': 'queue_settings'
        }

        self._id = None
        self._ticket_id = None
        self._online_status = None
        self._online_settings = None
        self._offline_settings = None
        self._queue_settings = None

    @property
    def id(self):
        """
        Gets the id of this Call.


        :return: The id of this Call.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Call.


        :param id: The id of this Call.
        :type: str
        """
        self._id = id

    @property
    def ticket_id(self):
        """
        Gets the ticket_id of this Call.


        :return: The ticket_id of this Call.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """
        Sets the ticket_id of this Call.


        :param ticket_id: The ticket_id of this Call.
        :type: str
        """
        self._ticket_id = ticket_id

    @property
    def online_status(self):
        """
        Gets the online_status of this Call.
        O - online, F - offline

        :return: The online_status of this Call.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """
        Sets the online_status of this Call.
        O - online, F - offline

        :param online_status: The online_status of this Call.
        :type: str
        """
        allowed_values = ["O", "F"]
        if online_status not in allowed_values:
            raise ValueError(
                "Invalid value for `online_status`, must be one of {0}"
                .format(allowed_values)
            )
        self._online_status = online_status

    @property
    def online_settings(self):
        """
        Gets the online_settings of this Call.


        :return: The online_settings of this Call.
        :rtype: list[CallCommand]
        """
        return self._online_settings

    @online_settings.setter
    def online_settings(self, online_settings):
        """
        Sets the online_settings of this Call.


        :param online_settings: The online_settings of this Call.
        :type: list[CallCommand]
        """
        self._online_settings = online_settings

    @property
    def offline_settings(self):
        """
        Gets the offline_settings of this Call.


        :return: The offline_settings of this Call.
        :rtype: list[CallCommand]
        """
        return self._offline_settings

    @offline_settings.setter
    def offline_settings(self, offline_settings):
        """
        Sets the offline_settings of this Call.


        :param offline_settings: The offline_settings of this Call.
        :type: list[CallCommand]
        """
        self._offline_settings = offline_settings

    @property
    def queue_settings(self):
        """
        Gets the queue_settings of this Call.


        :return: The queue_settings of this Call.
        :rtype: list[CallCommand]
        """
        return self._queue_settings

    @queue_settings.setter
    def queue_settings(self, queue_settings):
        """
        Sets the queue_settings of this Call.


        :param queue_settings: The queue_settings of this Call.
        :type: list[CallCommand]
        """
        self._queue_settings = queue_settings

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

