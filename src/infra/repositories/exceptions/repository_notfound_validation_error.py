class RepositoryLayerNotFoundError(Exception):

    @staticmethod
    def when(condicao: bool, mensagem: str) -> None:
        if condicao:
            raise RepositoryLayerNotFoundError(mensagem)
