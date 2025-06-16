• Comandos para instalar a versão 3.10 do python no ubuntu:
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install software-properties-common -y
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.10 python3.10-venv python3.10-dev
$ python3.10 --version

• Comandos para o poetry:
$ poetry new puc_mlops
$ cd puc_mlops
• Editar o arquivo pyproject.toml com a versão do python "^3.10" e executar o comando:
$ poetry env use python3.10
$ source $(poetry env info --path)/bin/activate
$ poetry install

• Caso use o requirements.txt:
$ poetry add $(grep -vE "^\s*#|^\s*$" requirements.txt)

