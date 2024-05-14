
# Github actions
A really nice feature to have always is a fully automated platform which tests the code in multiple platforms at once. In this case we are using Github Actions to do so. The configuration is stored in the `.github/workflows` folder.

## Current workflows
Currently, there are 2 workflows:

- `docs.yml`: It deploys automatically a newly updated documentation to the `gh-pages` branch.
- ``main.yml`: It ensures the correctness of the code. It runs the full test suite in multiple platforms (Linux, MacOS, and Windows) and also checks the code style.

## Testing workflows locally
In the case that you want to change any of the workflows, instead of doing 1000 pull-requests or commits to try it out, it is possible (and recommended) to run the workflows locally. To do so, you need to install the `act` package. Refer to their [official documentation](https://nektosact.com/) for more information. With the command `act` you can run the workflows locally. That's all!

!!! tip
    The full command is: **`act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`**

!!! failure
    Currently, the default runner does not work. It is recommended to use the `ghcr.io/catthehacker/ubuntu:act-latest`. Therefore the full command is `act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest`. In this case the image is way larger... but it works. As well see this [Github notice](https://github.blog/changelog/2024-03-07-github-actions-all-actions-will-run-on-node20-instead-of-node16-by-default/).