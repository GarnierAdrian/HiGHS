from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "highspy"
copyright = "2026, HiGHS"
author = "HiGHS"
release = "1.14.0"

base_dir = Path(__file__).parents[3]
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    #    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

autodoc_member_order = "bysource"
autodoc_mock_imports = ["highspy._core"]
autodoc_typehints = "description"

highspy_dir = base_dir / "highs" / "highspy"
autoapi_dirs = [highspy_dir]

autoapi_type = "python"
html_theme = "furo"
html_static_path = ["_static"]


def process_signature(app, what, name, obj, options, signature, return_annotation):
    if name.endswith("addVariables"):
        return "(*nvars, **kwargs)", None


def setup(app):
    app.connect("autodoc-process-signature", process_signature)
