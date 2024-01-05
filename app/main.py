from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Restaurant, Review, Customer

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)

session = Session(engine)

restaurant = Restaurant(name="Test Restaurant", price=4)
customer = Customer(first_name="Test", last_name="User")

customer.add_review(restaurant, 5)

print(session.query(Review).first().full_review())

fanciest_restaurant = Restaurant.fanciest()
print(f"The fanciest restaurant is {fanciest_restaurant.name}")

print("\n".join(restaurant.all_reviews()))

print(f"{customer.full_name()}'s favorite restaurant is {customer.favorite_restaurant().name}")

customer.delete_reviews(restaurant)

print(session.query(Review).filter_by(customer=customer, restaurant=restaurant).count())  