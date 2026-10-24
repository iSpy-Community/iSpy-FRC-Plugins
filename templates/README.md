# iSpy-FRC Developer Templates

This directory contains templates and working examples for developers building extensions for iSpy-FRC.

The goal is to provide examples that use the real iSpy-FRC APIs, configuration schemas, lifecycle methods, and output conventions.

## Community Add-ons

These three add-on types are discovered by iSpy's plugin loader.

### Trackers

**Files:** `addons/trackers/`

Trackers process detections and can modify or return the detection list.

- `TEMPLATE.py` — starter class showing the required base class, configuration schema, and methods.
- `example_tracker.py` — a working example of a tracker.

Base class: `TrackerBase`

### Frame Processors

**Files:** `addons/frame_processors/`

Frame processors transform camera frames before or during the vision processing workflow.

- `TEMPLATE.py` — starter class showing the frame-processing API.
- `example_frame_processor.py` — a grayscale frame-processing example.

Base class: `FrameProcessorBase`

### Utilities

**Files:** `addons/utilities/`

Utilities provide supporting functionality, process per-tick frame data, and can publish additional runtime outputs.

- `TEMPLATE.py` — starter class showing configuration, lifecycle methods, and output publishing.
- `example_utility.py` — a working utility example.

Base class: `UtilityBase`

## Core Contributions

The following categories are useful for developers extending iSpy itself. They are not currently loaded as arbitrary third-party add-ons simply by placing a file in this community repository.

### Vision Pipelines

**Files:** `core-contributions/vision-piplines/`

Vision pipelines implement vision algorithms and produce detections and processed frames.

- `TEMPLATE.py` — a starter implementation based on the actual `VisionPipeline` interface.
- `example_pipeline.py` — a working example designed to be integrated into iSpy's core pipeline registry.

Existing registered pipelines include object detection, AprilTag detection, depth estimation, optical flow, QR code detection, and YOLO-World.

**Important:** New pipelines currently require integration with iSpy's core code and pipeline registry. A file in this community repository will not automatically register a new pipeline.

### Camera Backends

**Files:** `core-contributions/camera-backends/`

Camera backends integrate new camera sources with iSpy.

- `TEMPLATE.py` — a starter implementation based on the actual `CameraBase` interface.
- `example_camera.py` — a camera-backend example for core integration.

New camera types currently need to be registered in iSpy's core camera registry.

### Inference Backends

**Files:** `core-contributions/inference-backends/`

Inference backends connect iSpy-FRC's model and inference layer to a runtime or hardware accelerator (e.g., ONNX Runtime, TensorRT, RKNN).

- `TEMPLATE.py` — implementation outline for a new core inference backend.
- `example_backend.py` — runtime-neutral example showing lifecycle and error handling.

These are **design scaffolds only**, not drop-in plugins. Integration requires changes to iSpy's model loader, inference dispatch, and hardware detection code.

## How to Use These Templates

1. Read the relevant category's README, if provided.
2. Start with `TEMPLATE.py` to understand the expected class structure and methods.
3. Study the corresponding working example.
4. Develop and test against the actual iSpy-FRC source code.
5. Follow the project's contribution guidelines when submitting changes.

Do not assume a template is installable as a third-party extension unless its category explicitly supports dynamic loading.

## Important Security Note

Community plugins contain executable Python code. Loading a plugin can execute that code with the privileges of the iSpy process. Listing a plugin in this repository does not certify that it is safe, and it does not sandbox the plugin.

Review third-party code and its dependencies before running it.

## Compatibility

Templates should match the current iSpy-FRC implementation. If a base class, required method, configuration schema, or output contract changes, update the corresponding template and example.

Each example should be tested against the actual interface it demonstrates rather than relying on assumed behavior.