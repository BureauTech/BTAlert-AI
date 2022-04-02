[![License](http://img.shields.io/github/license/BureauTech/BTAlert-AI)](https://github.com/BureauTech/BTAlert-AI/blob/main/LICENSE)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/BureauTech/BTAlert-AI/)
[![Python Conda CI](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python-conda.yml/badge.svg)](https://github.com/BureauTech/BTAlert-AI/actions/workflows/python-conda.yml)
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

```conda install --file requirements.txt --yes```

```conda run python src/app.py```

For production environment:

```bash setup-env.sh docker```

```conda install --file requirements.txt --yes```

Go to the ```src``` directory and run:

```gunicorn --bind 0.0.0.0:5000 app:app```

### Prerequisites:

You must have installed [Miniconda](https://docs.conda.io/en/latest/miniconda.html), [Python 3.7.11](https://www.python.org/downloads/release/python-3711/) and [MariaDB 10.3.x](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.3.34) previously.
