package br.ufrn.dct.es;

import static org.junit.jupiter.api.Assertions.*;

import java.math.BigDecimal;
import java.math.BigInteger;

import org.junit.jupiter.api.Test;

public class MyClassTest {

    //@Test
    void test() {
        fail("Not yet implemented");
    }
    
    @Test
    public void multiplicationOfZeroIntegersShouldReturnZero() {
        Calculadora calc = new Calculadora(); // MyClass is tested

        assertNotNull(calc, "Testa se não é nulo!");
        // assert statements
        assertEquals(0, calc.multiply(10, 0), "10 x 0 must be 0");
        assertEquals(0, calc.multiply(0, 10), "0 x 10 must be 0");
        assertEquals(0, calc.multiply(0, 0), "0 x 0 must be 0");
        assertEquals(6, calc.multiply(2, 3), "2 x 3 must be 6");
        assertEquals(8, calc.multiply(1, 8), "1 x 8 must be 8");
        assertEquals(8, calc.multiply(8, 1), "8 x 1 must be 8");
        
        assertNotEquals(1, calc.multiply(1, 0), "Testa multiplicação!");
    }
    
    @Test
    public void condicionaltTest() {
        Calculadora calc = new Calculadora();
        
        assertEquals(Integer.MAX_VALUE-1, calc.condicional(Integer.MAX_VALUE, 1));
        assertEquals(Integer.MAX_VALUE+1, calc.condicional(1, Integer.MAX_VALUE));
        
        System.out.println("Máximo: " + Integer.MAX_VALUE);
        System.out.println(Integer.MAX_VALUE-1);
        System.out.println(Integer.MAX_VALUE+1);
        System.out.println("Mínimo:" + Integer.MIN_VALUE);
        
        BigInteger big = new BigInteger(Integer.toString(Integer.MAX_VALUE));
        System.out.println(big);
        System.out.println(big.add(new BigInteger("1000000000")));
        BigDecimal decimal = new BigDecimal("1.0");
        System.out.println(decimal);
        
        assertEquals(13, calc.condicional(5, 8));
        assertEquals(1, calc.condicional(0, 1));
        assertEquals(3, calc.condicional(8, 5));
        assertEquals(1, calc.condicional(1, 0));
        assertEquals(0, calc.condicional(0, 0));
        assertEquals(25, calc.condicional(5, 5));
    }
}
