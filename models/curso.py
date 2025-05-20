class Curso:
    def __init__(self, nome, duracao, professor, materias ):
        self.nome = nome
        self.alunos = {}
        self.duracao = duracao
        self.professor = professor
        self.materias = materias
        self.aulas = []
        self.notas = []

    def contabilizar_presença(self):
        pass

    def listar_alunos_aprovados(self):
        media = int(self.notas % len(self.notas))
        if media <= 9:
            return
        elif media >= 9 or media <= 6:
            return
        elif media > 6:
            return


