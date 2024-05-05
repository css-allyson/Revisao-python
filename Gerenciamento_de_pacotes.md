Para encontrar um pacote específico podemos procura-lo no https://pypi.org/
Para instalar, desinstalar e listar os pacotes podemos utilizar o pip
```
pip install numpy
pip uninstall numpy
pip list
```
Para lidarmos com as várias versões de pacotes utilizamos ambientes virtuais
Para criar um ambiente virtual utilizamos o comando python3 -m venv myenv, onde myenv é o nome do inventório
```
python3 -m venv myenv
source myenv/bin/activate
```
Para sair do ambiente virtual usamos deactivate
```
deactivate
```
Para gerenciar pacotes podemos utilizar o pipenv, que deve ser instalado globalmente
```
pip install pipenv
```
Após a instalação podemos instalar outros pacotes atravez dele:
```
pipenv install numpy
```
Outra opção para gerenciar pacotes é com o pacote poetry
```
pip install proetry
poetry new myproiject
cd myproject
poetry add numpy
poetry remove numpy
```