from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Bot Token
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

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
        /jobs -> 2025 Job Search
        /games -> Play Online Games
        /articles -> Research Articles
        /contact -> Contact information
        """
    )

async def content(update: Update, context: CallbackContext):
    await update.message.reply_text("We have various playlists and articles available.")

async def python(update: Update, context: CallbackContext):
    await update.message.reply_text("Python Tutorial: https://youtu.be/DInMru2Eq6E")

async def sql(update: Update, context: CallbackContext):
    await update.message.reply_text("SQL Tutorial: https://youtu.be/_yXZvGH2MgA")

async def java(update: Update, context: CallbackContext):
    await update.message.reply_text("Java Tutorial: https://youtu.be/yRpLlJmRo2w")

async def jobs(update: Update, context: CallbackContext):
    await update.message.reply_text("2025 Job Search: https://youtu.be/pzHxBMOsrq8")

async def games(update: Update, context: CallbackContext):
    await update.message.reply_text("Play Online Games: https://www.msn.com/en-us/play")

async def articles(update: Update, context: CallbackContext):
    await update.message.reply_text("Research Articles: https://www.nature.com/nature/articles?type=news-&year=2025")

async def contact(update: Update, context: CallbackContext):
    await update.message.reply_text("Contact us via email on our website.")

# Main function
def main():
    try:
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

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
