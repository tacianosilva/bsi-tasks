package br.ufrn.bsi.bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 * Código de Exemplo de uso do Conector JDBC do MariaDB. Acesse:
 * https://mariadb.com/kb/en/library/java/
 * 
 * @author Taciano de Morais Silva
 * @since 25/10/2018
 *
 */
public class MariaDBConector {

    public static void main(String args[]) {
        try {
            Class.forName("org.mariadb.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mariadb://localhost:3306/meubanco", "root", "admin");

            System.out.println("Banco de Dados: " + con.getCatalog());
            System.out.println();

            Statement stmt = con.createStatement();
            
            ResultSet rs = stmt.executeQuery("select * from empregado");

            while (rs.next()) {
                System.out.println("Nome: " + rs.getString(1));
                System.out.println("Matrícula: " + rs.getString(2));
                System.out.println("Data Nasc.: " + rs.getDate(3));
            }

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
