import yagmail

email = yagmail.SMTP(user="silaslowe1@gmail.com", password="!")
email.send(to="silaslowe@gmail.com",
           subject="Hi there",
           contents="This is Silas.\n\n-Silas",
           attachments="design.txt")
