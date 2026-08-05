from app import app

def test_home_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome to Calculator App!" in response.data

        print(response.data.decode())  # Print the response data for debugging