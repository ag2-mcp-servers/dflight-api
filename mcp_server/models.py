# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T04:23:42+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class AerodromeDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class AerodromePolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class AerodromeRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class AerodromesByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class AerodromesByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class AerodromesByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class AirspaceByDistance(BaseModel):
    asptypes: List[str] = Field(..., title='Asptypes')
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class AirspaceByPolygon(BaseModel):
    asptypes: List[str] = Field(..., title='Asptypes')
    poly: Dict[str, Any] = Field(..., title='Poly')


class AirspaceByRoute(BaseModel):
    asptypes: List[str] = Field(..., title='Asptypes')
    route: Dict[str, Any] = Field(..., title='Route')


class AirspaceDistanceResponse(BaseModel):
    found: List[Dict[str, Any]] = Field(..., title='Found')


class AirspacePolyResponse(BaseModel):
    found: List[Dict[str, Any]] = Field(..., title='Found')


class AirspaceRouteResponse(BaseModel):
    found: List[Dict[str, Any]] = Field(..., title='Found')


class NOTAMsByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class NOTAMsByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class NOTAMsByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class NOTAMsDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class NOTAMsPolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class NOTAMsRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class ObstacleDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class ObstaclePolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class ObstacleRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class ObstaclesByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class ObstaclesByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class ObstaclesByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class SSAByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class SSAByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class SSAByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class SSADistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class SSAPolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class SSARouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class UOAsByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class UOAsByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class UOAsByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class UOAsDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class UOAsPolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class UOAsRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VenueDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class VenuePolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class VenueRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class VenuesByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')


class VenuesByPolygon(BaseModel):
    poly: Dict[str, Any] = Field(..., title='Poly')


class VenuesByRoute(BaseModel):
    route: Dict[str, Any] = Field(..., title='Route')


class WxByDistance(BaseModel):
    distance: Union[float, int] = Field(..., title='Distance')
    hours: int = Field(..., title='Hours')
    latitude: Union[float, int] = Field(..., title='Latitude')
    longitude: Union[float, int] = Field(..., title='Longitude')
    wxtypes: List[str] = Field(..., title='Wxtypes')


class WxByPolygon(BaseModel):
    hours: int = Field(..., title='Hours')
    poly: Dict[str, Any] = Field(..., title='Poly')
    wxtypes: List[str] = Field(..., title='Wxtypes')


class WxByRoute(BaseModel):
    hours: int = Field(..., title='Hours')
    route: Dict[str, Any] = Field(..., title='Route')
    wxtypes: List[str] = Field(..., title='Wxtypes')


class WxDistanceResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class WxPolyResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class WxRouteResponse(BaseModel):
    found: Dict[str, Any] = Field(..., title='Found')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
