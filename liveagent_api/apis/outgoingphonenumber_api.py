# coding: utf-8

"""
OutgoingphonenumberApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class OutgoingphonenumberApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_outgoing_phone_number(self, phone_number, **kwargs):
        """
        Get outgoing phone number
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_outgoing_phone_number(phone_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number:  (required)
        :return: OutgoingPhoneNumber
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_outgoing_phone_number" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in params) or (params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `get_outgoing_phone_number`")

        resource_path = '/outgoing_phone_numbers/{phoneNumber}'.replace('{format}', 'json')
        path_params = {}
        if 'phone_number' in params:
            path_params['phoneNumber'] = params['phone_number']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OutgoingPhoneNumber',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_outgoing_phone_numbers_list(self, **kwargs):
        """
        Gets list of outgoing phone numbers
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_outgoing_phone_numbers_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str filters: Filters (json object {column:value, ...})
        :return: list[OutgoingPhoneNumber]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to', 'filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_outgoing_phone_numbers_list" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/outgoing_phone_numbers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if '_from' in params:
            query_params['_from'] = params['_from']
        if 'to' in params:
            query_params['_to'] = params['to']
        if 'filters' in params:
            query_params['_filters'] = params['filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['privileges', 'apikey']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[OutgoingPhoneNumber]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response