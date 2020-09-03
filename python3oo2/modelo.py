from abc import ABC # abstract base classes

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # Todas as palavaras com letras maiúsculas
        self.ano = ano
        self._likes = 0

    @property
    def likes (self):
        return self._likes

    def dar_likes(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - Likes: {vingadores.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.temporadas} Temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    def __getitem__(self, item): #Duck typing - faz com que algo se comporte de certa maneira (faz com que os programas possam ser iteráveis)
        return self._programas[item]

    def __len__(self): # Faz com que programas sejam sizable
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)