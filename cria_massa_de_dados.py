import json
from faker import Faker
from random import randint

fake = Faker("pt_BR")

arquivo_de_massa = "dados/massa.json"
quantidade_de_jobs = 50

jobs = []

for id in range(1, randint(1, quantidade_de_jobs)):
    j = {
            "ID": f"{id}",
            "Descrição": f"{fake.catch_phrase()}",
            "Data Máxima de conclusão": f"{fake.future_datetime().strftime('%Y-%m-%d %H:%M:%S')}",
            "Tempo estimado": f"{randint(1,24)} horas"
        }
    jobs.append(j)

with open(arquivo_de_massa, mode="w") as file:
    file.write(json.dumps(jobs, indent=2, ensure_ascii=False))
