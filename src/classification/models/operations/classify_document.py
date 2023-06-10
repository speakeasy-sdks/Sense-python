"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import classifyasyncsingleresponse as shared_classifyasyncsingleresponse
from typing import Optional



@dataclasses.dataclass
class ClassifyDocumentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bad_request: Optional[str] = dataclasses.field(default=None)
    r"""Bad Request"""
    classify_async_single_response: Optional[shared_classifyasyncsingleresponse.ClassifyAsyncSingleResponse] = dataclasses.field(default=None)
    r"""Link to download the classification response. Poll the link until it returns a non-error response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    sensible_encountered_an_unknown_error: Optional[str] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    unauthorized: Optional[str] = dataclasses.field(default=None)
    r"""Not authorized"""
    unsupported_media_type: Optional[str] = dataclasses.field(default=None)
    r"""Unsupported Media Type"""
    

