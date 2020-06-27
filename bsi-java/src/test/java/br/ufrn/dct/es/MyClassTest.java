package br.ufrn.dct.es;

import static org.junit.jupiter.api.Assertions.*;

import java.math.BigInteger;

import org.junit.jupiter.api.Test;

public class MyClassTest {

    //@Test
    void test() {
        fail("Not yet implemented");
    }
    
    @Test
    public void multiplicationOfZeroIntegersShouldReturnZero() {
        MyClass calc = new MyClass(); // MyClass is tested

        // assert statements
        assertEquals(0, calc.multiply(10, 0), "10 x 0 must be 0");
        assertEquals(0, calc.multiply(0, 10), "0 x 10 must be 0");
        assertEquals(0, calc.multiply(0, 0), "0 x 0 must be 0");
        
        assertNotEquals(1, calc.multiply(1, 0), "Testa multiplicação!");
        assertNotNull(calc, "Testa se não é nulo!");
    }
    
    @Test
    public void condicionaltTest() {
        MyClass calc = new MyClass();
        
        assertEquals(Integer.MAX_VALUE-1, calc.condicional(Integer.MAX_VALUE, 1));
        assertEquals(Integer.MAX_VALUE+1, calc.condicional(1, Integer.MAX_VALUE));
        
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MAX_VALUE-1);
        System.out.println(Integer.MAX_VALUE+1);
        
        BigInteger big = new BigInteger(Integer.toString(Integer.MAX_VALUE));
        System.out.println(big);
        System.out.println(big.add(new BigInteger("1000000000")));
        
        assertEquals(13, calc.condicional(5, 8));
        assertEquals(1, calc.condicional(0, 1));
        assertEquals(3, calc.condicional(8, 5));
        assertEquals(1, calc.condicional(1, 0));
        assertEquals(0, calc.condicional(0, 0));
        assertEquals(25, calc.condicional(5, 5));
    }
}
