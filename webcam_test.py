import cv2
from ultralytics import YOLO

model = YOLO('best.pt')   ##load your custom model

cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video file"

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
        
    results = model.predict(im0,
    conf=0.3,
    show=False,
    show_labels=True,
    classes=[0],
    stream=True
)    
    for result in results:
        boxes = result.boxes.cpu().numpy()
        class_name = "subject"
        text = f'count: {len(boxes)}'
        cv2.putText(im0, text,(30,50),cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
        for box in boxes:                                          
            r = box.xyxy[0].astype(int)                                                                           
            cv2.rectangle(im0, r[:2], r[2:], (0, 255, 0), 2)
            cv2.putText(im0, class_name, (r[0], r[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        
    cv2.imshow("frame", im0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()
