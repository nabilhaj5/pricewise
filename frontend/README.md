# PriceWise — Frontend

Interfaz React que consume los dos microservicios vía Axios.

## Stack

- React 19 + Vite 8
- Tailwind CSS 4 (plugin oficial de Vite)
- Axios (cliente HTTP)
- Recharts (gráfico de barras, feature autoaprendido)

## Estructura
frontend/
├── src/
│ ├── api.js # cliente Axios (7 endpoints)
│ ├── App.jsx # componente principal
│ ├── main.jsx # entry point
│ ├── index.css # @import "tailwindcss"
│ └── components/
│ ├── ProductList.jsx # catálogo + botón Añadir
│ ├── ShoppingList.jsx # lista + botón Comparar
│ ├── ComparisonResult.jsx # ranking + tabla
│ └── ComparisonChart.jsx # gráfico Recharts
├── vite.config.js
└── package.json

text

## Cómo ejecutar

Requisito: Node.js 20+ y los dos backends corriendo en `:5001` y `:5002`.

```bash
npm install
npm run dev
Abre http://localhost:5173.

Flujo de la app
App.jsx pide GET /products a products_service y muestra el catálogo.

El usuario pulsa Añadir → POST /lists + POST /lists/:id/items.

Al pulsar 🔍 Comparar precios → GET /lists/:id/compare.

Se muestran:

Tarjetas con 🥇🥈🥉 y el total por supermercado.

Gráfico de barras (Recharts) con el más barato en verde.

Tabla de desglose producto × supermercado.

El botón 🔄 Reiniciar borra la lista (DELETE /lists/:id).

Feature autoaprendido: Recharts
ComparisonChart.jsx usa BarChart, Bar, XAxis, YAxis, Tooltip y Cell. El supermercado más barato se resalta en verde (#059669), el resto en gris (#9ca3af).

Variables de entorno
Actualmente las URLs están hardcodeadas en src/api.js:

js
const PRODUCTS_API = 'http://localhost:5001';
const LISTS_API = 'http://localhost:5002';
Para producción se cambian por las URLs de Render.

