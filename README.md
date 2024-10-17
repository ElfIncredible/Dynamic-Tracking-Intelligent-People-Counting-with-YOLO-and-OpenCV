# Dynamic Tracking: Intelligent People Counting with YOLO and OpenCV
This project develops a real-time people counting and tracking system using YOLO (You Only Look Once) and OpenCV. It detects individuals in video feeds, assigns unique identifiers, and counts them as they move in and out of defined zones. Utilizing the SORT (Simple Online and Realtime Tracking) algorithm, the system ensures accurate tracking even in crowded environments. Visual feedback is provided through bounding boxes and count displays, making it ideal for applications in crowd management and security surveillance.

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Computer Vision](#computer-vision)

## Project Overview
This project aims to create an intelligent, real-time people counting and tracking system leveraging advanced computer vision techniques. By integrating the YOLO (You Only Look Once) model, the system efficiently detects and identifies individuals in video streams.

## Problem Statement
In public spaces, effective crowd management and monitoring are crucial for ensuring safety and optimizing resource allocation. Traditional methods of counting and tracking individuals can be labor-intensive, prone to human error, and may not provide real-time insights. The need for an automated, efficient, and accurate solution to detect and count people in various environments has become increasingly important.

This project addresses the challenges of real-time people detection and tracking in video feeds, particularly in dynamic and crowded situations. The aim is to develop a robust system that can accurately identify and monitor individuals, providing instant feedback on crowd size and movement patterns. By utilizing advanced object detection algorithms like YOLO and tracking techniques such as SORT, this solution seeks to enhance situational awareness, improve security measures, and facilitate better decision-making in public safety and resource management contexts.

## Dataset
The dataset for this project comprises video recordings capturing various public environments, including indoor and outdoor spaces with varying levels of crowd density. It is designed to facilitate the training and evaluation of the people counting and tracking system. 

## Computer Vision
### Importing Libraries & Loading Model
- Imports essential libraries (YOLO, cv2, cvzone, Sort) for object detection, tracking, and image processing.
- Loads the YOLO model trained on COCO dataset to detect objects in video.

### Setting Up Video, Mask, and Tracker
- Captures video and applies a mask to focus on a specific region.
- Initializes the Sort tracker for tracking detected objects across frames.

### Object Detection & Filtering
- YOLO detects objects in the video feed, generating bounding boxes.
- Filters detections to only track "person" class with a confidence threshold above 0.3.

### Tracking & Counting People
- Tracks detected people using Sort, assigning unique IDs.
- Counts people crossing the defined limitsUp and limitsDown lines and updates counts.

### Visualizing & Displaying Results
- Displays bounding boxes, IDs, and counts on the video frame in real time, along with the final output showing the number of people moving in/out.
