package br.ufrn.dct.es;

import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.testng.asserts.SoftAssert;

public class MyClassTestNG {

    private SoftAssert softAssert;

    @BeforeMethod
    public void startTest() {
         softAssert = new SoftAssert();
    }

    @Test
    public void multiplicationOfZeroIntegersShouldReturnZero() {
        Calculadora tester = new Calculadora(); // MyClass is tested

        // assert statements
        Integer zero = 0;
        softAssert.assertEquals(tester.multiply(10, 0), zero, "10 x 0 must be 0");
        softAssert.assertEquals(tester.multiply(0, 10), zero, "0 x 10 must be 0");
        softAssert.assertEquals(tester.multiply(0, 0), zero, "0 x 0 must be 0");
    }
}
