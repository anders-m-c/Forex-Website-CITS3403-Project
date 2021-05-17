from app import app
from app.models import User, Quiz, Question, Image

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Quiz': Quiz, 'Question': Question, 'Image': Image}