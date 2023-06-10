# ClassifySingleResponseReferenceDocuments


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Unique ID for the reference document.                                               |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | User-friendly name for the reference document.                                      |
| `score`                                                                             | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | Similarity score comparing the document to the reference document, between 0 and 1. |