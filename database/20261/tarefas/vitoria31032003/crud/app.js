const { MongoClient } = require("mongodb");

const url = "mongodb://admin:admin123@localhost:27017";

const client = new MongoClient(url);

async function main() {

    try {

        await client.connect();

        console.log("Conectado ao Banco de Dados MongoDB!");

        const db = client.db("AtividadesProj");

        const projetos = db.collection("projetos");
        const empregados = db.collection("empregados");
        const atividades = db.collection("atividades");


        await empregados.insertOne({
            nome: "Vitória Geovanna",
            cargo: "Desenvolvedora Front-end",
        });

        console.log("Novo(a) empregado(a) inserido(a)!");

        
        console.log("\nProjetos:");

        const listaProjetos = await projetos.find().toArray();
        console.log(listaProjetos);

        console.log("\nEmpregados(as):");

        const listaEmpregados = await empregados.find().toArray();
        console.log(listaEmpregados);

        console.log("\nAtividades:");

        const listaAtividades = await atividades.find().toArray();
        console.log(listaAtividades);
        
        await empregados.updateOne(
            {
                nome: "Vitória Geovanna"
            },
            {
                $set: {
                    cargo: "Desenvolvedora Front-end"
                }
            }
        );

        console.log("\nCargo atualizado");

        await empregados.deleteOne({
            nome: "Vitória Geovanna"
        });

        console.log("Empregado(a) removido(a) do Banco de Dados!");

    } catch (erro) {

        console.log("Erro:");
        console.log(erro);

    } finally {

        await client.close();

        console.log("\nConexão encerrada!x");

    }

}

main();
