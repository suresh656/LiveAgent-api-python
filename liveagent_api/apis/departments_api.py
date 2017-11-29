# coding: utf-8

"""
DepartmentsApi.py
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


class DepartmentsApi(object):
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

    def get_department_list(self, **kwargs):
        """
        Gets list of departments
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_department_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Department]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_department_list" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/departments'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='list[Department]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_specific_department(self, department_id, **kwargs):
        """
        Get department by specific id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_specific_department(department_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str department_id:  (required)
        :return: list[Department]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['department_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_specific_department" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'department_id' is set
        if ('department_id' not in params) or (params['department_id'] is None):
            raise ValueError("Missing the required parameter `department_id` when calling `get_specific_department`")

        resource_path = '/departments/{departmentId}'.replace('{format}', 'json')
        path_params = {}
        if 'department_id' in params:
            path_params['departmentId'] = params['department_id']

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
                                            response_type='list[Department]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def if_agent_is_in_department(self, department_id, agent_id, **kwargs):
        """
        Is agent is department
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.if_agent_is_in_department(department_id, agent_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str department_id:  (required)
        :param str agent_id:  (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['department_id', 'agent_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method if_agent_is_in_department" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'department_id' is set
        if ('department_id' not in params) or (params['department_id'] is None):
            raise ValueError("Missing the required parameter `department_id` when calling `if_agent_is_in_department`")
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params) or (params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `if_agent_is_in_department`")

        resource_path = '/departments/{departmentId}/{agentId}'.replace('{format}', 'json')
        path_params = {}
        if 'department_id' in params:
            path_params['departmentId'] = params['department_id']
        if 'agent_id' in params:
            path_params['agentId'] = params['agent_id']

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
                                            response_type='OkResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
