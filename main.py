import os

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
    os.system('cls')
    if disciplinas:
        # exibe as disciplinas registradas
        print('\nDisciplinas registradas: ')
        for disc in list(disciplinas):
            print(f'- {disc}')

        # recebe a selecionada pelo usuário
        disciplina_selecionada = input('\nSelecione uma disciplina: ').upper()

        # retorna a disciplina selecionada caso seja válida
        if disciplina_selecionada in disciplinas:
            return disciplina_selecionada
        else:
            print(f'\n[ERRO] Disciplina {disciplina_selecionada} não registrada.')
            return False
    
    print('\nNenhuma disciplina registrada.')
    return False
    

def adicionar_disciplina():
    '''Registra novas disciplinas ao banco de dados.'''
    os.system('cls')
    print('\n>>> Preparando REGISTRO de nova disciplina...')

    # recebe os dados da nova disciplina
    nome = input('\nDigite o nome da disciplina: ').upper()
    while True:
        # verifica se a carga horária inserida é um número
        ch = input('\nDigite a carga horária total da disciplina (em horas): ')
        if not ch.isdigit():
            print(f'\n[ERRO] Entrada inválida: {ch}. Apenas números são aceitos para registrar a carga horária.')
        else:
            ch = float(ch)
            while True:
                faltas = input('\nDigite quantas faltas já constam nessa disciplina (em horas): ')
                if not faltas.isdigit():
                    print(f'\n[ERRO] Entrada inválida: {faltas}. Apenas números são aceitos para registrar faltas.')
                else:
                    faltas = float(faltas)
                    break
            break
    

    # insere os dados no dicionário
    os.system('cls')
    disciplinas[nome] = {'ch': ch, 'faltas': faltas}
    print(f'\nDisciplina {nome}, de carga horária {ch}h e com {faltas}h de faltas, adicionada com sucesso.')


def exibir_registros():
    '''Exibe cada disciplina registrada e os seus respectivos dados.'''
    os.system('cls')
    if disciplinas:
        for disc, dados in disciplinas.items():
            print(f'\nNOME: {disc}\nCH: {dados['ch']}h\nFALTAS: {dados['faltas']}h')
    else:
        print('\nNenhuma disciplina registrada.')


def adicionar_falta():
    '''Permite adicionar novas faltas aos dados de uma disciplina.'''
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
            if not nova_falta.isdigit():
                print(f'\n[ERRO] Entrada inválida: {nova_falta}. Apenas números são aceitos para registrar faltas.')
            else:
                nova_falta = float(nova_falta)
                break

        # atualiza os dados
        os.system('cls')
        disciplinas[disciplina_selecionada]['faltas'] += nova_falta
        print(f'\nFalta adicionada com sucesso! {nova_falta}h foram adicionadas às {faltas_registradas}h já registradas.')

def apagar_registro():
    '''Permite excluir uma disciplina e seus dados do registro.'''
    os.system('cls')
    # recebe a disciplina a ser apagada
    print('\n>>> Preparando EXCLUSÃO de dados de disciplina...')
    disciplina_selecionada = selecionar_disciplina()
    # caso o usuário insira uma disciplina válida, apaga seus dados
    if disciplina_selecionada:
        os.system('cls')
        del disciplinas[disciplina_selecionada]            
        print(f'\nA disciplina {disciplina_selecionada} e os seus dados foram apagados com sucesso.')


def resetar_registro():
    '''Apaga todos os dados registrados no programa.'''
    os.system('cls')
    global disciplinas
    print('\n>>> Preparando RESET de dados...')
    
    # caso haja dados a serem resetados, prossegue com o processo
    if disciplinas:
        # confirma a intenção de resetar dados
        confirmacao = input('\nTem certeza de que deseja excluir todos os dados armazenados? Essa ação é permanente e não será possível recuperar os dados apagados. [CONFIRMAR / VOLTAR]: ').upper()
        os.system('cls')
        # verifica se o comando inserido é válido
        if confirmacao == 'CONFIRMAR':
            disciplinas = {} # reseta a base de dados
            print('\nDados resetados com sucesso.')
        elif confirmacao != 'VOLTAR':
            print(f'\n[ERRO] Comando não reconhecido: {confirmacao}')
    else:
        print('\nNão há nenhum dado registrado, impossível resetar.')

if __name__ == '__main__':

    # cabeçalho do programa
    print(CABECALHO)
    comando = input('\nDigite aqui: ').upper()

    # banco de dados de disciplinas
    disciplinas = {}

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
        os.system('cls')


        


