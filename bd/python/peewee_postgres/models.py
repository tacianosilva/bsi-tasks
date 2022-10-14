from decouple import config
import peewee

# create the database connection (environment variables in .env file)
db = peewee.PostgresqlDatabase(config('DATABASE_NAME'),
                        host=config('DATABASE_HOST'),
                        port=config('DATABASE_PORT'),
                        user=config('DATABASE_USER'),
                        password=config('DATABASE_PASS'))

class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela sera criada
        database = db


class Funcionario(BaseModel):
    """
    Classe que representa a tabela Funcionario
    """
    codigo = peewee.AutoField(primary_key=True)
    nome = peewee.CharField(max_length=40)
    sexo = peewee.CharField(max_length=1)
    dtnasc = peewee.DateTimeField()
    salario = peewee.DecimalField()
    supervisor = peewee.ForeignKeyField('self', backref='supervisiona', column_name='codsupervisor')
    depto = peewee.DeferredForeignKey('Departamento', backref='funcionarios')


class Departamento(BaseModel):
    codigo = peewee.AutoField(primary_key=True)
    sigla = peewee.CharField(max_length=10)
    descricao = peewee.CharField(max_length=40)
    gerente = peewee.ForeignKeyField(Funcionario, backref='gerencia', column_name='codgerente')


def initialize():
    """Connect and create tables if they don't exist"""
    db.connect()
    # the database must be created in the DBMS
    db.create_tables([Funcionario, Departamento], safe=True)
    # creates the dereferenced foreign key (circular key), same as "ALTER TABLE ADD CONSTRAINT"
    Funcionario._schema.create_foreign_key(Funcionario.depto)
