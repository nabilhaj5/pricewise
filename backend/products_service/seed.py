from app import create_app
from database import db
from models import Product, Supermarket, Price

app = create_app()

with app.app_context():
    # Limpiamos por si ejecutas el seed varias veces
    db.drop_all()
    db.create_all()

    # --- Supermercados ---
    mercadona = Supermarket(name='Mercadona')
    carrefour = Supermarket(name='Carrefour')
    lidl = Supermarket(name='Lidl')
    db.session.add_all([mercadona, carrefour, lidl])
    db.session.commit()

    # --- Productos ---
    productos = [
        Product(name='Leche entera 1L', category='Lácteos', unit='L'),
        Product(name='Pan de molde', category='Panadería', unit='unidad'),
        Product(name='Huevos docena', category='Huevos', unit='docena'),
        Product(name='Arroz 1kg', category='Cereales', unit='kg'),
        Product(name='Pechuga de pollo 1kg', category='Carnes', unit='kg'),
    ]
    db.session.add_all(productos)
    db.session.commit()

    # --- Precios de prueba ---
    precios = [
        # (producto, supermercado, precio)
        (productos[0], mercadona, 0.95), (productos[0], carrefour, 1.05), (productos[0], lidl, 0.89),
        (productos[1], mercadona, 1.20), (productos[1], carrefour, 1.15), (productos[1], lidl, 1.10),
        (productos[2], mercadona, 2.10), (productos[2], carrefour, 2.25), (productos[2], lidl, 1.99),
        (productos[3], mercadona, 1.35), (productos[3], carrefour, 1.29), (productos[3], lidl, 1.40),
        (productos[4], mercadona, 5.90), (productos[4], carrefour, 6.10), (productos[4], lidl, 5.75),
    ]

    for prod, market, p in precios:
        db.session.add(Price(
            product_id=prod.id,
            supermarket_id=market.id,
            price=p
        ))

    db.session.commit()
    print('✅ Base de datos poblada con datos de prueba')
    print(f'   - {len(productos)} productos')
    print(f'   - 3 supermercados')
    print(f'   - {len(precios)} precios')