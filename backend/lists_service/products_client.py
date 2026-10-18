import os
import requests

PRODUCTS_SERVICE_URL = os.getenv(
    'PRODUCTS_SERVICE_URL', 'http://localhost:5001'
)


def get_all_products():
    r = requests.get(f'{PRODUCTS_SERVICE_URL}/products', timeout=5)
    r.raise_for_status()
    return r.json()


def get_product(product_id):
    r = requests.get(f'{PRODUCTS_SERVICE_URL}/products', timeout=5)
    r.raise_for_status()
    for p in r.json():
        if p['id'] == product_id:
            return p
    return None


def compare_products(product_ids):
    r = requests.post(
        f'{PRODUCTS_SERVICE_URL}/compare',
        json={'product_ids': product_ids},
        timeout=5
    )
    r.raise_for_status()
    return r.json()