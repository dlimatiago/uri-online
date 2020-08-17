class Testes:
    def __init__(self, path):
        self.arquivo = open(path)  # Abre o arquivo
        self._dados()
        self._Inputs()
        self._casosTeste()
        self.fecha()

    def fecha(self):  # Fecha o arquivo
        self.arquivo.close()

    def _dados(self):  # Remove o /n
        self.valores = self.arquivo.readlines()
        self.valores = list(map(lambda x: str(x).replace('\n', ''), self.valores))

    def _casosTeste(self):  # Separa os inputs dos casos no formato iterator
        self.lista = self.valores
        self.casos = iter(elemento for elemento in self.lista if ' ' not in elemento)

    def _Inputs(self):
        self.lst = self.valores
        self.entrada = iter(elemento for elemento in self.lst if ' ' in elemento)

    def proximoCasoinput(self):  # Retorna o próximo elemento dos casos
        return next(self.casos)

    def proximoinput(self):  # Retorna o próximo elemento dos inputs
        return next(self.entrada)

    def tam_casos(self):
        return len(list(self.casos))

    def tam_inputs(self):
        return len(list(self.entrada))


# t = Testes('Estruturas e Bibliotecas/respostas.txt')

