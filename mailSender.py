import smtplib # for mail

def send_email():
    email_server=smtplib.SMTP("smtp.gmail.com", 587)
    email_server.ehlo()
    email_server.starttls()
    email_server.login("uygulama.159@gmail.com","rnei fgem xuzn vimv")
    email_server.sendmail("uygulama.159@gmail.com","uygulama.159@gmail.com","Test")
    email_server.quit()

print("Sending...")
send_email()

##########
# mail göndermek için öncelikle mail hesabınızda iki faktörlü doğrulamayı aç
# uygulama şifreleri kısmına gir
# bir tane oluştur ve oluşturulan şifreyi bu uygulamada kullan
