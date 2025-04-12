import os

# salvar e carregar dados em um arquivo de texto
# cálculo da frequência
# melhorar exibição de disciplinas no comando EXIBIR

CABECALHO = '''
Comandos disponíveis:
    - DISCIPLINA : registre novas disciplinas.
    - EXIBIR : exibe as disciplinas registradas e seus respectivos dados.
    - FALTA : some uma nova falta aos dados de uma disciplina.
    - APAGAR : apaga o registro e os dados de uma disciplina.
    - RESETAR : apaga todos os registros do banco de dados.
    - SAIR : terminar programa.
'''

def selecionar_disciplina() -> str:
    '''
    Sistema que permite o usuário selecionar uma disciplina já registrada.

    Input:
    - disciplina_selecionada (str) : nome da disciplina que o usuário deseja selecionar.

    Retorno:
    - disciplina (str) : se a disciplina selecionada pelo usuário for válida.
    - False : se não existirem disciplinas registradas ou se o input do
    usuário for inválido.
    '''
    # limpa o terminal
    os.system('cls')

    # verifica se existem disciplinas registradas
    if disciplinas:
        # exibe as disciplinas registradas
        print('\nDisciplinas registradas: ')
        for disc in list(disciplinas):
            print(f'- {disc}')

        # recebe o input do usuário
        disciplina_selecionada = input('\nSelecione uma disciplina: ').upper()

        # retorna a disciplina selecionada, caso seja válida
        if disciplina_selecionada in disciplinas:
            return disciplina_selecionada
        else:
            print(f'\n[ERRO] Disciplina {disciplina_selecionada} não registrada.')
            return False
    
    # retorno caso não existam disciplinas no registro
    print('\nNenhuma disciplina registrada.')
    return False
    

def adicionar_disciplina():
    '''
    Registra novas disciplinas ao banco de dados.

    Input:
    - nome (str) : identificação da nova disciplina.
    - ch (float) : carga horária total da disciplina (em horas).
    - faltas (float) : quantidade de faltas já cometidas na disciplina    
    '''
    # limpa o terminal
    os.system('cls')

    print('\n>>> Preparando REGISTRO de nova disciplina...')
    # recebe os dados da nova disciplina
    nome = input('\nDigite o nome da disciplina: ').upper()
    while True:
        # recebe a carga horária
        ch = input('\nDigite a carga horária total da disciplina (em horas): ')
        # verifica se a ch inserida é válida
        if not ch.isdigit():
            print(f'\n[ERRO] Entrada inválida: {ch}. Apenas números são aceitos para registrar a carga horária.')
        else:
            # converte ch para float
            ch = float(ch)
            while True:
                # recebe as faltas
                faltas = input('\nDigite quantas faltas já constam nessa disciplina (em horas): ')
                # verifica se as faltas inseridas são válidas
                if not faltas.isdigit():
                    print(f'\n[ERRO] Entrada inválida: {faltas}. Apenas números são aceitos para registrar faltas.')
                else:
                    # covnerte as faltas para float
                    faltas = float(faltas)
                    break
            break
    
    # limpa o terminal
    os.system('cls')
    # insere os dados no dicionário
    disciplinas[nome] = {'ch': ch, 'faltas': faltas}
    print(f'\nDisciplina {nome}, de carga horária {ch}h e com {faltas}h de faltas, adicionada com sucesso.')


def exibir_registros():
    '''Exibe cada disciplina registrada e os seus respectivos dados.'''
    # limpa o terminal
    os.system('cls')
    if disciplinas:
        for disc, dados in disciplinas.items():
            print(f'\nNOME: {disc}\nCH: {dados['ch']}h\nFALTAS: {dados['faltas']}h')
    else:
        print('\nNenhuma disciplina registrada.')


