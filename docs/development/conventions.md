# Conventions
This sections is intended to briefly explain all the tools used inside the project. Those tools are mainly there to ensure that the code is correctly written and tested.

## General: Poetry
Poetry is a tool for managing Python dependencies and packaging projects. It simplifies the process of managing dependencies by providing a consistent and declarative way to specify them in a `pyproject.toml` file. Poetry also handles virtual environment creation, package building, and publishing. It's often preferred by developers for its ease of use and integration with other tools in the Python ecosystem.

All the configurations for the project can be found ion the `pyproject.toml`. Here are some basic commands:

- `poetry install`: use it to install all the dependencies.
- `poetry update`: use it to update the dependencies.
- `poetry shell`: it enters the shell created using poetry install.

## Tests: Pytest
Pytest is a testing framework for Python that makes it easy to write simple and scalable tests. It allows you to write test cases as regular Python functions, using assertions to verify expected outcomes. Pytest provides powerful features such as fixtures for setting up test environments, parameterized testing, and plugins for extending functionality. It's widely used in the Python community due to its simplicity, flexibility, and extensive ecosystem of plugins.

To run the tests do the following:
```bash
pytest
```

## Security check: Bandit
Bandit is a security tool for Python code that detects common security issues and vulnerabilities. It analyzes Python code statically to identify potential security threats such as insecure use of modules, unsafe function calls, and potential security risks. Bandit provides a set of plugins that check for various security issues and can be easily integrated into development workflows, helping developers identify and fix security issues early in the development process. It's a valuable tool for improving the security posture of Python applications and libraries.

To run the bandit tool do the following:
```bash
bandit -c pyproject.toml -r .
```

## Basic formatting: Black
Black is a Python code formatter that automatically formats your Python code according to a strict set of formatting rules. It ensures consistent code style across a project by automatically applying formatting such as indentation, line length, and spacing. Black follows the principle of "code formatting without configuration," meaning it applies its formatting rules uniformly without requiring any manual configuration or adjustment. It's often used to enforce a consistent code style in Python projects and to save developers time by automating the code formatting process.

To run the black tool do the following:
```bash
black .
```

## Code complexity and compliance: Flake8
Flake8 is a popular Python tool that combines multiple Python linting and style checking tools into a single package. It runs several checks on Python code for potential errors, code style violations, and adherence to PEP 8 style guidelines. Flake8 integrates tools like PyFlakes, pycodestyle (formerly known as pep8), and McCabe complexity checker, allowing developers to catch errors and enforce coding standards in their Python codebase. It's commonly used as a part of the development workflow to maintain code quality and readability.

To run flake8 do the following:
```bash
pylint
```

## Code coverage: coverage
Coverage is a tool used in software development to measure the extent to which the source code of a program is executed during testing. It helps developers understand how thoroughly their tests exercise the codebase by providing metrics on code coverage, typically expressed as a percentage. Coverage tools track which lines or branches of code are executed during tests and generate reports highlighting areas that are covered and those that are not. This information enables developers to identify untested code paths and improve the effectiveness of their testing efforts.

To run coverage in conjuntion with pytest do the following:
```bash
coverage run -m pytest
```

It will generate a report which can look in `coverage report -m` or `coverage html`.