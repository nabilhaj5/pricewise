from database import db


class Supermarket(db.Model):
    __tablename__ = 'supermarkets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    prices = db.relationship('Price', backref='supermarket', lazy=True)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    category = db.Column(db.String(100))
    unit = db.Column(db.String(50))

    prices = db.relationship('Price', backref='product', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'unit': self.unit
        }


class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarkets.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product.name,
            'supermarket_id': self.supermarket_id,
            'supermarket_name': self.supermarket.name,
            'price': self.price
        }