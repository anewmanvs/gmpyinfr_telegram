"""
EstBot

Bot específico do grupo de Estatística
"""

from gmpyinfr_telegram.bot.simplebot import SimpleBot

class EstBot(SimpleBot):
    """Implementa o bot da Estatística."""

    def __init__(self, filepath):
        """
        Construtor.

        Params:
            - filepath : str indicando local do arquivo de configuração do bot
        """

        super().__init__(filepath)

    def send_error(self, procname, msg):
        """
        Envia uma mensagem de erro para os destinatários da configuração.

        Params:
            - procname : str nome do processo onde ocorreu o erro.
            - msg : str mensagem de erro a ser incorporada no texto padrão.

        Returns:
            - dict contendo o status do envio para cada destinatário, True para
                sucesso e False para falha.
        """

        msg = ('Finalizada execução do proceso <b>{}</b> e algo deu errado. :(\n'
               '<code>{}</code>').format(procname, msg)

        status = {}
        for dest in self.errordest:
            response = self.send_msg(dest, msg, parse_mode='HTML')
            status[dest] = response.status_code == 200

        return status

    def send_warn(self, procname, msg_extra=''):
        """
        Envia mensagem padrão informando que o processo executou sem problemas.

        Params:
            - procname : str nome do processo que finalizou com sucesso.
            - msg_extra : str mensagem extra a ser adicionada ao final

        Returns:
            - dict contendo o status do envio para cada destinatário, True para
                sucesso e False para falha.
        """

        msg = ('Finalizada execução do processo <b>{}</b>. Tudo ocorreu'
               ' aparentemente bem :)\n{}').format(procname, msg_extra)

        status = {}
        for dest in self.warndest:
            response = self.send_msg(dest, msg, parse_mode='HTML')
            status[dest] = response.status_code == 200

        return status
