"""
запуск бота
"""
import os
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv

from game_state import GameState

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(bot=bot)
router = Router()
gamest = GameState()

# @router.message(Command("start"))
# async def start_handler(message: Message):
#     """приветствие"""
#     fname = message.from_user.full_name
#     await message.answer(
#         f"Привет, {fname}!"
#     )

@router.callback_query(F.data == "btn_1")
async def handle_btn1(callback: CallbackQuery):
    await callback.message.answer_dice(emoji="🎲")
    await asyncio.sleep(3)
    locname, locdesc = gamest.update_world()
    await callback.answer("Обновлена локация")
    await callback.message.answer(f"{locname} — {locdesc}")
    await main_mess(callback.message)

@router.callback_query(F.data == "btn_2")
async def handle_btn2(callback: CallbackQuery):
    await callback.message.answer_dice(emoji="🎲")
    await asyncio.sleep(3)
    questn, questdesc = gamest.update_quest()
    await callback.answer("Обновлён квест")
    await callback.message.answer(f"{questn}: {questdesc}")
    await main_mess(callback.message)

@router.callback_query(F.data == "btn_3")
async def handle_btn3(callback: CallbackQuery):
    await callback.message.answer_dice(emoji="🎲")
    await asyncio.sleep(3)
    itemname, itemeffect = gamest.update_item()
    await callback.answer("Обновлён предмет")
    await callback.message.answer(f"{itemname} — {itemeffect}")
    await main_mess(callback.message)

@router.callback_query(F.data == "btn_4")
async def handle_btn4(callback: CallbackQuery):
    await callback.message.answer_dice(emoji="🎲")
    await asyncio.sleep(3)
    ename, ehp, edmg = gamest.update_enemy()
    await callback.answer("Обновлён враг")
    await callback.message.answer(f"{ename} — HP: {ehp}, DMG: {edmg}")
    await main_mess(callback.message)

@router.message(Command("start"))
async def gen_output(message: Message):
    """обработка всех остальных сообщений"""
    await main_mess(message)

async def main_mess(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Локация", callback_data="btn_1"),
        InlineKeyboardButton(text="Квест", callback_data="btn_2"),
    )
    builder.row(
        InlineKeyboardButton(text="Предмет", callback_data="btn_3"),
        InlineKeyboardButton(text="Враг", callback_data="btn_4"),
    )

    text = (
        "🧪 Это тестовая генерация объектов игры. "
        "Вы можете попробовать сгенерировать разные игровые элементы "
        "— локации, квесты, предметы и врагов. "
        "Просто нажмите на соответствующую кнопку ниже, чтобы увидеть результат."
    )

    await message.answer(text, reply_markup=builder.as_markup())


async def main():
    """запуск бота"""
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
