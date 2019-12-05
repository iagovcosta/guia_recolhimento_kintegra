def download_file_headers(session_id):
    download_file_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'CFID=Z201nibyx9aq62mf28okyjmjlfdzjzcce35yj27f3dps5mj14jt-84164391; CFTOKEN=Z201nibyx9aq62mf28okyjmjlfdzjzcce35yj27f3dps5mj14jt-1ba2d7317eabde9a-686B3439-974F-80FD-001AC1444813548C; __utma=23080613.1510586854.1573421731.1573421731.1573421731.1; __utmz=23080613.1573421731.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId={}'.format(session_id),
        'Host': 'www2.agencianet.fazenda.df.gov.br',
        'Referer': 'https://www2.agencianet.fazenda.df.gov.br/DarAvulso/',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

    }
    return download_file_headers