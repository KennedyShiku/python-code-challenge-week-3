# Deliverables
Write the following methods in the classes. Feel free to build out any helper methods if needed.

**Remember:** SQLAlchemy gives your classes access to a lot of methods already! Keep in mind what methods SQLAlchemy gives you access to on each of your classes when you're approaching the deliverables below.

## Migrations
Before working on the rest of the deliverables, you will need to create a migration for all tables.

- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to a  `Customer`. In your migration, create any columns your `reviews` table will need to establish these relationships.

  The `reviews` table should also have:
  - A `star_rating` column that stores an integer.

After creating the `reviews` table using a migration, use the `seeds.py` file to create instances of all your classes so you can test your code.

**Once you've set up your tables**, work on building out the following deliverables.

## Object Relationship Methods
Use SQLAlchemy query methods where appropriate.

### Review
- `Review customer()`
  - should return the `Customer` instance for this review
- `Review restaurant()`
  - should return the `Restaurant` instance for this review

### Restaurant
- `Restaurant reviews()`
  - returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers()`
  - returns a collection of all the customers who reviewed the `Restaurant`

### Customer
- `Customer reviews()`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`
  - should return a collection of all the restaurants that the `Customer` has reviewed

Check that these methods work before proceeding. For example, you should be able to call `session.query(Customer).first().restaurants` and see a list of the restaurants for the first customer in the database based on your seed data; and `session.query(Review).first().customer` should return the customer for the first review in the database.

## Aggregate and Relationship Methods

### Customer
- `Customer full_name()`
  - returns the full name of the customer, with the first name and the last name concatenated, Western style.
- `Customer favorite_restaurant()`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and a rating
  - creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and
  - removes **all** their reviews for this restaurant
  - you will have to delete rows from the `reviews` table to get this to work!

### Review
- `Review full_review()`
  - should return a string formatted as follows:
  Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

### Restaurant
- `Restaurant fanciest(), this method should be a class method`
  - returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`
  - should return a list of strings with all the reviews for this restaurant formatted as follows:
  [
    "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
    "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
  ]
