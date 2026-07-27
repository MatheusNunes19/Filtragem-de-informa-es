import re  # Expressões regulares para pesquisa, combinação e manipulação de strings

# Melhoria do codigo Imóveis, encontrado perdido nos meus arquivos kk, para fins de treino e aprendizado, e para fins de estudo de regex, e manipulação de strings.

def filtrIinformacoes(string):  # Função para armazenar resultados
    info = {
        'modalidade': 'Não informado.',
        'tipo': 'Não informado.',
        'endereco': 'Não informado.',
        'cep': 'Não informado.',
        'area': 'Não informado.',
        'valor':' Não informado.',
        'telefone': 'Não informado.',
        'responsavel': 'Não informado.'
    }

    menor = string.lower()  # Vai deixar tudo no diminutivo

    "1 Modalidade: Aluquel/Venda"
    if any(palavra in menor for palavra in ['aluguel' 'alugo', 'alugar', 'alugando']):
        info['modalidade'] = 'Aluguel'
    elif any(palavra in menor for palavra in ['venda', 'vendo', 'vender', 'vendendo']):
        info['modalidade'] = 'Venda'

    "2 Tipo: Casa/Apartamento/Kitnet/Estúdio/Loft/Flat" # Para ter certeza que não esqueci nada! kkk
    if 'casa' in menor:
        info['tipo'] = 'Casa'
    elif any(palavra in menor for palavra in [ 'apartamento', 'apt', 'apto', 'apê', 'ap']):
        info['tipo'] = 'Apartamento'
    elif 'kitnet' in menor or  'kit' in menor:
        info['tipo'] = 'Kitnet'
    elif 'estúdio' in menor:
        info['tipo'] = 'Estúdio'
    elif 'loft' in menor:
        info['tipo'] = 'Loft'
    elif 'flat' in menor:
        info['tipo'] = 'Flat'

    # 3 CEP
    padrao_CEP = r'\b\d{5}-\d{3}\b'  # Padrão para encontrar CEPs em formatos 12345-678/123456789
    combina_CEP = re.search(padrao_CEP, string)
    if combina_CEP:
        info['cep'] = combina_CEP.group()

    # 4 Área
    padrao_area = r'(\d+)\s*(?:m²|m2|metros? quadrados?)'  #padrao pra encontrar áreas
    combina_area = re.search(padrao_area, menor)
    if combina_area:
        info['area'] = int(combina_area.group(1))

    # 5 Valor
    padrao_valor = r'(?:r?\$|reais)\s*([\d.,]+)'
    combina_valor = re.search(padrao_valor, menor)
    if combina_valor:
        valor_str = combina_valor.group(1).replace(',', '.')
        info['valor'] = valor_str

    # 6 Telefone
    padrao_telefone = r'(?:\(?\{2}\)?\s*)?(?:9?\d{4}[-\s]?\d{4})'  # Padrão para encontrar números de telefone
    telefone = re.findall(padrao_telefone, string)
    if telefone:
        info['telefone'] = ", ".join(telefone)

    # 7 Endereço (agora se nao funcionar eu desito)
    # separa logradouro, nome de rua e numero
    padrao_ender = r'(?P<logradouro>Rua|Avenida|Av\.|Travessa|Alameda|Praça|Rodovia|Estrada|Condominio\.?)\s+(?P<rua>[^\d,]+)(?:,\s*(?P<numero>\d+))?'
    combina_ender = re.search(padrao_ender, string, re.IGNORECASE)
    if combina_ender:
        endereco = combina_ender.group(0)
        padrao_numero = r'\b\d+\b'
        combina_numero = re.search(padrao_numero, endereco)
        if combina_numero:
            info['endereco'] = endereco
        else:
            info['endereco'] = f"{endereco}, S/N"

    # 8 Responsavel (Agora vai achar o caboclo)
    # procura pelos padroes mais comuns de falar com, resposavel, procurar por... pipipi popopo
    padrao_responsa = r'(?:respos[áa]vel|contato|falar com|procurar por|aos cuidadoes de)\s*[:;]\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})'
    combina_responsa = re.search(padrao_responsa, string, re.IGNORECASE)
    if combina_responsa:
        info['responsavel'] = combina_responsa.group(1)
    else:
        # se der ruim, tenta pega nome no fim do texto
        partes = string.split('\n')[-1]
        ultima_parte = partes[-1].strip()
        palavras = ultima_parte.split()
        nomes = [pala for pala in palavras if pala[0].isupper() and len(pala) > 2 
                 and pala.lower() not in ['valor', 'vendo', 'falar', 'contato', 'ligar', 'marcar', 'agendar']]
        if 2 <= len(nomes) <= 3:
            info['responsavel'] = ' '.join(nomes[:3])

    return info

s = input("Digite sobre o imovel: ")
resultado = filtrIinformacoes(s)

# vou melhorar essa exibição depois, ta muito fei
print("\n========================")
print("Informações extraídas:")
print("Modalidade:", resultado['modalidade'])
print("Tipo:", resultado['tipo'])
print("CEP:", resultado['cep'])
print(f"Área: {resultado['area']}m²")
print("Valor:", resultado['valor'])
print("Telefone:", resultado['telefone'])
print("Endereço:", resultado['endereco'])
print("Responsável:", resultado['responsavel'])
print("========================")
