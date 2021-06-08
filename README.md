# REST API Product Recommendations
Project using aiohttp

## Config file
config/api_recom_product.yaml
```yaml:
host: 127.0.0.1
port: 8282
```

## Run
Run application:
```bash:
$ pip install -r /path/to/requirements.txt
$ python product_recommendations/main.py
```
    
## API Description:

### Request 
HTTP GET
```bash:
curl -v -X http://127.0.0.1:8282/getProductRecommendations?sku=Fx7FQJ4ZkI&min_threshold=0.5
```

### Query Parameters

Parameter | Mandatory | Type 
----------|-----------|---------
sku | yes | string
min_threshold | no | float

### Success Response
```json:
[
    {
        "recommendation": "LgGNNDR7V9",
        "rank": "0.4"
    },
    {
        "recommendation": "LgGNNDR7Vl",
        "rank": "0.8"
    }
]
```

Parameter | Description 
----------|-----------
sku_recommendation | SKU рекомендованного товара 
rank | вероятность правильной рекомендации товара к исходному

### Error Response
```json:
{
    "status": "error",
    "error_message": "Required parameter sku not set"
}
```
http code | error message 
----------|-----------
500 | Internal Server Error 
400 | Required parameter sku not set
