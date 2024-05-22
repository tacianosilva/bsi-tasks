# Teste de Unidade em Python com unittest

O arquivo `test_calculadora.py` implementa o testes de unidade para as funções no arquivo `calculadora.py`.

Executando os testes com `unittest`:
```console
python3 -m unittest test_calculadora.py
```

## Cobertura dos Testes

Requisitos necessários:

```bash
    pip install coverage
```

Executando o *coverage* e exibindo o relatório:

```bash
    coverage run -m unittest discover
    coverage report -m
```

Para gerar o relatórios em xml e html:

```bash
    coverage xml
    coverage html
```

## Usando o PyDoc e o PyLint

Também temos a documentação com o *pydoc* e a checagem com o *pylint*.

Requisitos necessários:

```bash
    pip install pep8
    pip install pylint
```

Ver documentação e gerar documentação em html.

```bash
    pydoc calculadora.py
    pydoc -w calculadora
```

Verificação com o *pylint*:

```bash
    pylint calculadora.py
```
