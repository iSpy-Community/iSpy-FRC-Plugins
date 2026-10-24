"""
iSpy-FRC Community Tracker Template

Copy this file when creating a new tracker.

Replace:
- YourTracker with your class name.
- your_username/my_tracker with a unique plugin name.
- The example configuration and update logic with your own behavior.
"""

from iSpy.plugins.bases import TrackerBase


class YourTracker(TrackerBase):
    # Use a unique name, preferably namespace/plugin_name.
    plugin_name = "your_username/my_tracker"

    @classmethod
    def config_schema(cls) -> dict:
        """
        Declare settings for this tracker.

        iSpy uses this schema to provide configuration defaults
        and generate settings controls where supported.
        """
        return {
            "example_threshold": {
                "type": "number",
                "label": "Example Threshold",
                "hint": "Replace this with a setting your tracker needs.",
                "default": 0.5,
            },
        }

    def __init__(self, context: dict):
        """
        Initialize the tracker.

        Always call super().__init__(context).
        self.config contains this tracker's settings, with
        schema defaults applied.
        """
        super().__init__(context)

        self.example_threshold = float(
            self.config.get("example_threshold", 0.5)
        )

    def start(self):
        """
        Called when the tracker starts.

        Initialize resources here if your tracker needs them.
        """
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
        Process the current detections.

        Parameters:
            detections: Current detection collection.
            robot_x: Robot X position.
            robot_y: Robot Y position.
            robot_yaw: Robot heading.
            robot_z: Robot Z position, defaulting to 0.0.

        Return the detection collection expected by iSpy.
        You may modify it or return a processed collection.
        """
        # TODO: Implement your tracking logic.
        return detections

    def stop(self):
        """
        Release resources when the tracker stops.
        """
        pass