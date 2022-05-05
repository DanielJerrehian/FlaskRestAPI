from flask import Blueprint, request


store = Blueprint("main", __name__)

stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My Item",
                "price": 15.99
            }
        ]
    }
]

@store.post("/store")
def create_store():
    data = request.get_json()
    new_store = {
        "name": data["name"],
        "items": []
    }
    stores.append(new_store)
    return {"newStore": new_store}, 200


@store.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store}, 200
    return {"message": "Store not found"}, 404


@store.get("/stores")
def get_all_stores():
    return {"stores": stores}, 200


@store.post("/store/<string:name>/item")
def add_item_to_store(name):
    data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": data["name"],
                "price": data["price"]
            }
            store["items"].append(new_item)   
            return {"store": store}, 200
    return {"message": "Store not found"}, 404


@store.get("/store/<string:name>/items")
def get_items_from_store(name):
    for store in stores:
        if store["name"] == name:
            return {"storeItems": store["items"]}, 200
    return {"message": "Store not found"}, 404