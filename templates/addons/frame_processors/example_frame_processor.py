"""
iSpy-FRC Example: Grayscale Frame Processor

Converts camera frames to grayscale while preserving a
three-channel BGR output for compatibility with downstream
vision processing.
"""

import cv2

from iSpy.plugins.bases import FrameProcessorBase


class GrayscaleFrameProcessor(FrameProcessorBase):
    plugin_name = "community/example_grayscale"

    @classmethod
    def config_schema(cls) -> dict:
        return {
            "enabled": {
                "type": "toggle",
                "label": "Enable Grayscale",
                "hint": "Convert incoming camera frames to grayscale.",
                "default": True,
            },
        }

    def __init__(self, context: dict):
        super().__init__(context)
        self.enabled = bool(self.config.get("enabled", True))

    def start(self):
        """Called when the processor starts."""
        pass

    def process(self, frame):
        """Convert a supported image frame to grayscale."""
        if not self.enabled or frame is None:
            return frame

        # Handle a frame that is already single-channel grayscale.
        if frame.ndim == 2:
            gray = frame

        elif frame.ndim == 3:
            channels = frame.shape[2]

            if channels == 1:
                gray = frame[:, :, 0]

            elif channels == 3:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            elif channels == 4:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

            else:
                # Unknown layout: leave the frame unchanged.
                return frame

        else:
            return frame

        # Replicate grayscale intensity across B, G and R channels.
        # This preserves a three-channel output for typical
        # downstream OpenCV and object-detection pipelines.
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    def stop(self):
        """Release resources if needed."""
        pass