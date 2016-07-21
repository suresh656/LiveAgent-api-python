# coding: utf-8

"""
CallsApi.py
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


class CallsApi(object):
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

    def call_add_message(self, call_id, **kwargs):
        """
        Adds a message to the call
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_add_message(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :param CallMessage body: 
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_add_message" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_add_message`")

        resource_path = '/calls/{callId}/messages'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_answer(self, call_id, to_number, **kwargs):
        """
        Set call as answered by agent
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_answer(call_id, to_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :param str to_number: callee number (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id', 'to_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_answer" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_answer`")
        # verify the required parameter 'to_number' is set
        if ('to_number' not in params) or (params['to_number'] is None):
            raise ValueError("Missing the required parameter `to_number` when calling `call_answer`")

        resource_path = '/calls/{callId}/_answer'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

        query_params = {}
        if 'to_number' in params:
            query_params['to_number'] = params['to_number']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_create(self, call_id, to_number, from_number, **kwargs):
        """
        Create new call
        Creates new call (ingoing / outcoming)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_create(call_id, to_number, from_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :param str to_number: callee number (required)
        :param str from_number: caller number (required)
        :param str ticket_id: ticket id or code
        :param str direction: incoming call ('in' - default) or outgoing call ('out')
        :return: Call
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id', 'to_number', 'from_number', 'ticket_id', 'direction']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_create" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_create`")
        # verify the required parameter 'to_number' is set
        if ('to_number' not in params) or (params['to_number'] is None):
            raise ValueError("Missing the required parameter `to_number` when calling `call_create`")
        # verify the required parameter 'from_number' is set
        if ('from_number' not in params) or (params['from_number'] is None):
            raise ValueError("Missing the required parameter `from_number` when calling `call_create`")

        resource_path = '/calls/{callId}'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

        query_params = {}
        if 'to_number' in params:
            query_params['to_number'] = params['to_number']
        if 'from_number' in params:
            query_params['from_number'] = params['from_number']
        if 'ticket_id' in params:
            query_params['ticketId'] = params['ticket_id']
        if 'direction' in params:
            query_params['direction'] = params['direction']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Call',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_get_status(self, call_id, **kwargs):
        """
        Return the status of call
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_get_status(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :return: CallStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_get_status" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_get_status`")

        resource_path = '/calls/{callId}/status'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

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
                                            response_type='CallStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_reroute(self, call_id, **kwargs):
        """
        Let the call ring to another agent
        Lets the call ring to an another agent if available

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_reroute(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :return: CallStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_reroute" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_reroute`")

        resource_path = '/calls/{callId}/_reroute'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CallStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_ring(self, call_id, **kwargs):
        """
        Let the call ring
        Lets the call ring to an agent or adds it to queue if all agents are busy

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_ring(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :return: CallStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_ring" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_ring`")

        resource_path = '/calls/{callId}/_ring'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CallStatus',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def call_stop(self, call_id, **kwargs):
        """
        Stops the call
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.call_stop(call_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str call_id:  (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['call_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method call_stop" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'call_id' is set
        if ('call_id' not in params) or (params['call_id'] is None):
            raise ValueError("Missing the required parameter `call_id` when calling `call_stop`")

        resource_path = '/calls/{callId}/_stop'.replace('{format}', 'json')
        path_params = {}
        if 'call_id' in params:
            path_params['callId'] = params['call_id']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
