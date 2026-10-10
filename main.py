from fastapi import FastAPI

app = FastAPI()

@app.get("/pricing/{price}")
def pricing(price: float):

    discounted_price = price * 0.9

    return {
        "original": price,
        "discounted": discounted_price
    }
