from browser import Browser
from dotenv import load_dotenv
from login import login
from register_user import register_user
import os

load_dotenv()

def test_login():
    """TC 04 - Login com credenciais válidas."""
    browser = Browser()
    assert login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))


def test_login_invalid_credentials():
    """TC 05 - Login com credenciais inválidas.

    O acesso deve ser negado: login() retorna False quando o elemento
    indicativo de sessão autenticada não aparece após o envio do formulário.
    """
    browser = Browser()
    assert not login(browser, 'usuario.inexistente@teste.invalido', 'senha_invalida_123')