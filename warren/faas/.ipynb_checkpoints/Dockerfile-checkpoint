# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
#FROM ubuntu:xenial-20180228@sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6
FROM jupyter/scipy-notebook
MAINTAINER Jupyter Project <jupyter@googlegroups.com>

# Install Kernel Gateway
RUN pip install jupyter-kernel-gateway docker
ADD wrnaz wrnaz
ADD faas.ipynb faas.ipynb
ADD foo.ipynb foo.ipynb
# Configure container startup
#ENTRYPOINT ["jupyter-kernelgateway"]
ENTRYPOINT ["tini", "--", "jupyter-kernelgateway", "--KernelGatewayApp.api=notebook-http", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=7777"]
CMD ["--KernelGatewayApp.seed_uri=./faas.ipynb"]
## RUN pwd && ls -la
## RUN jupyter-kernelgateway --KernelGatewayApp.api=notebook-http --KernelGatewayApp.ip=0.0.0.0 --KernelGatewayApp.port=7777 --NotebookHTTPPersonality.allow_notebook_download=True --KernelGatewayApp.seed_uri=./faas.ipynb
