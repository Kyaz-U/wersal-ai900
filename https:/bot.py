import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from predict_model import predict_next_value

# Admin ID (faqat siz ko'rasiz)
ADMIN_ID = 92058415
user_stats = {}

# Menyu
menu = ReplyKeyboardMarkup(
    keyboard=[
        ["🔮 Signal olish"],
        ["📊 Statistika"],
        ["⚙️ Sozlamalar"]
    ],
    resize_keyboard=True
)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Wersal AI botga xush kelibsiz.\nKerakli bo'limni tanlang:",
        reply_markup=menu
    )

# Foydalanuvchi xabariga javob
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    # Statistika
    if user_id in user_stats:
        user_stats[user_id] += 1
    else:
        user_stats[user_id] = 1

    if text == "🔮 Signal olish":
        recent_data = [1.59, 1.58, 1.32, 63.96, 6.89, 1.56, 4.48, 2.20, 2.14, 17.47]  # test ma'lumot
        result = predict_next_value("ai_models/aviator_1win.pkl", recent_data)
        await update.message.reply_text(f"AI bashorati: {result}x")

    elif text == "📊 Statistika":
        if user_id == ADMIN_ID:
            msg = "Foydalanuvchi statistikasi:\n"
            for uid, count in user_stats.items():
                msg += f"ID: {uid} — {count} ta signal\n"
            await update.message.reply_text(msg)
        else:
            await update.message.reply_text("Bu bo‘lim faqat admin uchun.")

    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("Sozlamalar tez orada yangilanadi.")

    else:
        await update.message.reply_text("Iltimos, menyudagi tugmalardan birini tanlang.")

# Ishga tushirish
if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
