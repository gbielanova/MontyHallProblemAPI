from flask import Flask
from handlers import routes

app = Flask(__name__)

routes.configure_routes(app)

if __name__ == '__main__':
    app.run()
