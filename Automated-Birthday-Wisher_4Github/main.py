import pandas
import smtplib
import datetime as dt
import random

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_email = "example_email@gmail.com"
password = "password123"

with open("birthdays.csv") as birthdays_file:
    birthdays_data = pandas.read_csv(birthdays_file)


now = dt.datetime.now()
now_month = now.month
now_day = now.day

birthdays_dict = birthdays_data.to_dict(orient="records")

for record in birthdays_dict:
    if record["month"] == now_month and record["day"] == now_day:

        with open(f"letter_templates/{random.choice(letters_list)}") as letter:
            letter_text = letter.read()
            letter_text = letter_text.replace("[NAME]", record["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=record["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_text}"
            )

