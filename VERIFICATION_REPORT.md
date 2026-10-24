# iSpy-FRC-Plugins Templates Verification Report

**Verified against:** iSpy-FRC local repository (deploy branch equivalent) at `C:\Users\Aidan\Documents\Vscode\iSpy-FRC\iSpy-FRC\`

**Date:** 2026-10-24

---

## Summary

All templates and examples have been verified against the actual iSpy-FRC source code. **Critical issues have been fixed.**

| Category | Template Status | Example Status | Issues Found & Fixed |
|----------|-----------------|----------------|----------------------|
| Trackers | ✅ Accurate | ✅ Accurate | None |
| Frame Processors | ✅ Accurate | ✅ Accurate | Fixed doc reference in README |
| Utilities | ✅ Fixed | ✅ Accurate | Added missing `validate_output_key` import |
| Vision Pipelines | ✅ Accurate | ✅ **Fixed** | Fixed wrong constructor signature; renamed file |
| Camera Backends | ✅ Accurate | ✅ Fixed | Removed unused `plugin_name`; fixed config schema type |
| Inference Backends | ✅ Design scaffold | ✅ Design scaffold | Added to main README |

---

## Detailed Findings

### 1. Trackers (`templates/addons/trackers/`)

**Base class:** `iSpy.plugins.bases.TrackerBase` (extends `AddonBase`)

**Template (`TEMPLATE.py`):** ✅ **ACCURATE**
- Correctly inherits from `TrackerBase`
- Correct `plugin_name` attribute
- Correct `config_schema()` classmethod
- Correct `__init__(self, context: dict)` with `super().__init__(context)`
- Correct `start()`, `update()`, `stop()` method signatures
- `update()` signature matches base: `update(self, detections, robot_x, robot_y, robot_yaw, robot_z: float = 0.0)`

**Example (`example_tracker.py`):** ✅ **ACCURATE**
- Properly implements `ConfidenceFilterTracker`
- Correctly filters detections by confidence
- Uses `getattr(detection, "confidence", 0.0)` which matches iSpy's `Object` class

---

### 2. Frame Processors (`templates/addons/frame_processors/`)

**Base class:** `iSpy.plugins.bases.FrameProcessorBase` (extends `AddonBase`)

**Template (`TEMPLATE.py`):** ✅ **ACCURATE**
- Correctly inherits from `FrameProcessorBase`
- Correct `config_schema()` with `"toggle"` type
- Correct `process(self, frame)` method signature
- Properly returns original frame when disabled

**Example (`example_frame_processor.py`):** ✅ **ACCURATE**
- Implements `GrayscaleFrameProcessor` correctly
- Handles various channel configurations (1, 3, 4 channels)
- Returns 3-channel BGR for downstream compatibility
- Uses `cv2.cvtColor` appropriately

**Fixed:** 
- `templates/README.md` line 29: Changed reference from `example_grayscale.py` to `example_frame_processor.py`

---

### 3. Utilities (`templates/addons/utilities/`)

**Base class:** `iSpy.plugins.bases.UtilityBase` (extends `AddonBase`)

**Template (`TEMPLATE.py`):** ✅ **FIXED**
- Added missing import: `from iSpy.plugins.bases import UtilityBase, validate_output_key`
- The commented example code references `validate_output_key` which is now imported

**Example (`example_utility.py`):** ✅ **ACCURATE**
- Correctly implements `DetectionCountUtility`
- Properly uses `self.publish_output(frame_data, count, output_key=self.output_key)`
- Handles `frame_data.get("detections", [])` correctly
- Validates `output_key` as string in `__init__`

---

### 4. Vision Pipelines (`templates/core-contributions/vision-piplines/`)

**Base class:** `iSpy.vision.pipelines.base.VisionPipeline` (extends `Camera` + `VisionBase`)

**Template (`TEMPLATE.py`):** ✅ **ACCURATE**
- Correct constructor: `__init__(self, camera_config, input_size, grayscale)`
- Correctly calls `super().__init__(camera_config, input_size, grayscale)`
- Correct method stubs: `prepare()`, `run()`, `destroy()`
- `run()` correctly returns `(objects, frame)` tuple
- Uses `self.get_frame()` to obtain frame

**Example (`example_pipeline.py`):** ✅ **FIXED**
- **Was:** Wrong constructor signature `__init__(self, camera_config, config, core_mask=None)`
- **Now:** Correct signature `__init__(self, camera_config, input_size, grayscale)` matching `VisionPipeline` base
- **Was:** Hardcoded `(640, 480)` instead of using `input_size` parameter
- **Now:** Properly passes `input_size` and `grayscale` to super
- **Fixed:** Renamed file from `example_pipline.py` to `example_pipeline.py` (typo fix)

**Additional notes on VisionPipeline:**
- The base class provides `get_frame()`, `calibration_status()`, `is_ready()`, `get_health()`, `serialize_detections()`
- Pipelines must return `(list[Object], frame)` from `run()`
- The `Camera` base provides `get_frame()`, `destroy()`, `start()`, `stop()`

---

### 5. Camera Backends (`templates/core-contributions/camera-backends/`)

**Base class:** `iSpy.vision.Cameras.base.CameraBase`

**Template (`TEMPLATE.py`):** ✅ **ACCURATE**
- Correct constructor signature matching `CameraBase.__init__`
- Correct `camera_type` class attribute
- Correct `config_schema()` and `discover()` classmethods
- Properly calls `super().__init__(camera_config, input_size=input_size, grayscale=grayscale, **kwargs)`

**Example (`example_camera.py`):** ✅ **FIXED**
- **Removed:** `plugin_name = "example"` (not used by CameraBase; only `camera_type` is used)
- **Fixed:** Config schema type from `"source"` to `"text"` (valid schema types are: "text", "number", "toggle", "list", "range")
- **Fixed:** Default value from `0` to `"0"` (string type)

**Note on `config_schema` types:** The base `AddonBase` only recognizes these types: `text`, `number`, `toggle`, `list`, `range`. Custom types like `"source"` are not handled by the config UI.

---

### 6. Inference Backends (`templates/core-contributions/inference-backends/`)

**Status:** These are **design scaffolds**, not tied to a specific base class in the current iSpy-FRC codebase.

**Template (`TEMPLATE.py`):** Design outline with abstract base class `YourInferenceBackend`
- Defines lifecycle: `__init__`, `is_available`, `validate_model`, `_load_runtime`, `infer`, `close`
- Includes context manager support (`__enter__`, `__exit__`)

**Example (`example_backend.py`):** Runtime-neutral example showing lifecycle and error handling
- Not a real accelerator implementation
- Demonstrates structure only

**Added:** Documentation in main `templates/README.md` for this category

---

## Verification of Base Class Interfaces

### TrackerBase
```python
class TrackerBase(AddonBase):
    def __init__(self, context: dict): ...
    def start(self): ...
    def update(self, detections, robot_x, robot_y, robot_yaw, robot_z: float = 0.0): ...
    def stop(self): ...
