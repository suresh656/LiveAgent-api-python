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


class BillingStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BillingStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'valid_to_date': 'datetime',
            'next_billing_date': 'datetime',
            'errors': 'int',
            'last_error_date': 'datetime',
            'payment_compatible': 'bool'
        }

        self.attribute_map = {
            'status': 'status',
            'valid_to_date': 'valid_to_date',
            'next_billing_date': 'next_billing_date',
            'errors': 'errors',
            'last_error_date': 'last_error_date',
            'payment_compatible': 'payment_compatible'
        }

        self._status = None
        self._valid_to_date = None
        self._next_billing_date = None
        self._errors = None
        self._last_error_date = None
        self._payment_compatible = None

    @property
    def status(self):
        """
        Gets the status of this BillingStatus.
        N - No billing\nA - Billing active\nS = Billing stopped\n

        :return: The status of this BillingStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BillingStatus.
        N - No billing\nA - Billing active\nS = Billing stopped\n

        :param status: The status of this BillingStatus.
        :type: str
        """
        allowed_values = ["N", "A", "S"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def valid_to_date(self):
        """
        Gets the valid_to_date of this BillingStatus.


        :return: The valid_to_date of this BillingStatus.
        :rtype: datetime
        """
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, valid_to_date):
        """
        Sets the valid_to_date of this BillingStatus.


        :param valid_to_date: The valid_to_date of this BillingStatus.
        :type: datetime
        """
        self._valid_to_date = valid_to_date

    @property
    def next_billing_date(self):
        """
        Gets the next_billing_date of this BillingStatus.


        :return: The next_billing_date of this BillingStatus.
        :rtype: datetime
        """
        return self._next_billing_date

    @next_billing_date.setter
    def next_billing_date(self, next_billing_date):
        """
        Sets the next_billing_date of this BillingStatus.


        :param next_billing_date: The next_billing_date of this BillingStatus.
        :type: datetime
        """
        self._next_billing_date = next_billing_date

    @property
    def errors(self):
        """
        Gets the errors of this BillingStatus.
        Number of charge errors since last successful billing or account unsuspend.

        :return: The errors of this BillingStatus.
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this BillingStatus.
        Number of charge errors since last successful billing or account unsuspend.

        :param errors: The errors of this BillingStatus.
        :type: int
        """
        self._errors = errors

    @property
    def last_error_date(self):
        """
        Gets the last_error_date of this BillingStatus.
        Time an date of the last failed charge attempt. Only present if number or errors is greater than 0.

        :return: The last_error_date of this BillingStatus.
        :rtype: datetime
        """
        return self._last_error_date

    @last_error_date.setter
    def last_error_date(self, last_error_date):
        """
        Sets the last_error_date of this BillingStatus.
        Time an date of the last failed charge attempt. Only present if number or errors is greater than 0.

        :param last_error_date: The last_error_date of this BillingStatus.
        :type: datetime
        """
        self._last_error_date = last_error_date

    @property
    def payment_compatible(self):
        """
        Gets the payment_compatible of this BillingStatus.
        True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set.

        :return: The payment_compatible of this BillingStatus.
        :rtype: bool
        """
        return self._payment_compatible

    @payment_compatible.setter
    def payment_compatible(self, payment_compatible):
        """
        Sets the payment_compatible of this BillingStatus.
        True if used payment method is fully compatible with selected country, false otherwise. False when either payment method or country is not set.

        :param payment_compatible: The payment_compatible of this BillingStatus.
        :type: bool
        """
        self._payment_compatible = payment_compatible

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

