"""
Simple Bot
"""

import requests

from gmpyinfr_telegram.utils import read_conf_file

class SimpleBot:
    """Implementa um simples bot que só envia mensagens aos destinatários."""

    def __init__(self, filepath):
        """
        Construtor.

        Params:
            - filepath : str indicando local do arquivo de configuração do bot
        """

        conf = read_conf_file(filepath)
        self.token = conf['token']
        self.errordest = conf['error']
        self.warndest = conf['warn']

        if not self.token:
            raise ValueError("Token inválido")

        if not self.errordest:
            raise ValueError("Destinatários de erro inválidos")

        if not self.warndest:
            raise ValueError("Destinatários de warn inválidos")

    def send_msg(self, chat_id, msg, parse_mode='Markdown'):
        """
        Faz o envio de um texto qualquer para um id qualquer

        Params:
            - chat_id : int id do destinatário
            - msg : str mensagem a ser enviada
            - parse_mode : str parse mode para tratar a mensagem. Deve seguir os
                parse modes definidos na API do Telegram.
        """

        url = ('https://api.telegram.org/bot{}/sendMessage?'
               'chat_id={}&parse_mode={}&text={}')

        response = requests.get(url.format(self.token, chat_id, parse_mode, msg))
        return response
