from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(str(documento)) == 11:
            return DocCpf(documento)
        elif len(str(documento)) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento invalido!!')


class DocCpf:
    def __init__(self, documento):
        if self.valida:
            self.cpf = documento
        else:
            raise ValueError('Cpf INVALIDO!!!!')

    def __str__(self):
        return f'CPF {self.format()} VALIDO'


    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)


    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.documento = documento
        else:
            raise ValueError('Cpnj INVALIDO!!!')

    def __str__(self):
        return f'CNPJ {self.format(self.documento)} VALIDO'

    def valida(self, documento):
        valida = CNPJ()
        return valida.validate(documento)

    def format(self, documento):
        mask = CNPJ()
        return mask.mask(self.documento)









