import { DataTypes } from "sequelize";
import { sequelize } from "../sequelize";
import { Projeto } from "./projeto.model";

export const Atividade = sequelize.define(
    "atividade",
    {
        codigo: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        descricao: { type: DataTypes.STRING(250) },
        data_inicio: { type: DataTypes.DATE },
        data_fim: { type: DataTypes.DATE },
    },
    {
        tableName: "atividade",
        freezeTableName: false,
        timestamps: false,
    }
);

Atividade.belongsTo(Projeto, {
    foreignKey: "projeto",
    as: "projetoAssociado",
});
