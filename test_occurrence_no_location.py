from browser import Browser
from dotenv import load_dotenv
from login import login
import complaint
from os import getenv
import os

load_dotenv()


def test_occurrence_no_location():
    browser = Browser()
    login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))
    assert str(complaint.no_location(browser)) == getenv('TABLE_NO_LOCATION')


def test_occurrence_no_location_with_filter():
    """TC 08 - Aplicar filtro de busca por código."""
    browser = Browser()
    login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))
    assert complaint.no_location_with_filter(browser, getenv('TABLE_NO_LOCATION_FILTER')) == 1


def test_occurrence_no_location_with_invalid_filter():
    """TC 09 - Busca com código inexistente.

    Filtrar por um código que não corresponde a nenhuma ocorrência deve
    resultar em tabela sem linhas de dados (RF 06).
    """
    browser = Browser()
    login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))
    assert complaint.no_location_with_filter(browser, 'CODIGO-INEXISTENTE-0000') == 0
