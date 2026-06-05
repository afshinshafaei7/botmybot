from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from save import save

# ======= مشخصات تو =======
my_info = {
    "name": "افشین",
    "phone": "09121234567",
    "job": "خدمات طراحی سایت",
    "work_time": "9 صبح تا 6 عصر"
}

# ======= وضعیت کاربران =======
user_state = {}

TOKEN = "8384330394:AAEov4TaNmssTP0mcra_Y1HU-gmjDnf-K24"

# ======= فرمان start =======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nبرای شروع، اسم و شماره‌ات رو بفرست"
    )

# ======= دریافت پیام‌ها =======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    # اگر کاربر جدید است
    if user_id not in user_state:
        user_state[user_id] = {"step": 1}

    step = user_state[user_id]["step"]

    # مرحله 1: گرفتن اسم
    if step == 1:
        user_state[user_id]["name"] = text
        user_state[user_id]["step"] = 2
        await update.message.reply_text("شماره تماس‌ات را بفرست")

    # مرحله 2: گرفتن شماره
    elif step == 2:
        user_state[user_id]["phone"] = text
        user_state[user_id]["step"] = 3
        await update.message.reply_text("چه کاری داری؟")

    # مرحله 3: گرفتن نوع کار و نمایش اطلاعات
    elif step == 3:
        user_state[user_id]["job"] = text

        # نمایش اطلاعات تو به کاربر
        await update.message.reply_text(
            f" راه تماس با من :\n"
            f"نام: {my_info['name']}\n"
            f"شماره: {my_info['phone']}\n"
            f"خدمات: {my_info['job']}\n"
            f"ساعت کاری: {my_info['work_time']}\n\n"
            f"اطلاعات شما هم ثبت شد ✔️"
        )

        # ذخیره اطلاعات کاربر
        save(user_state[user_id])

        # بازگرداندن مرحله به 1 برای تعامل بعدی
        user_state[user_id]["step"] = 1

# ======= ساخت بات =======
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot started...")
app.run_polling()


