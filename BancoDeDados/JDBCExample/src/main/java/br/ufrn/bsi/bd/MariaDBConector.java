package br.ufrn.bsi.bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
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

            PrintInfo(con);

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

    private static void PrintInfo(Connection con) throws SQLException {
        System.out.println("Banco de Dados: " + con.getCatalog());
        System.out.println();
        String queryString = "select version()";
        Statement v = con.createStatement();
        ResultSet rset = v.executeQuery(queryString);

        while ( rset.next()) {
          System.out.println("SGBD Version: " + rset.getString(1));
        }

        System.out.println();
    }
}
