from inference import get_model
from image_process import image_process
from video_process import video_process
import supervision as sv
import cv2

model = get_model(model_id="basketball-players-fy4c2/16", api_key="ROBOFLOW_API_KEY")

path = video_process("test_480.mp4", model)
