from app import app, db, Product

def insert_custom_products():
    with app.app_context():
        db.create_all()

        # List of custom products to insert
        products = [
            Product(
                name="Boat Rockerz 255",
                category="Electronics",
                price=1499.00,
                image="https://via.placeholder.com/150?text=Boat+Rockerz+255",
                description="Wireless Bluetooth headset with deep bass and fast charging."
            ),
            Product(
                name="Realme Buds Wireless",
                category="Electronics",
                price=1999.00,
                image="https://via.placeholder.com/150?text=Realme+Buds",
                description="Lightweight wireless earbuds with magnetic connection."
            ),
            Product(
                name="Slim Fit Cotton Shirt",
                category="Apparel",
                price=1299.00,
                image="https://via.placeholder.com/150?text=Cotton+Shirt",
                description="Premium slim-fit shirt made of 100% cotton, available in multiple colors."
            ),
            Product(
                name="Fiction Book - The Lost Symbol",
                category="Books",
                price=499.00,
                image="https://via.placeholder.com/150?text=Lost+Symbol",
                description="A mystery thriller novel by Dan Brown featuring Robert Langdon."
            ),
            Product(
                name="Laptop Stand Adjustable",
                category="Accessories",
                price=899.00,
                image="https://via.placeholder.com/150?text=Laptop+Stand",
                description="Ergonomic stand for laptops with adjustable height and angle."
            )
        ]

        db.session.bulk_save_objects(products)
        db.session.commit()
        print("✅ Custom products inserted successfully!")

if __name__ == '__main__':
    insert_custom_products()
