from database import Base, engine

# Create all tables based on model definitions
Base.metadata.create_all(engine)

print("Tables created successfully!")
