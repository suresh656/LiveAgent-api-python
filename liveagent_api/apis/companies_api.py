# coding: utf-8

"""
CompaniesApi.py
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


class CompaniesApi(object):
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

    def create_company(self, **kwargs):
        """
        Create new company
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_company(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Company company: 
        :return: list[Company]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_company" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/companies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'company' in params:
            body_params = params['company']

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
                                            response_type='list[Company]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_company(self, company_id, delete_tickets, **kwargs):
        """
        Delete company
        Deletes a company

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_company(company_id, delete_tickets, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str company_id:  (required)
        :param bool delete_tickets: <u>true</u>: Delete company from all lists and also delete all its tickets.<br> <u>false</u>: Delete company from all lists but leave its tickets intact. (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'delete_tickets']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_company" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'company_id' is set
        if ('company_id' not in params) or (params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `delete_company`")
        # verify the required parameter 'delete_tickets' is set
        if ('delete_tickets' not in params) or (params['delete_tickets'] is None):
            raise ValueError("Missing the required parameter `delete_tickets` when calling `delete_company`")

        resource_path = '/companies/{companyId}'.replace('{format}', 'json')
        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']

        query_params = {}
        if 'delete_tickets' in params:
            query_params['deleteTickets'] = params['delete_tickets']

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

        response = self.api_client.call_api(resource_path, 'DELETE',
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

    def get_companies_list(self, **kwargs):
        """
        Gets list of companies
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_companies_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page: Page to display. Not used if _from is defined.
        :param int per_page: Results per page. Used only if _page is used.
        :param int _from: Result set start. Takes precedence over _page.
        :param int to: Result set end. Used only if _from is used.
        :param str sort_dir: Sorting direction ASC or DESC
        :param str sort_field: Sorting field
        :param str filters: Filters (json object {column:value, ...})
        :return: list[CompanyListItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', '_from', 'to', 'sort_dir', 'sort_field', 'filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_companies_list" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/companies'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['_page'] = params['page']
        if 'per_page' in params:
            query_params['_perPage'] = params['per_page']
        if '_from' in params:
            query_params['_from'] = params['_from']
        if 'to' in params:
            query_params['_to'] = params['to']
        if 'sort_dir' in params:
            query_params['_sortDir'] = params['sort_dir']
        if 'sort_field' in params:
            query_params['_sortField'] = params['sort_field']
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
                                            response_type='list[CompanyListItem]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_specific_company(self, company_id, **kwargs):
        """
        Get company by specific id
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_specific_company(company_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str company_id:  (required)
        :return: list[Company]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_specific_company" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'company_id' is set
        if ('company_id' not in params) or (params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `get_specific_company`")

        resource_path = '/companies/{companyId}'.replace('{format}', 'json')
        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']

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
                                            response_type='list[Company]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_company(self, company_id, **kwargs):
        """
        Update company
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_company(company_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str company_id:  (required)
        :param Company company: 
        :return: list[Company]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'company']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_company" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'company_id' is set
        if ('company_id' not in params) or (params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `update_company`")

        resource_path = '/companies/{companyId}'.replace('{format}', 'json')
        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'company' in params:
            body_params = params['company']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Company]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
