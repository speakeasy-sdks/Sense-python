# document

## Overview

Classify documents by type

### Available Operations

* [classify_document](#classify_document) - Classify document by type
* [classify_document_sync](#classify_document_sync) - Classify document by type (sync)

## classify_document

Score a document's similarity to each document type you defined in your Sensible account and to each reference document in the highest-scoring type.
To retrieve the scores, poll the `download_link` in this endpoint's response until it returns a non-error response.
For more information about scores, expand the 200 response in the synchronous [classification](ref:classify-document-sync) endpoint.

Use this endpoint:

 - In an extraction workflow. For example, determine which documents to extract prior to calling a Sensible extraction endpoint.
 - Outside an extraction workflow. For example, to determine where to route each document or to label each document in a system of record.

To post the document bytes, specify the non-encoded document bytes as the entire request body,and specify the `Content-Type` header, for example,"application/pdf" or "image/jpeg".

This endpoint supports documents up to 4.5MB in size.

For a list of supported document file types, see the [/extract](ref:extract-data-from-a-document) endpoint.


### Example Usage

```python
import classification


s = classification.Classification(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = 'provident'.encode()

res = s.document.classify_document(req)

if res.classify_async_single_response is not None:
    # handle response
```

## classify_document_sync


**Note:** Use this Classify endpoint for testing. Use the asynchronous Classify endpoint for production.

Score a document's similarity to each document type you defined in your Sensible account. Get scores for the document's similarity to document types and to their reference documents.

Use this endpoint:

 - In an extraction workflow. For example, determine which documents to extract prior to calling a Sensible extraction endpoint.
 - Outside an extraction workflow. For example, determine where to route each document or to label each document in a system of record.

To post the document bytes, specify the non-encoded document bytes as the entire request body,and specify the `Content-Type` header, for example,"application/pdf" or "image/jpeg".
This endpoint supports documents up to 4.5MB in size.

For a list of supported document file types, see the [/extract](ref:extract-data-from-a-document) endpoint.


### Example Usage

```python
import classification


s = classification.Classification(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = 'distinctio'.encode()

res = s.document.classify_document_sync(req)

if res.classify_single_response is not None:
    # handle response
```
