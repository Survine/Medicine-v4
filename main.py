from fastapi import FastAPI
from databases.database import Base, engine
from Routes import medicine,order,customer

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(medicine.router, prefix="/medicines", tags=["Medicine"])
app.include_router(order.router, prefix="/orders", tags=["Order"])
app.include_router(customer.router, prefix="/customers", tags=["Customer"])