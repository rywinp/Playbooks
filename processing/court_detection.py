from inference import get_model
import supervision as sv



def court_detect(source_video: str)
    # ROBOFLOW_API_KEY = userdata.get('ROBOFLOW_API_KEY')
    COURT_DETECTION_MODEL_ID = "basketball-court-hlifr/3"
    COURT_DETECTION_MODEL = get_model(model_id=COURT_DETECTION_MODEL_ID, api_key="ROBOFLOW_API_KEY")



    SOURCE_VIDEO_PATH = source_video

    vertex_annotator = sv.VertexAnnotator(
        color=sv.Color.from_hex('#FF1493'),
        radius=8)

    frame_generator = sv.get_video_frames_generator(SOURCE_VIDEO_PATH)
    frame = next(frame_generator)

    result = COURT_DETECTION_MODEL.infer(frame, confidence=0.3)[0]
    key_points = sv.KeyPoints.from_inference(result)

    annotated_frame = frame.copy()
    annotated_frame = vertex_annotator.annotate(
        scene=annotated_frame,
        key_points=key_points)

    sv.plot_image(annotated_frame)