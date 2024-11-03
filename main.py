# import cv2
# from ultralytics import YOLO
#
# # Videoyu aç
# video_path = 'video2.mp4'  # Tespit yapılacak video
# output_path = 'output_video.mp4'  # Tespit edilen video için çıkış dosyası
#
# # YOLOv8 modelini yükle (pretrained)
# model = YOLO('yolov8n.pt')  # Küçük model, istersen 'yolov8s.pt', 'yolov8l.pt' kullanabilirsin.
#
# # Videoyu oku
# cap = cv2.VideoCapture(video_path)
# if not cap.isOpened():
#     print("Video dosyası açılamadı!")
#     exit()
#
# # Video özellikleri
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# # VideoWriter: Sonuçları kaydetmek için kullanılır
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
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
#     # Görüntüyü kaydet
#     out.write(result_img)
#
#     # (İsteğe bağlı) Ekranda tespit edilen sonuçları göster
#     cv2.imshow('YOLOv8 Detection', result_img)
#
#     # 'q' tuşuna basarak işlemi durdurabilirsin
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Kaynakları serbest bırak
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")


##### insan tespitini kaldırmak için yazılan kod. Güzel çalışmadı
# import cv2
# from ultralytics import YOLO
#
#
# video_path = 'video3.mp4'
# output_path = 'output_video.mp4'
#
# model = YOLO('best_animal.pt')
#
# cap = cv2.VideoCapture(video_path)
# if not cap.isOpened():
#     print("Video dosyası açılamadı!")
#     exit()
#
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
#
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#
# person_class_id = 3
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     results = model(frame)
#
#     filtered_boxes = []
#     for box in results[0].boxes:
#         if int(box.cls[0]) != person_class_id:
#             filtered_boxes.append(box)
#
#     if filtered_boxes:
#         result_img = results[0].plot(filtered_boxes)
#         out.write(result_img)
#
# cap.release()
# out.release()
#
# print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")



##### hayvan tespiti için geçerli kod. Süre tutma eklendi
import cv2
from ultralytics import YOLO
import time

# Videoyu aç
video_path = 'Mera.mp4'  # Tespit yapılacak video dosyasının adı
output_path = 'output_video.mp4'  # Tespit edilen video için çıkış dosyası

# YOLOv8 modelini yükle (pretrained)
model = YOLO('best_custom_detect.pt')  # Küçük model, istersen 'yolov8s.pt', 'yolov8l.pt' kullanabilirsin.

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

# Videoyu kare kare işle
while cap.isOpened():
    ret, frame = cap.read()  # Her kareyi oku
    if not ret:
        break

    # YOLOv8 modelini kullanarak tespit yap
    results = model(frame)

    # Tespit edilen sonuçları görselleştir (bounding box çizimi)
    result_img = results[0].plot()

    # Görüntüyü kaydet
    out.write(result_img)

# Kaynakları serbest bırak
cap.release()
out.release()

print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")

end_time = time.time()
execution_time = end_time - start_time
print(f"Kodun çalışma süresi: {execution_time} saniye")
