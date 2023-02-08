import requests


def get_hero(url):
    resp = requests.get(url)
    return resp.json()


def find_smarter(all_hero, *our_hero):
    smarter = None
    max_int = 0
    for el in all_hero:
        if el['name'] in our_hero:
            if el['powerstats']['intelligence'] > max_int:
                smarter = el['name']
    return smarter


if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    all_hero = get_hero(url)
    our_hero = ('Hulk', 'Captain America', 'Thanos')
    smarter_hero = find_smarter(all_hero, *our_hero)
    print(smarter_hero)