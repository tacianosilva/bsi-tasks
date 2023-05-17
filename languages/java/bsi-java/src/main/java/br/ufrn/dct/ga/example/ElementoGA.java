package br.ufrn.dct.ga.example;

public class ElementoGA implements Comparable<ElementoGA> {

    protected String valor;

    protected double avaliacao;

    public boolean equals(final ElementoGA outro) {
        // Usada para testar se dois indivíduos são iguais - importante
        // quando formos ver os módulos de população mais avançados
        return (valor.equals(outro.getValor()));
    }

    public int compareTo(final ElementoGA outro) {
        // Será usada na hora de inserir os elementos em ordem em uma população
        // para o GA com steady state (capítulo 7)
        int retorno = -1;
        final ElementoGA aux = (ElementoGA) outro;
        if (avaliacao > aux.getAvaliacao()) {
            retorno = 1;
        }
        if (avaliacao == aux.getAvaliacao()) {
            retorno = 0;
        }
        return (retorno);
    }

    public double calculaAvaliacao() {
        /*
         * Esta função deve ser sobreescrita por uma função dentro da sub-classe a ser
         * usada como definidora dos cromossomos do GA
         */
        this.avaliacao = 0;
        return (this.avaliacao);
    }

    public double getAvaliacao() {
        return (this.avaliacao);
    }

    public String getValor() {
        return (this.valor);
    }

    public void setValor(final String aux) {
        this.valor = aux;
    }

    protected void inicializaElemento(final int tamanho) {
        int i;
        this.valor = "";
        for (i = 0; i < tamanho; ++i) {
            if (Math.random() < 0.5) {
                this.valor = this.valor + "0";
            } else {
                this.valor = this.valor + "1";
            }
        }
    }

    /****************/
    /* Construtores */
    /****************/

    public ElementoGA(final String novoValor) {
        this.valor = novoValor;
    }

    public ElementoGA(final int tamanho) {
        inicializaElemento(tamanho);
    }

    public ElementoGA() {
        this(100);
    }

    /************************/
    /* Operadores Geneticos */
    /************************/

    public void mutacao(final double chance) {
        int i;
        final int tamanho = this.valor.length();
        String aux, inicio, fim;
        for (i = 0; i < tamanho; i++) {
            if (java.lang.Math.random() < chance) {
                aux = this.valor.substring(i, i + 1);
                if (aux.equals("1")) {
                    aux = "0";
                } else {
                    aux = "1";
                }
                inicio = this.valor.substring(0, i);
                fim = this.valor.substring(i + 1, tamanho);
                this.valor = inicio + aux + fim;
            }
        }
    }

    public void mutacao() {
        this.mutacao(0.005);
    }

    public ElementoGA crossoverUmPonto(final ElementoGA outroPai) {
        String aux1;
        ElementoGA retorno = null;
        final int pontoCorte = (Double.valueOf(java.lang.Math.random() * this.valor.length())).intValue();
        ;
        if (java.lang.Math.random() < 0.5) {
            aux1 = this.valor.substring(0, pontoCorte)
                    + outroPai.getValor().substring(pontoCorte, outroPai.getValor().length());
        } else {
            aux1 = outroPai.getValor().substring(0, pontoCorte) + this.valor.substring(pontoCorte, this.valor.length());
        }
        try {
            retorno = (ElementoGA) outroPai;
            retorno.setValor(aux1);
        } catch (final Exception e) {
        }
        return (retorno);
    }

    /********************************/
    /* Metodos Basicos de Classe */
    /********************************/

    public String toString() {
        return ("String:" + this.valor + "\nAvaliacao:" + this.avaliacao);
    }
}
