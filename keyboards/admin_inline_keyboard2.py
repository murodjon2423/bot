from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.database import Database
from aiogram.types import Message
from config import DB_NAME

db = Database(DB_NAME)

async def make_product_messages():
    products = db.get_product()
    messages = []
    for product in products:
        if len(product) >= 2:
            text = str(product[0])
            callback_data = product[1]
            message = f"Product: {text}\nCallback Data: {callback_data}"
            messages.append(message)
    return messages
