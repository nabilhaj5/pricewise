function ProductList({ products, onAdd, loading }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">
        Catálogo de productos
      </h2>

      {products.length === 0 ? (
        <p className="text-gray-500 text-sm">
          Cargando productos... (¿está corriendo el products_service en :5001?)
        </p>
      ) : (
        <ul className="space-y-2">
          {products.map((product) => (
            <li
              key={product.id}
              className="flex items-center justify-between border-b border-gray-100 py-2"
            >
              <div>
                <p className="font-medium text-gray-800">{product.name}</p>
                <p className="text-xs text-gray-500">
                  {product.category} · {product.unit}
                </p>
              </div>
              <button
                onClick={() => onAdd(product.id)}
                disabled={loading}
                className="bg-emerald-600 hover:bg-emerald-700 disabled:bg-gray-300 text-white text-sm font-medium px-3 py-1 rounded transition"
              >
                Añadir
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProductList;