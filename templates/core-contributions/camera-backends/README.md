
# Camera Backend Contributions

Camera backends connect iSpy-FRC to image sources, such as physical cameras or other supported video inputs.

These templates are reference material for developers contributing new camera backends to the iSpy-FRC core repository.

## Important

**Adding a camera backend to this community repository does not install it into iSpy.** New backends must be integrated into the core codebase and registered with its camera-backend registry.

## Files

- `TEMPLATE.py` — starting point for a new camera backend.
- `example_camera.py` — example implementation for reference.

## Development Guidelines

1. Inspect the existing camera interface in `iSpy/vision/Cameras/base.py`.
2. Follow the method signatures and lifecycle expected by the existing camera classes.
3. Handle unavailable cameras and failed frame reads gracefully.
4. Preserve the frame format and dimensions expected by the rest of the vision system.
5. Release camera handles and other resources during shutdown.
6. Register the backend in the appropriate core registry.
7. Test initialization, frame acquisition, failure handling, and cleanup.

## Configuration

Use the configuration conventions established by existing camera backends. Document required settings, optional settings, and their defaults.

## Security and Reliability

- Validate camera configuration before opening resources.
- Avoid blocking the vision loop unnecessarily.
- Handle disconnections and read failures safely.
- Do not expose credentials or sensitive connection details in logs.
- Do not load or execute untrusted community code automatically.
