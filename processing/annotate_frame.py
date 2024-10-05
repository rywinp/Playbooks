import numpy as np
import supervision as sv

def annotate_frame(
    frame: np.ndarray, box_annotator: sv.BoxAnnotator, label_annotator: sv.LabelAnnotator, BASKETBALL_MODEL) -> np.ndarray:
    """
    Annotate the input frame with bounding boxes and labels.

    Args:
        frame (np.ndarray): The image frame to annotate.
        box_annotator (sv.BoxAnnotator): The annotator for drawing bounding boxes.
        label_annotator (sv.LabelAnnotator): The annotator for drawing labels.

    Returns:
        np.ndarray: The annotated image frame.
    """
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    result = BASKETBALL_MODEL.infer(frame, confidence=0.4)[0]
    detections = sv.Detections.from_inference(result)

    labels = [
        f"{class_name} {confidence:.2f}"
        for class_name, confidence
        in zip(detections["class_name"], detections.confidence)
    ]

    annotated_frame = frame.copy()
    annotated_frame = box_annotator.annotate(annotated_frame, detections)
    annotated_frame = label_annotator.annotate(annotated_frame, detections, labels=labels)
    return annotated_frame
