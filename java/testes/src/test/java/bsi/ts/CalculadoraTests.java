package bsi.ts;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

public class CalculadoraTests {

    @Test
	@DisplayName("1 + 1 = 2")
	void addsTwoNumbers() {
		Calculadora calculator = new Calculadora("Teste 1");
		assertEquals(2, calculator.sum(1, 1), "1 + 1 should equal 2");
    }
    
    @Test
    void somaDoisNumeros() {
        Calculadora calc = new Calculadora("Teste 2");

        Integer expected = 13;
        Integer actual = calc.sum(5, 8);

        assertEquals(expected, actual, "Somar 5 + 8 deve resultar 13");
    }

    @Test
    void testaCondicional() {
        Calculadora calc = new Calculadora("Teste 3");
        assertEquals(13, calc.condicional(5, 8), "T 1");
        assertEquals(1, calc.condicional(0, 1), "T 2");
        assertEquals(3, calc.condicional(8, 5));
        assertEquals(1, calc.condicional(1, 0));
        assertEquals(0, calc.condicional(0, 0));
        assertEquals(25, calc.condicional(5, 5));
    }

    @Test
    void testaNulo() {
        Calculadora calc = new Calculadora("Teste 4");

        assertNotNull(calc);
        assertEquals("Teste 4", calc.getNome());
    }

    @Test
    void testaMutiplicar() {
        Calculadora calc = new Calculadora("Teste 5");

        assertEquals(25, calc.multiply(5, 5), "5 * 5 deve resultar 25");        
    }
}
