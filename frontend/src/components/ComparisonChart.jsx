import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts';

function ComparisonChart({ data }) {
  // Adaptar los datos al formato que espera Recharts
  const chartData = data.map((market) => ({
    name: market.supermarket,
    total: market.total || 0,
    complete: market.complete
  }));

  // Colores: el más barato en verde, el resto en gris
  const colors = chartData.map((entry, index) =>
    index === 0 ? '#059669' : '#9ca3af'
  );

  return (
    <div className="mt-6">
      <h3 className="font-semibold text-gray-700 mb-2">
        📊 Comparación visual
      </h3>
      <div style={{ width: '100%', height: 300 }}>
        <ResponsiveContainer>
          <BarChart data={chartData} margin={{ top: 20, right: 20, left: 0, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
            <XAxis dataKey="name" tick={{ fontSize: 13 }} />
            <YAxis
              tick={{ fontSize: 13 }}
              tickFormatter={(value) => `${value} €`}
            />
            <Tooltip
              formatter={(value) => [`${value.toFixed(2)} €`, 'Total']}
              contentStyle={{ borderRadius: 8, border: '1px solid #e5e7eb' }}
            />
            <Bar dataKey="total" radius={[8, 8, 0, 0]}>
              {chartData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={colors[index]} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
      <p className="text-xs text-gray-500 text-center mt-2">
        El supermercado más barato aparece en verde
      </p>
    </div>
  );
}

export default ComparisonChart;