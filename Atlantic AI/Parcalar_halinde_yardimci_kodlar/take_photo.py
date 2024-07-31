def capture_photo():
    # Kamerayı aç
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı.")
        return

    # Kamera görüntüsünü al
    ret, frame = cap.read()
    if ret:
        # Dosya adını oluştur
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        photo_filename = f"photo_{timestamp}.png"
        # Fotoğrafı kaydet
        cv2.imwrite(photo_filename, frame)
        print(f"Fotoğraf kaydedildi: {photo_filename}")
    else:
        print("Fotoğraf alınamadı.")

    # Kamerayı kapat
    cap.release()
    cv2.destroyAllWindows()