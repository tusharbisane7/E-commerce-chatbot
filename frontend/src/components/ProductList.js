import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await axios.get('http://localhost:5000/products');
      setProducts(res.data.products);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <div className="product-list">
        {products.map(p => (
          <div key={p.id} className="product-card">
            <img src={p.image} alt={p.name} />
            <h4>{p.name}</h4>
            <p>{p.description}</p>
            <strong>₹{p.price}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductList;
