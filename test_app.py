from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket_sends_default_response():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({})
        data = websocket.receive_json()

        assert data == {"msg": "Hello WebSocket"}


def test_websocket_receives_message_and_forms_response():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({"msg": 'blah'})
        message = websocket.receive_json()

        assert message == {"msg": "No you blah"}
