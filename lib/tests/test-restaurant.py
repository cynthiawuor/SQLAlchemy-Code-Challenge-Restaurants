import unittest;
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from restaurant import Restaurant, Customer, Review;

class TestRestaurantReviews(unittest.TestCase):
    def setUp(self):
        # Create an SQLite database in memory for testing
        self.engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
        # Create the tables
        Restaurant.metadata.create_all(self.engine)
        Customer.metadata.create_all(self.engine)
        Review.metadata.create_all(self.engine)
        
        # Add sample data
        self.restaurant1 = Restaurant(name='Restaurant A', price=3)
        self.restaurant2 = Restaurant(name='Restaurant B', price=2)
        self.customer1 = Customer(first_name='John', last_name='Doe')
        self.customer2 = Customer(first_name='Jane', last_name='Smith')
        self.review1 = Review(rating=5, restaurant=self.restaurant1, customer=self.customer1)
        self.review2 = Review(rating=4, restaurant=self.restaurant2, customer=self.customer1)
        self.review3 = Review(rating=3, restaurant=self.restaurant1, customer=self.customer2)
        self.session.add_all([self.restaurant1, self.restaurant2, self.customer1, self.customer2, self.review1, self.review2, self.review3])
        self.session.commit()
    
    def tearDown(self):
        self.session.close()
    
    def test_customer_full_name(self):
        first_customer = self.session.query(Customer).first()
        self.assertEqual(first_customer.full_name(), 'John Doe')
    
    def test_customer_favorite_restaurant(self):
        first_customer = self.session.query(Customer).first()
        self.assertEqual(first_customer.favorite_restaurant(), self.restaurant1)
    
    def test_customer_add_review(self):
        new_restaurant = Restaurant(name='New Restaurant', price=4)
        self.session.add(new_restaurant)
        self.session.commit()
        
        first_customer = self.session.query(Customer).first()
        first_customer.add_review(new_restaurant, 4)
        
        new_review = self.session.query(Review).filter_by(customer_id=first_customer.id, restaurant_id=new_restaurant.id).first()
        self.assertIsNotNone(new_review)
        self.assertEqual(new_review.rating, 4)
    
    def test_customer_delete_reviews(self):
        first_customer = self.session.query(Customer).first()
        self.assertEqual(len(first_customer.reviews), 2)
        
        first_customer.delete_reviews(self.restaurant1)
        self.session.commit()
        
        self.assertEqual(len(first_customer.reviews), 1)
    
    def test_restaurant_fanciest(self):
        fanciest = Restaurant.fanciest(self.session)
        self.assertEqual(fanciest, self.restaurant1)
    
    def test_restaurant_all_reviews(self):
        reviews = self.restaurant1.all_reviews()
        expected_reviews = [
            f"Review for {self.restaurant1.name} by {self.customer1.full_name()}: 5 stars.",
            f"Review for {self.restaurant1.name} by {self.customer2.full_name()}: 3 stars.",
        ]
        self.assertEqual(reviews, expected_reviews)

if __name__ == '__main__':
    unittest.main()
