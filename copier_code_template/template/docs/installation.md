# Installation

## Create environment

```bash
conda create -n [[package_name]] python=[[python_version]]
conda activate [[package_name]]
```

## Install

```bash
pip install -e ".[docs]"
```

!!! note
    The `[docs]` extra installs MkDocs and mkdocstrings for building documentation locally.
    Omit it for a minimal install: `pip install -e .`
