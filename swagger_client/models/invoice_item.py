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


class InvoiceItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InvoiceItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'price': 'float',
            'description': 'str',
            'from_date': 'datetime',
            'to_date': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'price': 'price',
            'description': 'description',
            'from_date': 'from_date',
            'to_date': 'to_date'
        }

        self._type = None
        self._price = None
        self._description = None
        self._from_date = None
        self._to_date = None

    @property
    def type(self):
        """
        Gets the type of this InvoiceItem.


        :return: The type of this InvoiceItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InvoiceItem.


        :param type: The type of this InvoiceItem.
        :type: str
        """
        
        self._type = type

    @property
    def price(self):
        """
        Gets the price of this InvoiceItem.


        :return: The price of this InvoiceItem.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this InvoiceItem.


        :param price: The price of this InvoiceItem.
        :type: float
        """
        
        self._price = price

    @property
    def description(self):
        """
        Gets the description of this InvoiceItem.


        :return: The description of this InvoiceItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InvoiceItem.


        :param description: The description of this InvoiceItem.
        :type: str
        """
        
        self._description = description

    @property
    def from_date(self):
        """
        Gets the from_date of this InvoiceItem.


        :return: The from_date of this InvoiceItem.
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """
        Sets the from_date of this InvoiceItem.


        :param from_date: The from_date of this InvoiceItem.
        :type: datetime
        """
        
        self._from_date = from_date

    @property
    def to_date(self):
        """
        Gets the to_date of this InvoiceItem.


        :return: The to_date of this InvoiceItem.
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """
        Sets the to_date of this InvoiceItem.


        :param to_date: The to_date of this InvoiceItem.
        :type: datetime
        """
        
        self._to_date = to_date

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

