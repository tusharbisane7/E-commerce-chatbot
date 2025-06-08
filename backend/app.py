from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import jwt, datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(300))
    description = db.Column(db.String(300))

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if not all([name, email, username, password]):
        return jsonify({'error': 'Missing required fields'}), 400

    if username in users:  # 'users' is your in-memory dict
        return jsonify({'error': 'Username already exists'}), 400

    users[username] = {
        'name': name,
        'email': email,
        'password': password
    }

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password required"), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify(token=token)

    return jsonify(message="Invalid credentials"), 401

@app.route('/seed-products', methods=['POST'])
def seed_products():
    products = [
        Product(name="Phone Model X", category="Electronics", price=699.99, image="https://example.com/image1.jpg", description="Latest smartphone."),
        Product(name="Gaming Laptop", category="Electronics", price=1299.99, image="https://example.com/image2.jpg", description="High performance laptop."),
        Product(name="Coffee Mug", category="Kitchenware", price=12.99, image="https://example.com/image3.jpg", description="Ceramic mug for coffee lovers."),
    ]
    db.session.bulk_save_objects(products)
    db.session.commit()
    return jsonify(message="Products seeded"), 201


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = [{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price,
        'image': p.image,
        'description': p.description
    } for p in products]
    return jsonify(products=output)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
