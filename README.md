\# 🛒 PriceWise



Comparador de precios de supermercados. El usuario crea una lista de la compra y la app le dice en qué supermercado (Mercadona, Carrefour, Lidl) es más barata, con un ranking visual y un gráfico comparativo.



\## 🎯 Problema que resuelve



Los precios de los mismos productos varían entre supermercados, y calcular a mano cuál es la opción más barata para una lista completa es tedioso. PriceWise lo resuelve en un clic.



\## 👤 Usuario final 



Consumidores habituales de supermercado que hacen compras semanales o mensuales y quieren optimizar su presupuesto.



\## 🏗️ Arquitectura



El proyecto usa una \*\*arquitectura de microservicios\*\*:

┌──────────────────────────┐

│ Frontend (React) │

│ Vite + Tailwind │

│ http://localhost:5173 │

└──────────┬───────────────┘

│ Axios (HTTP)

┌─────┴─────┐

│ │

▼ ▼

┌─────────┐ ┌─────────┐

│Products │ │ Lists │

│Service │◄─│ Service │

│ :5001 │ │ :5002 │

│ SQLite │ │ SQLite │

└─────────┘ └─────────┘

▲ │

└────────────┘

HTTP (products\_client)



text



\- \*\*`products\_service`\*\* (puerto 5001): catálogo de productos, supermercados y precios. Expone `/products`, `/supermarkets`, `/compare`.

\- \*\*`lists\_service`\*\* (puerto 5002): listas de la compra del usuario. Consulta a `products\_service` vía HTTP para validar productos y comparar precios. Expone `/lists`, `/lists/:id/items`, `/lists/:id/compare`.

\- \*\*`frontend`\*\* (puerto 5173): interfaz React que consume ambos servicios con Axios.



\## 🛠️ Stack



\### Backend

\- \*\*Python 3.13\*\*

\- \*\*Flask 3.0.3\*\* — framework web

\- \*\*Flask-Cors 4.0.1\*\* — habilitar CORS

\- \*\*Flask-SQLAlchemy 3.1.1\*\* — ORM

\- \*\*SQLite\*\* — base de datos (2 archivos: `products.db`, `lists.db`)

\- \*\*requests 2.32.3\*\* — cliente HTTP entre microservicios



\### Frontend

\- \*\*React 19\*\* — UI

\- \*\*Vite 8\*\* — bundler

\- \*\*Tailwind CSS 4\*\* — estilos responsive

\- \*\*Axios\*\* — llamadas HTTP

\- \*\*Recharts\*\* — gráfico de barras (feature autoaprendido)



\### Herramientas

\- \*\*Git / GitHub\*\* — control de versiones

\- \*\*DB Browser for SQLite\*\* — inspección de datos



\## 🚀 Cómo ejecutar en local



\### Requisitos

\- Python 3.10+

\- Node.js 20+

\- Git



\### 1. Backend: `products\_service`



```bash

cd backend/products\_service

python -m venv venv

\# Windows: venv\\Scripts\\Activate.ps1

\# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt

python seed.py

python app.py

## 👤 Autor

**MAJID**
- GitHub: [@nabilhaj5](https://github.com/nabilhaj5)
- Email: nabilhaj5@gmail.com





