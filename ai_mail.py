
### sadece mail gönderen kısım. Başarılı çalışıyor.
# import cv2
# from ultralytics import YOLO
# import time
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# # E-posta gönderme fonksiyonu
# def send_email():
#     from_email = "uygulama.159@gmail.com"
#     to_email = "uygulama.159@gmail.com"
#     subject = "Fire Detection Alert!"
#     body = "A fire has been detected in the video."
#
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     msg.attach(MIMEText(body, 'plain'))
#
#     try:
#         # Gmail SMTP sunucusuna bağlanma ve e-posta gönderme
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(from_email, "rnei fgem xuzn vimv")  # E-posta şifrenizi buraya yazın
#         server.sendmail(from_email, to_email, msg.as_string())
#         server.quit()
#         print("E-posta başarıyla gönderildi!")
#     except Exception as e:
#         print(f"E-posta gönderilemedi: {e}")
#
# # Videoyu aç
# video_path = 'video_fire.mp4'  # Tespit yapılacak video dosyasının adı
# output_path = 'output_video.mp4'  # Tespit edilen video için çıkış dosyası
#
# # YOLOv8 modelini yükle (pretrained)
# model = YOLO('best_fire.pt')  # Küçük model, istersen 'yolov8s.pt', 'yolov8l.pt' kullanabilirsin.
#
# start_time = time.time()
#
# # Videoyu oku
# cap = cv2.VideoCapture(video_path)
# if not cap.isOpened():
#     print("Video dosyası açılamadı!")
#     exit()
#
# # Video özelliklerini al
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# # VideoWriter: Sonuçları kaydetmek için kullanılır
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#
# # Ateş tespit edildiğinde sadece bir kez e-posta göndermek için bayrak
# email_sent = False
#
# # Videoyu kare kare işle
# while cap.isOpened():
#     ret, frame = cap.read()  # Her kareyi oku
#     if not ret:
#         break
#
#     # YOLOv8 modelini kullanarak tespit yap
#     results = model(frame)
#
#     # Tespit edilen sonuçları görselleştir (bounding box çizimi)
#     result_img = results[0].plot()
#
#     # Ateş tespiti olup olmadığını kontrol et
#     if not email_sent:  # Eğer daha önce e-posta gönderilmediyse
#         for result in results:
#             for box in result.boxes:
#                 if box.cls == 0:  # Ateş tespit edilen sınıfın numarası '0' olabilir, modeline göre kontrol et
#                     print("Ateş tespit edildi!")
#                     send_email()
#                     email_sent = True  # E-posta gönderildikten sonra bayrağı güncelle
#                     break
#             if email_sent:
#                 break
#
#     # Görüntüyü kaydet
#     out.write(result_img)
#
# # Kaynakları serbest bırak
# cap.release()
# out.release()
#
# print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Kodun çalışma süresi: {execution_time} saniye")


# ### resim gönderme kısmı da başarılı. Kare içerisine alıp gönderiyor
# import cv2
# from ultralytics import YOLO
# import time
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import os
#
# # E-posta gönderme fonksiyonu
# def send_email_with_image(image_path):
#     from_email = "uygulama.159@gmail.com"
#     to_email = "uygulama.159@gmail.com"
#     subject = "Fire Detection Alert!"
#     body = "A fire has been detected in the video. Please find the attached screenshot of the detection."
#
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject
#
#     # E-posta mesajına metni ekle
#     msg.attach(MIMEText(body, 'plain'))
#
#     # Görüntüyü ek olarak ekle
#     with open(image_path, "rb") as attachment:
#         part = MIMEBase("application", "octet-stream")
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(image_path)}")
#         msg.attach(part)
#
#     try:
#         # Gmail SMTP sunucusuna bağlanma ve e-posta gönderme
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(from_email, "rnei fgem xuzn vimv")  # E-posta şifrenizi buraya yazın
#         server.sendmail(from_email, to_email, msg.as_string())
#         server.quit()
#         print("E-posta başarıyla gönderildi!")
#     except Exception as e:
#         print(f"E-posta gönderilemedi: {e}")
#
# # Videoyu aç
# video_path = 'video_fire.mp4'  # Tespit yapılacak video dosyasının adı
# output_path = 'output_video.mp4'  # Tespit edilen video için çıkış dosyası
# screenshot_path = 'fire_screenshot_with_bbox.jpg'  # Kutucuk çizilen görüntü kaydedilecek dosya adı
#
# # YOLOv8 modelini yükle (pretrained)
# model = YOLO('best_fire.pt')  # Küçük model, istersen 'yolov8s.pt', 'yolov8l.pt' kullanabilirsin.
#
# start_time = time.time()
#
# # Videoyu oku
# cap = cv2.VideoCapture(video_path)
# if not cap.isOpened():
#     print("Video dosyası açılamadı!")
#     exit()
#
# # Video özelliklerini al
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# # VideoWriter: Sonuçları kaydetmek için kullanılır
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#
# # Ateş tespit edildiğinde sadece bir kez e-posta göndermek için bayrak
# email_sent = False
#
# # Videoyu kare kare işle
# while cap.isOpened():
#     ret, frame = cap.read()  # Her kareyi oku
#     if not ret:
#         break
#
#     # YOLOv8 modelini kullanarak tespit yap
#     results = model(frame)
#
#     # Tespit edilen sonuçları görselleştir (bounding box çizimi)
#     result_img = results[0].plot()
#
#     # Ateş tespiti olup olmadığını kontrol et
#     if not email_sent:  # Eğer daha önce e-posta gönderilmediyse
#         for result in results:
#             for box in result.boxes:
#                 if box.cls == 0:  # Ateş tespit edilen sınıfın numarası '0' olabilir, modeline göre kontrol et
#                     print("Ateş tespit edildi!")
#
#                     # Tespit edilen kareye bounding box çizildiği haliyle kaydet
#                     cv2.imwrite(screenshot_path, result_img)
#                     print(f"Ekran görüntüsü (kutucuklu) '{screenshot_path}' olarak kaydedildi.")
#
#                     # E-posta ile kutucuklu ekran görüntüsünü gönder
#                     send_email_with_image(screenshot_path)
#
#                     email_sent = True  # E-posta gönderildikten sonra bayrağı güncelle
#                     break
#             if email_sent:
#                 break
#
#     # Görüntüyü kaydet
#     out.write(result_img)
#
# # Kaynakları serbest bırak
# cap.release()
# out.release()
#
# print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Kodun çalışma süresi: {execution_time} saniye")




