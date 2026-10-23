# Contributing to iSpy-FRC Community Plugins

Thank you for helping grow the iSpy-FRC plugin ecosystem! This directory helps users discover community-built plugins while allowing developers to maintain control of their own projects.

## How It Works

- You maintain your plugin in your own GitHub repository.
- This directory contains listings that point to your repository.
- Users install plugins using the installation method documented by each plugin.
- Submissions are reviewed before they are added to the directory.
- Listing a plugin does not mean that iSpy-FRC guarantees its safety or functionality.

## Requirements for Listed Plugins

Before submitting a plugin, make sure it meets these requirements.

### 1. Public Repository

Your plugin must have a publicly accessible source repository so users and maintainers can inspect its code.

### 2. Documentation

Include a README explaining:

- What the plugin does.
- Which iSpy-FRC versions it supports.
- How to install and configure it.
- Which permissions, network connections, files, or external services it requires.
- Any dependencies or system requirements.
- How to report bugs or security concerns.

### 3. Compatibility

Explain which iSpy-FRC plugin interfaces and versions your plugin supports. Do not claim compatibility that you have not tested.

### 4. Configuration

Document the plugin's configuration options, including required fields, optional fields, defaults, and validation rules.

### 5. Security

Plugins must not conceal their behavior or perform unrelated actions without the user's knowledge.

Document sensitive operations, including access to credentials, local files, cameras, networks, and external services.

Never commit passwords, API keys, access tokens, or other secrets to your repository.

### 6. Maintenance

Identify a maintainer and provide a way to report issues. Indicate whether the plugin is actively maintained or archived.

## How to Submit a Plugin

1. Fork this repository.
2. Edit `README.md` and add your plugin under **Browse Plugins**.
3. Include the plugin name, a short description, a link to its source repository, supported iSpy-FRC versions, and installation documentation.
4. Open a pull request against this repository.
5. Explain what your plugin does and confirm that you have reviewed these guidelines.
6. Respond to review feedback.

Please keep each submission focused on one plugin.

## Listing Format

Use this format when adding a plugin to the directory:

```markdown
### Plugin Name

- **Description:** A clear explanation of what the plugin does.
- **Repository:** https://github.com/OWNER/REPOSITORY
- **Compatibility:** Tested iSpy-FRC versions.
- **Installation:** Link to installation instructions.
- **Permissions:** Important access requirements.
- **Maintenance:** Active, limited, or archived.
```

Replace all example values with accurate information. Do not submit placeholders as though they were verified facts.

## Review Process

Maintainers may check:

- Whether the repository exists and is accessible.
- Whether the documentation is sufficient.
- Whether the plugin identifies its compatibility requirements.
- Whether installation and configuration instructions are understandable.
- Whether the plugin's stated permissions match its documented purpose.
- Whether obvious security, privacy, or supply-chain concerns need further review.

A review is not a guarantee that a plugin is secure, bug-free, or suitable for every environment.

Maintainers may request changes, decline a submission, or remove a listing if it becomes misleading, unmaintained, or presents unacceptable risks.

## Reporting Security Issues

Do not publish sensitive vulnerability details in a public issue or pull request.

Contact the plugin's maintainer through their documented private security-reporting channel. For issues affecting the core iSpy-FRC project, use the reporting instructions provided by that project.

## Questions

For questions about this directory, open an issue in this repository.

Thank you for contributing to iSpy-FRC!
