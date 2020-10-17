import requests
class BuscaEndereco:
    def __init__(self, cep):
        if self.cepValido(cep):
            self.cep = str(cep)
        else:
            raise ValueError('Cep invalido.')

    def __str__(self):
        return self.format_cep()

    def cepValido(self, cep):
        cep = str(cep)
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[0:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        dados = requests.get(url)
        dadosJson = dados.json()

        return f"Rua: {dadosJson['logradouro']}\n" \
               f"Bairro: {dadosJson['bairro']}\n" \
               f"Complemento: {dadosJson['complemento']}\n" \
               f"Cidade: {dadosJson['localidade']}"
