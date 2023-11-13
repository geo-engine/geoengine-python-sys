# coding: utf-8

# flake8: noqa
"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from geoengine_sys.models.aborted_task_status import AbortedTaskStatus
from geoengine_sys.models.add_collection200_response import AddCollection200Response
from geoengine_sys.models.add_dataset import AddDataset
from geoengine_sys.models.add_layer import AddLayer
from geoengine_sys.models.add_layer_collection import AddLayerCollection
from geoengine_sys.models.add_role import AddRole
from geoengine_sys.models.auto_create_dataset import AutoCreateDataset
from geoengine_sys.models.auto_ogr_source_time_format import AutoOgrSourceTimeFormat
from geoengine_sys.models.axis_order import AxisOrder
from geoengine_sys.models.bounding_box2_d import BoundingBox2D
from geoengine_sys.models.breakpoint import Breakpoint
from geoengine_sys.models.classification_measurement import ClassificationMeasurement
from geoengine_sys.models.classification_measurement_with_type import ClassificationMeasurementWithType
from geoengine_sys.models.collection_item import CollectionItem
from geoengine_sys.models.collection_type import CollectionType
from geoengine_sys.models.color_param import ColorParam
from geoengine_sys.models.colorizer import Colorizer
from geoengine_sys.models.completed_task_status import CompletedTaskStatus
from geoengine_sys.models.continuous_measurement import ContinuousMeasurement
from geoengine_sys.models.continuous_measurement_with_type import ContinuousMeasurementWithType
from geoengine_sys.models.coordinate2_d import Coordinate2D
from geoengine_sys.models.create_dataset import CreateDataset
from geoengine_sys.models.create_dataset_handler200_response import CreateDatasetHandler200Response
from geoengine_sys.models.create_project import CreateProject
from geoengine_sys.models.csv_header import CsvHeader
from geoengine_sys.models.custom_ogr_source_time_format import CustomOgrSourceTimeFormat
from geoengine_sys.models.data_id import DataId
from geoengine_sys.models.data_path import DataPath
from geoengine_sys.models.data_path_one_of import DataPathOneOf
from geoengine_sys.models.data_path_one_of1 import DataPathOneOf1
from geoengine_sys.models.dataset import Dataset
from geoengine_sys.models.dataset_definition import DatasetDefinition
from geoengine_sys.models.dataset_id_resource_id import DatasetIdResourceId
from geoengine_sys.models.dataset_listing import DatasetListing
from geoengine_sys.models.dataset_resource import DatasetResource
from geoengine_sys.models.date_time import DateTime
from geoengine_sys.models.date_time_parse_format import DateTimeParseFormat
from geoengine_sys.models.default_colors import DefaultColors
from geoengine_sys.models.default_colors_one_of import DefaultColorsOneOf
from geoengine_sys.models.derived_color import DerivedColor
from geoengine_sys.models.derived_color_with_type import DerivedColorWithType
from geoengine_sys.models.derived_number import DerivedNumber
from geoengine_sys.models.derived_number_with_type import DerivedNumberWithType
from geoengine_sys.models.describe_coverage_request import DescribeCoverageRequest
from geoengine_sys.models.error_response import ErrorResponse
from geoengine_sys.models.external_data_id import ExternalDataId
from geoengine_sys.models.external_data_id_with_type import ExternalDataIdWithType
from geoengine_sys.models.failed_task_status import FailedTaskStatus
from geoengine_sys.models.feature_data_type import FeatureDataType
from geoengine_sys.models.file_not_found_handling import FileNotFoundHandling
from geoengine_sys.models.format_specifics import FormatSpecifics
from geoengine_sys.models.format_specifics_one_of import FormatSpecificsOneOf
from geoengine_sys.models.format_specifics_one_of_csv import FormatSpecificsOneOfCsv
from geoengine_sys.models.gdal_dataset_geo_transform import GdalDatasetGeoTransform
from geoengine_sys.models.gdal_dataset_parameters import GdalDatasetParameters
from geoengine_sys.models.gdal_loading_info_temporal_slice import GdalLoadingInfoTemporalSlice
from geoengine_sys.models.gdal_meta_data_list import GdalMetaDataList
from geoengine_sys.models.gdal_meta_data_list_with_type import GdalMetaDataListWithType
from geoengine_sys.models.gdal_meta_data_regular import GdalMetaDataRegular
from geoengine_sys.models.gdal_meta_data_regular_with_type import GdalMetaDataRegularWithType
from geoengine_sys.models.gdal_meta_data_static import GdalMetaDataStatic
from geoengine_sys.models.gdal_meta_data_static_with_type import GdalMetaDataStaticWithType
from geoengine_sys.models.gdal_metadata_mapping import GdalMetadataMapping
from geoengine_sys.models.gdal_metadata_net_cdf_cf import GdalMetadataNetCdfCf
from geoengine_sys.models.gdal_metadata_net_cdf_cf_with_type import GdalMetadataNetCdfCfWithType
from geoengine_sys.models.gdal_source_time_placeholder import GdalSourceTimePlaceholder
from geoengine_sys.models.geo_json import GeoJson
from geoengine_sys.models.get_capabilities_format import GetCapabilitiesFormat
from geoengine_sys.models.get_capabilities_request import GetCapabilitiesRequest
from geoengine_sys.models.get_coverage_format import GetCoverageFormat
from geoengine_sys.models.get_coverage_request import GetCoverageRequest
from geoengine_sys.models.get_feature_request import GetFeatureRequest
from geoengine_sys.models.get_legend_graphic_request import GetLegendGraphicRequest
from geoengine_sys.models.get_map_exception_format import GetMapExceptionFormat
from geoengine_sys.models.get_map_format import GetMapFormat
from geoengine_sys.models.get_map_request import GetMapRequest
from geoengine_sys.models.infinite_ogr_source_duration_spec import InfiniteOgrSourceDurationSpec
from geoengine_sys.models.internal_data_id import InternalDataId
from geoengine_sys.models.layer import Layer
from geoengine_sys.models.layer_collection import LayerCollection
from geoengine_sys.models.layer_collection_listing import LayerCollectionListing
from geoengine_sys.models.layer_collection_listing_with_type import LayerCollectionListingWithType
from geoengine_sys.models.layer_collection_resource import LayerCollectionResource
from geoengine_sys.models.layer_collection_resource_id import LayerCollectionResourceId
from geoengine_sys.models.layer_listing import LayerListing
from geoengine_sys.models.layer_listing_with_type import LayerListingWithType
from geoengine_sys.models.layer_resource import LayerResource
from geoengine_sys.models.layer_resource_id import LayerResourceId
from geoengine_sys.models.layer_update import LayerUpdate
from geoengine_sys.models.layer_visibility import LayerVisibility
from geoengine_sys.models.line_symbology import LineSymbology
from geoengine_sys.models.line_symbology_with_type import LineSymbologyWithType
from geoengine_sys.models.linear_gradient import LinearGradient
from geoengine_sys.models.linear_gradient_with_type import LinearGradientWithType
from geoengine_sys.models.logarithmic_gradient import LogarithmicGradient
from geoengine_sys.models.logarithmic_gradient_with_type import LogarithmicGradientWithType
from geoengine_sys.models.measurement import Measurement
from geoengine_sys.models.meta_data_definition import MetaDataDefinition
from geoengine_sys.models.meta_data_suggestion import MetaDataSuggestion
from geoengine_sys.models.mock_dataset_data_source_loading_info import MockDatasetDataSourceLoadingInfo
from geoengine_sys.models.mock_meta_data import MockMetaData
from geoengine_sys.models.mock_meta_data_with_type import MockMetaDataWithType
from geoengine_sys.models.model_id_resource_id import ModelIdResourceId
from geoengine_sys.models.multi_line_string import MultiLineString
from geoengine_sys.models.multi_point import MultiPoint
from geoengine_sys.models.multi_polygon import MultiPolygon
from geoengine_sys.models.none_ogr_source_dataset_time_type import NoneOgrSourceDatasetTimeType
from geoengine_sys.models.number_param import NumberParam
from geoengine_sys.models.ogr_meta_data import OgrMetaData
from geoengine_sys.models.ogr_meta_data_with_type import OgrMetaDataWithType
from geoengine_sys.models.ogr_source_column_spec import OgrSourceColumnSpec
from geoengine_sys.models.ogr_source_dataset import OgrSourceDataset
from geoengine_sys.models.ogr_source_dataset_time_type import OgrSourceDatasetTimeType
from geoengine_sys.models.ogr_source_duration_spec import OgrSourceDurationSpec
from geoengine_sys.models.ogr_source_error_spec import OgrSourceErrorSpec
from geoengine_sys.models.ogr_source_time_format import OgrSourceTimeFormat
from geoengine_sys.models.order_by import OrderBy
from geoengine_sys.models.over_under_colors import OverUnderColors
from geoengine_sys.models.palette_colorizer import PaletteColorizer
from geoengine_sys.models.permission import Permission
from geoengine_sys.models.permission_request import PermissionRequest
from geoengine_sys.models.plot import Plot
from geoengine_sys.models.plot_output_format import PlotOutputFormat
from geoengine_sys.models.plot_query_rectangle import PlotQueryRectangle
from geoengine_sys.models.plot_result_descriptor import PlotResultDescriptor
from geoengine_sys.models.plot_result_descriptor_with_type import PlotResultDescriptorWithType
from geoengine_sys.models.plot_update import PlotUpdate
from geoengine_sys.models.point_symbology import PointSymbology
from geoengine_sys.models.point_symbology_with_type import PointSymbologyWithType
from geoengine_sys.models.polygon_symbology import PolygonSymbology
from geoengine_sys.models.polygon_symbology_with_type import PolygonSymbologyWithType
from geoengine_sys.models.project import Project
from geoengine_sys.models.project_layer import ProjectLayer
from geoengine_sys.models.project_listing import ProjectListing
from geoengine_sys.models.project_resource import ProjectResource
from geoengine_sys.models.project_resource_id import ProjectResourceId
from geoengine_sys.models.project_version import ProjectVersion
from geoengine_sys.models.provenance import Provenance
from geoengine_sys.models.provenance_entry import ProvenanceEntry
from geoengine_sys.models.provenance_output import ProvenanceOutput
from geoengine_sys.models.provider_layer_collection_id import ProviderLayerCollectionId
from geoengine_sys.models.provider_layer_id import ProviderLayerId
from geoengine_sys.models.quota import Quota
from geoengine_sys.models.raster_data_type import RasterDataType
from geoengine_sys.models.raster_dataset_from_workflow import RasterDatasetFromWorkflow
from geoengine_sys.models.raster_dataset_from_workflow_result import RasterDatasetFromWorkflowResult
from geoengine_sys.models.raster_properties_entry_type import RasterPropertiesEntryType
from geoengine_sys.models.raster_properties_key import RasterPropertiesKey
from geoengine_sys.models.raster_query_rectangle import RasterQueryRectangle
from geoengine_sys.models.raster_result_descriptor import RasterResultDescriptor
from geoengine_sys.models.raster_result_descriptor_with_type import RasterResultDescriptorWithType
from geoengine_sys.models.raster_stream_websocket_result_type import RasterStreamWebsocketResultType
from geoengine_sys.models.raster_symbology import RasterSymbology
from geoengine_sys.models.raster_symbology_with_type import RasterSymbologyWithType
from geoengine_sys.models.resource import Resource
from geoengine_sys.models.resource_id import ResourceId
from geoengine_sys.models.rgba_colorizer import RgbaColorizer
from geoengine_sys.models.role import Role
from geoengine_sys.models.role_description import RoleDescription
from geoengine_sys.models.running_task_status import RunningTaskStatus
from geoengine_sys.models.st_rectangle import STRectangle
from geoengine_sys.models.server_info import ServerInfo
from geoengine_sys.models.spatial_partition2_d import SpatialPartition2D
from geoengine_sys.models.spatial_reference_authority import SpatialReferenceAuthority
from geoengine_sys.models.spatial_reference_specification import SpatialReferenceSpecification
from geoengine_sys.models.spatial_resolution import SpatialResolution
from geoengine_sys.models.start_duration_ogr_source_dataset_time_type import StartDurationOgrSourceDatasetTimeType
from geoengine_sys.models.start_end_ogr_source_dataset_time_type import StartEndOgrSourceDatasetTimeType
from geoengine_sys.models.start_ogr_source_dataset_time_type import StartOgrSourceDatasetTimeType
from geoengine_sys.models.static_color_param import StaticColorParam
from geoengine_sys.models.static_number_param import StaticNumberParam
from geoengine_sys.models.stroke_param import StrokeParam
from geoengine_sys.models.symbology import Symbology
from geoengine_sys.models.task_abort_options import TaskAbortOptions
from geoengine_sys.models.task_filter import TaskFilter
from geoengine_sys.models.task_list_options import TaskListOptions
from geoengine_sys.models.task_response import TaskResponse
from geoengine_sys.models.task_status import TaskStatus
from geoengine_sys.models.task_status_with_id import TaskStatusWithId
from geoengine_sys.models.text_symbology import TextSymbology
from geoengine_sys.models.time_granularity import TimeGranularity
from geoengine_sys.models.time_interval import TimeInterval
from geoengine_sys.models.time_reference import TimeReference
from geoengine_sys.models.time_step import TimeStep
from geoengine_sys.models.time_step_with_type import TimeStepWithType
from geoengine_sys.models.typed_geometry import TypedGeometry
from geoengine_sys.models.typed_geometry_one_of import TypedGeometryOneOf
from geoengine_sys.models.typed_geometry_one_of1 import TypedGeometryOneOf1
from geoengine_sys.models.typed_geometry_one_of2 import TypedGeometryOneOf2
from geoengine_sys.models.typed_geometry_one_of3 import TypedGeometryOneOf3
from geoengine_sys.models.typed_operator import TypedOperator
from geoengine_sys.models.typed_operator_operator import TypedOperatorOperator
from geoengine_sys.models.typed_result_descriptor import TypedResultDescriptor
from geoengine_sys.models.unitless_measurement import UnitlessMeasurement
from geoengine_sys.models.unix_time_stamp_ogr_source_time_format import UnixTimeStampOgrSourceTimeFormat
from geoengine_sys.models.unix_time_stamp_type import UnixTimeStampType
from geoengine_sys.models.update_project import UpdateProject
from geoengine_sys.models.update_quota import UpdateQuota
from geoengine_sys.models.upload_file_layers_response import UploadFileLayersResponse
from geoengine_sys.models.upload_files_response import UploadFilesResponse
from geoengine_sys.models.user_credentials import UserCredentials
from geoengine_sys.models.user_info import UserInfo
from geoengine_sys.models.user_registration import UserRegistration
from geoengine_sys.models.user_session import UserSession
from geoengine_sys.models.vector_column_info import VectorColumnInfo
from geoengine_sys.models.vector_data_type import VectorDataType
from geoengine_sys.models.vector_query_rectangle import VectorQueryRectangle
from geoengine_sys.models.vector_result_descriptor import VectorResultDescriptor
from geoengine_sys.models.vector_result_descriptor_with_type import VectorResultDescriptorWithType
from geoengine_sys.models.volume import Volume
from geoengine_sys.models.wcs_boundingbox import WcsBoundingbox
from geoengine_sys.models.wcs_service import WcsService
from geoengine_sys.models.wcs_version import WcsVersion
from geoengine_sys.models.wfs_service import WfsService
from geoengine_sys.models.wfs_version import WfsVersion
from geoengine_sys.models.wms_service import WmsService
from geoengine_sys.models.wms_version import WmsVersion
from geoengine_sys.models.workflow import Workflow
from geoengine_sys.models.wrapped_plot_output import WrappedPlotOutput
from geoengine_sys.models.zero_ogr_source_duration_spec import ZeroOgrSourceDurationSpec