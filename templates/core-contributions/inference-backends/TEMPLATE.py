"""
iSpy-FRC inference-backend contribution template.

This is a design scaffold, not a drop-in iSpy plugin. Inspect the current
model loader, inference dispatch, result types, metadata, conversion code,
and cleanup conventions before adapting it.

A core contribution must be integrated into the core repository. Copying this
file into the community templates repository does not enable it.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class YourInferenceBackend(ABC):
    """Outline for a runtime-specific inference adapter.

    Replace these illustrative signatures with the interfaces used by the
    current iSpy core implementation.
    """

    backend_name = "your_backend"
    supported_model_suffixes: tuple[str, ...] = ()

    def __init__(self, model_path: str | Path, **options: Any) -> None:
        self.model_path = Path(model_path)
        self.options = dict(options)
        self._closed = False
        self._runtime: Any = None

        if not self.model_path.is_file():
            raise FileNotFoundError(
                f"Model file does not exist: {self.model_path}"
            )

        suffix = self.model_path.suffix.lower()
        if (
            self.supported_model_suffixes
            and suffix not in self.supported_model_suffixes
        ):
            supported = ", ".join(self.supported_model_suffixes)
            raise ValueError(
                f"{self.backend_name} does not support {suffix!r}. "
                f"Supported suffixes: {supported}"
            )

        # Release any partially initialized resources if loading fails.
        try:
            self._runtime = self._load_runtime(
                self.model_path, self.options
            )
        except Exception:
            self.close()
            raise

    @classmethod
    def is_available(cls) -> tuple[bool, str]:
        """Return availability plus an actionable explanation."""
        return (
            False,
            "Implement runtime and device availability checks.",
        )

    @classmethod
    def validate_model(cls, model_path: str | Path) -> None:
        """Validate basic path/format requirements and runtime-specific details."""
        path = Path(model_path)

        if not path.is_file():
            raise FileNotFoundError(f"Model file does not exist: {path}")

        if (
            cls.supported_model_suffixes
            and path.suffix.lower() not in cls.supported_model_suffixes
        ):
            supported = ", ".join(cls.supported_model_suffixes)
            raise ValueError(
                f"Unsupported model suffix {path.suffix!r}; "
                f"expected: {supported}"
            )

    @abstractmethod
    def _load_runtime(
        self, model_path: Path, options: dict[str, Any]
    ) -> Any:
        """Create the runtime session/device context and load the model."""
        raise NotImplementedError

    @abstractmethod
    def infer(self, input_data: Any) -> Any:
        """Run inference and return data matching iSpy's existing result contract.

        Do not return raw tensors if the surrounding iSpy code expects decoded
        detections. Document preprocessing, output layout, and coordinate rules.
        """
        raise NotImplementedError

    def close(self) -> None:
        """Release runtime resources; safe to call more than once."""
        if self._closed:
            return

        runtime = self._runtime
        self._runtime = None
        self._closed = True

        if runtime is not None:
            self._release_runtime(runtime)

    def _release_runtime(self, runtime: Any) -> None:
        """Override for vendor-specific cleanup and activation scopes."""
        for method_name in ("close", "release"):
            method = getattr(runtime, method_name, None)
            if callable(method):
                method()
                return

    def __enter__(self) -> "YourInferenceBackend":
        if self._closed:
            raise RuntimeError("Cannot use a closed inference backend.")
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        self.close()