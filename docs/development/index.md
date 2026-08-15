# Development
!!! info
    This project is open-source and it is run without any funding. It relies entirely on the good will of the maintainers and their limited free time. Please, feel free to do a PR doing any feature you may want.

This section is intended for anyone who wants to get involve on the development of the library. All PR are welcome! :stars: The only requisite is that the code is clear enough, has a well-defined goal, and it has the corresponding testing (whenever possible). Maintainers are more than welcome to help with anything you need :smiley:.

We encourage you to read the [conventions section](conventions.md). The following is a short summary of how to submit a pull request.

!!! note
    Install Python and `uv` before working on the project. Docker is required only for container-based checks.

1. Fork the project.
2. Develop the code: code + **tests**.
3. Document the feature/change.
4. Run the checks with `uv run invoke tests --local`.
5. If everything passes, submit it for code review.

!!! tip
    Code review may take from a day to a few weeks. Keep each pull request focused so it can be reviewed independently.
