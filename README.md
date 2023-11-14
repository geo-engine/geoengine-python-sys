# geoengine-openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.7.0
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import geoengine_openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import geoengine_openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import geoengine_openapi_client
from geoengine_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = geoengine_openapi_client.Configuration(
    host = "http://0.0.0.0:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (UUID): session_token
configuration = geoengine_openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with geoengine_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geoengine_openapi_client.DatasetsApi(api_client)
    auto_create_dataset = geoengine_openapi_client.AutoCreateDataset() # AutoCreateDataset | 

    try:
        # Creates a new dataset using previously uploaded files.
        api_response = api_instance.auto_create_dataset_handler(auto_create_dataset)
        print("The response of DatasetsApi->auto_create_dataset_handler:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetsApi->auto_create_dataset_handler: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8080/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatasetsApi* | [**auto_create_dataset_handler**](docs/DatasetsApi.md#auto_create_dataset_handler) | **POST** /dataset/auto | Creates a new dataset using previously uploaded files.
*DatasetsApi* | [**create_dataset_handler**](docs/DatasetsApi.md#create_dataset_handler) | **POST** /dataset | Creates a new dataset referencing files. Users can reference previously uploaded files. Admins can reference files from a volume.
*DatasetsApi* | [**delete_dataset_handler**](docs/DatasetsApi.md#delete_dataset_handler) | **DELETE** /dataset/{dataset} | Delete a dataset
*DatasetsApi* | [**get_dataset_handler**](docs/DatasetsApi.md#get_dataset_handler) | **GET** /dataset/{dataset} | Retrieves details about a dataset using the internal name.
*DatasetsApi* | [**list_datasets_handler**](docs/DatasetsApi.md#list_datasets_handler) | **GET** /datasets | Lists available datasets.
*DatasetsApi* | [**list_volumes_handler**](docs/DatasetsApi.md#list_volumes_handler) | **GET** /dataset/volumes | Lists available volumes.
*DatasetsApi* | [**suggest_meta_data_handler**](docs/DatasetsApi.md#suggest_meta_data_handler) | **GET** /dataset/suggest | Inspects an upload and suggests metadata that can be used when creating a new dataset based on it.
*GeneralApi* | [**available_handler**](docs/GeneralApi.md#available_handler) | **GET** /available | Server availablity check.
*GeneralApi* | [**server_info_handler**](docs/GeneralApi.md#server_info_handler) | **GET** /info | Shows information about the server software version.
*LayersApi* | [**add_collection**](docs/LayersApi.md#add_collection) | **POST** /layerDb/collections/{collection}/collections | Add a new collection to an existing collection
*LayersApi* | [**add_existing_collection_to_collection**](docs/LayersApi.md#add_existing_collection_to_collection) | **POST** /layerDb/collections/{parent}/collections/{collection} | Add an existing collection to a collection
*LayersApi* | [**add_existing_layer_to_collection**](docs/LayersApi.md#add_existing_layer_to_collection) | **POST** /layerDb/collections/{collection}/layers/{layer} | Add an existing layer to a collection
*LayersApi* | [**add_layer**](docs/LayersApi.md#add_layer) | **POST** /layerDb/collections/{collection}/layers | Add a new layer to a collection
*LayersApi* | [**layer_handler**](docs/LayersApi.md#layer_handler) | **GET** /layers/{provider}/{layer} | Retrieves the layer of the given provider
*LayersApi* | [**layer_to_dataset**](docs/LayersApi.md#layer_to_dataset) | **POST** /layers/{provider}/{layer}/dataset | Persist a raster layer from a provider as a dataset.
*LayersApi* | [**layer_to_workflow_id_handler**](docs/LayersApi.md#layer_to_workflow_id_handler) | **POST** /layers/{provider}/{layer}/workflowId | Registers a layer from a provider as a workflow and returns the workflow id
*LayersApi* | [**list_collection_handler**](docs/LayersApi.md#list_collection_handler) | **GET** /layers/collections/{provider}/{collection} | List the contents of the collection of the given provider
*LayersApi* | [**list_root_collections_handler**](docs/LayersApi.md#list_root_collections_handler) | **GET** /layers/collections | List all layer collections
*LayersApi* | [**remove_collection**](docs/LayersApi.md#remove_collection) | **DELETE** /layerDb/collections/{collection} | Remove a collection
*LayersApi* | [**remove_collection_from_collection**](docs/LayersApi.md#remove_collection_from_collection) | **DELETE** /layerDb/collections/{parent}/collections/{collection} | Delete a collection from a collection
*LayersApi* | [**remove_layer_from_collection**](docs/LayersApi.md#remove_layer_from_collection) | **DELETE** /layerDb/collections/{collection}/layers/{layer} | Remove a layer from a collection
*OGCWCSApi* | [**wcs_capabilities_handler**](docs/OGCWCSApi.md#wcs_capabilities_handler) | **GET** /wcs/{workflow}?request&#x3D;GetCapabilities | Get WCS Capabilities
*OGCWCSApi* | [**wcs_describe_coverage_handler**](docs/OGCWCSApi.md#wcs_describe_coverage_handler) | **GET** /wcs/{workflow}?request&#x3D;DescribeCoverage | Get WCS Coverage Description
*OGCWCSApi* | [**wcs_get_coverage_handler**](docs/OGCWCSApi.md#wcs_get_coverage_handler) | **GET** /wcs/{workflow}?request&#x3D;GetCoverage | Get WCS Coverage
*OGCWFSApi* | [**wfs_capabilities_handler**](docs/OGCWFSApi.md#wfs_capabilities_handler) | **GET** /wfs/{workflow}?request&#x3D;GetCapabilities | Get WFS Capabilities
*OGCWFSApi* | [**wfs_feature_handler**](docs/OGCWFSApi.md#wfs_feature_handler) | **GET** /wfs/{workflow}?request&#x3D;GetFeature | Get WCS Features
*OGCWMSApi* | [**wms_capabilities_handler**](docs/OGCWMSApi.md#wms_capabilities_handler) | **GET** /wms/{workflow}?request&#x3D;GetCapabilities | Get WMS Capabilities
*OGCWMSApi* | [**wms_legend_graphic_handler**](docs/OGCWMSApi.md#wms_legend_graphic_handler) | **GET** /wms/{workflow}?request&#x3D;GetLegendGraphic | Get WMS Legend Graphic
*OGCWMSApi* | [**wms_map_handler**](docs/OGCWMSApi.md#wms_map_handler) | **GET** /wms/{workflow}?request&#x3D;GetMap | Get WMS Map
*PermissionsApi* | [**add_permission_handler**](docs/PermissionsApi.md#add_permission_handler) | **PUT** /permissions | Adds a new permission.
*PermissionsApi* | [**remove_permission_handler**](docs/PermissionsApi.md#remove_permission_handler) | **DELETE** /permissions | Removes an existing permission.
*ProjectsApi* | [**create_project_handler**](docs/ProjectsApi.md#create_project_handler) | **POST** /project | Create a new project for the user.
*ProjectsApi* | [**delete_project_handler**](docs/ProjectsApi.md#delete_project_handler) | **DELETE** /project/{project} | Deletes a project.
*ProjectsApi* | [**list_projects_handler**](docs/ProjectsApi.md#list_projects_handler) | **GET** /projects | List all projects accessible to the user that match the selected criteria.
*ProjectsApi* | [**load_project_latest_handler**](docs/ProjectsApi.md#load_project_latest_handler) | **GET** /project/{project} | Retrieves details about the latest version of a project.
*ProjectsApi* | [**load_project_version_handler**](docs/ProjectsApi.md#load_project_version_handler) | **GET** /project/{project}/{version} | Retrieves details about the given version of a project.
*ProjectsApi* | [**project_versions_handler**](docs/ProjectsApi.md#project_versions_handler) | **GET** /project/{project}/versions | Lists all available versions of a project.
*ProjectsApi* | [**update_project_handler**](docs/ProjectsApi.md#update_project_handler) | **PATCH** /project/{project} | Updates a project.
*SessionApi* | [**anonymous_handler**](docs/SessionApi.md#anonymous_handler) | **POST** /anonymous | Creates session for anonymous user. The session&#39;s id serves as a Bearer token for requests.
*SessionApi* | [**login_handler**](docs/SessionApi.md#login_handler) | **POST** /login | Creates a session by providing user credentials. The session&#39;s id serves as a Bearer token for requests.
*SessionApi* | [**logout_handler**](docs/SessionApi.md#logout_handler) | **POST** /logout | Ends a session.
*SessionApi* | [**register_user_handler**](docs/SessionApi.md#register_user_handler) | **POST** /user | Registers a user.
*SessionApi* | [**session_handler**](docs/SessionApi.md#session_handler) | **GET** /session | Retrieves details about the current session.
*SpatialReferencesApi* | [**get_spatial_reference_specification_handler**](docs/SpatialReferencesApi.md#get_spatial_reference_specification_handler) | **GET** /spatialReferenceSpecification/{srsString} | 
*TasksApi* | [**abort_handler**](docs/TasksApi.md#abort_handler) | **DELETE** /tasks/{id} | Abort a running task.
*TasksApi* | [**list_handler**](docs/TasksApi.md#list_handler) | **GET** /tasks/list | Retrieve the status of all tasks.
*TasksApi* | [**status_handler**](docs/TasksApi.md#status_handler) | **GET** /tasks/{id}/status | Retrieve the status of a task.
*UploadsApi* | [**list_upload_file_layers_handler**](docs/UploadsApi.md#list_upload_file_layers_handler) | **GET** /uploads/{upload_id}/files/{file_name}/layers | List the layers of on uploaded file.
*UploadsApi* | [**list_upload_files_handler**](docs/UploadsApi.md#list_upload_files_handler) | **GET** /uploads/{upload_id}/files | List the files of on upload.
*UploadsApi* | [**upload_handler**](docs/UploadsApi.md#upload_handler) | **POST** /upload | Uploads files.
*UserApi* | [**add_role_handler**](docs/UserApi.md#add_role_handler) | **PUT** /roles | Add a new role. Requires admin privilige.
*UserApi* | [**assign_role_handler**](docs/UserApi.md#assign_role_handler) | **POST** /users/{user}/roles/{role} | Assign a role to a user. Requires admin privilige.
*UserApi* | [**get_role_descriptions**](docs/UserApi.md#get_role_descriptions) | **GET** /user/roles/descriptions | Query roles for the current user.
*UserApi* | [**get_user_quota_handler**](docs/UserApi.md#get_user_quota_handler) | **GET** /quotas/{user} | Retrieves the available and used quota of a specific user.
*UserApi* | [**quota_handler**](docs/UserApi.md#quota_handler) | **GET** /quota | Retrieves the available and used quota of the current user.
*UserApi* | [**remove_role_handler**](docs/UserApi.md#remove_role_handler) | **DELETE** /roles/{role} | Remove a role. Requires admin privilige.
*UserApi* | [**revoke_role_handler**](docs/UserApi.md#revoke_role_handler) | **DELETE** /users/{user}/roles/{role} | Revoke a role from a user. Requires admin privilige.
*UserApi* | [**update_user_quota_handler**](docs/UserApi.md#update_user_quota_handler) | **POST** /quotas/{user} | Update the available quota of a specific user.
*WorkflowsApi* | [**dataset_from_workflow_handler**](docs/WorkflowsApi.md#dataset_from_workflow_handler) | **POST** /datasetFromWorkflow/{id} | Create a task for creating a new dataset from the result of the workflow given by its &#x60;id&#x60; and the dataset parameters in the request body.
*WorkflowsApi* | [**get_workflow_all_metadata_zip_handler**](docs/WorkflowsApi.md#get_workflow_all_metadata_zip_handler) | **GET** /workflow/{id}/allMetadata/zip | Gets a ZIP archive of the worklow, its provenance and the output metadata.
*WorkflowsApi* | [**get_workflow_metadata_handler**](docs/WorkflowsApi.md#get_workflow_metadata_handler) | **GET** /workflow/{id}/metadata | Gets the metadata of a workflow
*WorkflowsApi* | [**get_workflow_provenance_handler**](docs/WorkflowsApi.md#get_workflow_provenance_handler) | **GET** /workflow/{id}/provenance | Gets the provenance of all datasets used in a workflow.
*WorkflowsApi* | [**load_workflow_handler**](docs/WorkflowsApi.md#load_workflow_handler) | **GET** /workflow/{id} | Retrieves an existing Workflow.
*WorkflowsApi* | [**raster_stream_websocket**](docs/WorkflowsApi.md#raster_stream_websocket) | **GET** /workflow/{id}/rasterStream | Query a workflow raster result as a stream of tiles via a websocket connection.
*WorkflowsApi* | [**register_workflow_handler**](docs/WorkflowsApi.md#register_workflow_handler) | **POST** /workflow | Registers a new Workflow.


## Documentation For Models

 - [AbortedTaskStatus](docs/AbortedTaskStatus.md)
 - [AddCollection200Response](docs/AddCollection200Response.md)
 - [AddDataset](docs/AddDataset.md)
 - [AddLayer](docs/AddLayer.md)
 - [AddLayerCollection](docs/AddLayerCollection.md)
 - [AddRole](docs/AddRole.md)
 - [AutoCreateDataset](docs/AutoCreateDataset.md)
 - [AutoOgrSourceTimeFormat](docs/AutoOgrSourceTimeFormat.md)
 - [AxisOrder](docs/AxisOrder.md)
 - [BoundingBox2D](docs/BoundingBox2D.md)
 - [Breakpoint](docs/Breakpoint.md)
 - [ClassificationMeasurement](docs/ClassificationMeasurement.md)
 - [ClassificationMeasurementWithType](docs/ClassificationMeasurementWithType.md)
 - [CollectionItem](docs/CollectionItem.md)
 - [CollectionType](docs/CollectionType.md)
 - [ColorParam](docs/ColorParam.md)
 - [Colorizer](docs/Colorizer.md)
 - [CompletedTaskStatus](docs/CompletedTaskStatus.md)
 - [ContinuousMeasurement](docs/ContinuousMeasurement.md)
 - [ContinuousMeasurementWithType](docs/ContinuousMeasurementWithType.md)
 - [Coordinate2D](docs/Coordinate2D.md)
 - [CreateDataset](docs/CreateDataset.md)
 - [CreateDatasetHandler200Response](docs/CreateDatasetHandler200Response.md)
 - [CreateProject](docs/CreateProject.md)
 - [CsvHeader](docs/CsvHeader.md)
 - [CustomOgrSourceTimeFormat](docs/CustomOgrSourceTimeFormat.md)
 - [DataId](docs/DataId.md)
 - [DataPath](docs/DataPath.md)
 - [DataPathOneOf](docs/DataPathOneOf.md)
 - [DataPathOneOf1](docs/DataPathOneOf1.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetDefinition](docs/DatasetDefinition.md)
 - [DatasetIdResourceId](docs/DatasetIdResourceId.md)
 - [DatasetListing](docs/DatasetListing.md)
 - [DatasetResource](docs/DatasetResource.md)
 - [DateTime](docs/DateTime.md)
 - [DateTimeParseFormat](docs/DateTimeParseFormat.md)
 - [DefaultColors](docs/DefaultColors.md)
 - [DefaultColorsOneOf](docs/DefaultColorsOneOf.md)
 - [DerivedColor](docs/DerivedColor.md)
 - [DerivedColorWithType](docs/DerivedColorWithType.md)
 - [DerivedNumber](docs/DerivedNumber.md)
 - [DerivedNumberWithType](docs/DerivedNumberWithType.md)
 - [DescribeCoverageRequest](docs/DescribeCoverageRequest.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExternalDataId](docs/ExternalDataId.md)
 - [ExternalDataIdWithType](docs/ExternalDataIdWithType.md)
 - [FailedTaskStatus](docs/FailedTaskStatus.md)
 - [FeatureDataType](docs/FeatureDataType.md)
 - [FileNotFoundHandling](docs/FileNotFoundHandling.md)
 - [FormatSpecifics](docs/FormatSpecifics.md)
 - [FormatSpecificsOneOf](docs/FormatSpecificsOneOf.md)
 - [FormatSpecificsOneOfCsv](docs/FormatSpecificsOneOfCsv.md)
 - [GdalDatasetGeoTransform](docs/GdalDatasetGeoTransform.md)
 - [GdalDatasetParameters](docs/GdalDatasetParameters.md)
 - [GdalLoadingInfoTemporalSlice](docs/GdalLoadingInfoTemporalSlice.md)
 - [GdalMetaDataList](docs/GdalMetaDataList.md)
 - [GdalMetaDataListWithType](docs/GdalMetaDataListWithType.md)
 - [GdalMetaDataRegular](docs/GdalMetaDataRegular.md)
 - [GdalMetaDataRegularWithType](docs/GdalMetaDataRegularWithType.md)
 - [GdalMetaDataStatic](docs/GdalMetaDataStatic.md)
 - [GdalMetaDataStaticWithType](docs/GdalMetaDataStaticWithType.md)
 - [GdalMetadataMapping](docs/GdalMetadataMapping.md)
 - [GdalMetadataNetCdfCf](docs/GdalMetadataNetCdfCf.md)
 - [GdalMetadataNetCdfCfWithType](docs/GdalMetadataNetCdfCfWithType.md)
 - [GdalSourceTimePlaceholder](docs/GdalSourceTimePlaceholder.md)
 - [GeoJson](docs/GeoJson.md)
 - [GetCapabilitiesFormat](docs/GetCapabilitiesFormat.md)
 - [GetCapabilitiesRequest](docs/GetCapabilitiesRequest.md)
 - [GetCoverageFormat](docs/GetCoverageFormat.md)
 - [GetCoverageRequest](docs/GetCoverageRequest.md)
 - [GetFeatureRequest](docs/GetFeatureRequest.md)
 - [GetLegendGraphicRequest](docs/GetLegendGraphicRequest.md)
 - [GetMapExceptionFormat](docs/GetMapExceptionFormat.md)
 - [GetMapFormat](docs/GetMapFormat.md)
 - [GetMapRequest](docs/GetMapRequest.md)
 - [InfiniteOgrSourceDurationSpec](docs/InfiniteOgrSourceDurationSpec.md)
 - [InternalDataId](docs/InternalDataId.md)
 - [Layer](docs/Layer.md)
 - [LayerCollection](docs/LayerCollection.md)
 - [LayerCollectionListing](docs/LayerCollectionListing.md)
 - [LayerCollectionListingWithType](docs/LayerCollectionListingWithType.md)
 - [LayerCollectionResource](docs/LayerCollectionResource.md)
 - [LayerCollectionResourceId](docs/LayerCollectionResourceId.md)
 - [LayerListing](docs/LayerListing.md)
 - [LayerListingWithType](docs/LayerListingWithType.md)
 - [LayerResource](docs/LayerResource.md)
 - [LayerResourceId](docs/LayerResourceId.md)
 - [LayerUpdate](docs/LayerUpdate.md)
 - [LayerVisibility](docs/LayerVisibility.md)
 - [LineSymbology](docs/LineSymbology.md)
 - [LineSymbologyWithType](docs/LineSymbologyWithType.md)
 - [LinearGradient](docs/LinearGradient.md)
 - [LinearGradientWithType](docs/LinearGradientWithType.md)
 - [LogarithmicGradient](docs/LogarithmicGradient.md)
 - [LogarithmicGradientWithType](docs/LogarithmicGradientWithType.md)
 - [Measurement](docs/Measurement.md)
 - [MetaDataDefinition](docs/MetaDataDefinition.md)
 - [MetaDataSuggestion](docs/MetaDataSuggestion.md)
 - [MockDatasetDataSourceLoadingInfo](docs/MockDatasetDataSourceLoadingInfo.md)
 - [MockMetaData](docs/MockMetaData.md)
 - [MockMetaDataWithType](docs/MockMetaDataWithType.md)
 - [ModelIdResourceId](docs/ModelIdResourceId.md)
 - [MultiLineString](docs/MultiLineString.md)
 - [MultiPoint](docs/MultiPoint.md)
 - [MultiPolygon](docs/MultiPolygon.md)
 - [NoneOgrSourceDatasetTimeType](docs/NoneOgrSourceDatasetTimeType.md)
 - [NumberParam](docs/NumberParam.md)
 - [OgrMetaData](docs/OgrMetaData.md)
 - [OgrMetaDataWithType](docs/OgrMetaDataWithType.md)
 - [OgrSourceColumnSpec](docs/OgrSourceColumnSpec.md)
 - [OgrSourceDataset](docs/OgrSourceDataset.md)
 - [OgrSourceDatasetTimeType](docs/OgrSourceDatasetTimeType.md)
 - [OgrSourceDurationSpec](docs/OgrSourceDurationSpec.md)
 - [OgrSourceErrorSpec](docs/OgrSourceErrorSpec.md)
 - [OgrSourceTimeFormat](docs/OgrSourceTimeFormat.md)
 - [OrderBy](docs/OrderBy.md)
 - [OverUnderColors](docs/OverUnderColors.md)
 - [PaletteColorizer](docs/PaletteColorizer.md)
 - [Permission](docs/Permission.md)
 - [PermissionRequest](docs/PermissionRequest.md)
 - [Plot](docs/Plot.md)
 - [PlotOutputFormat](docs/PlotOutputFormat.md)
 - [PlotQueryRectangle](docs/PlotQueryRectangle.md)
 - [PlotResultDescriptor](docs/PlotResultDescriptor.md)
 - [PlotResultDescriptorWithType](docs/PlotResultDescriptorWithType.md)
 - [PlotUpdate](docs/PlotUpdate.md)
 - [PointSymbology](docs/PointSymbology.md)
 - [PointSymbologyWithType](docs/PointSymbologyWithType.md)
 - [PolygonSymbology](docs/PolygonSymbology.md)
 - [PolygonSymbologyWithType](docs/PolygonSymbologyWithType.md)
 - [Project](docs/Project.md)
 - [ProjectLayer](docs/ProjectLayer.md)
 - [ProjectListing](docs/ProjectListing.md)
 - [ProjectResource](docs/ProjectResource.md)
 - [ProjectResourceId](docs/ProjectResourceId.md)
 - [ProjectVersion](docs/ProjectVersion.md)
 - [Provenance](docs/Provenance.md)
 - [ProvenanceEntry](docs/ProvenanceEntry.md)
 - [ProvenanceOutput](docs/ProvenanceOutput.md)
 - [ProviderLayerCollectionId](docs/ProviderLayerCollectionId.md)
 - [ProviderLayerId](docs/ProviderLayerId.md)
 - [Quota](docs/Quota.md)
 - [RasterDataType](docs/RasterDataType.md)
 - [RasterDatasetFromWorkflow](docs/RasterDatasetFromWorkflow.md)
 - [RasterDatasetFromWorkflowResult](docs/RasterDatasetFromWorkflowResult.md)
 - [RasterPropertiesEntryType](docs/RasterPropertiesEntryType.md)
 - [RasterPropertiesKey](docs/RasterPropertiesKey.md)
 - [RasterQueryRectangle](docs/RasterQueryRectangle.md)
 - [RasterResultDescriptor](docs/RasterResultDescriptor.md)
 - [RasterResultDescriptorWithType](docs/RasterResultDescriptorWithType.md)
 - [RasterStreamWebsocketResultType](docs/RasterStreamWebsocketResultType.md)
 - [RasterSymbology](docs/RasterSymbology.md)
 - [RasterSymbologyWithType](docs/RasterSymbologyWithType.md)
 - [Resource](docs/Resource.md)
 - [ResourceId](docs/ResourceId.md)
 - [RgbaColorizer](docs/RgbaColorizer.md)
 - [Role](docs/Role.md)
 - [RoleDescription](docs/RoleDescription.md)
 - [RunningTaskStatus](docs/RunningTaskStatus.md)
 - [STRectangle](docs/STRectangle.md)
 - [ServerInfo](docs/ServerInfo.md)
 - [SpatialPartition2D](docs/SpatialPartition2D.md)
 - [SpatialReferenceAuthority](docs/SpatialReferenceAuthority.md)
 - [SpatialReferenceSpecification](docs/SpatialReferenceSpecification.md)
 - [SpatialResolution](docs/SpatialResolution.md)
 - [StartDurationOgrSourceDatasetTimeType](docs/StartDurationOgrSourceDatasetTimeType.md)
 - [StartEndOgrSourceDatasetTimeType](docs/StartEndOgrSourceDatasetTimeType.md)
 - [StartOgrSourceDatasetTimeType](docs/StartOgrSourceDatasetTimeType.md)
 - [StaticColorParam](docs/StaticColorParam.md)
 - [StaticNumberParam](docs/StaticNumberParam.md)
 - [StrokeParam](docs/StrokeParam.md)
 - [Symbology](docs/Symbology.md)
 - [TaskAbortOptions](docs/TaskAbortOptions.md)
 - [TaskFilter](docs/TaskFilter.md)
 - [TaskListOptions](docs/TaskListOptions.md)
 - [TaskResponse](docs/TaskResponse.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskStatusWithId](docs/TaskStatusWithId.md)
 - [TextSymbology](docs/TextSymbology.md)
 - [TimeGranularity](docs/TimeGranularity.md)
 - [TimeInterval](docs/TimeInterval.md)
 - [TimeReference](docs/TimeReference.md)
 - [TimeStep](docs/TimeStep.md)
 - [TimeStepWithType](docs/TimeStepWithType.md)
 - [TypedGeometry](docs/TypedGeometry.md)
 - [TypedGeometryOneOf](docs/TypedGeometryOneOf.md)
 - [TypedGeometryOneOf1](docs/TypedGeometryOneOf1.md)
 - [TypedGeometryOneOf2](docs/TypedGeometryOneOf2.md)
 - [TypedGeometryOneOf3](docs/TypedGeometryOneOf3.md)
 - [TypedOperator](docs/TypedOperator.md)
 - [TypedOperatorOperator](docs/TypedOperatorOperator.md)
 - [TypedResultDescriptor](docs/TypedResultDescriptor.md)
 - [UnitlessMeasurement](docs/UnitlessMeasurement.md)
 - [UnixTimeStampOgrSourceTimeFormat](docs/UnixTimeStampOgrSourceTimeFormat.md)
 - [UnixTimeStampType](docs/UnixTimeStampType.md)
 - [UpdateProject](docs/UpdateProject.md)
 - [UpdateQuota](docs/UpdateQuota.md)
 - [UploadFileLayersResponse](docs/UploadFileLayersResponse.md)
 - [UploadFilesResponse](docs/UploadFilesResponse.md)
 - [UserCredentials](docs/UserCredentials.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserRegistration](docs/UserRegistration.md)
 - [UserSession](docs/UserSession.md)
 - [VectorColumnInfo](docs/VectorColumnInfo.md)
 - [VectorDataType](docs/VectorDataType.md)
 - [VectorQueryRectangle](docs/VectorQueryRectangle.md)
 - [VectorResultDescriptor](docs/VectorResultDescriptor.md)
 - [VectorResultDescriptorWithType](docs/VectorResultDescriptorWithType.md)
 - [Volume](docs/Volume.md)
 - [WcsBoundingbox](docs/WcsBoundingbox.md)
 - [WcsService](docs/WcsService.md)
 - [WcsVersion](docs/WcsVersion.md)
 - [WfsService](docs/WfsService.md)
 - [WfsVersion](docs/WfsVersion.md)
 - [WmsService](docs/WmsService.md)
 - [WmsVersion](docs/WmsVersion.md)
 - [Workflow](docs/Workflow.md)
 - [WrappedPlotOutput](docs/WrappedPlotOutput.md)
 - [ZeroOgrSourceDurationSpec](docs/ZeroOgrSourceDurationSpec.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="session_token"></a>
### session_token

- **Type**: Bearer authentication (UUID)


## Author

dev@geoengine.de


