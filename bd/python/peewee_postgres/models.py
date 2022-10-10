from decouple import config
from peewee import PostgresqlDatabase
from peewee import Model
import peewee

db = PostgresqlDatabase(config('DATABASE_NAME'),
                        host=config('DATABASE_HOST'),
                        port=config('DATABASE_PORT'),
                        user=config('DATABASE_USER'),
                        password=config('DATABASE_PASS'))

class BaseModel(Model):
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
    codsupervisor = peewee.IntegerField()
    coddepto = peewee.IntegerField()

db.connect()

# db.create_tables([Funcionario])
