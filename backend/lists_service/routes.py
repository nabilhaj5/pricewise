from flask import Blueprint, request, jsonify
from database import db
from models import ShoppingList, ListItem
import products_client

lists_bp = Blueprint('lists', __name__)


# ---------- LISTAS (CRUD) ----------

@lists_bp.route('/lists', methods=['GET'])
def get_lists():
    lists = ShoppingList.query.all()
    return jsonify([l.to_dict() for l in lists]), 200


@lists_bp.route('/lists', methods=['POST'])
def create_list():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'El campo name es obligatorio'}), 400

    lst = ShoppingList(name=data['name'])
    db.session.add(lst)
    db.session.commit()
    return jsonify(lst.to_dict()), 201


@lists_bp.route('/lists/<int:list_id>', methods=['GET'])
def get_list(list_id):
    lst = ShoppingList.query.get_or_404(list_id)
    return jsonify(lst.to_dict()), 200


@lists_bp.route('/lists/<int:list_id>', methods=['PUT'])
def update_list(list_id):
    lst = ShoppingList.query.get_or_404(list_id)
    data = request.get_json()
    if 'name' in data:
        lst.name = data['name']
    db.session.commit()
    return jsonify(lst.to_dict()), 200


@lists_bp.route('/lists/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    lst = ShoppingList.query.get_or_404(list_id)
    db.session.delete(lst)
    db.session.commit()
    return jsonify({'message': 'Lista eliminada'}), 200


# ---------- ÍTEMS DE LA LISTA ----------

@lists_bp.route('/lists/<int:list_id>/items', methods=['POST'])
def add_item(list_id):
    lst = ShoppingList.query.get_or_404(list_id)
    data = request.get_json()

    if 'product_id' not in data:
        return jsonify({'error': 'product_id es obligatorio'}), 400

    product = products_client.get_product(data['product_id'])
    if not product:
        return jsonify({'error': 'Producto no existe en el catálogo'}), 404

    existing = ListItem.query.filter_by(
        list_id=lst.id, product_id=product['id']
    ).first()

    if existing:
        existing.quantity += data.get('quantity', 1)
        db.session.commit()
        return jsonify(existing.to_dict()), 200

    item = ListItem(
        list_id=lst.id,
        product_id=product['id'],
        product_name=product['name'],
        quantity=data.get('quantity', 1)
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@lists_bp.route('/lists/<int:list_id>/items/<int:item_id>', methods=['DELETE'])
def remove_item(list_id, item_id):
    ShoppingList.query.get_or_404(list_id)
    item = ListItem.query.filter_by(id=item_id, list_id=list_id).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Ítem eliminado'}), 200


# ---------- COMPARACIÓN ----------

@lists_bp.route('/lists/<int:list_id>/compare', methods=['GET'])
def compare_list(list_id):
    lst = ShoppingList.query.get_or_404(list_id)

    if not lst.items:
        return jsonify({'error': 'La lista está vacía'}), 400

    product_ids = []
    for item in lst.items:
        product_ids.extend([item.product_id] * item.quantity)

    try:
        comparison = products_client.compare_products(product_ids)
    except Exception as e:
        return jsonify({'error': f'Error consultando products_service: {str(e)}'}), 502

    return jsonify({
        'list_id': lst.id,
        'list_name': lst.name,
        'item_count': len(product_ids),
        'comparison': comparison
    }), 200