def adicionar_falta():
    '''
    Permite adicionar novas faltas aos dados de uma disciplina.
    
    Input:
    - nova_falta (float) : faltas, em horas, a serem adicionadas.
    '''
    # limpa o terminal
    os.system('cls')

    # recebe uma disciplina selecionada pelo usuário
    print('\n>>> Preparando ADIÇÃO DE FALTA...')
    disciplina_selecionada = selecionar_disciplina()
    if disciplina_selecionada:
        # verifica quantas faltas já estão registradas
        faltas_registradas = disciplinas[disciplina_selecionada]['faltas']
        # recebe quantas horas serão adicionadas
        while True:
            nova_falta = input(f'\nDisciplina selecionada: {disciplina_selecionada}. Digite a quantidade de faltas (em horas) que você deseja somar às {faltas_registradas}h já registradas: ') 
            # verifica se a falta é válida
            if not nova_falta.isdigit():
                print(f'\n[ERRO] Entrada inválida: {nova_falta}. Apenas números são aceitos para registrar faltas.')
            else:
                # converte para float
                nova_falta = float(nova_falta)
                break
        
        # limpa o terminal
        os.system('cls')
        # atualiza os dados da disciplina
        disciplinas[disciplina_selecionada]['faltas'] += nova_falta
        print(f'\nFalta adicionada com sucesso! {nova_falta}h foram adicionadas às {faltas_registradas}h já registradas.')

def apagar_registro():
    '''
    Permite excluir uma disciplina e seus dados do registro.
    
    Input:
    - disciplina_selecionada (str) : recebe o nome da disciplina a ser excluída.
    '''
    # limpa o terminal
    os.system('cls')
    
    print('\n>>> Preparando EXCLUSÃO de dados de disciplina...')
    # recebe a disciplina a ser apagada
    disciplina_selecionada = selecionar_disciplina()
    # caso o usuário insira uma disciplina válida, apaga seus dados
    if disciplina_selecionada:
        # limpa o terminal
        os.system('cls')
        # apaga os dados
        del disciplinas[disciplina_selecionada]            
        print(f'\nA disciplina {disciplina_selecionada} e os seus dados foram apagados com sucesso.')


def resetar_registro():
    '''
    Apaga todos os dados registrados no programa.
    
    Input:
    - confirmacao (str) : recebe a confirmação da intenção do usuário.
    '''
    # limpa o terminal
    os.system('cls')

    print('\n>>> Preparando RESET de dados...')
    # caso haja dados a serem resetados, prossegue com o processo
    if disciplinas:
        # recebe a confirmação da intenção de resetar dados
        confirmacao = input('\nTem certeza de que deseja excluir todos os dados armazenados? Essa ação é permanente e não será possível recuperar os dados apagados. [CONFIRMAR / VOLTAR]: ').upper()
        # limpa o terminal
        os.system('cls')
        # verifica se o comando inserido é válido
        if confirmacao == 'CONFIRMAR':
            disciplinas.clear() # reseta a base de dados
            print('\nDados resetados com sucesso.')
        elif confirmacao == 'VOLTAR':
            print(f'\nReset de dados cancelado. Nenhuma informação apagada.')
        else:
            print(f'\n[ERRO] Comando não reconhecido: {confirmacao}')
    else:
        print('\nNão há nenhum dado registrado, impossível resetar.')

if __name__ == '__main__':

    # cabeçalho do programa
    print(CABECALHO)
    comando = input('\nDigite aqui: ').upper()

    # banco de dados de disciplinas
    disciplinas = {}
    
    # exibe o menu de comandos do programa até que 'SAIR' seja inserido
    while comando != 'SAIR':

        if comando == 'DISCIPLINA':
            adicionar_disciplina()
        elif comando == 'EXIBIR':
            exibir_registros()
        elif comando == 'FALTA':
            adicionar_falta()
        elif comando == 'APAGAR':
            apagar_registro()
        elif comando == 'RESETAR':
            resetar_registro()
        else:
            # exibe mensagem de erro caso nenhum dos comandos acima listados tenham sido reconhecidos
            print(f'\n[ERRO] Comando não reconhecido: {comando}')
        
        # exibe novamente o cabeçalho e o input
        print(CABECALHO)
        comando = input('\nDigite aqui: ').upper()
        # limpa o terminal
        os.system('cls')


        


