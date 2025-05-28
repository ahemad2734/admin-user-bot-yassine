import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT2_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def activate(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("🚫 ليس لديك صلاحية التفعيل.")
        return

    if not context.args:
        await update.message.reply_text("❗ أرسل ID المستخدم بعد الأمر.")
        return

    user_id = context.args[0]
    with open("users_activated.txt", "a") as f:
        f.write(user_id + "\n")
    await update.message.reply_text(f"✅ تم تفعيل المستخدم {user_id}.\n\n— Yassine MDV. Dev")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("activate", activate))
    app.run_polling()

if __name__ == "__main__":
    main()