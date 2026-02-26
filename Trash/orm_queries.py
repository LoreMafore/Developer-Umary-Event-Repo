from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Learning SQLAlchemy ORM
# Query syntax is confusing

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100))
    # posts = relationship('Post', back_populates='author')  # causes circular import?
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    # author = relationship('User', back_populates='posts')

# Database setup
# TODO: use environment variable for database URL
engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(username, email):
    """Add a new user"""
    user = User(username=username, email=email)
    session.add(user)
    # session.commit()  # forgot to commit
    return user

def get_user_by_username(username):
    """Get user by username"""
    # TODO: is this the right way to query?
    user = session.query(User).filter_by(username=username).first()
    # Or should I use: session.query(User).filter(User.username == username).first()
    return user

def update_user_email(username, new_email):
    """Update user email"""
    user = get_user_by_username(username)
    if user:
        user.email = new_email
        session.commit()
    # TODO: handle case when user doesn't exist

# TODO: implement delete function
# def delete_user(username):
#     

# TODO: implement complex queries with joins
# Getting lost in the documentation

# TODO: add error handling for database operations
# TODO: add transaction management

if __name__ == "__main__":
    # Test queries
    # add_user("john_doe", "john@example.com")
    # user = get_user_by_username("john_doe")
    # print(user)
    
    # session.close()  # should I close the session?
    pass
