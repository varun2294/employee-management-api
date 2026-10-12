from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


import os
from dotenv import load_dotenv

# Load the variables from the hidden .env file
load_dotenv()

# Safely fetch the URL without exposing it in the code
empDBURL = os.getenv("DATABASE_URL")

# (Optional check) Ensure the variable loaded correctly
if not empDBURL:
    raise ValueError("DATABASE_URL is missing from the .env file!")



engine = create_engine(empDBURL)
sessionLocal = sessionmaker(autoflush=False,bind=engine)

## Create the Declarative Base Class
# CRUCIAL ADDITION: Every database model you write (e.g., Employee) must inherit from this Base

Base = declarative_base()


# 5. Add a Database Session Lifecycle Helper (Dependency)
# CRUCIAL ADDITION: Ensures database connections are automatically closed after a request finishes,
# preventing memory leaks or hung connections in your app.

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()    


