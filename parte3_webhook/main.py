from fastapi import FastAPI

webhook_logs = []

app = FastAPI()
app.title = "Bayma Notification Center"

@app.post("/webhook")
def receive_data(event:str, message:str, timestamp:str):
    webhook_logs.append({
        "evento": event,
        "mensaje": message,
        "timestamp": timestamp
    })

    return {
        "status": "ok",
        "recibido": webhook_logs[-1]
    }