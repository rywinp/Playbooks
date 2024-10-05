from annotate_frame import annotate_frame
import supervision as sv

def image_process(source_photo_path: str, BASKETBALL_MODEL):

    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    frame_generator = sv.get_video_frames_generator(source_photo_path)
    frame = next(frame_generator)

    result = annotate_frame(frame, box_annotator, label_annotator, BASKETBALL_MODEL)

    return result
