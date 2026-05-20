package br.bsi.ismael.mongodb;

import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Updates;
import org.bson.Document;
import org.bson.types.ObjectId;

import java.time.LocalDateTime;
import java.util.Scanner;

public class App {

    private static final String MONGO_URI =
            "mongodb://atividades_user:atividades123@localhost:27017/AtividadesProj?authSource=AtividadesProj";

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create(MONGO_URI)) {
            MongoDatabase database = mongoClient.getDatabase("AtividadesProj");

            int opcao;

            do {
                System.out.println("\n===== CRUD MongoDB - AtividadesProj =====");
                System.out.println("1 - Listar projetos e atividades");
                System.out.println("2 - Criar nova atividade");
                System.out.println("3 - Atualizar líder de um projeto");
                System.out.println("4 - Remover atividade");
                System.out.println("0 - Sair");
                System.out.print("Escolha uma opção: ");

                opcao = Integer.parseInt(scanner.nextLine());

                switch (opcao) {
                    case 1 -> listarProjetos(database);
                    case 2 -> criarAtividade(database);
                    case 3 -> atualizarLiderProjeto(database);
                    case 4 -> removerAtividade(database);
                    case 0 -> System.out.println("Encerrando programa.");
                    default -> System.out.println("Opção inválida.");
                }

            } while (opcao != 0);
        }
    }

    private static void listarProjetos(MongoDatabase database) {
        MongoCollection<Document> projetos = database.getCollection("projetos");
        MongoCollection<Document> empregados = database.getCollection("empregados");
        MongoCollection<Document> atividades = database.getCollection("atividades");

        System.out.println("\n=== Projetos cadastrados ===");

        for (Document projeto : projetos.find()) {
            ObjectId liderId = projeto.getObjectId("liderId");
            Document lider = empregados.find(Filters.eq("_id", liderId)).first();

            System.out.println("\nProjeto: " + projeto.getString("nome"));
            System.out.println("Descrição: " + projeto.getString("descricao"));
            System.out.println("Líder: " + (lider != null ? lider.getString("nome") : "Sem líder"));
            System.out.println("Status: " + projeto.getString("status"));
            System.out.println("Atividades:");

            FindIterable<Document> atividadesProjeto =
                    atividades.find(Filters.eq("projetoId", projeto.getObjectId("_id")));

            for (Document atividade : atividadesProjeto) {
                System.out.println(" - " + atividade.getString("titulo")
                        + " | Status: " + atividade.getString("status"));
            }
        }
    }

    private static void criarAtividade(MongoDatabase database) {
        MongoCollection<Document> projetos = database.getCollection("projetos");
        MongoCollection<Document> empregados = database.getCollection("empregados");
        MongoCollection<Document> atividades = database.getCollection("atividades");

        System.out.print("Nome do projeto existente: ");
        String nomeProjeto = scanner.nextLine();

        System.out.print("E-mail do responsável: ");
        String emailResponsavel = scanner.nextLine();

        System.out.print("Título da nova atividade: ");
        String titulo = scanner.nextLine();

        System.out.print("Descrição da atividade: ");
        String descricao = scanner.nextLine();

        System.out.print("Prioridade: ");
        String prioridade = scanner.nextLine();

        Document projeto = projetos.find(Filters.eq("nome", nomeProjeto)).first();
        Document responsavel = empregados.find(Filters.eq("email", emailResponsavel)).first();

        if (projeto == null) {
            System.out.println("Projeto não encontrado.");
            return;
        }

        if (responsavel == null) {
            System.out.println("Responsável não encontrado.");
            return;
        }

        Document novaAtividade = new Document("titulo", titulo)
                .append("descricao", descricao)
                .append("projetoId", projeto.getObjectId("_id"))
                .append("responsavelId", responsavel.getObjectId("_id"))
                .append("status", "Pendente")
                .append("prioridade", prioridade)
                .append("estimativaHoras", 4)
                .append("criadoEm", LocalDateTime.now().toString());

        atividades.insertOne(novaAtividade);

        System.out.println("Atividade criada com sucesso.");
    }

    private static void atualizarLiderProjeto(MongoDatabase database) {
        MongoCollection<Document> projetos = database.getCollection("projetos");
        MongoCollection<Document> empregados = database.getCollection("empregados");

        System.out.print("Nome do projeto: ");
        String nomeProjeto = scanner.nextLine();

        System.out.print("E-mail do novo líder: ");
        String emailNovoLider = scanner.nextLine();

        Document novoLider = empregados.find(Filters.eq("email", emailNovoLider)).first();

        if (novoLider == null) {
            System.out.println("Novo líder não encontrado.");
            return;
        }

        long alterados = projetos.updateOne(
                Filters.eq("nome", nomeProjeto),
                Updates.set("liderId", novoLider.getObjectId("_id"))
        ).getModifiedCount();

        if (alterados > 0) {
            System.out.println("Líder do projeto atualizado com sucesso.");
        } else {
            System.out.println("Nenhum projeto foi atualizado.");
        }
    }

    private static void removerAtividade(MongoDatabase database) {
        MongoCollection<Document> atividades = database.getCollection("atividades");

        System.out.print("Título da atividade que será removida: ");
        String titulo = scanner.nextLine();

        long removidos = atividades.deleteOne(Filters.eq("titulo", titulo)).getDeletedCount();

        if (removidos > 0) {
            System.out.println("Atividade removida com sucesso.");
        } else {
            System.out.println("Nenhuma atividade foi encontrada com esse título.");
        }
    }
}
