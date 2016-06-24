# coding: utf-8

"""
    LiveAgent API


    OpenAPI spec version: 3.0.0
    Contact: support@qualityunit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class VariationUpgrade(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VariationUpgrade - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'variation': 'Variation',
            'addons': 'list[VariationAddon]',
            'metrics': 'list[BillingMetric]',
            'base_price': 'int'
        }

        self.attribute_map = {
            'variation': 'variation',
            'addons': 'addons',
            'metrics': 'metrics',
            'base_price': 'base_price'
        }

        self._variation = None
        self._addons = None
        self._metrics = None
        self._base_price = None

    @property
    def variation(self):
        """
        Gets the variation of this VariationUpgrade.


        :return: The variation of this VariationUpgrade.
        :rtype: Variation
        """
        return self._variation

    @variation.setter
    def variation(self, variation):
        """
        Sets the variation of this VariationUpgrade.


        :param variation: The variation of this VariationUpgrade.
        :type: Variation
        """
        
        self._variation = variation

    @property
    def addons(self):
        """
        Gets the addons of this VariationUpgrade.


        :return: The addons of this VariationUpgrade.
        :rtype: list[VariationAddon]
        """
        return self._addons

    @addons.setter
    def addons(self, addons):
        """
        Sets the addons of this VariationUpgrade.


        :param addons: The addons of this VariationUpgrade.
        :type: list[VariationAddon]
        """
        
        self._addons = addons

    @property
    def metrics(self):
        """
        Gets the metrics of this VariationUpgrade.


        :return: The metrics of this VariationUpgrade.
        :rtype: list[BillingMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this VariationUpgrade.


        :param metrics: The metrics of this VariationUpgrade.
        :type: list[BillingMetric]
        """
        
        self._metrics = metrics

    @property
    def base_price(self):
        """
        Gets the base_price of this VariationUpgrade.


        :return: The base_price of this VariationUpgrade.
        :rtype: int
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """
        Sets the base_price of this VariationUpgrade.


        :param base_price: The base_price of this VariationUpgrade.
        :type: int
        """
        
        self._base_price = base_price

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

