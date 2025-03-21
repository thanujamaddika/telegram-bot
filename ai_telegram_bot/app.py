from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Bot Token
TOKEN = "7856501291:AAHyboXvRRvYwBXuS3RKj6bTQR2QrpxE6yM"

# Command Handlers
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Welcome to ai_telegram_bot")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This message
        /content -> About various playlists
        /python -> Python tutorial link
        /sql -> SQL tutorial link
        /java -> Java tutorial link
        /jobs -> 2025 jobs to search
        /games -> online games to pass time
        /articles  -> research of nature
        /contact -> Contact information
        """
    )

async def content(update: Update, context: CallbackContext):
    await update.message.reply_text("We have various playlists and articles available")

async def python(update: Update, context: CallbackContext):
    await update.message.reply_text("Tutorial link: https://youtu.be/DInMru2Eq6E?si=xy6j-8eH5NlRKRIs")

async def sql(update: Update, context: CallbackContext):
    await update.message.reply_text("Tutorial link: https://youtu.be/_yXZvGH2MgA?si=D9qHvR0LOLyFu6yo")

async def java(update: Update, context: CallbackContext):
    await update.message.reply_text("Tutorial link: https://youtu.be/yRpLlJmRo2w?si=fi8I2Qoja4ovHM6i")

async def jobs(update: Update, context: CallbackContext):
    await update.message.reply_text("Click here to search for jobs: [2025 Job Search](https://youtu.be/pzHxBMOsrq8?si=jLlrc8-PtCx2NGbi)", parse_mode="Markdown")


async def games(update: Update, context: CallbackContext):
    await update.message.reply_text("Play online games here: [Click to Play](https://www.msn.com/en-us/play)", parse_mode="Markdown")


async def articles(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Read research articles here: [Nature Articles](https://www.nature.com/nature/articles?type=news-&year=2025)", 
        parse_mode="Markdown"
    )


async def contact(update: Update, context: CallbackContext):
    await update.message.reply_text("You can contact us via the email provided on our website.")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("content", content))
    app.add_handler(CommandHandler("python", python))
    app.add_handler(CommandHandler("sql", sql))
    app.add_handler(CommandHandler("java", java))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("games", games))
    app.add_handler(CommandHandler("articles", articles))
    app.add_handler(CommandHandler("contact", contact))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()