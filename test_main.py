import pytest

from run import app

def test_main():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_profiles_register():
    response = app.test_client().get('/profiles/register')
    assert response.status_code == 200

def test_profiles_login():
    response = app.test_client().get('/profiles/login')
    assert response.status_code == 200

def test_profiles_logout():
    response = app.test_client().get('/profiles/logout')
    assert response.status_code == 302

