from core.database import Base, engine
from models.user import User
from models.situation import Situation

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
