# API - Receitas dos Chefs

## Api Criada em Django Rest Framework.

### Como Desenvolver?
1. Clone o repositório.
2. Crie um virtualenv com Python 3.9
3. Ative o virutalenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes
7. Rode as Migrações
8. Crie um Super Usuario
9. Rode o Servidor django
10. Acesse o Django Admin
11. Adicione uma nova application, marcando as opções:
> Client type: Confidential
> Authorization grant type: Resource owner password-based
12. Use o "Client id" e o "Client secret" para fazer a autenticação.

````console
git clone https://github.com/Sidneyasjr/Receitas-dos-Chefs.git
cd Receitas-dos-Chefs
python -m venv .receitas-chefe
source .receitas-chefe/bin/activate
pip install -r requirements-dev.txt
cp contrib/env.example .env
python manage.py test
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````

### Documentação
https://documenter.getpostman.com/view/14846437/TzCHAA2j





