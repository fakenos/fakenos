# Based on https://github.com/astral-sh/uv-docker-example/

# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:alpine

# Setup a non-root user
RUN addgroup -S -g 456 nonroot \
 && adduser -S -u 456 -G nonroot -D -s /bin/sh -h /home/nonroot -k /etc/skel nonroot \
 && mkdir -p /home/nonroot/.cache/uv \
 && chown -R nonroot:nonroot /home/nonroot \
 && chmod -R 755 /home/nonroot

ENV HOME=/home/nonroot


# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Use the non-root user to run our application
USER nonroot

CMD ["fakenos", "-i", "/app/docker/inventory.yaml"]