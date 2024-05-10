import os
from datetime import datetime
import pytest

# @pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Génération du rapport excel
    config.option.excelreport = True

    # Génération du rapport excel
    config.option.excelpath = 'reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".xlsx"