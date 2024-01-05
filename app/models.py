from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self, session):
        reviews = session.query(Review).filter_by(restaurant=self).all()
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars." for review in reviews]

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')

    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='reviews')

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        reviews = session.query(Review).filter_by(customer=self).order_by(Review.star_rating.desc()).first()
        return reviews.restaurant if reviews else None

    def add_review(self, restaurant, rating, session):
        review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        session.add(review)
        session.commit()

    def delete_reviews(self, restaurant, session):
        session.query(Review).filter_by(customer=self, restaurant=restaurant).delete()
        session.commit()