class Config:

    SECRET_KEY = 'secretkey123'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost:5432/taskmanager'

    SQLALCHEMY_TRACK_MODIFICATIONS = False