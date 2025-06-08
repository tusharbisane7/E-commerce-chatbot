import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import "./chatbot.css";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const savedUser = localStorage.getItem('username');
    if (savedUser) {
      setUsername(savedUser);
    } else {
      navigate('/login');
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('username');
    navigate('/login');
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      sender: 'user',
      text: input,
      time: new Date().toLocaleTimeString(),
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.get('http://localhost:5000/products');
      const products = res.data.products;

      const matches = products.filter((product) =>
        product.name.toLowerCase().includes(input.toLowerCase()) ||
        product.description.toLowerCase().includes(input.toLowerCase())
      );

      if (matches.length > 0) {
        const productMessages = matches.slice(0, 5).map((product) => ({
          sender: 'bot',
          text: `${product.name} - ₹${product.price}`,
          image: product.image,
          time: new Date().toLocaleTimeString(),
        }));

        setMessages((prev) => [...prev, ...productMessages]);
      } else {
        setMessages((prev) => [
          ...prev,
          {
            sender: 'bot',
            text: `No products found for "${input}"`,
            time: new Date().toLocaleTimeString(),
          },
        ]);
      }
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          sender: 'bot',
          text: 'Error fetching product data.',
          time: new Date().toLocaleTimeString(),
        },
      ]);
    }

    setInput('');
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <div>
          <h2>E-Commerce Bot</h2>
          <span className="status">Online Assistant</span>
        </div>
        <div className="user-info">
          <span><strong>{username}</strong></span>
          <button className="logout-btn" onClick={handleLogout}>Logout</button>
        </div>
      </div>

      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            <p><strong>{msg.sender === 'user' ? username : 'Bot'}</strong>: {msg.text}</p>
            {msg.image && <img src={msg.image} alt="product" className="product-image" />}
            <small>{msg.time}</small>
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Ask about a product..."
        />
        <button onClick={sendMessage}>➤</button>
      </div>
    </div>
  );
}

export default Chatbot;
