import pytest

from src.app import create_app


@pytest.fixture()
def app(request):
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    
    client = app.test_client()
    
    request.cls.app = app
    request.cls.client = client