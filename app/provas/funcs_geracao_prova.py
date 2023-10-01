from .funcs import (
filtra_questoes_simulado_humanas,
filtra_questoes_simulado_linguagens,
filtra_questoes_simulado_matematica,
filtra_questoes_simulado_natureza
)
from usuarios.models import Aluno
from materiais.models import SubMateria, Conteudo, Questao, Materia, Simulado

def geracao_simulado(simulado_id_list:list, num_questoes:int, aluno:Aluno):
    simulados = Simulado.objects.filter(pk__in=simulado_id_list).prefetch_related('materia')
    questoes = []
    questoes_unicas = set()
    for simulado in simulados:
        # Materia de cada simulado
        materia_in_simulado = simulado.materia.all()
        # Se um simulado for de matematica a quantidade de questoes do simulado sera 100% matematica como no enem

        if (
            len(materia_in_simulado) == 1
            and materia_in_simulado[0].nome == "Matemática"
        ):
            questoes.extend(filtra_questoes_simulado_matematica(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
        # Se um dos simulados for de ciencias da natureza

        elif len(materia_in_simulado) == 3:
            questoes.extend(filtra_questoes_simulado_natureza(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
        # Se um dos simulados for de Linguagens

        elif len(materia_in_simulado) == 5:
            questoes.extend(filtra_questoes_simulado_linguagens(
                num_questoes,
                materia_in_simulado,
                questoes_unicas,
                aluno,
            ))
    return questoes, simulados    


def geracao_prova(materia_id_list:list, num_questoes:int):
    materias = Materia.objects.filter(pk__in=materia_id_list)
    questoes_unicas = set()
    questoes = []

    for materia in materias:
        sub_materias_da_materia = SubMateria.objects.filter(materia=materia)
        conteudos = Conteudo.objects.filter(         

            sub_materia__in=sub_materias_da_materia
        )
        questoes_da_materia = Questao.objects.filter(
            conteudo__in=conteudos
        ).order_by("?")
        questoes_selecionadas = 0

        for questao in questoes_da_materia:

            if questoes_selecionadas >= num_questoes:
                break

            if questao.id not in questoes_unicas:
                questoes_unicas.add(questao.id)
                questoes.append(questao)
                questoes_selecionadas += 1
    return questoes, materias