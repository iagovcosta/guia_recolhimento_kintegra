def emitirBoleto_headers(session_id):
    emitirBoleto_payload = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '4317',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'CFID=Z201nibyx9aq62mf28okyjmjlfdzjzcce35yj27f3dps5mj14jt-84164391; CFTOKEN=Z201nibyx9aq62mf28okyjmjlfdzjzcce35yj27f3dps5mj14jt-1ba2d7317eabde9a-686B3439-974F-80FD-001AC1444813548C; __utma=23080613.1510586854.1573421731.1573421731.1573421731.1; __utmz=23080613.1573421731.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId={}'.format(session_id),
        'Host': 'www2.agencianet.fazenda.df.gov.br',
        'Origin': 'https://www2.agencianet.fazenda.df.gov.br',
        'Referer': 'https://www2.agencianet.fazenda.df.gov.br/DarAvulso/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

    }
    return emitirBoleto_payload