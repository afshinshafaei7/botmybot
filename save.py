# save.py
import json

def save(data):
    """
    داده‌های کاربر را داخل فایل users.json ذخیره می‌کند
    """
    with open("users.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")