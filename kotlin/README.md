# Tutoriais

Alguns exemplos de código em Kotlin

## Exemplo 1: Compilando via Linha de Comando

Instalação no Ubuntu com *snap*:

```bash
sudo snap install --classic kotlin
```

1. Criar arquivo hello.kt:

    ```kotlin
    fun main() {
        println("Hello, World!")
    }
    ```

2. Compilar:

    ```bash
    kotlinc hello.kt -include-runtime -d hello.jar
    ```

3. Executar:

    ```bash
    java -jar hello.jar
    ```

Fonte: [Working with the Command Line Compiler](https://kotlinlang.org/docs/tutorials/command-line.html)
