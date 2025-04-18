from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, Enum, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from databases.database import Base



class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    total_amount = Column(Float, default=0)
    order_date = Column(DateTime(timezone=True), server_default=func.now())

    
    # Define relationships
    customer = relationship("Customer", back_populates="orders") 
    order_medicines = relationship("OrderMedicine", back_populates="order")
    invoice = relationship("Invoice", back_populates="order", uselist=False) #invoice is created so  it can be linked to the order



class OrderMedicine(Base):
    __tablename__ = "order_medicines"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    quantity = Column(Integer, default=1)
    unit_price = Column(Float)
    
    # Define relationships
    order = relationship("Order", back_populates="order_medicines")
    medicine = relationship("Medicine", back_populates="order_medicines")