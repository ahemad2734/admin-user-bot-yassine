import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

BOT_TOKEN = os.getenv("BOT1_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("📄 الملف الشخصي", callback_data="profile")],
        [InlineKeyboardButton("✅ التحقق من الانتساب", callback_data="verify")],
        [InlineKeyboardButton("💎 السيرفرات المدفوعة", callback_data="servers")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("أهلا بك، اختر من القائمة:", reply_markup=reply_markup)

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user = query.from_user
    await query.answer()

    if query.data == "profile":
        await query.edit_message_text(f"👤 الاسم: {user.first_name}\n🆔 ID: {user.id}\n\n— Yassine MDV. Dev")
    elif query.data == "verify":
        chat_member = await context.bot.get_chat_member(CHANNEL_USERNAME, user.id)
        if chat_member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text("✅ تم التحقق من اشتراكك.\n\n— Yassine MDV. Dev")
        else:
            await query.edit_message_text("❌ المرجو الاشتراك في القناة أولاً.\n\n— Yassine MDV. Dev")
    elif query.data == "servers":
        with open("users_activated.txt", "r") as f:
            activated_ids = f.read().splitlines()
        if str(user.id) in activated_ids:
            servers = "\n".join([f"🔗 سيرفر {i+1}" for i in range(5)])
            await query.edit_message_text(f"{servers}\n\n— Yassine MDV. Dev")
        else:
            await query.edit_message_text("🚫 هذا القسم خاص بالمشتركين فقط.\n\n— Yassine MDV. Dev")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()