#d1 = {'chave1':'valor da chave'}
#d1['nova_chave'] = 'valor da nova chave'

#print (d1)

#d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')

#d1['nova_chave'] = 'valor da nova chave'

clientes ={
    'cliente1' : {
        'nome' : 'Walter',
        'sobrenome' : 'Nobrega',
    },
    'cliente2' : {
        'nome' : 'Helena',
        'sobrenome' : 'Nobrega',

    },

}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')