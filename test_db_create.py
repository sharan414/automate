from app import create_app, db
from app.models import User, Vehicle, Maintenance

app = create_app()

with app.app_context():
    print("📡 Connecting to MySQL database...")
    db.create_all()
    print("✅ Tables created successfully.")
