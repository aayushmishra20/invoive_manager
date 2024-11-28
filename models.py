from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    invoice_no = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
