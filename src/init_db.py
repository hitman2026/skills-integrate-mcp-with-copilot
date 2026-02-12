from sqlalchemy.orm import Session
from src.db import Base, Activity
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./activities.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

def seed_activities():
    from src.db import Participant
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    if db.query(Activity).count() == 0:
        activities = [
            Activity(name="Chess Club", description="Learn strategies and compete in chess tournaments", schedule="Fridays, 3:30 PM - 5:00 PM", max_participants=12),
            Activity(name="Programming Class", description="Learn programming fundamentals and build software projects", schedule="Tuesdays and Thursdays, 3:30 PM - 4:30 PM", max_participants=20),
            Activity(name="Gym Class", description="Physical education and sports activities", schedule="Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM", max_participants=30),
            Activity(name="Soccer Team", description="Join the school soccer team and compete in matches", schedule="Tuesdays and Thursdays, 4:00 PM - 5:30 PM", max_participants=22),
            Activity(name="Basketball Team", description="Practice and play basketball with the school team", schedule="Wednesdays and Fridays, 3:30 PM - 5:00 PM", max_participants=15),
            Activity(name="Art Club", description="Explore your creativity through painting and drawing", schedule="Thursdays, 3:30 PM - 5:00 PM", max_participants=15),
            Activity(name="Drama Club", description="Act, direct, and produce plays and performances", schedule="Mondays and Wednesdays, 4:00 PM - 5:30 PM", max_participants=20),
            Activity(name="Math Club", description="Solve challenging problems and participate in math competitions", schedule="Tuesdays, 3:30 PM - 4:30 PM", max_participants=10),
            Activity(name="Debate Team", description="Develop public speaking and argumentation skills", schedule="Fridays, 4:00 PM - 5:30 PM", max_participants=12)
        ]
        db.add_all(activities)
        db.commit()
    db.close()

if __name__ == "__main__":
    seed_activities()
