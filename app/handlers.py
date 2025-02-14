from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.states as st

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=kb.main)
    await message.reply('How are you?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('This is help')


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Choose an item category', reply_markup=kb.catalog)


@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('You have chosen some category', show_alert=True)
    await callback.message.answer('You have chosen t-shirts')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(st.Register.name)
    await message.answer('Enter your name')

@router.message(st.Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(st.Register.age)
    await message.answer('Enter your age')

@router.message(st.Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(st.Register.phone_number)
    await message.answer('Enter your phone number', reply_markup=kb.get_number)


@router.message(st.Register.phone_number, F.contact)
async def register_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Your name: {data["name"]}\nYour age: {data["age"]}\nYour phone number: {data["phone_number"]}')
    await state.clear()