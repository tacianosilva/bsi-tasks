package br.ufrn.bsi.bd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MySqlConector {

    public static void main(String args[]) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = 
                    DriverManager.getConnection(
                            "jdbc:mysql://localhost:3306/meubanco", "root", "admin");
            
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
