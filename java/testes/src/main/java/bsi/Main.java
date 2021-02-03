package bsi;

import bsi.ts.Calculadora;

public class Main {

    public static void main(String[] args) {
        Calculadora calc = new Calculadora("Main");
        int x = 5;
        int y = 8;

        System.out.println("Calc não é nulo: " + calc);
        System.out.println("X = " + x);
        System.out.println("Y = " + y);
        System.out.println("X + Y = " + calc.sum(x, y));
        System.out.println("X * Y = " + calc.multiply(x, y));
    }
}
