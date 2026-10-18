function ShoppingList({ list, onCompare, loading }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">
        Mi lista
      </h2>

      {!list || list.items.length === 0 ? (
        <p className="text-gray-500 text-sm">
          Aún no has añadido productos. Haz clic en "Añadir" en el catálogo.
        </p>
      ) : (
        <>
          <ul className="space-y-2 mb-4">
            {list.items.map((item) => (
              <li
                key={item.id}
                className="flex items-center justify-between border-b border-gray-100 py-2"
              >
                <span className="text-gray-800">{item.product_name}</span>
                <span className="text-sm text-gray-500">
                  x{item.quantity}
                </span>
              </li>
            ))}
          </ul>

          <button
            onClick={onCompare}
            disabled={loading}
            className="w-full bg-emerald-600 hover:bg-emerald-700 disabled:bg-gray-300 text-white font-medium py-2 rounded transition"
          >
            {loading ? 'Comparando...' : '🔍 Comparar precios'}
          </button>
        </>
      )}
    </div>
  );
}

export default ShoppingList;