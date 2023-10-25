def load_categories():
    return [
        {
            "id":"1",
            "name":"Mobile",
            # "image": Image.open("D:\images.png")
        },
        {
            "id": "1",
            "name": "Mobile",
            # "image": Image.open("D:\images.png")
        }
    ]

def load_products(kw=None):
    products = [
        {
            "id":"1",
            "name":"Iphone",
            "price": 20000000,
            "image":'https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953606803_thumb_iphone_15_pro_didongviet.jpg'
        },
        {
            "id": "2",
            "name": "Samsung",
            "price": 10000000,
            "image":"https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953356175_thumb_iphone_15_didongviet.jpg"
        },
        {
            "id": "3",
            "name": "Oppo",
            "price": 1500000,
            "image":'https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-11-64gb-chinh-hang_3.jpg'
        },{
            "id":"4",
            "name":"Galaxy",
            "price": 2000000,
            "image":"https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-13-pro-max-128gb-didongviet_5.jpg"
        },{
            "id":"5",
            "name":"Iphone",
            "price": 20000000,
            "image":'https://cdn-v2.didongviet.vn/files/products/2023/4/3/1/1683100852721_iphone_xs_max_vang_didongviet.jpg'
        },{
            "id":"6",
            "name":"Iphone",
            "price": 20000000,
            "image":"https://cdn-v2.didongviet.vn/files/media/catalog/product/s/a/samsung-galaxy-z-flip4-5g-256gb-fullbox-likenew-didongviet.jpg"
        }
    ]
    if kw:
        return (x for x in products if x['x.name'].find(kw) >= 0)

    return products
