from aiogram.types import BotCommand
from aiogram.filters import Command

admin_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='categories', description='All categories list'),
    BotCommand(command='add_category', description='Add a new category'),
    BotCommand(command='edit_category', description='Update any category'),
    BotCommand(command='add_product', description='Start/restart bot'),
    BotCommand(command='edit_product', description='All categories list'),
    BotCommand(command='dell_product', description='Add a new category'),
    BotCommand(command='product', description='Update any category')
]

user_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='help', description='Manual for using bot'),
]