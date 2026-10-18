import { useState, useEffect } from 'react';
import {
  getProducts,
  createList,
  addItemToList,
  compareList,
  deleteList
} from './api';
import ProductList from './components/ProductList';
import ShoppingList from './components/ShoppingList';
import ComparisonResult from './components/ComparisonResult';

function App() {
  const [products, setProducts] = useState([]);
  const [list, setList] = useState(null);
  const [comparison, setComparison] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Cargar productos al inicio
  useEffect(() => {
    getProducts()
      .then(setProducts)
      .catch(() => setError('No se pudo cargar el catálogo de productos'));
  }, []);

  // Crear lista si no existe
  const ensureList = async () => {
    if (list) return list;
    const newList = await createList('Mi compra');
    setList(newList);
    return newList;
  };

  // Añadir producto a la lista
  const handleAddProduct = async (productId) => {
    try {
      setLoading(true);
      setError(null);
      const currentList = await ensureList();
      await addItemToList(currentList.id, productId);
      const updated = await getListById(currentList.id);
      setList(updated);
      setComparison(null); // invalidar comparación previa
    } catch (err) {
      setError('Error al añadir producto. ¿Están los dos backends corriendo?');
    } finally {
      setLoading(false);
    }
  };

  // Pequeño helper para recargar la lista
  const getListById = async (id) => {
    const res = await fetch(`http://localhost:5002/lists/${id}`);
    return res.json();
  };

  // Comparar precios
  const handleCompare = async () => {
    if (!list) return;
    try {
      setLoading(true);
      setError(null);
      const result = await compareList(list.id);
      setComparison(result);
    } catch (err) {
      setError('Error al comparar. ¿Están los dos backends corriendo?');
    } finally {
      setLoading(false);
    }
  };
  // Reset: borra la lista y vuelve al estado inicial
  const handleReset = async () => {
    try {
      setLoading(true);
      if (list) {
        await deleteList(list.id);
      }
    } catch (err) {
      // Si falla el borrado, seguimos igualmente limpiando el estado
      console.warn('No se pudo borrar la lista del backend:', err);
    } finally {
      setList(null);
      setComparison(null);
      setError(null);
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
           <header className="bg-emerald-600 text-white shadow-lg">
        <div className="max-w-6xl mx-auto px-4 py-6 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold">🛒 PriceWise</h1>
            <p className="text-emerald-100 text-sm mt-1">
              Compara los precios de tu compra entre supermercados
            </p>
          </div>
          <button
            onClick={handleReset}
            disabled={loading || (!list && !comparison)}
            className="bg-white text-emerald-700 hover:bg-emerald-50 disabled:bg-emerald-400 disabled:text-emerald-100 font-medium px-4 py-2 rounded-lg transition shadow"
          >
            🔄 Reiniciar
          </button>
        </div>
      </header>

      {/* Error banner */}
      {error && (
        <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 max-w-6xl mx-auto mt-4">
          {error}
        </div>
      )}

      {/* Main */}
      <main className="max-w-6xl mx-auto px-4 py-8 grid md:grid-cols-2 gap-6">
        <ProductList
          products={products}
          onAdd={handleAddProduct}
          loading={loading}
        />
        <ShoppingList
          list={list}
          onCompare={handleCompare}
          loading={loading}
        />
      </main>

      {/* Resultados de comparación */}
      {comparison && (
        <section className="max-w-6xl mx-auto px-4 pb-12">
          <ComparisonResult data={comparison} />
        </section>
      )}
    </div>
  );
}

export default App;