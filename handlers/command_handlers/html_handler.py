from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from handlers.base_handler import BaseHandler


class HtmlHandler(BaseHandler):
    @classmethod
    def register(cls, app):
        app.add_handler(CommandHandler('html', cls.callback))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = (
            "Paragraph text here \n"
            "<a href=\"https://vpu29.lviv.ua/\">Сайт Вищого Професійного Училища</a> \n"
            "<b>Hello World bold!</b> \n"
            "<i>Hello World italic!</i> \n"
            "<u>Hello World underline!</u>"
            "<pre><code class=\"language-python\">print(\"Hello world!\")</code></pre>"
        )
        await update.message.reply_text(message, parse_mode=ParseMode.HTML)
