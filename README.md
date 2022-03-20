# BTAlert-AI

[![Python Conda CI](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python-conda.yml/badge.svg)](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python-conda.yml)
[![Docker Image CI](https://github.com/BureauTech/BTAlert-AI/actions/workflows/docker-image.yml/badge.svg)](https://github.com/BureauTech/BTAlert-AI/actions/workflows/docker-image.yml)

## How to install

### Docker Image

To make it run on your machine without installing everything locally, you can simply run it via docker image, by following the commands below.

```docker build -t btalert-ai .```

```docker run btalert-ai```

NOTE: It's important to have [docker installed](https://docs.docker.com/engine/install/) on your machine.

### Locally

In case you want to run it in your machine without using docker, you must run the following commands.

```conda install --file requirements.txt --yes```

```conda run python src/main/app.py```

### Prerequisites:

You must have installed [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and [Python 3.8.10](https://www.python.org/downloads/release/python-3810/) previously.