import os
from time import sleep

import requests

resource = 'https://resultados.tse.jus.br'
url = f'{resource}/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'


def percentage_loadbar(percentage: float):
    load_bar = ['='] * 100
    candidate_bar = load_bar[:int(percentage)]

    while len(candidate_bar) < 100:
        candidate_bar.append(' ')

    print(f'{percentage}% [{"".join(candidate_bar)}]')


def get_candidates() -> list:
    request = requests.get(url)
    result: dict = request.json()

    return result.get('cand')


def print_candidates(candidates: list) -> None:
    for cand in candidates:
        print('=-' * 10)

        print(f'\n\033[42m  {cand["n"]}  \033[m - {cand["nm"]}')
        print(f'Número de votos: {cand["vap"]}\n')

        votes_percent = cand["vap"].replace(',', '.')
        votes_percent = float(votes_percent)

        percentage_loadbar(votes_percent)
        print()

