# Excel to Mongo

این پروژه یک API برای دریافت فایل اکسل و ذخیره شماره تلفن‌ها در MongoDB است. با استفاده از این API می‌توانید داده‌های موجود در فایل‌های اکسل را به سادگی در دیتابیس MongoDB ذخیره کنید.

## پیش‌نیازها

- Python 3.8 یا بالاتر
- MongoDB
- Docker (اختیاری، برای اجرای MongoDB)

## نصب و راه‌اندازی

### مراحل نصب

1. **کلون کردن مخزن**:

   ```sh
   git clone https://github.com/username/excel_to_mongo.git
   cd excel_to_mongo
2. ایجاد و فعال‌سازی محیط مجازی:
python -m venv env
source env/bin/activate  # برای ویندوز: env\Scripts\activate
3.نصب وابستگی‌ها:
pip install -r requirements.txt
استفاده
ارسال فایل اکسل
برای ارسال فایل اکسل و ذخیره داده‌ها در دیتابیس MongoDB، می‌توانید از ابزارهایی مانند Postman استفاده کنید.

URL: http://127.0.0.1:8000/api/upload/

Method: POST

Body:

انتخاب form-data

اضافه کردن کلید file و انتخاب فایل اکسل.

APIهای دیگر
برای مدیریت داده‌های ذخیره شده می‌توانید از APIهای زیر استفاده کنید:

دریافت لیست شماره‌ها:

URL: http://127.0.0.1:8000/api/users/

Method: GET

دریافت شماره مشخص بر اساس ID:

URL: http://127.0.0.1:8000/api/users/<id>/

Method: GET

ایجاد شماره جدید:

URL: http://127.0.0.1:8000/api/users/

Method: POST

Body:

json
{
  "number": "09123456789"
}
بروزرسانی شماره:

URL: http://127.0.0.1:8000/api/users/<id>/

Method: PUT

Body:

json
{
  "number": "09123456789"
}
حذف شماره:

URL: http://127.0.0.1:8000/api/users/<id>/

Method: DELETE

تست‌ها
برای اطمینان از کارکرد صحیح سیستم، می‌توانید تست‌های موجود را اجرا کنید:

sh
python manage.py test