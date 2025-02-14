from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                     [KeyboardButton(text='Cart')],
                                     [KeyboardButton(text='Contacts'),
                                      KeyboardButton(text='About us')]],
                           resize_keyboard=True,
                           input_field_placeholder='Select command from menu')

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='T-shirts', callback_data='t-shirt')],
                                                [InlineKeyboardButton(text='Sneakers', callback_data='sneakers')],
                                                [InlineKeyboardButton(text='Cap', callback_data='cap')]
                                                ]
                               )

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Send my phone number', request_contact=True)]
                                           ],
                                 resize_keyboard=True
                                 )