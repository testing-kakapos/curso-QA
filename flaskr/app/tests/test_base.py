from flask import Flask
import json
from .. import routes


def test_base():
    app = Flask(__name__)
    routes.configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, World!'
    assert response.status_code == 200
