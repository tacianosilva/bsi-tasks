import peewee

# Conexão com o banco atividade_db
db = peewee.PostgresqlDatabase('atividade_db',
                               host='localhost',
                               port=5432,
                               user='postgres',
                               password='123456')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Funcionario(BaseModel):
    codigo = peewee.AutoField(primary_key=True)
    nome = peewee.CharField(max_length=50)
    sexo = peewee.CharField(max_length=1)
    dtnasc = peewee.DateField()
    salario = peewee.DecimalField(max_digits=10, decimal_places=2)
    codsupervisor = peewee.ForeignKeyField('self', column_name='codsupervisor', null=True, on_delete='SET NULL', on_update='CASCADE')
    coddepto = peewee.DeferredForeignKey('Departamento', column_name='coddepto', on_delete='SET NULL', on_update='CASCADE')

    class Meta:
        table_name = 'funcionario'

class Departamento(BaseModel):
    codigo = peewee.AutoField(primary_key=True)
    sigla = peewee.CharField(max_length=10, unique=True)
    descricao = peewee.CharField(max_length=50)
    codgerente = peewee.ForeignKeyField(Funcionario, column_name='codgerente', null=True, on_delete='SET NULL', on_update='CASCADE')

    class Meta:
        table_name = 'departamento'

class Projeto(BaseModel):
    codigo = peewee.AutoField(primary_key=True)
    nome = peewee.CharField(max_length=50, unique=True)
    descricao = peewee.TextField()
    codresponsavel = peewee.ForeignKeyField(Funcionario, column_name='codresponsavel', null=True, on_delete='SET NULL', on_update='CASCADE')
    coddepto = peewee.ForeignKeyField(Departamento, column_name='coddepto', null=True, on_delete='SET NULL', on_update='CASCADE')
    datainicio = peewee.DateField()
    datafim = peewee.DateField()

    class Meta:
        table_name = 'projeto'

class Atividade(BaseModel):
    codigo = peewee.AutoField(primary_key=True)
    descricao = peewee.TextField()
    codprojeto = peewee.ForeignKeyField(Projeto, column_name='codprojeto', on_delete='SET NULL', on_update='CASCADE')
    datainicio = peewee.DateField()
    datafim = peewee.DateField()

    class Meta:
        table_name = 'atividade'

def initialize():
    db.connect()
    # As tabelas já existem, então não criar novamente
    print("Conectado ao banco AtividadesBD via ORM Peewee.")