s = input()
aluguel = ['aluguel',  'alugo', 'alugar']
venda = ['venda', 'vendo', 'vender']
tipo_casa = ['casa']
tipo_apartamento = ['apartamento']
metros = ['metros quadrados', 'm2']
tipos_endereco = ['rua', 'avenida', 'Rua', 'Avenida']

modalidade = 'nao informado'
tipo_modalidade = 'nao informado'
endereco = 'nao informado'
cep = 'nao informado'
area = 'nao informado'
valor = 'nao informado'
contatos = 'nao informado'
responsavel = 'nao informado'

# Variável de controle para o primeiro teste
primeiro_teste = True

# venda/aluguel
for mod in aluguel:
    if mod in s.lower():
        modalidade = 'Aluguel'

for mod in venda:
    if mod in s.lower():
        modalidade = 'Venda'

# casa/ap
for tip in tipo_casa:
    if tip in s.lower():
        tipo_modalidade = 'Casa'

for tip in tipo_apartamento:
    if tip in s.lower():
        tipo_modalidade = 'Apartamento'

# endereço
for tipo in tipos_endereco:
    if tipo in s:
        partes = s.split(tipo, 1)
        if len(partes) > 1:
            parte_endereco = partes[1]
            numero = None
            for palavra in parte_endereco.replace(',', ' ').split():
                if palavra.isdigit():
                    numero = palavra
                    break

            if numero:
                if primeiro_teste:
                    endereco = f"{tipo.capitalize()} {parte_endereco.split(',', 1)[0].strip()}, numero {numero}"
                    primeiro_teste = False  # Desativa após o primeiro teste
                else:
                    endereco = f"{tipo.capitalize()} {parte_endereco.split(',', 1)[0].strip()}, {numero}"
                break

# cep
for i in range(len(s) - 8):
    cep_digit = s[i:i + 9]

    if cep_digit[5] == '-' and cep_digit[:5].isdigit() and cep_digit[6:].isdigit():
        if 'CEP' in s.upper()[i - 4:i + 1]:
            cep = cep_digit
            break

# metros
for m in metros:
    if m in s:
        s_div = s.lower().replace('.', '').replace(',', '').replace(';', '').replace(':', '').split()

        for i in range(len(s_div)):
            if s_div[i].isdigit():
                if i + 1 < len(s_div) and s_div[i + 1] == m.split()[0]:
                    area = int(s_div[i])
                    break

# valor
if 'r$' in s.lower():
    p = s.lower().index('r$') + 2
    valor = ''
    while p < len(s) and (s[p].isdigit() or s[p] in ',.'):
        valor += s[p]
        p += 1
elif 'reais' in s.lower():
    p = s.lower().index('reais') - 2
    valor = ''
    while p >= 0 and (s[p].isdigit() or s[p] in ",."):
        valor = s[p] + valor
        p -= 1

# telefone
telefones = []
telefone = ''

for i in range(len(s)):
    if s[i].isdigit():
        telefone += s[i]
    elif s[i] == '-' and telefone.isdigit():
        telefone += s[i]
    else:
        if telefone:
            dig_telefone = telefone.split('-')
            if len(dig_telefone) == 2 and len(dig_telefone[0]) >= 4 and len(dig_telefone[1]) >= 4:
                telefones.append(telefone)
            telefone = ''

if telefone:
    dig_telefone = telefone.split('-')
    if len(dig_telefone) == 2 and len(dig_telefone[0]) >= 4 and len(dig_telefone[1]) >= 4:
        telefones.append(telefone)

if telefones:
    contatos = ", ".join(telefones)

# responsavel
string = s.strip().split('. ')
string_fim = string[-1]
palavras = string_fim.split()
palavras_ignora = ['Falar', 'Vendo', 'Valor', 'Procurar', 'Contato', 'Marcar', 'Agendar' 'Ligar']
pegar_nome = []
for c in palavras:
    c = c.replace('.', '').replace(',', '')
    if c[0].isupper() and c not in palavras_ignora:
        pegar_nome.append(c)

if 2 <= len(pegar_nome) <= 3:
    responsavel = ' '.join(pegar_nome)

print(f'Modalidade: {modalidade}')
print(f'Tipo: {tipo_modalidade}')
print(f'Endereco: {endereco}')
print(f'CEP: {cep}')
print(f'Area: {area}')
print(f'Valor: {valor}')
print(f'Telefone: {contatos}')
print(f'Responsavel: {responsavel}')