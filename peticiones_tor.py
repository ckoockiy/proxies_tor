import requests
from proxies_tor import ProxiesTor
import multiprocessing




def peticion_pagina():
    
    session = ProxiesTor.get_tor_session()
    print(session.get("http://httpbin.org/ip").text)
    
    print("IP SIN PROXY",requests.get("http://httpbin.org/ip").text)


def peticion_pagina_dos():
    
    session = ProxiesTor.get_tor_session1()
    print(session.get("http://httpbin.org/ip").text)
    
    print("IP SIN PROXY",requests.get("http://httpbin.org/ip").text)


def peticion_pagina_tres():
    
    session = ProxiesTor.get_tor_session2()
    print(session.get("http://httpbin.org/ip").text)
    
    print("IP SIN PROXY",requests.get("http://httpbin.org/ip").text)


def peticion_pagina_cuatro():
    
    session = ProxiesTor.get_tor_session3()
    print(session.get("http://httpbin.org/ip").text)
    
    print("IP SIN PROXY",requests.get("http://httpbin.org/ip").text)




p1 = multiprocessing.Process(target=peticion_pagina)
p2 = multiprocessing.Process(target=peticion_pagina_dos)
p3 = multiprocessing.Process(target=peticion_pagina_tres)
p4 = multiprocessing.Process(target=peticion_pagina_cuatro)

p1.start()
p2.start()
p3.start()
p4.start()