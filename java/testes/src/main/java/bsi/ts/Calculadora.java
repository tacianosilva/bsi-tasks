package bsi.ts;

public class Calculadora {

    private String nome;

    public Calculadora(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return this.nome;
    }

    public Integer sum(final int x, final int y) {
        return x + y;
    }
    
    public Integer multiply(final int i, final int j) {
        return i * j;
    }

    public Integer condicional(final int i, final int j) {
        if (i < j) {
            return i + j;
        } else if (i == j) {
            return i * j;
        } else {
            return i - j;
        }
    }
}