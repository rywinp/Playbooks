from tqdm import tqdm
from annotate_frame import annotate_frame
import supervision as sv

def video_process(source_video_path: str, BASKETBALL_MODEL):
    SOURCE_VIDEO_PATH = source_video_path
    TARGET_VIDEO_PATH = SOURCE_VIDEO_PATH[:-4] + "_result.mp4"

    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    video_info = sv.VideoInfo.from_video_path(SOURCE_VIDEO_PATH)
    video_sink = sv.VideoSink(target_path=TARGET_VIDEO_PATH, video_info=video_info)
    frame_generator = sv.get_video_frames_generator(SOURCE_VIDEO_PATH)

    with video_sink:
        for frame in tqdm(frame_generator, total=video_info.total_frames):
            result = annotate_frame(frame, box_annotator, label_annotator, BASKETBALL_MODEL)
            video_sink.write_frame(result)

    return TARGET_VIDEO_PATH