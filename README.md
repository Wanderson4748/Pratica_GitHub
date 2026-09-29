# GIT Terminal >>>> Git Desktop

Aqui explico a diferença entre o Github Desktop e o Git Terminal.
## Diferenças:

### 1. Reflog
    Registro de Referências, todo repositório inicializado em git possui uma caixa preta que registra tudo que acontece: commits, branchs, pull-requests, push, merge, clone...

### 2. Interactive Rebase (git rebase -i)
Permite reescrever o histórico de commits de forma cirúrgica antes de enviar para o repositório remoto.

No terminal, você pode usar o modo interativo para juntar (squash) vários commits bagunçados em um só, reordenar a linha do tempo, mudar mensagens antigas de commit ou até dividir um commit grande em partes menores. O GitHub Desktop tem recursos limitados para isso e não oferece o mesmo nível de personalização.

### 3. Git Bisect (O Detetive de Bugs)
É um comando de busca binária automatizada para encontrar qual commit exatamente introduziu um bug no código.

Você diz ao Git qual era o último commit bom e o commit atual com defeito. O terminal testa os commits intermediários automaticamente, perguntando se o erro está presente em cada etapa, até achar o culpado exato. O GitHub Desktop não possui interface para essa funcionalidade.

### 4. Staging Interativo Linha por Linha (git add -p)
Embora o GitHub Desktop permita selecionar arquivos ou blocos inteiros (chunks), o terminal com a flag -p (patch) permite avaliar linha por linha exata de uma modificação.

Você decide com precisão cirúrgica o que vai entrar no commit atual e o que vai ficar de fora, ideal para quando você misturou correções de bugs e refatorações no mesmo arquivo.