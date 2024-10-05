from inference import get_model
from image_process import image_process
from extract import extract_crops
from embed import embed
from cluster import cluster
from team_seperate import team_seperate
import supervision as sv
import cv2

model = get_model(model_id="basketball-players-fy4c2/16", api_key="ROBOFLOW_API_KEY")

result = image_process("test.jpg", model)
crops = extract_crops("test.jpg", model)
data = embed(crops)
clusters = cluster(data)


img = team_seperate("test.jpg", model)
cv2.imwrite("team_seperate.jpg", img)

cv2.imwrite("result.jpg", result)
for i in range(len(crops)):
    cv2.imwrite("crop_" + str(i) + "team_" + str(clusters[i]) +".jpg", crops[i])