```

### FrameProcessorBase
```python
class FrameProcessorBase(AddonBase):
    def __init__(self, context: dict): ...
    def start(self): ...
    def process(self, frame): ...
    def stop(self): ...
```

### UtilityBase
```python
class UtilityBase(AddonBase):
    def __init__(self, context: dict): ...
    def start(self): ...
    def update(self, frame_data: dict): ...
    def declared_output_key(self) -> str | None: ...
    def publish_output(self, frame_data: dict, value, output_key: str | None = None) -> bool: ...
    def stop(self): ...
```

### VisionPipeline
```python
class VisionPipeline(Camera, VisionBase):
    def __init__(self, camera_config, input_size, grayscale): ...
    def prepare(self): ...
    def run(self) -> tuple[list, np.ndarray]: ...  # returns (objects, frame)
    def destroy(self): ...
    def get_frame(self) -> np.ndarray | None: ...
    def is_ready(self) -> tuple[bool, str]: ...
    def get_status(self) -> str: ...
    def get_health(self) -> dict: ...
    def calibration_status(self) -> tuple[str, str | None]: ...
```

### CameraBase
```python
class CameraBase:
    camera_type = "generic"
    @classmethod
    def config_schema(cls) -> dict: ...
    @classmethod
    def discover(cls, claimed_sources: set | None = None) -> list[dict]: ...
    def __init__(self, camera_config, input_size: tuple | None = None, grayscale: bool = False, **kwargs): ...
    def get_frame(self) -> np.ndarray | None: ...
    def destroy(self): ...
    def start(self): ...
    def is_ready(self) -> tuple[bool, str]: ...
```

---

## Changes Made

### Files Modified

1. **`templates/core-contributions/vision-piplines/example_pipeline.py`** (renamed from `example_pipline.py`)
   - Fixed constructor signature to match `VisionPipeline.__init__(self, camera_config, input_size, grayscale)`
   - Removed hardcoded `(640, 480)` and redundant `self.config` assignment

2. **`templates/addons/utilities/TEMPLATE.py`**
   - Added import: `from iSpy.plugins.bases import UtilityBase, validate_output_key`

3. **`templates/core-contributions/camera-backends/example_camera.py`**
   - Removed unused `plugin_name` attribute
   - Changed config schema type from `"source"` to `"text"`
   - Changed default value from `0` to `"0"`

4. **`templates/README.md`**
   - Fixed Frame Processor example reference: `example_grayscale.py` → `example_frame_processor.py`
   - Fixed Vision Pipelines directory path: `vision_pipelines` → `vision-piplines`
   - Fixed Camera Backends directory path: `camera_backends` → `camera-backends`
   - Added Inference Backends section

---

## Conclusion

All templates and examples now **accurately reflect the actual iSpy-FRC APIs** as of the verified codebase. The critical bug in the Vision Pipeline example (wrong constructor signature) has been fixed, along with several minor issues. The templates are ready for developers to use as accurate starting points for building iSpy-FRC extensions.