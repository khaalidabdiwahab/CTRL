import requests

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update, Bot
from telegram.ext import run_async

@run_async
def paste(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text

    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]

    else:
        message.reply_text("What am I supposed to do with this?")
        return

    key = requests.post(
        'https://nekobin.com/api/documents', json={
            "content": data
        }).json().get('result').get('key')

    url = f'https://nekobin.com/{key}'

    reply_text = f'Nekofied to *Nekobin* : {url}'

    message.reply_text(
        reply_text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True)


__help__ = """
 - /paste: Paste on [Nekobin](https://nekobin.com)
"""

__mod_name__ = "Paste"

PASTE_HANDLER = DisableAbleCommandHandler("paste", paste, pass_args=True)

dispatcher.add_handler(PASTE_HANDLER)
