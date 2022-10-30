import requests

resource = 'https://resultados.tse.jus.br'
url = f'{resource}/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'


def percentage_loadbar(percentage: float):
    load_bar = ['='] * 100
    candidate_bar = load_bar[:int(percentage)]

    while len(candidate_bar) < 100:
        candidate_bar.append(' ')

    print(f'{percentage}% [{"".join(candidate_bar)}]')
