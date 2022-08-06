# syntax = edrevo/dockerfile-plus
# For more information, please refer to https://aka.ms/vscode-docker-python
INCLUDE+ .sharedcontainer/Dockerfile.python_version
FROM python:${PYTHON_VERSION}

INCLUDE+ .sharedcontainer/Dockerfile.environment_variables

# Install pip requirements
INCLUDE+ .sharedcontainer/Dockerfile.requirements_install

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]
