import supervision as sv
from tqdm import tqdm

def cluster2(source_video_path: str, BASKETBALL_MODEL):
    # SOURCE_VIDEO_PATH = "test_480_result.mp4"
    PLAYER_ID = 2
    STRIDE = 30

    frame_generator = sv.get_video_frames_generator(
        source_path=source_video_path, stride=STRIDE)

    crops = []
    for frame in tqdm(frame_generator, desc='collecting crops'):
        result = BASKETBALL_MODEL.infer(frame, confidence=0.3)[0]
        detections = sv.Detections.from_inference(result)
        players_detections = detections[detections.class_id == PLAYER_ID]
        players_crops = [sv.crop_image(frame, xyxy) for xyxy in detections.xyxy]
        crops += players_crops

    team_classifier = TeamClassifier(device="cuda")
    team_classifier.fit(crops)

    return crops