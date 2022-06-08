import requests


class ProxiesTor():

    def get_tor_session():
        session = requests.session()

        session.proxies = {'http':  'socks5://127.0.0.1:9050',
                           'https': 'socks5://127.0.0.1:9050'}
        return session

    def get_tor_session1():
        session = requests.session()

        session.proxies = {'http':  'socks5://127.0.0.1:9052',
                           'https': 'socks5://127.0.0.1:9052'}
        return session

    def get_tor_session2():
        session = requests.session()

        session.proxies = {'http':  'socks5://127.0.0.1:9053',
                           'https': 'socks5://127.0.0.1:9053'}
        return session

    def get_tor_session3():
        session = requests.session()

        session.proxies = {'http':  'socks5://127.0.0.1:9054',
                           'https': 'socks5://127.0.0.1:9054'}
        return session
