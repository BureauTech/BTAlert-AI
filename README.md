[![License](http://img.shields.io/github/license/BureauTech/BTAlert-AI)](https://github.com/BureauTech/BTAlert-AI/blob/main/LICENSE)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/BureauTech/BTAlert-AI/)
[![Python CI](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python.yml/badge.svg)](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python.yml)
[![Docker Image CI](https://github.com/BureauTech/BTAlert-AI/actions/workflows/docker-image.yml/badge.svg)](https://github.com/BureauTech/BTAlert-AI/actions/workflows/docker-image.yml)

# BTAlert-AI

## How to install

### Docker Image

To make it run on your machine without installing everything locally, you can simply run it via docker image, by following the commands below.

```docker compose up```

NOTE: It's important to have [docker installed](https://docs.docker.com/engine/install/) on your machine.

### Locally

In case you want to run it in your machine without using docker, you must run the following commands.

For development environment:

```bash setup-env.sh```

```pip install -r requirements.txt```

```python src/app.py```

### Prerequisites:

You must have installed [Python 3.7.11](https://www.python.org/downloads/release/python-3711/) previously.
