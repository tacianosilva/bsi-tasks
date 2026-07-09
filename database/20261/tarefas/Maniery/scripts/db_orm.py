import os
import django

# Configurando o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atividades_projeto.settings')
django.setup()

from minha_app.models import Atividade, Projeto # Ajuste o nome da sua app

def executar_tarefa_orm():
    # 6.a Inserir atividade via ORM
    projeto = Projeto.objects.get(id=1)
    Atividade.objects.create(id=2, nome="Atividade via ORM", projeto=projeto)
    
    # 6.b Atualizar líder
    projeto.lider_id = 2
    projeto.save()
    
    # 6.c Listar todos
    projetos = Projeto.objects.prefetch_related('atividade_set').all()
    for p in projetos:
        print(f"Projeto: {p.nome}")
        for a in p.atividade_set.all():
            print(f"  - Atividade: {a.nome}")

if __name__ == "__main__":
    executar_tarefa_orm()