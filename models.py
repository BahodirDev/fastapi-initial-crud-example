from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), unique=True)
    password = Column(String)  # Consider using a secure hashing mechanism
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User {self.username}>"


# class Order(Base):
#     ORDER_STATUSES = (
#         ('PENDING', 'pending'),
#         ('IN_TRANSIT', 'in_transit'),
#         ('DELIVERED', 'delivered'),
#     )
#     __tablename__ = 'order'
#     id = Column(Integer, primary_key=True)
#     quantity = Column(Integer, nullable=False)
#     order_statuses = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship("User", back_populates="order")
#     product_id = Column(Integer, ForeignKey('product.id'))
#     product = relationship('Product', back_populates='order')

#     def __repr__(self):
#         return f"<Order {self.id}>"

# class Product(Base):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     price = Column(Integer)
#     orders = relationship("Order", back_populates='product')

#     def __repr__(self):
#         return f"<Product {self.name}>"
