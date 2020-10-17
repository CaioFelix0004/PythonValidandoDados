from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = ["Janeiro",
                 "Fevereiro",
                 "Março",
                 "Abril",
                 "Maio",
                 "Junho",
                 "Julho",
                 "Agosto",
                 "Setembro",
                 "Outubro",
                 "Novembro",
                 "Dezembro"]
        mesCadastro = self.momento_cadastro.month -1
        return meses[mesCadastro]

    def dia_semana(self):
        dias_semana = ["Segunda", "Terça", "Quarta",
                      "Quinta", "Sexta", "Sabado", "Domingo"]
        dia_semana = dias_semana[self.momento_cadastro.weekday()]
        return dia_semana

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y as %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro