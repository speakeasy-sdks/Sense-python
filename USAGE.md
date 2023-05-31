<!-- Start SDK Example Usage -->
```python
import classification


s = classification.Classification(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = 'corrupti'.encode()

res = s.document.classify_document(req)

if res.classify_async_single_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->