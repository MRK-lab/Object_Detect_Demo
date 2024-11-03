import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
from collections import defaultdict

# Video ve model yolları
video_path = 'Mera.mp4'
output_path = 'output_video.mp4'
info_path = 'info.txt'

# YOLOv8 modelini yükle
model = YOLO('best_custom_detect.pt')

# DeepSORT nesne izleyiciyi başlat
tracker = DeepSort(max_age=30, n_init=2)

# Video okuyucu ve yazıcı
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()

# Video özellikleri
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Nesne sayacı ve izlenen nesneler
object_counts = defaultdict(int)
tracked_objects = set()

# Video işlemi
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv8 modelini kullanarak tespit yap
    results = model(frame)
    detections = []
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Detayları takip için hazırlayın
        detections.append(([x1, y1, x2, y2], box.conf[0], class_name))

    # DeepSORT ile nesne takibi
    tracked = tracker.update_tracks(detections, frame=frame)

    for track in tracked:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        class_name = track.det_class

        # Yeni bir nesne gördüğümüzde sayısını artır
        if track_id not in tracked_objects:
            tracked_objects.add(track_id)
            object_counts[class_name] += 1

        # Koordinatları kullanarak doğru kutucuk çizimi yap
        x1, y1, x2, y2 = map(int, track.to_tlbr())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{class_name} {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)

# Kaynakları serbest bırak
cap.release()
out.release()

# info.txt'ye sayım sonuçlarını yazdır
with open(info_path, 'w') as f:
    for class_name, count in object_counts.items():
        f.write(f"{class_name}: {count}\n")

print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")
print(f"Nesne sayıları '{info_path}' dosyasına kaydedildi.")
