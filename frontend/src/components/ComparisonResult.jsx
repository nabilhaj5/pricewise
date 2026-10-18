import ComparisonChart from './ComparisonChart';

function ComparisonResult({ data }) {
  const { comparison, list_name, item_count } = data;

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-800 mb-1">
        Resultado de la comparación
      </h2>
      <p className="text-sm text-gray-500 mb-6">
        Lista: <strong>{list_name}</strong> · {item_count} productos
      </p>

      <div className="grid md:grid-cols-3 gap-4 mb-8">
        {comparison.map((market, index) => (
          <div
            key={market.supermarket_id}
            className={`rounded-lg p-4 border-2 ${
              index === 0
                ? 'border-emerald-500 bg-emerald-50'
                : 'border-gray-200 bg-white'
            }`}
          >
            <p className="text-2xl mb-1">
              {index === 0 ? '🥇' : index === 1 ? '🥈' : '🥉'}
            </p>
            <p className="font-semibold text-gray-800">
              {market.supermarket}
            </p>
            <p className="text-3xl font-bold text-emerald-600 mt-2">
              {market.total !== null ? `${market.total.toFixed(2)} €` : 'Incompleto'}
            </p>
            {!market.complete && (
              <p className="text-xs text-red-500 mt-1">
                Faltan productos en este supermercado
              </p>
            )}
          </div>
        ))}
      </div>

      <ComparisonChart data={comparison} />

      <div className="mt-8 overflow-x-auto">
        <h3 className="font-semibold text-gray-700 mb-2">Desglose por producto</h3>
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-gray-100">
              <th className="text-left p-2">Producto</th>
              {comparison.map((m) => (
                <th key={m.supermarket_id} className="text-right p-2">
                  {m.supermarket}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {[...new Set(comparison[0].detail.map((d) => d.product_id))].map(
              (productId) => {
                const productName = comparison[0].detail.find(
                  (d) => d.product_id === productId
                ).product_name;
                return (
                  <tr key={productId} className="border-b border-gray-100">
                    <td className="p-2">{productName}</td>
                    {comparison.map((m) => {
                      const item = m.detail.find(
                        (d) => d.product_id === productId
                      );
                      return (
                        <td
                          key={m.supermarket_id}
                          className="text-right p-2 text-gray-700"
                        >
                          {item?.price !== null && item?.price !== undefined
                            ? `${item.price.toFixed(2)} €`
                            : '—'}
                        </td>
                      );
                    })}
                  </tr>
                );
              }
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ComparisonResult;