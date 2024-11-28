from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the database path (adjust as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your database models here
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(4), nullable=False)

# Ensure the app runs properly
if __name__ == "__main__":
    # Fix: Create database tables within the app context
    with app.app_context():
        db.create_all()  # Ensures tables are created

    # Run the Flask app
    app.run(debug=True)
