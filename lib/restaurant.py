from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite database in memory
engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

review1 = Review(rating=5, restaurant=restaurant1, customer=customer1)
review2 = Review(rating=4, restaurant=restaurant2, customer=customer1)
review3 = Review(rating=3, restaurant=restaurant1, customer=customer2)

# Add data to the session and commit to the database
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()

# Query and test the relationships
first_customer = session.query(Customer).first()
print(f"Customer's Full Name: {first_customer.first_name} {first_customer.last_name}")
print(f"Customer's Reviews:")
for review in first_customer.reviews:
    print(f"- Review for {review.restaurant.name}: {review.rating} stars")

restaurant_with_highest_price = session.query(Restaurant).order_by(Restaurant.price.desc()).first()
print(f"\nFanciest Restaurant: {restaurant_with_highest_price.name}")

restaurant_reviews = restaurant_with_highest_price.reviews
print(f"\nReviews for {restaurant_with_highest_price.name}:")
for review in restaurant_reviews:
    print(f"- Review by {review.customer.first_name}: {review.rating} stars")
