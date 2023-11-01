from sqlalchemy import Column, Integer, String, Float, ForeignKey
from SaleApp.App import app,db
from sqlalchemy.orm import relationship


class Categories(db.Model):
    # __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Products', backref='categories', lazy=True)

class Products(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float,default=90)
    image = Column(String(100))
    product_id = Column(Integer, ForeignKey(Categories.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        # c1 = Categories(name ='Moblie')
        # c2 = Categories(name ='Tablet')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        p1 = Products(name = 'iPhone',price = 20000000, image = 'https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953606803_thumb_iphone_15_pro_didongviet.jpg',product_id= 1)
        p2 = Products(name ='SamSung', price = 15000000, image = 'https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953356175_thumb_iphone_15_didongviet.jpg', product_id =2)
        p3 = Products(name ='iPhone 11', price = 2300000, image = 'https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-11-64gb-chinh-hang_3.jpg',product_id=3)
        p4 = Products(name ='iPhone 14', price = 300000000 , image = 'https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-13-pro-max-128gb-didongviet_5.jpg',product_id=1)
        p5 = Products(name='iPhone XS', price= 29000000, image='https://cdn-v2.didongviet.vn/files/products/2023/4/3/1/1683100852721_iphone_xs_max_vang_didongviet.jpg',product_id=2)
        p6 = Products(name='SamSung Utra 22', price= 2500000, image='https://cdn-v2.didongviet.vn/files/media/catalog/product/s/a/samsung-galaxy-z-flip4-5g-256gb-fullbox-likenew-didongviet.jpg',product_id=3)
        p7 = Products(name ='iPhone 11', price = 2300000, image = 'https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-11-64gb-chinh-hang_3.jpg',product_id=2)
        p8 = Products(name ='iPhone 14', price = 300000000 , image = 'https://cdn-v2.didongviet.vn/files/media/catalog/product/i/p/iphone-13-pro-max-128gb-didongviet_5.jpg',product_id=1)
        p9 = Products(name = 'iPhone',price = 20000000, image = 'https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953606803_thumb_iphone_15_pro_didongviet.jpg',product_id=3)
        p10= Products(name ='SamSung', price = 15000000, image = 'https://cdn-v2.didongviet.vn/files/products/2023/8/29/1/1695953356175_thumb_iphone_15_didongviet.jpg',product_id=1)
        db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
        db.session.commit()
        # db.create_all()
