package bsi.ts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Selenium {

    public static void main(String[] args) {
        // cria um driver para acessar um servidor Web
        System.setProperty("webdriver.gecko.driver", "src/test/java/bsi/ts/geckodriver");

        DesiredCapabilities capabilities = DesiredCapabilities.firefox();
        capabilities.setCapability("marionette", true);

        WebDriver driver = new FirefoxDriver(capabilities);

        // instrui o driver para "navegar" pelo Google
        driver.navigate().to("http://www.google.com");

        // obtém um campo de entrada de dados, de nome "q"
        WebElement element = driver.findElement(By.name("q"));

        // preenche esse campo com as palavras "software"
        element.sendKeys("software");

        // submete os dados; como se fosse dado um "enter"
        element.submit();

        // espera a página de resposta carregar (timeout de 8s)
        (new WebDriverWait(driver, 30)).until(new ExpectedCondition<Boolean>() {
            public Boolean apply(WebDriver d) {
                return d.getTitle().toLowerCase().startsWith("software");
            }
        });

        // resultado deve ser: "software - Google Search"
        System.out.println("Page title is: " + driver.getTitle());

        // fecha o navegador
        driver.quit();
    }
}
