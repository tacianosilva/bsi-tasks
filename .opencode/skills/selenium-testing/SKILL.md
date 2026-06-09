---
name: selenium-testing
description: Use ao escrever testes de interface web com Selenium WebDriver na disciplina de Teste de Software do BSI/UFRN.
---

# Selenium Testing

## Perfil

Testes automatizados de interface web utilizando Selenium WebDriver.
Aplicado na disciplina de Teste de Software com exemplos em Java e Python.

## Estrutura de teste recomendada

```
testes/
├── pages/
│   ├── LoginPage.java
│   └── HomePage.java
├── tests/
│   ├── LoginTest.java
│   └── CadastroTest.java
└── support/
    └── DriverFactory.java
```

## Padrões adotados

- **Page Object Model** para organização
- **WebDriverManager** para gerenciamento de drivers
- **JUnit 5** como framework de teste (Java)
- **pytest** como framework de teste (Python)
- **Selenium Grid** para execução paralela (quando aplicável)

## Exemplos no repositório

- `languages/java/testes/` — projeto Maven com Selenium + JUnit 5
- `softwaretesting/docs/selenium.md` — guia de uso com Django

## Comandos frequentes (Java/Maven)

```bash
mvn test -Dtest=NomeTeste
mvn test
```

## Referências

- [Selenium Docs](https://www.selenium.dev/documentation/)
- [WebDriverManager](https://bonigarcia.dev/webdrivermanager/)
- `softwaretesting/docs/selenium.md`
