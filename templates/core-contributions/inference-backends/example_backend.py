"""
Illustrative inference-backend adapter for iSpy-FRC contributors.

This example deliberately does not load a real model or claim support for
specific hardware. It demonstrates lifecycle and error handling without
inventing an iSpy registration API.

Use it as a structural reference only. Connect a real runtime, decode outputs
according to iSpy's existing result contract, and integrate it in core.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from TEMPLATE import YourInferenceBackend


class ExampleRuntime:
    """Stand-in for a runtime session; not an actual inference engine."""

    def __init__(
        self, model_path: Path, options: dict[str, Any]
    ) -> None:
        self.model_path = model_path
        self.options = options
        self.closed = False

    def run(self, input_data: Any) -> Any:
        if self.closed:
            raise RuntimeError("Example runtime is closed.")

        raise NotImplementedError(
            "Connect this example to a real runtime and output decoder."
        )

    def close(self) -> None:
        self.closed = True


class ExampleInferenceBackend(YourInferenceBackend):
    """Lifecycle example only; not registered or usable as an iSpy backend."""

    backend_name = "example"
    supported_model_suffixes = (".example",)

    @classmethod
    def is_available(cls) -> tuple[bool, str]:
        return (
            False,
            "This is a documentation example, not a real inference backend.",
        )

    def _load_runtime(
        self, model_path: Path, options: dict[str, Any]
    ) -> ExampleRuntime:
        # A real implementation would import its optional SDK here, verify
        # provider/device availability, and create the runtime session.
        return ExampleRuntime(model_path, options)

    def infer(self, input_data: Any) -> Any:
        if self._closed or self._runtime is None:
            raise RuntimeError(
                "Inference backend is not initialized or is closed."
            )

        return self._runtime.run(input_data)


if __name__ == "__main__":
    print(
        "ExampleInferenceBackend is a scaffold, not a working model runtime. "
        "Integrate a real runtime before using it."
    )