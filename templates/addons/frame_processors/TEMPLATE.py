"""
iSpy-FRC Community Frame Processor Template

Copy this file when creating a new frame processor.

Replace:
- YourFrameProcessor with your class name.
- community/my_frame_processor with a unique plugin name.
- The example configuration and processing logic with your own.
"""

from iSpy.plugins.bases import FrameProcessorBase


class YourFrameProcessor(FrameProcessorBase):
    plugin_name = "community/my_frame_processor"

    @classmethod
    def config_schema(cls) -> dict:
        """Declare the settings this processor needs."""
        return {
            "enabled": {
                "type": "toggle",
                "label": "Enable Processing",
                "hint": "When disabled, return the original frame.",
                "default": True,
            },
        }

    def __init__(self, context: dict):
        """
        Initialize the processor.

        Always call super().__init__(context).
        self.config contains the processor's settings with
        defaults from config_schema() applied.
        """
        super().__init__(context)

        self.enabled = bool(self.config.get("enabled", True))

    def start(self):
        """Initialize resources needed before processing frames."""
        pass

    def process(self, frame):
        """
        Process one camera frame and return the resulting frame.

        Keep the output compatible with downstream iSpy vision
        processing. Returning the original frame is a valid no-op.
        """
        if not self.enabled:
            return frame

        # TODO: Replace this with your image-processing logic.
        return frame

    def stop(self):
        """Release resources when the processor stops."""
        pass