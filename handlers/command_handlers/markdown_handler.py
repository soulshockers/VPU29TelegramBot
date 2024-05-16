from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from handlers.base_handler import BaseHandler


class MarkdownHandler(BaseHandler):
    @classmethod
    def register(cls, app):
        app.add_handler(CommandHandler('markdown', cls.callback))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = (
            "Welcome to Markdown 2 Showcase Bot\!\n\n"
           "You can use markdown syntax to format your messages\. Here are some examples:\n\n"
           "*Bold Text*: **bold**\n"
           "_Italic Text_: _italic_\n"
           "[Inline URL](https://www\.example\.com)\n"
           "[Inline mention of a user](tg://user?id=6570732383)\n"
           "`Inline fixed-width code`\n"
           "```Multi-line\nfixed-width\ncode block```\n"
           "```python\nprint('Hello, world!')```\n"
           "* Unordered list item 1\n"
           "* Unordered list item 2\n"
           "1\. Ordered list item 1\n"
           "2\. Ordered list item 2\n"
           "> Blockquotes are very handy in email to emulate reply text\.\n"
           ">> This line is part of the same quote\.\n"
           ">>> And this is another quote\.\n"
           "For more information, refer to the [Markdown Documentation](https://core\.telegram\.org/bots/api#markdownv2-style)"
           )

        message = (
            "*bold text* \n"
            "_italic text_ \n"
            "__underline__ \n"
            "~strikethrough~ \n"
            "||spoiler|| \n"
            "*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold* \n"
            "[inline URL](http://www.example.com/) \n"
            "[inline mention of a user](tg://user?id=6570732383) \n"
            "![👍](tg://emoji?id=5368324170671202286) \n"
            "`inline fixed-width code` \n"
            "``` \n"
            "pre-formatted fixed-width code block \n"
            "``` \n"
            "```python \n"
            "# pre-formatted fixed-width code block written in the Python programming language \n"
            "print('Hello, world!') \n"
            "``` \n"
            ">Block quotation started \n"
            ">Block quotation continued \n"
            ">The last line of the block quotation \n\n"
            ">The second block quotation started right after the previous \n"
            ">The third block quotation started right after the previous"
        )
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN_V2)
