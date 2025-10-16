import { DataTypes } from "sequelize";
import { sequelize } from "../sequelize";

export const Funcionario = sequelize.define(
    "funcionario",
    {
        codigo: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        nome: { type: DataTypes.STRING(150), allowNull: false },
        sexo: { type: DataTypes.CHAR(1) },
        dt_nasc: { type: DataTypes.DATE },
        salario: { type: DataTypes.DECIMAL },
        supervisor: { type: DataTypes.INTEGER, allowNull: true },
        depto: { type: DataTypes.INTEGER, allowNull: true },
    },
    {
        tableName: "funcionario",
        freezeTableName: false,
        timestamps: false,
    }
);
