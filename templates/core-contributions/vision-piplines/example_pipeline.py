
"""
Example iSpy-FRC vision pipeline.

Demonstrates the basic frame-processing lifecycle without running
a detector. This pipeline is for core-development reference only;
it is not automatically loaded from the community repository.
"""

from iSpy.vision.pipelines.base import VisionPipeline


class ExamplePassthroughPipeline(VisionPipeline):
    plugin_name = "example_passthrough"

    def __init__(self, camera_config, input_size, grayscale):
        # Match the actual VisionPipeline constructor signature.
        super().__init__(camera_config, input_size, grayscale)

        # TODO: Initialize your detector or other resources here.

    def prepare(self):
        """Initialize resources before processing begins."""
        super().prepare()

    def run(self):
        """Return an empty detection list and the current camera frame."""
        frame = self.get_frame()

        if frame is None:
            return [], None

        # Add image processing or detection logic here.
        return [], frame

    def destroy(self):
        """Release resources owned by this pipeline."""
        super().destroy()
