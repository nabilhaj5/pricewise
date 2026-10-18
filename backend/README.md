\# PriceWise — Backend



Backend de PriceWise: \*\*dos microservicios Flask\*\* que se comunican por HTTP.



\## Estructura

backend/

├── products\_service/ # catálogo y precios (puerto 5001)

│ ├── app.py

│ ├── models.py # Product, Supermarket, Price

│ ├── routes.py # products\_bp

│ ├── database.py

│ ├── seed.py

│ └── requirements.txt

│

└── lists\_service/ # listas del usuario (puerto 5002)

├── app.py

├── models.py # ShoppingList, ListItem

├── routes.py # lists\_bp

├── database.py

├── products\_client.py

└── requirements.txt



text



\## Microservicios



\### products\_service (`:5001`)



\- Modelos: `Product`, `Supermarket`, `Price`.

\- BD: `instance/products.db`.

\- Endpoint clave: `POST /compare`.



\### lists\_service (`:5002`)



\- Modelos: `ShoppingList`, `ListItem`.

\- BD: `instance/lists.db`.

\- Endpoint clave: `GET /lists/:id/compare`.



\## Comunicación entre servicios



`lists\_service` llama a `products\_service` con `requests`:



```python

PRODUCTS\_SERVICE\_URL = os.getenv('PRODUCTS\_SERVICE\_URL', 'http://localhost:5001')

En producción se cambia con la variable de entorno PRODUCTS\_SERVICE\_URL.



Ejecutar en local

products\_service

bash

cd products\_service

python -m venv venv

pip install -r requirements.txt

python seed.py

python app.py

lists\_service

bash

cd lists\_service

python -m venv venv

pip install -r requirements.txt

python app.py

Variables de entorno

Variable	Servicio	Default

PRODUCTS\_SERVICE\_URL	lists\_service	http://localhost:5001

Datos de prueba

seed.py crea:



3 supermercados: Mercadona, Carrefour, Lidl.



5 productos: Leche, Pan, Huevos, Arroz, Pechuga de pollo.



15 precios (5 productos × 3 supermercados).



Probar la API con curl / PowerShell

bash

\# Health checks

curl http://localhost:5001/health

curl http://localhost:5002/health



\# Crear lista

curl -X POST http://localhost:5002/lists -H "Content-Type: application/json" -d '{"name":"Compra semanal"}'



\# Añadir producto

curl -X POST http://localhost:5002/lists/1/items -H "Content-Type: application/json" -d '{"product\_id":1,"quantity":2}'



\# Comparar

curl http://localhost:5002/lists/1/compare

