import requests

resource = 'https://resultados.tse.jus.br'
url = f'{resource}/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'


def percentage_loadbar(percentage: float):
    load_bar = ['='] * 100
    candidate_bar = load_bar[:int(percentage)]

    while len(candidate_bar) < 100:
        candidate_bar.append(' ')

    print(f'{percentage:.2f}% [{"".join(candidate_bar)}]')


def get_results() -> dict:
    request = requests.get(url)
    result = request.json()

    return result


def get_candidates(result: dict) -> list:
    return result.get('cand')


def get_total_urns(result: dict) -> float:
    total = result.get('pst')

    total = total.replace(',', '.')
    total = float(total)

    return total


def get_blank_votes(result: dict) -> int:
    blank_votes = result.get('vb')

    blank_votes = blank_votes.replace(',', '.')
    blank_votes = int(blank_votes)

    return blank_votes


def get_null_votes(result: dict) -> int:
    null_votes = result.get('tvn')

    null_votes = null_votes.replace(',', '.')
    null_votes = int(null_votes)

    return null_votes


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

            result = get_results()

            total_urns = get_total_urns(result)
            blank_votes = get_blank_votes(result)
            null_votes = get_null_votes(result)

            print(f'Total de urnas apuradas: {total_urns:.2f}%')
            print(f'Votos em branco: {blank_votes}')
            print(f'Votos nulos: {blank_votes}\n')

            candidates = get_candidates(result)
            print_candidates(candidates)
            
            sleep(30)
        except KeyboardInterrupt:
            os.system('clear')
            break
