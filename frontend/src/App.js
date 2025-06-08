import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Chatbot from './components/Chatbot';
import ProductList from './components/ProductList';

function App() {
  const token = localStorage.getItem('token');

  return (
    <Router>
      <Routes>
        {/* Protected Chatbot route */}
        <Route path="/" element={token ? <Chatbot /> : <Navigate to="/login" />} />

        {/* Public login and register routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected products route */}
        <Route path="/products" element={token ? <ProductList /> : <Navigate to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;
