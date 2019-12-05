import requests
import base64
import json

def boleto(nome, num_doc, insc_estadual, cep, endereco, bairro, cidade, uf, cod_receita, obs, data_vencimento, num_nota, valor):
    with requests.session() as session:
        from headers import emitirBoleto_headers, emitirPDF_headers, download_file_headers
        from payload import emitirBoleto_payload

        session.get('https://www2.agencianet.fazenda.df.gov.br/DarAvulso/')
        session_id = session.cookies.get_dict()
        session_id = session_id['ASP.NET_SessionId']

        emitirBoleto_headers = emitirBoleto_headers.emitirBoleto_headers(session_id)
        emitirBoleto_payload = emitirBoleto_payload.emitirBoleto_payload(nome, num_doc, insc_estadual, cep, endereco, bairro, cidade, uf, cod_receita, obs, data_vencimento, num_nota, valor)
        emitirBoleto = session.post(url='https://www2.agencianet.fazenda.df.gov.br/DarAvulso/Home/EmitirBoleto',
                                    headers=emitirBoleto_headers, data=emitirBoleto_payload)

        emitirPDF_headers = emitirPDF_headers.emitirPDF_headers(session_id)
        emitirPDF_payload = json.dumps(emitirBoleto.text).encode('utf-8')
        emitirPDF = session.post(url='https://www2.agencianet.fazenda.df.gov.br/DarAvulso/Home/EmitirBoletoPDF', headers=emitirPDF_headers, data=emitirPDF_payload)

        fName = json.loads(emitirPDF.text)
        fName = fName['fName']

        download_file_headers = download_file_headers.download_file_headers(session_id)
        download_file = session.get('https://www2.agencianet.fazenda.df.gov.br/DarAvulso/Home/DownloadFile?fName={}'.format(fName), headers=download_file_headers)

        pdf_base64 = base64.b64encode(download_file.content)
        pdf_base64 = str(pdf_base64)

        detalhes = json.loads(emitirBoleto.text)

        return {'detalhes': detalhes,
                'documento': pdf_base64}
