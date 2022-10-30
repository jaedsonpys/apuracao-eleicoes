import requests

resource = 'https://resultados.tse.jus.br'
url = f'{resource}/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'


def percentage_loadbar(percentage: float):
    load_bar = ['='] * 100
    candidate_bar = load_bar[:int(percentage)]

    while len(candidate_bar) < 100:
        candidate_bar.append(' ')

    print(f'{percentage}% [{"".join(candidate_bar)}]')


def get_results() -> dict:
    request = requests.get(url)
    result = request.json()

    return result


def get_candidates() -> list:
    result = get_results()
    return result.get('cand')


def get_total_urns() -> float:
    result = get_results()
    total = result.get('pst')

    total = total.replace(',', '.')
    total = float(total)

    return total


def print_candidates(candidates: list) -> None:
    for cand in candidates:
        print('=-' * 10)

        print(f'\n\033[42m  {cand["n"]}  \033[m - {cand["nm"]}')
        print(f'Número de votos: {cand["vap"]}\n')

        votes_percent = cand["pvap"].replace(',', '.')
        votes_percent = float(votes_percent)

        percentage_loadbar(votes_percent)
        print()


if __name__ == '__main__':
    import os
    from time import sleep

    while True:
        try:
            os.system('clear')

            print('Apuração de dados das \033[1mEleições de 2022\033[m')
            print('\033[3;32mDados coletados do site Resultados TSE\033[m')
            print('\033[3;32mScript by \033[4m@jaedsonpys\033[m\n')

            candidates = get_candidates()
            print_candidates(candidates)
            
            sleep(60)
        except KeyboardInterrupt:
            os.system('clear')
            break
