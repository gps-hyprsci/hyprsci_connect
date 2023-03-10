# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.streams_list_read_streams_inner import StreamsListReadStreamsInner


class StreamsListRead(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    StreamsListRead - a model defined in OpenAPI

        streams: The streams of this StreamsListRead.
    """

    streams: List[StreamsListReadStreamsInner] = Field(alias="streams")

StreamsListRead.update_forward_refs()
