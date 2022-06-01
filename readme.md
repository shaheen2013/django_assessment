# Django Assessment

REST end points

| Method | End Point | Payload| Description |
|--------|-----------|--------|-------------|
|GET| http://127.0.0.1:8000/api/products/ | NULL | Fetch All Product|
|GET| http://127.0.0.1:8000/api/product/<id>| NULL | Fetch Procut by it's id|
|POST| http://127.0.0.1:8000/api/products/ | ```{"name": "", "status": null, "price": null, "image": null, "product_class": ""} ``` | Save Product Into Database|
|PUT| http://127.0.0.1:8000/api/product/<id>/ | [PUT Payload](#put-payload) | It will update specific product|
|DELETE| http://127.0.0.1:8000/api/product/<id>/ | NULL| it will delete product by it's id|



#### PUT Payload
```
{
    "id": 1,
    "name": "Milk",
    "product_class": "Dairy",
    "price": 350.0,
    "image": "http://127.0.0.1:8000/doctor-trust.jpeg",
    "status": "available",
    "variants": [
        {
            "title": "Anchor",
            "available_stock": 60.0
        },
        {
            "title": "Nestle",
            "available_stock": 20.0
        },
        {
            "title": "Cadbury",
            "available_stock": 20.0
        }
    ]
}
```