from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *  # Importing the SORT (Simple Online and Realtime Tracking) algorithm

# Open video capture from a specified video file
cap = cv2.VideoCapture("../Videos/people.mp4")

# Load the YOLOv8 model weights for object detection
model = YOLO("../Yolo-Weights/yolov8l.pt")

# List of class names that the model can detect
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# Load a mask image to define a specific region of interest
mask = cv2.imread('Mask-1.png')

# Initialize the SORT tracker with specified parameters
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# Define lines to set limits for tracking entry and exit
limitsUp = [103, 161, 296, 161]
limitsDown = [527, 489, 735, 489]

# Lists to count unique IDs for people entering and exiting
totalCountUp = []
totalCountDown = []

# Main loop for processing video frames
while True:
    success, img = cap.read()  # Read the next frame from the video
    imgRegion = cv2.bitwise_and(img, mask)  # Apply mask to the image

    # Load graphics for overlaying on the video frame
    imgGraphics = cv2.imread("graphics-1.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (730,260))  # Overlay the graphics onto the image

    # Perform object detection using the YOLO model
    results = model(imgRegion, stream=True)

    detections = np.empty((0, 5))  # Initialize an empty array for detections

    for r in results:
        boxes = r.boxes  # Get detected bounding boxes
        for box in boxes:
            # Extract bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1  # Calculate width and height of the bounding box

            # Confidence score of the detection
            conf = math.ceil((box.conf[0]*100))/100

            # Class index and name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            # If detected class is a person and confidence is above threshold
            if currentClass == "person" and conf > 0.3:
                currentArray = np.array([x1, y1, x2, y2, conf])  # Create an array for the detection
                detections = np.vstack((detections, currentArray))  # Append detection to the detections array

    # Update tracker with current detections
    resultsTracker = tracker.update(detections)

    # Draw limit lines for tracking
    cv2.line(img, (limitsUp[0], limitsUp[1]), (limitsUp[2], limitsUp[3]), (0, 0, 255), 5)
    cv2.line(img, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 0, 255), 5)

    # Process results from the tracker
    for result in resultsTracker:
        x1, y1, x2, y2, id = result  # Get coordinates and ID from the tracking result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Draw a rectangle and put the ID on the image
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255,0,255))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)), scale=2, offset=10, thickness=3)

        # Calculate center point of the bounding box
        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)  # Draw a circle at the center

        # Check if the center point crosses the upper limit line
        if limitsUp[0] < cx < limitsUp[2] and limitsUp[1] - 15 < cy < limitsUp[1] + 15:
            if totalCountUp.count(id) == 0:  # If ID is not already counted
                totalCountUp.append(id)  # Add ID to totalCountUp
                cv2.line(img, (limitsUp[0], limitsUp[1]), (limitsUp[2], limitsUp[3]), (0, 255, 0), 5)  # Draw a green line

        # Check if the center point crosses the lower limit line
        if limitsDown[0] < cx < limitsDown[2] and limitsDown[1] - 15 < cy < limitsDown[1] + 15:
            if totalCountDown.count(id) == 0:  # If ID is not already counted
                totalCountDown.append(id)  # Add ID to totalCountDown
                cv2.line(img, (limitsDown[0], limitsDown[1]), (limitsDown[2], limitsDown[3]), (0, 255, 0), 5)  # Draw a green line

    # Display the total counts of people moving up and down
    cv2.putText(img, str(len(totalCountUp)), (929, 345), cv2.FONT_HERSHEY_PLAIN, 5, (139, 195, 75), 7)
    cv2.putText(img, str(len(totalCountDown)), (1191, 345), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 230), 7)

    cv2.imshow("Image", img)  # Show the processed image
    #cv2.imshow("ImageRegion", imgRegion)  # Optional: Show the masked image region
    cv2.waitKey(1)  # Wait for 1 millisecond before the next frame
