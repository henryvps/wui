# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
#FROM ubuntu:xenial-20180228@sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6
FROM jupyter/scipy-notebook
MAINTAINER Jupyter Project <jupyter@googlegroups.com>


# Install Kernel Gateway
RUN pip install jupyter-kernel-gateway docker

# add some files needed
COPY wrnaz wrnaz
COPY faas.ipynb faas.ipynb
COPY foo.ipynb foo.ipynb
RUN ls -la && pwd
COPY fix-permissions /usr/local/bin/fix-permissions

# fix permissions
USER root
RUN chmod a+x /usr/local/bin/fix-permissions && \
    fix-permissions /home/jovyan/work
RUN ls -la && pwd
USER jovyan

# Configure container startup
ENTRYPOINT ["tini", "--", "jupyter-kernelgateway", "--KernelGatewayApp.api=notebook-http", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=7777"]
CMD ["--KernelGatewayApp.seed_uri=./faas.ipynb"]


