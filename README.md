# Filtragem-de-informa-es
Achei esse código perdido no meus arquivos e resolvi melhorá-lo para ficar. Ele filtra informações de textos com foco na  venda/aluguel de imóveis.

# Como usar
É muito simples na verdade, o código pegará as informações de textos sobre imóveis, por exemplo, se usarmos:

"Vendo apartamento na Rua dos Bobos, 123 - CEP 12345-678, 80m², valor R$ 350.000, contato: Matt Corvo, telefone (11) 98765-4321"

Então o código pegará:

Informações extraídas:
Modalidade: Venda
Tipo: Apartamento
CEP: 12345-678
Área: 80m²
Valor: 350.000.
Telefone: 98765-4321
Endereço: Rua dos Bobos, 123
Responsável: Matt Corvo

# O que temos em funcionamento?
As informações estão sendo colhidas de forma adequada na maioria dos testes feitos, cerca de 20 textos (10 em bom português, 10 com diversos erros e/ou escritos de forma incorreta para testes). 
No geral, o código está funcionando bem, mas claro, se o texto inserido for muito mal escrito ou se informações faltarem haverá feedback na saída.

# Para o futuro
- Vou fazer muito mais testes;
- Vou colocar mais uma função para o preço de alugueis por mês;
- Vou melhorar o design da saída de informações;
- (Talvez) Colocar se o imóvel aceita animais de estimação.
