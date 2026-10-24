# Inference Backend Contributions

Inference backends connect iSpy-FRC's model and inference layer to a runtime or hardware accelerator. Examples include ONNX Runtime execution providers, vendor-specific runtimes, and accelerator-specific model formats.

These are **core-contribution reference files**, not an installable plugin package. Adding files here does not enable a backend in iSpy-FRC by itself.

## Identify the Contribution Type

1. **New runtime or accelerator** — support a runtime or hardware target not currently supported.
2. **Existing backend improvement** — fix detection, preprocessing, postprocessing, cleanup, compatibility, or errors in an existing implementation.
3. **Model conversion/export** — add or improve conversion from a source model to a runtime-supported format.
4. **Packaging or device detection** — improve dependency guidance, hardware detection, or diagnostics.

Check the current iSpy-FRC code before starting. Avoid creating a second backend when the existing implementation can be extended safely.

## Before Coding

1. Find the model loader, inference dispatch, metadata handling, model validation, conversion/export code, hardware detection, and cleanup paths.
2. Verify which model formats and runtimes are already supported. Incomplete documentation does not prove a format is unsupported.
3. Identify the existing inference-result contract. Preserve result types, coordinate conventions, class IDs, confidence scores, and image-size semantics.
4. Check vendor SDK, driver, compiled-artifact, and platform-specific package requirements.
5. Discuss major architecture changes in an issue before opening a large pull request.

## Files

- `TEMPLATE.py` — implementation outline for a new core inference backend.
- `example_backend.py` — runtime-neutral example showing lifecycle and error handling.

The example is intentionally not a real accelerator implementation and is not automatically registered with iSpy-FRC.

## Integration Checklist

A complete contribution may need changes in several places. Confirm the actual current interfaces rather than copying paths or names blindly.

- [ ] Backend selection and model-format detection
- [ ] Model loading and validation
- [ ] Input preprocessing: layout, dtype, normalization, resizing, and color order
- [ ] Runtime invocation and output extraction
- [ ] Output decoding/postprocessing into iSpy's existing result contract
- [ ] Model metadata and sidecar handling, if applicable
- [ ] Model conversion/export workflow, if applicable
- [ ] Hardware and dependency detection with actionable diagnostics
- [ ] Configuration and user-facing documentation
- [ ] Cleanup after normal shutdown and partial initialization failure
- [ ] Tests for supported behavior and failure paths
- [ ] Verification on target hardware, or an explicit note that hardware testing was unavailable

Not every backend needs every item. Explain which items do not apply and why.

## Document the Input/Output Contract

State these explicitly:

- Input shape and layout, such as NHWC or NCHW
- Channel order and preprocessing
- Input dtype, normalization, and value range
- Output tensor names, shapes, dtypes, and meaning
- Whether outputs are raw predictions or already-decoded/NMS-filtered detections
- Coordinate order and units, such as pixels or normalized coordinates
- Supported tasks, model versions, batch sizes, and input resolutions

Do not infer output format from shape alone when reliable metadata is available. If the format cannot be determined safely, fail with an actionable error rather than silently producing incorrect detections.

## Reliability and Security

- Validate model paths and configuration before opening hardware resources.
- Treat model files, metadata, and runtime outputs as potentially malformed.
- Do not download or execute remote code automatically.
- Do not silently fall back to CPU after explicit hardware selection unless existing iSpy behavior specifies it and reports it.
- Do not log credentials, tokens, or sensitive connection details.
- Release resources after normal shutdown and partial initialization failure.
- Do not swallow exceptions that indicate a broken backend contract.
- Keep vendor dependencies optional; importing iSpy should not fail because an unrelated SDK is missing.
- Do not claim acceleration is active merely because a device is detected. Report the runtime/provider actually selected when possible.

## Testing Expectations

At minimum, cover:

1. Backend selection and unsupported-format errors.
2. Missing runtime dependency or unavailable device.
3. Model-load failure and malformed metadata.
4. A representative inference result with known expected output.
5. Preprocessing and coordinate/postprocessing correctness.
6. Cleanup after successful initialization.
7. Cleanup after partial initialization failure.
8. Unexpected output shapes or dtypes.

Prefer deterministic fixtures and mocked runtime objects for unit tests. Document hardware tests separately when they require a specific accelerator or vendor SDK.

## Pull Request Description

Include runtime, device, driver, and SDK versions; operating systems and architectures tested; supported model formats and tasks; conversion requirements; input/output contract; benchmark conditions; known limitations; and reproducible test steps.

Benchmarks should compare equivalent models, resolutions, precision, and preprocessing. Explain any material differences.