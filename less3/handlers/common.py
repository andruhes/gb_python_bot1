from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.utils.random_fox import fox
from less3.keyboards.keyboards import kb1, kb2
from random import randint


router = Router()



@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f'Привет, {name}', reply_markup=kb1)


@router.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer(f'УРАААА!', reply_markup=kb1)



@router.message(Command("fox"))
@router.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    await message.answer(f'{image_fox}')
    # await bot.send_photo(message.chat.id, image_fox)
    # await message.answer(f"{image_fox}")


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1,10)
    await message.answer(f"{number}")





@router.message(Command('stop'))
@router.message(Command('Стоп'))
@router.message(F.text.lower() == 'стоп')
@router.message(F.text.lower() == 'пока')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока-пока, {name}')

# Хэндлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет, - {name}')
    elif 'инфо' in msg_user:
        await message.answer(f'Я бот и мне очень хочется показать тебе лису, - {name}')
    elif 'закрыть' in msg_user:
        await message.answer(f'Не хочу закрываться, лучше попроси показать тебе лису')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот Андрея Маркушева')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, - {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

