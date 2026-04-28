// projeto.model.ts
import { DataTypes } from "sequelize";
import { sequelize } from "../sequelize";
import { Funcionario } from "./funcionario.model";

export const Projeto = sequelize.define(
    "projeto",
    {
        codigo: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        nome: { type: DataTypes.STRING(50), unique: true },
        descricao: { type: DataTypes.STRING(250) },
        depto: { type: DataTypes.INTEGER, allowNull: true },
        data_inicio: { type: DataTypes.DATE },
        data_fim: { type: DataTypes.DATE },
    },
    {
        tableName: "projeto",
        freezeTableName: true,
        timestamps: false,
    }
);

Projeto.belongsTo(Funcionario, {
    foreignKey: 'responsavel',
    as: 'funcionarioAssociado'
})