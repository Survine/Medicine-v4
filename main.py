from fastapi import FastAPI
from databases.database import Base, engine
from Routes import medicine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(medicine.router, prefix="/medicines", tags=["Medicine"])