
"""
Example iSpy-FRC camera backend.

Demonstrates the CameraBase interface using the existing OpenCV capture
mechanism. This is a core-development example, not a new hardware driver.

To support a genuinely different camera source, implement the required
source-specific behavior and integrate the backend into iSpy core.
"""

from iSpy.vision.Cameras.base import CameraBase


class ExampleCameraBackend(CameraBase):
    camera_type = "example"

    @classmethod
    def config_schema(cls) -> dict:
        return {
            "source": {
                "type": "text",
                "label": "Source",
                "default": "0",
                "help": (
                    "Camera device index, device path, supported stream URL, "
                    "or image path accepted by the existing capture system."
                ),
            },
        }

    @classmethod
    def discover(cls, claimed_sources: set | None = None) -> list[dict]:
        # No separate discovery implementation in this example.
        return []

    def __init__(
        self,
        camera_config,
        input_size: tuple | None = None,
        grayscale: bool = False,
        **kwargs,
    ):
        super().__init__(
            camera_config,
            input_size=input_size,
            grayscale=grayscale,
            **kwargs,
        )
