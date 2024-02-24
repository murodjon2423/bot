from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database


db = Database(DB_NAME)



def make_product_kb():
    products = db.get_product()
    rows = []
    for product in products:
        # Assuming the first column contains the text for the button and the second column contains the callback data
        if len(product) >= 2:  # Check if the tuple has at least 2 elements
            text = str(product[0])  # Convert to string
            callback_data = product[1]  # Adjust the index according to your database structure
            rows.append([InlineKeyboardButton(text=text, callback_data=str(callback_data))])
    inl_kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return inl_kb


