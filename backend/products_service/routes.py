from flask import Blueprint, request, jsonify
from database import db
from models import Product, Supermarket, Price

products_bp = Blueprint('products', __name__)


@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200


@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'El campo name es obligatorio'}), 400
    if Product.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'El producto ya existe'}), 409
    product = Product(
        name=data['name'],
        category=data.get('category'),
        unit=data.get('unit')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201


@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.unit = data.get('unit', product.unit)
    db.session.commit()
    return jsonify(product.to_dict()), 200


@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    Price.query.filter_by(product_id=product_id).delete()
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Producto eliminado'}), 200


@products_bp.route('/supermarkets', methods=['GET'])
def get_supermarkets():
    markets = Supermarket.query.all()
    return jsonify([m.to_dict() for m in markets]), 200


@products_bp.route('/supermarkets', methods=['POST'])
def create_supermarket():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'El campo name es obligatorio'}), 400
    if Supermarket.query.filter_by(name=data['name']).first():
        return jsonify({'error': 'El supermercado ya existe'}), 409
    market = Supermarket(name=data['name'])
    db.session.add(market)
    db.session.commit()
    return jsonify(market.to_dict()), 201


@products_bp.route('/prices', methods=['POST'])
def create_price():
    data = request.get_json()
    required = ['product_id', 'supermarket_id', 'price']
    if not all(k in data for k in required):
        return jsonify({'error': f'Campos requeridos: {required}'}), 400
    price = Price(
        product_id=data['product_id'],
        supermarket_id=data['supermarket_id'],
        price=data['price']
    )
    db.session.add(price)
    db.session.commit()
    return jsonify(price.to_dict()), 201


@products_bp.route('/products/<int:product_id>/prices', methods=['GET'])
def get_product_prices(product_id):
    Product.query.get_or_404(product_id)
    prices = Price.query.filter_by(product_id=product_id).all()
    return jsonify([p.to_dict() for p in prices]), 200


@products_bp.route('/compare', methods=['POST'])
def compare_prices():
    data = request.get_json()
    product_ids = data.get('product_ids', [])
    if not product_ids:
        return jsonify({'error': 'Debes enviar product_ids'}), 400

    supermarkets = Supermarket.query.all()
    results = []

    for market in supermarkets:
        total = 0.0
        found_all = True
        detail = []

        for pid in product_ids:
            price = Price.query.filter_by(
                product_id=pid, supermarket_id=market.id
            ).first()

            if price:
                total += price.price
                detail.append({
                    'product_id': pid,
                    'product_name': price.product.name,
                    'price': price.price
                })
            else:
                found_all = False
                product = Product.query.get(pid)
                detail.append({
                    'product_id': pid,
                    'product_name': product.name if product else 'Desconocido',
                    'price': None
                })

        results.append({
            'supermarket': market.name,
            'supermarket_id': market.id,
            'total': round(total, 2) if found_all else None,
            'complete': found_all,
            'detail': detail
        })

    results.sort(key=lambda r: (not r['complete'], r['total'] or 999999))
    return jsonify(results), 200