import { Sequelize } from "sequelize";

export const sequelize = new Sequelize("atividade_db", "admin", "senha", {
    dialect: "postgres",
    host: "localhost",
});
