import uvicorn
from fastapi import FastAPI
from fastapi.websockets import WebSocket

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_json()

    if data.get('msg') == 'blah':
        await websocket.send_json({"msg": "No you blah"})
    else:
        await websocket.send_json({"msg": "Hello WebSocket"})

    await websocket.close()


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, log_level="info")