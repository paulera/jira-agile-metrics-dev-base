#!./venv/bin/python
import pathlib
import sys
import os

agilemetricspath = str(pathlib.Path(__file__).parent.resolve())
path = os.path.join(agilemetricspath, 'jira-agile-metrics')

sys.path.insert(0, path)
from jira_agile_metrics.cli import main
main()
sys.path.remove(path)
