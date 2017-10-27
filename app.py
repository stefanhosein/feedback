#!/usr/bin/env python3
from src import app
from src.routes import feedback


if __name__ == '__main__':
    # resigter the feedback blueprint
    app.register_blueprint(feedback, url_prefix='/checker')
    app.run(port=8080)
