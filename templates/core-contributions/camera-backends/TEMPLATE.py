
"""
iSpy-FRC Camera Backend Contribution Template

Reference for developers adding a new camera source to iSpy core.

New backends must be integrated and registered in the core repository.
They are not automatically loaded from the community templates repo.
"""

from iSpy.vision.Cameras.base import CameraBase


class YourCameraBackend(CameraBase):
    camera_type = "your_camera_type"

    @classmethod
    def config_schema(cls) -> dict:
        """Describe backend-specific settings using iSpy's schema format."""
        return {
            # Example:
            # "device_option": {
            #     "type": "text",
            #     "label": "Device Option",
            #     "default": "",
            # },
        }

    @classmethod
    def discover(cls, claimed_sources: set | None = None) -> list[dict]:
        """
        Return available sources in the format expected by iSpy.

        Replace this with real discovery logic if the backend supports it.
        """
        return []

    def __init__(
        self,
        camera_config,
        input_size: tuple | None = None,
        grayscale: bool = False,
        **kwargs,
    ):
        # CameraBase expects camera_config to include a "source" key.
        # It handles the standard camera lifecycle and frame acquisition.
        super().__init__(
            camera_config,
            input_size=input_size,
            grayscale=grayscale,
            **kwargs,
        )

        # TODO: Initialize any additional backend-specific resources here.

    # TODO: Override only the methods required by your source type.
    # Inspect iSpy/vision/Cameras/base.py and existing camera classes
    # before overriding frame acquisition, cleanup, or reconnection.
