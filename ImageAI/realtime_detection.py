import os
from imageai.Detection import VideoObjectDetection
import cv2


camera = cv2.VideoCapture(0)
execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                             output_file_path=os.path.join(execution_path + "videos/",
                                                                           "camera_detected_1"),
                                             frames_per_second=29, log_progress=True)
print(video_path)