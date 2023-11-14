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

from geoengine_openapi_client.models.default_colors_one_of import DefaultColorsOneOf  # noqa: E501

class TestDefaultColorsOneOf(unittest.TestCase):
    """DefaultColorsOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefaultColorsOneOf:
        """Test DefaultColorsOneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefaultColorsOneOf`
        """
        model = DefaultColorsOneOf()  # noqa: E501
        if include_optional:
            return DefaultColorsOneOf(
                default_color = [
                    56
                    ]
            )
        else:
            return DefaultColorsOneOf(
                default_color = [
                    56
                    ],
        )
        """

    def testDefaultColorsOneOf(self):
        """Test DefaultColorsOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
