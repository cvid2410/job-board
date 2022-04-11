from datetime import datetime
from app import db

class Job(db.Model):
    __tablename__ = "jobs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50))
    remote = db.Column(db.Boolean, default=False, nullable=False)
    available = db.Column(db.Boolean, default=True, nullable=False)
    salary = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.title}"