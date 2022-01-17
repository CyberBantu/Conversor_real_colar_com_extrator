import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?(bytebank.com)(.br)?/(cambio)') # Validação da URL
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é Valida")



    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self): # A função Extrator URL a possibilidade de Contar a quantidade de Caracteres
        return len(self.url)

    def __str__(self): # Retornar somente a uRL pelo STR
        print("URL Total: ")
        return self.url + "\n" + "Parâmetros " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

# Conversão dolar - Real

cotacao_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    conversao_moeda = int(quantidade) / cotacao_dolar
    print('O valor R$ ' + quantidade + ' reais é $' + str(round(conversao_moeda,2)) , 'Dolares.')
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * cotacao_dolar
    print("O valor de $ " + quantidade + " dólares é R$" + srt(round(conversao_moeda,2)) + "dólares.")
else:
    print(f'Conversão {moeda_origem} para {moeda_destino} não disponível.')
