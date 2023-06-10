# Classification

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/Sense-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import classification


s = classification.Classification(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = 'corrupti'.encode()

res = s.document.classify_document(req)

if res.classify_async_single_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [document](docs/sdks/document/README.md)

* [classify_document](docs/sdks/document/README.md#classify_document) - Classify document by type
* [classify_document_sync](docs/sdks/document/README.md#classify_document_sync) - Classify document by type (sync)
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
