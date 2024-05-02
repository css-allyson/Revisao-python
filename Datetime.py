# %%
#importa a biblioteca datetime para trabalhar com datas e horas,
#ver documentação em: https://docs.python.org/3/library/datetime.html 
import datetime 


# %%
#armazena na variável d uma data por ano, mês e dia
d = datetime.date(2024,5,19)
print(d)


# %%
#para evitar de colocar datetime, fazer a importação a seguir
from datetime import date
d = date(2025,5,20)
print(d)


# %%
from datetime import datetime
#Método datetime() além de armazenar data armazena hora, minuto e segundo
d = datetime(2024,5,19, 20,35,25)
print(d)

# %%
from datetime import datetime
#Caso nao seja informado hora, minuto e segundo retorna zerado
d = datetime(2024,5,19)
print(d)

# %%
from datetime import date
#Método today() retorna o dia, mês e ano atual
print(date.today())


# %%
from datetime import datetime
#Para objeto tipo datetime o método today() também retorna hora, minuto e segundo atual
print(datetime.today())


# %%
#objeto time armazena informação de hora
from datetime import time
d = time(10, 20, 0)
print(d)


# %%
from datetime import datetime, timedelta
d= datetime(2024,5,24, 20,35,25)
#Ao utilizar timedelta é possível fazer operações com datas
#como a adição ou subtração de períodos de tempo de uma data
print(d)
d2 = d+ timedelta(weeks=1)
print(d2)


#%%
#Não é possível trabalhar com timedelta e time. é preciso trabalhar com
#datetime e depois converter para time()
from datetime import datetime, time, timedelta
d = datetime.today() - timedelta(hours=1)
d2 = d.time()
print(d2)


# %%
#para converser formatos de datas diferentes da utilizada no datetime
#utilizamos o método strftime, passando a string com a data e uma máscara
#de como a data e hora está organizada
from datetime import datetime
data = "20/07/2023 15:30"
d = datetime.strptime(data, "%d/%m/%Y %H:%M")
print(d)

# %%
#já o método strftime transforma uma datetime para uma formatação específica
#como por exemplo a formatação utilizada em PT-BR
from datetime import datetime
date_format = "%d/%m/%Y %a %H:%M"
d = datetime.today()
d2 = d.strftime(date_format)
print(d)
print(d2)

# %%
#para trabalhar com fusos horários utilizamos a biblioteca pytz
#obs é necessário instalar o módulo com pip install pytz
import pytz
from datetime import datetime

d= datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)
d2= datetime.now(pytz.timezone("Europe/Paris"))
print(d2)


# %%
#Outra opção de trabalhar com diferentes fusos horários é com o método timezone e o timedelta
#da biblioteca datetime para utilizar diferentes valores de UTC

from datetime import datetime, timezone, timedelta

d = datetime.now(timezone(timedelta(hours=6)))
d2 = datetime.now(timezone(timedelta(hours=-3)))

print(d)

print(d2)