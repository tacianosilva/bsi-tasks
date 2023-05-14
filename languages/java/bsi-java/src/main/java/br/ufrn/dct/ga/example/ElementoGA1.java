package br.ufrn.dct.ga.example;

public class ElementoGA1 extends ElementoGA {

    private final double FATOR = 0.00004768372718899898;

    private float converteBooleano(int inicio, int fim) {
        int i;
        float aux = 0;
        String s = this.getValor();
        for (i = inicio; i <= fim; ++i) {
            aux *= 2;
            if (s.substring(i, i + 1).equals("1")) {
                aux += 1;
            }
        }
        return (aux);
    }

    public double calculaAvaliacao() {
        double x = this.converteBooleano(0, 21);
        double y = this.converteBooleano(22, 43);
        x = x * FATOR - 100;
        y = y * FATOR - 100;
        this.avaliacao = 1 / ((x * x + y * y) + 1);
        return (this.avaliacao);
    }

    /****************/
    /* Construtores */
    /****************/

    public ElementoGA1(int tamanho) {
        super(tamanho);
    }

    public ElementoGA1() {
        super(44);
    }

    public ElementoGA1(String novoValor) {
        this.valor = novoValor;
    }

    /********************************/
    /* Metodos Basicos de Classe */
    /********************************/

    public String toString() {
        return ("String: x=" + (this.converteBooleano(0, 21) * FATOR - 100) + " y="
                + (this.converteBooleano(22, 43) * FATOR - 100) + "\nAvaliacao:" + this.avaliacao);
    }
}
