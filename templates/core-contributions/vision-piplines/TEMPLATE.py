"""
iSpy-FRC Vision Pipeline Template

This is a starting point for contributing a new pipeline to
the iSpy-FRC core repository.

IMPORTANT:
- Custom pipelines are not automatically loaded from this community repo.
- A new pipeline must be registered in iSpy/vision/pipelines/__init__.py.
- Match the actual VisionPipeline interface.
"""

from iSpy.vision.pipelines.base import VisionPipeline


class YourVisionPipeline(VisionPipeline):
    # Use a unique identifier when integrating this class into
    # iSpy's pipeline registry.
    plugin_name = "your_pipeline"

    def __init__(self, camera_config, input_size, grayscale):
        """
        Initialize the camera and pipeline using iSpy's real
        VisionPipeline constructor signature.
        """
        super().__init__(
            camera_config,
            input_size,
            grayscale,
        )

        # TODO: Initialize your detector or other resources here.

    def prepare(self):
        """
        Prepare models, detectors, or other resources if needed.

        Keep this lightweight if preparation is not required.
        """
        pass

    def run(self):
        """
        Process one frame.

        Return:
            (objects, frame)

        objects must follow iSpy's shared detection output contract.
        frame is the processed image to return to the vision loop.
        """
        frame = self.get_frame()

        if frame is None:
            return [], None

        # TODO:
        # 1. Run your vision algorithm on frame.
        # 2. Convert detections to iSpy's expected Object format.
        # 3. Return the detections and displayable frame.

        return [], frame

    def destroy(self):
        """
        Release models, detectors, and other resources.

        Override this when your implementation owns resources
        that need explicit cleanup.
        """
        pass