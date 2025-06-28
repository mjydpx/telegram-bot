from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"🎥 File ID:\n{file_id}")
    else:
        await update.message.reply_text("دریافت ویدۀو")

app = ApplicationBuilder().token("7731333232:AAFB_jjKo3tQdpEmnw8JlbAROxJprPKhpLw").build()
app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
app.run_polling()
