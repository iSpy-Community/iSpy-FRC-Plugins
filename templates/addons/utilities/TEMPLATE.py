"""
iSpy-FRC Community Utility Template

Copy this file to create a utility.

Replace:
- YourUtility with your class name.
- your_username/my_utility with a unique plugin name.
- The example settings and TODOs with your implementation.
"""

from iSpy.plugins.bases import UtilityBase, validate_output_key


class YourUtility(UtilityBase):
    plugin_name = "your_username/my_utility"

    @classmethod
    def config_schema(cls) -> dict:
        """Declare settings for this utility."""
        return {
            "enabled": {
                "type": "toggle",
                "label": "Enable Utility",
                "default": True,
            },
            "output_key": {
                "type": "text",
                "label": "Output Key",
                "description": (
                    "Key used to expose this utility's output "
                    "under frame_data['addon_data']."
                ),
                "default": "my_utility_output",
            },
        }

    def __init__(self, context: dict):
        """
        Initialize the utility.

        Always call super().__init__(context).
        Configuration defaults are merged by the base class.
        """
        super().__init__(context)

        self.enabled = bool(self.config.get("enabled", True))
        self.output_key = self.config.get(
            "output_key", "my_utility_output"
        )

    def start(self):
        """Initialize any resources this utility needs."""
        pass

    def update(self, frame_data: dict):
        """
        Called with the current vision-loop data.

        Read the data you need, calculate your result, and
        optionally publish it for other iSpy components.
        """
        if not self.enabled:
            return

        # TODO: Calculate a useful value from frame_data.
        # Example publishing pattern:
        #
        # value = ...
        # self.publish_output(
        #     frame_data,
        #     value,
        #     output_key=self.output_key,
        # )

    def stop(self):
        """Release resources when the utility stops."""
        pass