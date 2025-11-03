# Import the SQLAlchemy class from the Flask extension 'flask_sqlalchemy'
# This is a Flask-friendly wrapper around the SQLAlchemy ORM (Object Relational Mapper),
# which helps us interact with databases using Python objects instead of raw SQL queries.

from flask_sqlalchemy import SQLAlchemy
# Create a single global instance of SQLAlchemy.
# This 'db' object will be used throughout the app to define models and handle database operations.
# Think of it as the bridge between your Flask app and your database.

db = SQLAlchemy()
# Define a helper function to initialize the database.
# This function will be called from your main Flask application (usually in app.py).

def init_db(app):
  """
    This function takes the Flask app instance as an argument,
    connects it with the SQLAlchemy database instance,
    and ensures that all the database tables (defined in your models)
    are created.
    """
  # Step 1: Link (bind) the Flask application instance with the SQLAlchemy object.
    # This tells SQLAlchemy to use the database configuration (like URI, options, etc.)
    # that is stored in the Flask app's config dictionary.
  
    db.init_app(app)
    with app.app_context():
      # Step 3: Create all the tables in the database.
        # SQLAlchemy looks at all classes that inherit from db.Model (your models)
        # and creates the corresponding tables in the database, if they don't already exist.
      
    db.create_all()
      # Note: This function doesn't drop existing tables; it only creates missing ones.
      # So it's safe to run it every time your app starts.
