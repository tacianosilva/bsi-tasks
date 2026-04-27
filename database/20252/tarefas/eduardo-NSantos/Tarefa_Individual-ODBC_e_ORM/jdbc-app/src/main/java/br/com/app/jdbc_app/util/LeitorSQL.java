package br.com.app.jdbc_app.util;

import java.io.InputStream;
import java.nio.charset.StandardCharsets;

public class LeitorSQL {

    public static String ler(String caminho) throws Exception {

        try (InputStream input = LeitorSQL.class
            .getClassLoader()
            .getResourceAsStream(caminho)) {

            if (input == null) {
                throw new RuntimeException("Arquivo não encontrado: " + caminho);
            }

            return new String(input.readAllBytes(), StandardCharsets.UTF_8);
        }
    }
}
