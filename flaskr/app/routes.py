from app import app


def configure_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return "Hello, World!"
