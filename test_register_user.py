from browser import Browser
from dotenv import load_dotenv
from login import login
from register_user import register_user, gen_fake_user
import os

load_dotenv()

def test_register_user():
    """TC 06 - Cadastrar novo usuário administrador."""
    browser = Browser()
    login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))
    assert register_user(browser)


def test_register_existing_user():
    """TC 07 - Cadastrar usuário já existente.

    O mesmo usuário é submetido duas vezes: o primeiro cadastro deve ser
    aceito e o segundo recusado, preservando a unicidade do e-mail (RF 05).
    """
    browser = Browser()
    login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))

    user = gen_fake_user()
    assert register_user(browser, user)
    assert not register_user(browser, user)

