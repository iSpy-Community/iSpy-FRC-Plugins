"""
iSpy-FRC Example Utility: Detection Counter

Counts the detections in each vision-loop update and publishes
the count under frame_data["addon_data"] using iSpy's UtilityBase API.
"""

from iSpy.plugins.bases import UtilityBase


class DetectionCountUtility(UtilityBase):
    plugin_name = "community/example_detection_counter"

    @classmethod
    def config_schema(cls) -> dict:
        return {
            "enabled": {
                "type": "toggle",
                "label": "Enable Detection Counter",
                "default": True,
            },
            "output_key": {
                "type": "text",
                "label": "Output Key",
                "description": (
                    "Key used to publish the detection count "
                    "under addon_data."
                ),
                "default": "community_detection_count",
            },
        }

    def __init__(self, context: dict):
        super().__init__(context)

        self.enabled = bool(self.config.get("enabled", True))
        self.output_key = str(
            self.config.get(
                "output_key",
                "community_detection_count",
            )
        )

    def start(self):
        """Called when the utility starts."""
        pass

    def update(self, frame_data: dict):
        """Count current detections and publish the result."""
        if not self.enabled or not isinstance(frame_data, dict):
            return

        detections = frame_data.get("detections", [])

        if detections is None:
            detections = []

        try:
            count = len(detections)
        except TypeError:
            return

        self.publish_output(
            frame_data,
            count,
            output_key=self.output_key,
        )

    def stop(self):
        """Release resources if needed."""
        pass