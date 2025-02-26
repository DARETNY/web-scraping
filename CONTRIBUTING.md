# Contributing to Web Scraping Project

Thank you for considering contributing to our web scraping project! We welcome contributions from the community to help improve and expand the project. Please follow the guidelines below to ensure a smooth and collaborative contribution process.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Submitting Changes](#submitting-changes)
5. [Reporting Issues](#reporting-issues)
6. [Contact](#contact)

## Code of Conduct

We expect all contributors to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the standards of behavior we expect from everyone participating in the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by opening an issue on our [GitHub repository](https://github.com/DARETNY/web-scraping/issues). Provide as much detail as possible, including steps to reproduce the bug and any relevant error messages.

### Suggesting Enhancements

We welcome suggestions for new features and improvements. Please open an issue on our [GitHub repository](https://github.com/DARETNY/web-scraping/issues) and describe your idea in detail. If possible, include examples of how the enhancement would be used.

### Submitting Pull Requests

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bugfix:
   ```sh
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them with clear and descriptive commit messages.
4. Push your changes to your forked repository:
   ```sh
   git push origin feature/your-feature-name
   ```
5. Open a pull request on the main repository and provide a detailed description of your changes.

## Setting Up the Development Environment

To set up the development environment, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DARETNY/web-scraping.git
   cd web-scraping
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```sh
   playwright install
   ```

## Submitting Changes

Before submitting your changes, please ensure that you have:

1. Followed the coding style and conventions used in the project.
2. Written or updated tests to cover your changes.
3. Run the tests to ensure that they pass:
   ```sh
   pytest
   ```

## Reporting Issues

If you encounter any issues while using the project, please report them by opening an issue on our [GitHub repository](https://github.com/DARETNY/web-scraping/issues). Provide as much detail as possible to help us understand and resolve the issue.

