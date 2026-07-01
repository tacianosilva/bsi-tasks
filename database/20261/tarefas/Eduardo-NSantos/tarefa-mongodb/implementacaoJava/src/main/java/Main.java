import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

import org.bson.Document;

import static com.mongodb.client.model.Filters.eq;
import static com.mongodb.client.model.Updates.set;

public class Main {

    public static void main(String[] args) {

        String uri = "mongodb://usuarioApp:senha123@localhost:27017/AtividadesProj?authSource=AtividadesProj";

        try (MongoClient mongoClient = MongoClients.create(uri)) {

            MongoDatabase database = mongoClient.getDatabase("AtividadesProj");

            MongoCollection<Document> projetos = database.getCollection("projetos");

            MongoCollection<Document> atividades = database.getCollection("atividades");

            
            // CREATE
            Document novaAtividade = new Document("titulo", "Implementar Login")
                            .append("descricao", "Criar autenticação de usuários")
                            .append("responsavel", "Carlos Silva")
                            .append("projeto", "Sistema Acadêmico")
                            .append("status", "Em andamento");

            atividades.insertOne(novaAtividade);

            System.out.println("Nova atividade inserida.");

            // READ
            System.out.println("\n===== PROJETOS E ATIVIDADES =====\n");

            FindIterable<Document> listaProjetos = projetos.find();

            for (Document projeto : listaProjetos) {
                String nomeProjeto = projeto.getString("nome");

                System.out.println("Projeto: " + nomeProjeto);
                System.out.println("Líder: " + projeto.getString("lider"));

                FindIterable<Document> listaAtividades = atividades.find(eq("projeto", nomeProjeto));

                for (Document atividade : listaAtividades) {
                    System.out.println(" - Atividade: " + atividade.getString("titulo"));
                    System.out.println("   Status: " + atividade.getString("status"));
                }

                System.out.println();
            }

            // UPDATE
            projetos.updateOne(
                    eq("nome", "Sistema Acadêmico"),
                    set("lider", "Marcos Lima")
            );
            System.out.println("Líder do projeto atualizado.");

            // DELETE
            atividades.deleteOne(
                    eq("titulo", "Implementar Login")
            );
            System.out.println("Atividade removida.");

        } catch (Exception e) {

            e.printStackTrace();
        }

        mongoClient.close();
    }
}