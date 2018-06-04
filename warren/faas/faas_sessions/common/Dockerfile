FROM jupyter/scipy-notebook
MAINTAINER Jupyter Project <jupyter@googlegroups.com>



# Install Kernel Gateway
RUN pip install --upgrade pip && \
    pip install jupyter-kernel-gateway && \
    pip install docker

# fix permissions
#COPY fix-permissions /usr/local/bin/fix-permissions
#USER root
#RUN chmod a+x /usr/local/bin/fix-permissions && \
#    fix-permissions /home/jovyan/faas/faas_sessions
#USER jovyan
# add some files needed


RUN ls -la
# Configure container startup
#ENTRYPOINT ["cd /home/jovyan && ", "tini", "--", "jupyter-kernelgateway", "--KernelGatewayApp.api=notebook-http", "--KernelGatewayApp.ip=0.0.0.0"]
#CMD ["--KernelGatewayApp.port=7000", "--KernelGatewayApp.seed_uri=./faas/faas_sessions/" + $FAAS_SID + "/nb.ipynb"]
CMD ['jupyter-kernelgateway']

