
# Vision Pipeline Contributions

Vision pipelines are part of the iSpy-FRC core codebase. These files are reference templates for developers who want to contribute new pipeline implementations.

## Important

**Adding a pipeline to this community repository does not install it into iSpy.** The pipeline must be integrated into the main iSpy-FRC repository and registered with the existing pipeline registry.

## Files

- `TEMPLATE.py` — starting point for a new pipeline.
- `example_pipeline.py` — minimal example that reads a frame and returns an empty detection list with that frame.

## Development Guidelines

1. Follow the actual `VisionPipeline` interface in `iSpy/vision/pipelines/base.py`.
2. Use `get_frame()` to obtain the current frame.
3. Implement `run()` so it returns `(objects, frame)`, including `([], None)` when no frame is available.
4. Return detections in the format expected by iSpy's existing pipelines.
5. Override `prepare()` when initialization is needed.
6. Override `destroy()` to release resources owned by your pipeline.
7. Add the new pipeline to the appropriate registry and integration points in the core repository.
8. Test with representative camera input and verify that existing pipelines continue to work.

## Configuration

Use the configuration patterns and schemas already established by existing pipelines. Do not assume that arbitrary constructor arguments or configuration fields are supported.

## Security and Reliability

- Validate configuration values before using them.
- Handle missing frames and unavailable models gracefully.
- Avoid blocking the vision loop with unnecessary work.
- Release models, threads, and other resources during shutdown.
- Do not load or execute untrusted community code automatically.
