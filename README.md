# Dynamic Tracking: Intelligent People Counting with YOLO and OpenCV
This project develops a real-time people counting and tracking system using YOLO (You Only Look Once) and OpenCV. It detects individuals in video feeds, assigns unique identifiers, and counts them as they move in and out of defined zones. Utilizing the SORT (Simple Online and Realtime Tracking) algorithm, the system ensures accurate tracking even in crowded environments. Visual feedback is provided through bounding boxes and count displays, making it ideal for applications in crowd management and security surveillance.

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Computer Vision](#computer-vision)
  - [Importing Libraries and Loading Model](#importing-libraries-and-Loading-model)
  - [Setting Up Video, Mask, and Tracker](#setting-up-video,-mask,-and-tracker)
  - [Object Detection and Filtering](#object-detection-and-filtering)
  - [Tracking and Counting People](#tracking-and-counting-people)
  - [Visualizing and Displaying Results](#visualizing-and-displaying-results)
- [Results](#results)
- [Impact](#impact)
- [Future Improvements](#future-improvements)

## Project Overview
This project aims to create an intelligent, real-time people counting and tracking system leveraging advanced computer vision techniques. By integrating the YOLO (You Only Look Once) model, the system efficiently detects and identifies individuals in video streams.

## Problem Statement
In public spaces, effective crowd management and monitoring are crucial for ensuring safety and optimizing resource allocation. Traditional methods of counting and tracking individuals can be labor-intensive, prone to human error, and may not provide real-time insights. The need for an automated, efficient, and accurate solution to detect and count people in various environments has become increasingly important.

This project addresses the challenges of real-time people detection and tracking in video feeds, particularly in dynamic and crowded situations. The aim is to develop a robust system that can accurately identify and monitor individuals, providing instant feedback on crowd size and movement patterns. By utilizing advanced object detection algorithms like YOLO and tracking techniques such as SORT, this solution seeks to enhance situational awareness, improve security measures, and facilitate better decision-making in public safety and resource management contexts.

## Dataset
The dataset for this project comprises video recordings capturing various public environments, including indoor and outdoor spaces with varying levels of crowd density. It is designed to facilitate the training and evaluation of the people counting and tracking system. 

## Computer Vision
### Importing Libraries and Loading Model
- Imports essential libraries (YOLO, cv2, cvzone, Sort) for object detection, tracking, and image processing.
- Loads the YOLO model trained on COCO dataset to detect objects in video.

### Setting Up Video, Mask, and Tracker
- Captures video and applies a mask to focus on a specific region.
- Initializes the Sort tracker for tracking detected objects across frames.

### Object Detection and Filtering
- YOLO detects objects in the video feed, generating bounding boxes.
- Filters detections to only track "person" class with a confidence threshold above 0.3.

### Tracking and Counting People
- Tracks detected people using Sort, assigning unique IDs.
- Counts people crossing the defined limitsUp and limitsDown lines and updates counts.

### Visualizing and Displaying Results
- Displays bounding boxes, IDs, and counts on the video frame in real time, along with the final output showing the number of people moving in/out.

## Results
The implemented system successfully tracks and counts people in real-time from video footage. Using the YOLO object detection model and the SORT tracker, the system accurately detects individuals, even in crowded or dynamic environments. The visual overlay, with bounding boxes and unique IDs for each person, provides a clear view of the tracking process. Additionally, the system reliably counts people moving in and out of defined zones, updating the counts instantly.

## Impact
This solution improves crowd monitoring and management by automating the counting and tracking process. It can be used in a variety of public spaces like malls, train stations, and event venues to enhance security, optimize staffing, and ensure safety. The real-time nature of the system provides immediate insights, allowing for better decision-making and resource allocation.

## Future Improvements
- **Enhanced Detection Accuracy:** Incorporating more advanced models or fine-tuning the YOLO model specifically for different environments (e.g., low-light conditions) can improve detection accuracy, particularly in complex scenarios like occlusions or dense crowds.
- **Multi-Camera Integration:** Expanding the system to support multiple camera feeds would enable broader area coverage and more comprehensive tracking, particularly in large venues or city-wide surveillance.
- **Real-Time Alerts:** Implementing real-time notifications for specific events (e.g., overcrowding or unusual movement patterns) can enhance security and management.
- **Optimized Resource Use:** Leveraging edge computing to perform detection and tracking locally would reduce latency and bandwidth usage, making the system more scalable for large-scale deployments.
- **Behavior Analysis:** Adding functionality to analyze movement patterns or detect suspicious behavior could provide more insightful analytics for crowd management and security monitoring.
