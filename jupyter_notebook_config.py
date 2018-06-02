# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from jupyter_core.paths import jupyter_data_dir
import subprocess
import os
import errno
import stat

c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False



# Notebook template folders
c.JupyterLabTemplates.template_dirs = ['./warren/faas/nbtemplates']

# Generate a self-signed certificate
if 'GEN_CERT' in os.environ:
    dir_name = jupyter_data_dir()
    pem_file = os.path.join(dir_name, 'notebook.pem')
    try:
        os.makedirs(dir_name)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(dir_name):
            pass
        else:
            raise
    # Generate a certificate if one doesn't exist on disk
    subprocess.check_call(['openssl', 'req', '-new',
                           '-newkey', 'rsa:2048',
                           '-days', '365',
                           '-nodes', '-x509',
                           '-subj', '/C=XX/ST=XX/L=XX/O=generated/CN=generated',
                           '-keyout', pem_file,
                           '-out', pem_file])
    # Restrict access to the file
    os.chmod(pem_file, stat.S_IRUSR | stat.S_IWUSR)
    c.NotebookApp.certfile = pem_file



def clear_cell_outputs(model, **kwargs):
    """scrub output before saving notebooks"""
    # only run on notebooks
    if model['type'] != 'notebook':
        return
    # and for version 4
    if model['content']['nbformat'] != 4:
        return
    for cell in model['content']['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['outputs'] = []
        cell['execution_count'] = None

c.FileContentsManager.pre_save_hook = clear_cell_outputs


# after all the cell output nodes are deleted and we have nice and lean
# Notebook JSON, we might also want to start a revision tracking
# on a conventional Python script.
# def script_post_save(model, os_path, contents_manager, **kwargs):
#     """convert notebooks to Python script after save with nbconvert

#     replaces `ipython notebook --script`
#     """
#     from nbconvert.exporters.script import ScriptExporter

#     if model['type'] != 'notebook':
#         return

#     global _script_exporter

#     if _script_exporter is None:
#         _script_exporter = ScriptExporter(parent=contents_manager)

#     log = contents_manager.log

#     base, ext = os.path.splitext(os_path)
#     py_fname = base + '.py'
#     script, resources = _script_exporter.from_filename(os_path)
#     script_fname = base + resources.get('output_extension', '.txt')
#     log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))

#     with io.open(script_fname, 'w', encoding='utf-8') as f:
#         f.write(script)

# c.FileContentsManager.post_save_hook = script_post_save