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


class IvrStep(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IvrStep - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'params': 'str',
            'choices': 'list[IvrChoice]'
        }

        self.attribute_map = {
            'type': 'type',
            'params': 'params',
            'choices': 'choices'
        }

        self._type = None
        self._params = None
        self._choices = None

    @property
    def type(self):
        """
        Gets the type of this IvrStep.
        P - play message (URL in params), R - ring to agent (optional departmentId in params), V - redirect to voicemail, D - choice (choices), G - goto (IVR name in params), T - transfer (optional ivr settings in choices {\"1\":\"online\",\"0\":\"offline\",\"9\":\"queue\"}), F - fetch next IVR steps from URL in params

        :return: The type of this IvrStep.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IvrStep.
        P - play message (URL in params), R - ring to agent (optional departmentId in params), V - redirect to voicemail, D - choice (choices), G - goto (IVR name in params), T - transfer (optional ivr settings in choices {\"1\":\"online\",\"0\":\"offline\",\"9\":\"queue\"}), F - fetch next IVR steps from URL in params

        :param type: The type of this IvrStep.
        :type: str
        """
        allowed_values = ["P", "R", "V", "D", "G", "T", "F"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def params(self):
        """
        Gets the params of this IvrStep.


        :return: The params of this IvrStep.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this IvrStep.


        :param params: The params of this IvrStep.
        :type: str
        """
        self._params = params

    @property
    def choices(self):
        """
        Gets the choices of this IvrStep.


        :return: The choices of this IvrStep.
        :rtype: list[IvrChoice]
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """
        Sets the choices of this IvrStep.


        :param choices: The choices of this IvrStep.
        :type: list[IvrChoice]
        """
        self._choices = choices

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

