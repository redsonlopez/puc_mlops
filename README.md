• Instale o pyenv para o gerenciamento de versões do python:
$ curl -fsSL https://pyenv.run | bash

• Execute o comando para configurar o arquivo .bashrc com o pyenv:
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

• Reinicie o terminal e execute o comando abaixo para as dependências necessárias para o pyenv:
$ sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

• Instale a versão do python 3.10 usando o pyenv:
$ pyenv install 3.10
$ pyenv versions

• No diretótio do projeto
$ pyenv local 3.10.18
$ poetry install

---

• Comandos para o poetry:
$ poetry new puc_mlops
$ cd puc_mlops

• Editar o arquivo pyproject.toml com a versão do python "^3.10" e executar o comando:
$ poetry env use python3.10
$ source $(poetry env info --path)/bin/activate
$ poetry install

• Caso use o requirements.txt:
$ poetry add $(grep -vE "^\s*#|^\s*$" requirements.txt)

