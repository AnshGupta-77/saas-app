from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

subscriptions = []
id_counter = 1


@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}


@app.get("/subscriptions")
def get_subscriptions():
    return subscriptions


@app.post("/subscriptions")
def add_subscription(sub: dict):
    global id_counter
    sub["id"] = id_counter
    id_counter += 1
    subscriptions.append(sub)
    return sub