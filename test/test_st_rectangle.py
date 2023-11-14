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

from geoengine_openapi_client.models.st_rectangle import STRectangle  # noqa: E501

class TestSTRectangle(unittest.TestCase):
    """STRectangle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> STRectangle:
        """Test STRectangle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `STRectangle`
        """
        model = STRectangle()  # noqa: E501
        if include_optional:
            return STRectangle(
                bounding_box = geoengine_openapi_client.models.bounding_box2_d.BoundingBox2D(
                    lower_left_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), 
                    upper_right_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), ),
                spatial_reference = '',
                time_interval = geoengine_openapi_client.models.time_interval.TimeInterval(
                    end = 56, 
                    start = 56, )
            )
        else:
            return STRectangle(
                bounding_box = geoengine_openapi_client.models.bounding_box2_d.BoundingBox2D(
                    lower_left_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), 
                    upper_right_coordinate = geoengine_openapi_client.models.coordinate2_d.Coordinate2D(
                        x = 1.337, 
                        y = 1.337, ), ),
                spatial_reference = '',
                time_interval = geoengine_openapi_client.models.time_interval.TimeInterval(
                    end = 56, 
                    start = 56, ),
        )
        """

    def testSTRectangle(self):
        """Test STRectangle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
