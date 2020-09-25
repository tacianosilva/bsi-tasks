package br.ufrn.dct.es;

public class Calculadora {
    
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
