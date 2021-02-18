# Isto é uma classe!
class HelloWorld
    # Construtor recebendo 'your_name' como parâmetro.
    def initialize your_name
    
        # Armazena o parâmetro em uma variável de instância.
        @your_name = your_name
    end
    # Método que imprime uma mensagem de boas vindas seguida de um nome.
    def say_hello
        puts "Bem vindo ao Ruby, #{@your_name}!"
    end
end
# Instancia a classe enviando meu nome como argumento para o construtor.
hello_world = HelloWorld.new "Taciano Morais Silva"
# Invoca o método say_hello, o qual imprime a mensagem.
hello_world.say_hello