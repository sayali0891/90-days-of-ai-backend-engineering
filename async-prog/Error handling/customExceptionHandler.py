
class CustomExceptionHandler(Exception):
    """Base exception class for our app"""
    pass

class ItemNotFoundError(CustomExceptionHandler):
    def __init__(self, item_id: str):
        self.item_id = item_id
        self.message = f"Item {item_id} does not exist."
