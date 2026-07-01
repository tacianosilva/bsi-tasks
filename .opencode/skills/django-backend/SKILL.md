---
name: django-backend
description: Use ao desenvolver projetos Django e Django REST Framework nas disciplinas de Engenharia de Software, Teste de Software e Programação Web do BSI/UFRN.
---

# Django Backend

## Perfil

Stack principal de backend das disciplinas. Os projetos seguem a estrutura
padrão do Django com apps modularizados e utilizam DRF para construção de
APIs REST.

## Estrutura de projeto recomendada

```
projeto/
├── manage.py
├── requirements.txt
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── usuarios/
│   ├── tarefas/
│   └── ...
└── templates/
```

## Padrões adotados

- **Ambiente virtual** com `python -m venv .venv`
- **Configuração de ambiente** com variáveis via python-decouple ou django-environ
- **Testes** com pytest-django ou Django TestCase
- **APIs** com Django REST Framework (ViewSets + Serializers)
- **Autenticação** com djoser ou dj-rest-auth (JWT)

## Tutoriais de referência

- `lessons/dev-web-django.md` — aulas 05 e 06
- [Tutorial Oficial Django](https://docs.djangoproject.com/)
- [Tutorial DRF](https://www.django-rest-framework.org/tutorial/quickstart/)

## Comandos frequentes

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```
