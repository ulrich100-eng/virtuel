import os
from datetime import datetime
import pytest

# @pytest.hookimpl(tryfirst=True)


def pytest_configure(config):
    # to remove environment section
    config._metadata = None

    if not os.path.exists('repportsocm'):
        os.makedirs('repportsocm')

    # Définition du titre du rapport
    config.option.htmlpath = 'repportsocm/' + \
        datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

    # Modification de la valeur par défaut de --self-contained-html
    config.option.self_contained_html = True

    # Génération du rapport excel
    config.option.excelreport = True

    # Génération du rapport excel
    config.option.excelpath = 'repportsocm/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".xlsx"
