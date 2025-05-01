# ⏰ FALTÔMETRO

Projeto pessoal feito em **Python** que possibilita um melhor controle do número de faltas em cada uma das suas disciplinas da faculdade. 

Geralmente, é necessário que o aluno tenha no **mínimo** 75% de presença nas aulas de uma disciplina para conquistar, de fato, a aprovação. A partir da carga horária total e da quantidade de faltas, é possível calcular se esse requesito está sendo atendido pelo discente ou não. 

Utilize o faltômetro e evite surpresas ao fim do semestre!

![screenshot](https://github.com/ricdavila/faltometro/blob/02aca63e253213a498cc24e61c4d8837bf7ffd67/imgs/program_screenshot.png)

## 💾 Instalação 

1. Clone o repositório:
```
git clone https://github.com/ricdavila/faltometro.git
   
cd faltometro
```
2. Execute o script **main.py**:
```
python main.py
```
3. Pronto! O programa está pronto para ser utilizado. Leia as instruções e adicione as disciplinas e seus dados pelo terminal.

4. Para encerrar a execução do programa, digite `SAIR`.

> [!NOTE]
> Os dados do registro (nomes de disciplinas, suas cargas horárias, suas faltas, etc.) ficarão salvas em um arquivo `registros.txt`, em formato JSON. O registro será **criado e atualizado automaticamente** pelo script no diretório em que ele estiver sendo executado.

## 📃 Como usar

Uma vez executado o script principal, o programa exibirá a lista de comandos disponíveis para uso. Utilize-os para criar, atualizar e apagar dados do seu registro de dados.

- `DISCIPLINA` : use este comando para adicionar uma nova disciplina ao registro. Em seguida, insira os dados solicitados: nome da disciplina, carga horária total, faltas até o momento.
- `EXIBIR` : digite esse comando para visualizar o seu registro de dados. As disciplinas e suas respectivas cargas horárias, faltas e presenças (%) serão exibidas.
- `FALTA` : comando usado para atualizar o registro de uma disciplina. Insira em que disciplina a falta ocorreu e digite as horas a que essa falta corresponde.
- `APAGAR` : atualize o registro apagando por completo uma disciplina e os seus dados. Use o comando e digite o nome da disciplina a ser deletada.
- `RESETAR` : apague o registro de dados, incluindo todas as disciplinas, faltas, etc. O arquivo `registros.txt` terá todos os dados apagados.

## ⚙️ Funcionamento

O programa funciona de maneira simples e direta: cria um **dicionário** e usa-o como banco de dados, com pares `disciplina:dados`, onde `disciplina` representa uma chave e identifica-se pelo nome da disciplina, e `dados` é o valor atrelado à chave, sendo um subdicionário que contém carga horária, faltas e porcentagem de frequência. 

Sendo criado o dicionário, basta que o script realize, mediante os comandos inseridos, as solicitações do usuário. 

Ou seja, o fluxo do programa segue a seguinte linha de processamento:

1. Carregar registro de dados (caso exista)
2. Processar comandos do usuário para modificar o banco de dados
3. Atualizar o registro a cada modificação

**Obsevação:** Nesse repositório, disponibilizei também o arquivo `algoritmo.txt`, contendo o algoritmo inicial em **pseudocódigo**. Esse algoritmo não afeta diretamente o código e nem realiza operações por si só, porém, é uma maneira de visualizar e arquitetar o programa antes de iniciar a codificação do projeto. Normalmente, um algoritmo bem estruturado e com lógica eficiente torna o processo de criar o código fonte mais prático, uma vez que o transforma em uma mera "tradução" e adaptação do pseudocódigo para uma linguagem de programação. 

---

Desenvolvido com muito 🤍 e ☕ utilizando Python 🐍. Deseja conferir outros projetos? Acesse [meu perfil](https://github.com/ricdavila).

