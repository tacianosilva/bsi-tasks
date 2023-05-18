package br.ufrn.dct.ga.example;

import java.util.*;

public class GA1 extends GA {

    public void inicializaPopulacao() {
        int i;
        this.populacao = new Vector<ElementoGA>();
        for (i = 0; i < this.tamanho_populacao; ++i) {
            System.out.println("Aqui!!!");
            this.populacao.add(new ElementoGA1());
        }
    }

    /****************/
    /* Construtores */
    /****************/

    public GA1(int num_geracoes, int tam_populacao, double prob_mut) {
        super(num_geracoes, tam_populacao, prob_mut);
    }

    public GA1(int tam_populacao, double prob_mut) {
        super(60, tam_populacao, prob_mut);
    }

    public GA1(double prob_mut) {
        super(60, 100, prob_mut);
    }

    public GA1() {
        super(60, 100, 0.001);
    }

}
