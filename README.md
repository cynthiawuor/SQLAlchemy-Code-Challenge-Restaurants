# SQLAlchemy-Code-Challenge-Restaurants
Phase 3 Code Challenge: Restaurants
 

For this assignment, we'll be working with a restaurant review domain. We have three models: `Restaurant`, `Review`, and `Customer`.
For our purposes, a Restaurant  has many `Review`s, a `Customer` has many `Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`. `Restaurant` - `Customer` is a many-to-many relationship.
**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.
 

Topics
- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying
Instructions
To get started, use this Pipfile to install all dependencies required for this project.
Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.
Note!  - You'll need to create your own test sample instances so that you can try/test out your code. Make sure your relationships and methods work in the console before submitting.
Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.
Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.
Before you submit! - Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.
 

Sample Schema:
`restaurants` Table:
| Column | Type    |
| --------- | -------  |
| name    | String   |
| price     | Intege  |
 

`customers` Table:
|Column     | Type   |
| ------------ | ------  |
| first_name | String |
| last_name  | String |
 

Deliverables
Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.
 

Remember:
SQLAlchemy gives your classes access to a lot of methods already! Keep in mind what methods SQLAlchemy gives you access to on each of your classes when you're approaching the deliverables below.
 

Object Relationship Methods
Use SQLAlchemy query methods where appropriate.
Review
- `Review customer()`
  - should return the `Customer` instance for this review
- `Review restaurant()`
  - should return the `Restaurant` instance for this review
 

Restaurant
- `Restaurant reviews()`
  - returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers()`
  - returns a collection of all the customers who reviewed the `Restaurant`
 

Customer
- `Customer reviews()`
  - should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`
  - should return a collection of all the restaurants that the `Customer` has reviewed
 

You can create a `debug.py` file and use it to check that these methods work before proceeding.
For example, you should be able to call `session.query(Customer).first().restaurants` and see a list of the restaurants for the first customer in the database based on your seed data; and `session.query(Review).first().customer` should return the customer for the first review in the database.
 

Aggregate and Relationship Methods
Customer
- `Customer full_name()`
  - returns the full name of the customer, with the first name and the last name concatenated Western style.
- `Customer favorite_restaurant()`
  - returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and a rating creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`
  - takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant
Review
- `Review full_review()`
  - should return a string formatted as follows:
        - Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
Restaurant
- `Restaurant fanciest(), this method should be a class method`
  - returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`
  - should return a list of strings with all the reviews for this restaurant formatted as follows:
-------------------------------------------------------------------------------------------------------------------------
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
  "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
]
Project Submission
Once you have completed the project;

Create a new project folder.
Create a new GitHub repository (NB: ENSURE IT IS PRIVATE).
Add your TM as a contributor to the project. (This is only for grading purposes.)
Please make sure you regularly commit to the repository.
