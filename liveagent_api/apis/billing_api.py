# coding: utf-8

"""
BillingApi.py
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


class BillingApi(object):
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

    def check_vat(self, vat_id, **kwargs):
        """
        Vat validity
        Vat validity check

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.check_vat(vat_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str vat_id:  (required)
        :return: OkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vat_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_vat" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vat_id' is set
        if ('vat_id' not in params) or (params['vat_id'] is None):
            raise ValueError("Missing the required parameter `vat_id` when calling `check_vat`")

        resource_path = '/billing/_check_vat'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'vat_id' in params:
            query_params['vatId'] = params['vat_id']

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
        auth_settings = []

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

    def get_coupon(self, coupon_code, **kwargs):
        """
        Coupon
        Get coupon

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_coupon(coupon_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str coupon_code:  (required)
        :return: Coupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_code']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_coupon" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'coupon_code' is set
        if ('coupon_code' not in params) or (params['coupon_code'] is None):
            raise ValueError("Missing the required parameter `coupon_code` when calling `get_coupon`")

        resource_path = '/coupons/{couponCode}'.replace('{format}', 'json')
        path_params = {}
        if 'coupon_code' in params:
            path_params['couponCode'] = params['coupon_code']

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
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Coupon',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
