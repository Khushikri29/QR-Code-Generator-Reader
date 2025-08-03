import cv2

# Load image or from camera
path = input("Enter path to QR image (or press Enter to open webcam): ")

# Read from image
if path:
    img = cv2.imread(path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("QR Code Data:", data)
    else:
        print("No QR Code found.")
else:
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            print("QR Code Detected:", data)
            break

        cv2.imshow("QR Scanner - Press 'q' to Quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
