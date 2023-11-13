# coding: utf-8

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from geoengine_sys.models.layer_listing import LayerListing  # noqa: E501

class TestLayerListing(unittest.TestCase):
    """LayerListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LayerListing:
        """Test LayerListing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LayerListing`
        """
        model = LayerListing()  # noqa: E501
        if include_optional:
            return LayerListing(
                description = '',
                id = geoengine_sys.models.provider_layer_id.ProviderLayerId(
                    layer_id = '', 
                    provider_id = '', ),
                name = '',
                properties = [
                    [
                        ''
                        ]
                    ]
            )
        else:
            return LayerListing(
                description = '',
                id = geoengine_sys.models.provider_layer_id.ProviderLayerId(
                    layer_id = '', 
                    provider_id = '', ),
                name = '',
        )
        """

    def testLayerListing(self):
        """Test LayerListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()