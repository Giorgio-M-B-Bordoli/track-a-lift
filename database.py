from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Interval
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'user_info'

    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)

    workouts = relationship('WorkoutInfo', back_populates='user')

class WorkoutInfo(Base):
    __tablename__ = 'workout_info'

    workout_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_info.user_id'))
    workout_time = Column(String, nullable=False)
    workout_type = Column(String(255), nullable=False)

    user = relationship('UserInfo', back_populates='workouts')
    exercises = relationship('Exercises', back_populates='workout')

class Exercises(Base):
    __tablename__ = 'exercises'

    exercise_id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workout_info.workout_id'))
    name = Column(String(255), nullable=False)
    weight = Column(Float)
    reps = Column(Integer)
    time = Column(Interval)

    workout = relationship('WorkoutInfo', back_populates='exercises')

# Configuration to your PostgreSQL
DATABASE_URL = "postgresql://postgres:#y_yU6U-PU3XT&vJ@localhost:5432/track_a_lift"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Create tables in the database (This is usually done once)
Base.metadata.create_all(engine)

# Function to add a new user
def add_user(email):
    session = Session()
    new_user = UserInfo(email=email)
    session.add(new_user)
    session.commit()
    session.close()

# Function to add a new workout
def add_workout(user_id, workout_time, workout_type):
    session = Session()
    new_workout = WorkoutInfo(user_id=user_id, workout_time=workout_time, workout_type=workout_type)
    session.add(new_workout)
    session.commit()
    session.close()

# Function to add a new exercise
def add_exercise(workout_id, name, weight, reps, time):
    session = Session()
    new_exercise = Exercises(workout_id=workout_id, name=name, weight=weight, reps=reps, time=time)
    session.add(new_exercise)
    session.commit()
    session.close() 

# Example usage
if __name__ == '__main__':
    add_user('user@example.com')
    add_workout(1, '2024-04-17T12:00:00', 'Cardio')
    add_exercise(1, 'Running', None, 0, '00:30:00')