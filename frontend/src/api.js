import axios from 'axios';

const PRODUCTS_API = import.meta.env.VITE_PRODUCTS_API || 'http://localhost:5001';
const LISTS_API = import.meta.env.VITE_LISTS_API || 'http://localhost:5002';

// ---------- PRODUCTOS ----------

export const getProducts = async () => {
  const res = await axios.get(`${PRODUCTS_API}/products`);
  return res.data;
};

export const getSupermarkets = async () => {
  const res = await axios.get(`${PRODUCTS_API}/supermarkets`);
  return res.data;
};

// ---------- LISTAS ----------

export const createList = async (name) => {
  const res = await axios.post(`${LISTS_API}/lists`, { name });
  return res.data;
};

export const getList = async (listId) => {
  const res = await axios.get(`${LISTS_API}/lists/${listId}`);
  return res.data;
};

export const addItemToList = async (listId, productId, quantity = 1) => {
  const res = await axios.post(`${LISTS_API}/lists/${listId}/items`, {
    product_id: productId,
    quantity
  });
  return res.data;
};

export const removeItemFromList = async (listId, itemId) => {
  const res = await axios.delete(`${LISTS_API}/lists/${listId}/items/${itemId}`);
  return res.data;
};

export const compareList = async (listId) => {
  const res = await axios.get(`${LISTS_API}/lists/${listId}/compare`);
  return res.data;
};

export const deleteList = async (listId) => {
  const res = await axios.delete(`${LISTS_API}/lists/${listId}`);
  return res.data;
};