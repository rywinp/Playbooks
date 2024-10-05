from tqdm import tqdm
import supervision as sv

def extract_crops(source_video_path: str, BASKETBALL_MODEL):
  STRIDE = 30
  PLAYER_ID = 3
  frame_generator = sv.get_video_frames_generator(source_path=source_video_path, stride=STRIDE)
  crops = []

  for frame in tqdm(frame_generator, desc='collecting crops'):
    result = BASKETBALL_MODEL.infer(frame, confidence=0.4)[0]
    detections = sv.Detections.from_inference(result)
    detections = detections.with_nms(threshold=0.5, class_agnostic=True)
    detections = detections[detections.class_id == PLAYER_ID]
    crops += [
        sv.crop_image(frame, xyxy)
        for xyxy
        in detections.xyxy
    ]
  return crops