import cv2
from ultralytics import YOLO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# E-posta gönderme fonksiyonu
def send_email_with_image(image_path, recipients):
    from_email = "uygulama.159@gmail.com"
    # to_email = "uygulama.159@gmail.com"
    subject = "Fire Detection Alert!"
    body = "A fire has been detected in the video. Please find the attached screenshot of the detection."

    msg = MIMEMultipart()
    msg['From'] = from_email
    # msg['To'] = to_email
    msg['To'] = ", ".join(recipients)  # Alıcıları virgülle ayırarak ekle
    msg['Subject'] = subject

    # E-posta mesajına metni ekle
    msg.attach(MIMEText(body, 'plain'))

    # Görüntüyü ek olarak ekle
    with open(image_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(image_path)}")
        msg.attach(part)

    try:
        # Gmail SMTP sunucusuna bağlanma ve e-posta gönderme
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, "rnei fgem xuzn vimv")  # E-posta şifrenizi buraya yazın
        # server.sendmail(from_email, to_email, msg.as_string())
        server.sendmail(from_email, recipients, msg.as_string())  # recipients burada kullanılıyor
        server.quit()
        print("E-posta başarıyla gönderildi!")
    except Exception as e:
        print(f"E-posta gönderilemedi: {e}")

# Alıcıların e-posta adreslerini bir listeye ekleyin
recipients = ["uygulama.159@gmail.com", "emre@youreye.com.tr", "muhammetriza@youreye.com.tr"]

# Videoyu aç
video_path = 'video_fire.mp4'  # Tespit yapılacak video dosyasının adı
output_path = 'output_video.mp4'  # Tespit edilen video için çıkış dosyası
screenshot_path = 'fire_screenshot_with_bbox.jpg'  # Kutucuk çizilen görüntü kaydedilecek dosya adı

# YOLOv8 modelini yükle (pretrained)
model = YOLO('best_fire.pt')  # Küçük model, istersen 'yolov8s.pt', 'yolov8l.pt' kullanabilirsin.

start_time = time.time()

# Videoyu oku
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()

# Video özelliklerini al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter: Sonuçları kaydetmek için kullanılır
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Ateş tespit edildiğinde sadece bir kez e-posta göndermek için bayrak
email_sent = False
fire_detection_count = 0  # Ateş tespit sayacı
max_fire_detection = 5  # 5 ardışık karede ateş tespiti olursa uyarı gönderilecek

# Videoyu kare kare işle
while cap.isOpened():
    ret, frame = cap.read()  # Her kareyi oku
    if not ret:
        break

    # YOLOv8 modelini kullanarak tespit yap
    results = model(frame)

    # Tespit edilen sonuçları görselleştir (bounding box çizimi)
    result_img = results[0].plot()

    # Ateş tespiti olup olmadığını kontrol et
    fire_detected_in_this_frame = False  # Bu karede ateş tespit edilip edilmediği
    if not email_sent:  # Eğer daha önce e-posta gönderilmediyse
        for result in results:
            for box in result.boxes:
                if box.cls == 0:  # Ateş tespit edilen sınıfın numarası '0' olabilir, modeline göre kontrol et
                    fire_detected_in_this_frame = True
                    fire_detection_count += 1
                    print(f"Ateş tespit edildi! Ardışık tespit sayısı: {fire_detection_count}")

                    # Eğer 5 ardışık karede ateş tespiti yapıldıysa uyarı gönder
                    if fire_detection_count >= max_fire_detection:
                        # Tespit edilen kareye bounding box çizildiği haliyle kaydet
                        cv2.imwrite(screenshot_path, result_img)
                        print(f"Ekran görüntüsü (kutucuklu) '{screenshot_path}' olarak kaydedildi.")

                        # E-posta ile kutucuklu ekran görüntüsünü gönder
                        # send_email_with_image(screenshot_path)
                        send_email_with_image(screenshot_path, recipients)

                        email_sent = True  # E-posta gönderildikten sonra bayrağı güncelle
                        fire_detection_count = 0  # Sayacı sıfırla
                    break
            if fire_detected_in_this_frame:
                break

    # Eğer bu karede ateş tespit edilmediyse, sayacı sıfırla
    if not fire_detected_in_this_frame:
        fire_detection_count = 0

    # Görüntüyü kaydet
    out.write(result_img)

# Kaynakları serbest bırak
cap.release()
out.release()

print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")

end_time = time.time()
execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {execution_time} saniye")
