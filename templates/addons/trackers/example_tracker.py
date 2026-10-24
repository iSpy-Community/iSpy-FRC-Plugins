"""
Example iSpy-FRC tracker: Confidence Filter

Demonstrates:
- TrackerBase inheritance
- Configuration with config_schema()
- Reading settings in __init__()
- Processing Object detections in update()
- Returning detections using iSpy's expected interface

This example filters detections below a configurable confidence threshold.
It demonstrates detection filtering, not temporal object association.
"""

from iSpy.plugins.bases import TrackerBase


class ConfidenceFilterTracker(TrackerBase):
    plugin_name = "community/example_confidence_filter"

    @classmethod
    def config_schema(cls) -> dict:
        return {
            "min_confidence": {
                "type": "number",
                "label": "Minimum Confidence",
                "hint": (
                    "Discard detections with confidence below this value. "
                    "Use a value between 0.0 and 1.0."
                ),
                "default": 0.5,
            },
        }

    def __init__(self, context: dict):
        super().__init__(context)

        raw_threshold = self.config.get("min_confidence", 0.5)

        try:
            threshold = float(raw_threshold)
        except (TypeError, ValueError):
            threshold = 0.5

        # Keep the threshold within the documented confidence range.
        self.min_confidence = max(0.0, min(1.0, threshold))

    def start(self):
        """Called when the tracker starts."""
        pass

    def update(
        self,
        detections,
        robot_x,
        robot_y,
        robot_yaw,
        robot_z: float = 0.0,
    ):
        """
        Keep detections meeting the configured confidence threshold.

        The robot pose parameters are part of iSpy's tracker interface.
        This example does not need to use them.
        """
        return [
            detection
            for detection in detections
            if float(getattr(detection, "confidence", 0.0) or 0.0)
            >= self.min_confidence
        ]

    def stop(self):
        """Release resources if the implementation acquires any."""
        pass