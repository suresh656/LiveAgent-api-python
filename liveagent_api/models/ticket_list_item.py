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


class TicketListItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TicketListItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'useridentifier': 'str',
            'subject': 'str',
            'departmentid': 'str',
            'recipient': 'str',
            'message': 'str',
            'recipient_name': 'str',
            'carbon_copy': 'str',
            'status': 'str',
            'mail_message_id': 'str',
            'do_not_send_mail': 'str',
            'use_template': 'str',
            'is_html_message': 'str',
            'custom_fields': 'list[CustomFields]',
            'tags': 'list[str]',
            'attachments': 'str'
        }

        self.attribute_map = {
            'useridentifier': 'useridentifier',
            'subject': 'subject',
            'departmentid': 'departmentid',
            'recipient': 'recipient',
            'message': 'message',
            'recipient_name': 'recipient_name',
            'carbon_copy': 'carbon_copy',
            'status': 'status',
            'mail_message_id': 'mail_message_id',
            'do_not_send_mail': 'do_not_send_mail',
            'use_template': 'use_template',
            'is_html_message': 'is_html_message',
            'custom_fields': 'custom_fields',
            'tags': 'tags',
            'attachments': 'attachments'
        }

        self._useridentifier = None
        self._subject = None
        self._departmentid = None
        self._recipient = None
        self._message = None
        self._recipient_name = None
        self._carbon_copy = None
        self._status = 'N'
        self._mail_message_id = None
        self._do_not_send_mail = 'N'
        self._use_template = 'Y'
        self._is_html_message = 'N'
        self._custom_fields = None
        self._tags = None
        self._attachments = None

    @property
    def useridentifier(self):
        """
        Gets the useridentifier of this TicketListItem.


        :return: The useridentifier of this TicketListItem.
        :rtype: str
        """
        return self._useridentifier

    @useridentifier.setter
    def useridentifier(self, useridentifier):
        """
        Sets the useridentifier of this TicketListItem.


        :param useridentifier: The useridentifier of this TicketListItem.
        :type: str
        """
        self._useridentifier = useridentifier

    @property
    def subject(self):
        """
        Gets the subject of this TicketListItem.


        :return: The subject of this TicketListItem.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this TicketListItem.


        :param subject: The subject of this TicketListItem.
        :type: str
        """
        self._subject = subject

    @property
    def departmentid(self):
        """
        Gets the departmentid of this TicketListItem.


        :return: The departmentid of this TicketListItem.
        :rtype: str
        """
        return self._departmentid

    @departmentid.setter
    def departmentid(self, departmentid):
        """
        Sets the departmentid of this TicketListItem.


        :param departmentid: The departmentid of this TicketListItem.
        :type: str
        """
        self._departmentid = departmentid

    @property
    def recipient(self):
        """
        Gets the recipient of this TicketListItem.


        :return: The recipient of this TicketListItem.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this TicketListItem.


        :param recipient: The recipient of this TicketListItem.
        :type: str
        """
        self._recipient = recipient

    @property
    def message(self):
        """
        Gets the message of this TicketListItem.


        :return: The message of this TicketListItem.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TicketListItem.


        :param message: The message of this TicketListItem.
        :type: str
        """
        self._message = message

    @property
    def recipient_name(self):
        """
        Gets the recipient_name of this TicketListItem.


        :return: The recipient_name of this TicketListItem.
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """
        Sets the recipient_name of this TicketListItem.


        :param recipient_name: The recipient_name of this TicketListItem.
        :type: str
        """
        self._recipient_name = recipient_name

    @property
    def carbon_copy(self):
        """
        Gets the carbon_copy of this TicketListItem.


        :return: The carbon_copy of this TicketListItem.
        :rtype: str
        """
        return self._carbon_copy

    @carbon_copy.setter
    def carbon_copy(self, carbon_copy):
        """
        Sets the carbon_copy of this TicketListItem.


        :param carbon_copy: The carbon_copy of this TicketListItem.
        :type: str
        """
        self._carbon_copy = carbon_copy

    @property
    def status(self):
        """
        Gets the status of this TicketListItem.
        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed

        :return: The status of this TicketListItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TicketListItem.
        <br> I - init<br> N - new<br> T - chatting<br> P - calling<br> R - resolved<br> X - deleted<br> B - spam<br> A - answered<br> C - open<br> W - postponed

        :param status: The status of this TicketListItem.
        :type: str
        """
        allowed_values = ["I", "N", "T", "P", "R", "X", "B", "A", "C", "W"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def mail_message_id(self):
        """
        Gets the mail_message_id of this TicketListItem.


        :return: The mail_message_id of this TicketListItem.
        :rtype: str
        """
        return self._mail_message_id

    @mail_message_id.setter
    def mail_message_id(self, mail_message_id):
        """
        Sets the mail_message_id of this TicketListItem.


        :param mail_message_id: The mail_message_id of this TicketListItem.
        :type: str
        """
        self._mail_message_id = mail_message_id

    @property
    def do_not_send_mail(self):
        """
        Gets the do_not_send_mail of this TicketListItem.
        Y - yes, N - no

        :return: The do_not_send_mail of this TicketListItem.
        :rtype: str
        """
        return self._do_not_send_mail

    @do_not_send_mail.setter
    def do_not_send_mail(self, do_not_send_mail):
        """
        Sets the do_not_send_mail of this TicketListItem.
        Y - yes, N - no

        :param do_not_send_mail: The do_not_send_mail of this TicketListItem.
        :type: str
        """
        allowed_values = ["Y", "N"]
        if do_not_send_mail not in allowed_values:
            raise ValueError(
                "Invalid value for `do_not_send_mail`, must be one of {0}"
                .format(allowed_values)
            )
        self._do_not_send_mail = do_not_send_mail

    @property
    def use_template(self):
        """
        Gets the use_template of this TicketListItem.
        Y - yes, N - no

        :return: The use_template of this TicketListItem.
        :rtype: str
        """
        return self._use_template

    @use_template.setter
    def use_template(self, use_template):
        """
        Sets the use_template of this TicketListItem.
        Y - yes, N - no

        :param use_template: The use_template of this TicketListItem.
        :type: str
        """
        allowed_values = ["Y", "N"]
        if use_template not in allowed_values:
            raise ValueError(
                "Invalid value for `use_template`, must be one of {0}"
                .format(allowed_values)
            )
        self._use_template = use_template

    @property
    def is_html_message(self):
        """
        Gets the is_html_message of this TicketListItem.
        Y - yes, N - no

        :return: The is_html_message of this TicketListItem.
        :rtype: str
        """
        return self._is_html_message

    @is_html_message.setter
    def is_html_message(self, is_html_message):
        """
        Sets the is_html_message of this TicketListItem.
        Y - yes, N - no

        :param is_html_message: The is_html_message of this TicketListItem.
        :type: str
        """
        allowed_values = ["Y", "N"]
        if is_html_message not in allowed_values:
            raise ValueError(
                "Invalid value for `is_html_message`, must be one of {0}"
                .format(allowed_values)
            )
        self._is_html_message = is_html_message

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this TicketListItem.


        :return: The custom_fields of this TicketListItem.
        :rtype: list[CustomFields]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this TicketListItem.


        :param custom_fields: The custom_fields of this TicketListItem.
        :type: list[CustomFields]
        """
        self._custom_fields = custom_fields

    @property
    def tags(self):
        """
        Gets the tags of this TicketListItem.
        array of tags id

        :return: The tags of this TicketListItem.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TicketListItem.
        array of tags id

        :param tags: The tags of this TicketListItem.
        :type: list[str]
        """
        self._tags = tags

    @property
    def attachments(self):
        """
        Gets the attachments of this TicketListItem.


        :return: The attachments of this TicketListItem.
        :rtype: str
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this TicketListItem.


        :param attachments: The attachments of this TicketListItem.
        :type: str
        """
        self._attachments = attachments

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
