"""Sphinx configuration for GEOMETOR • altshiller-court."""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

from photon_platform.publish.global_conf import *  # noqa: E402, F403
import geometor.altshiller_court as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "altshiller-court"
repo_name = "altshiller-court"

setup_globals(org, org_name, repo, repo_name)

autoapi_dirs = [os.path.abspath("../src/geometor")]
if "modules/api/geometor/altshiller_court/index.rst" not in exclude_patterns:
    exclude_patterns.append("modules/api/geometor/altshiller_court/index.rst")

project = "GEOMETOR • altshiller-court"
author = "Nathan Altshiller-Court • Digital Edition GEOMETOR"
copyright = "1952 Nathan Altshiller-Court; 2007 Dover Publications • Digital Apparatus GEOMETOR"
