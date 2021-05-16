from datetime import datetime
from typing import List

from ad import Advertising
from report import create_report, filter_ads


def clear_terminal_screen():
    """Limpa o terminal com 101 'enters'"""

    print("\n" * 100)


def retry_function(message: str, clear_screen=True) -> bool:
    """
    Verifica se o usuário deseja repetir a última ação

    :param message: Mensagem de nova tentativa
    :param clear_screen: Booleano que determina se o terminal deve ser limpo ou não
    :return: Verdade se o usuário digitar 's'.
    """

    if clear_screen:
        clear_terminal_screen()

    retry = input(f"{message} (s/n) -> ")
    return retry.lower() == "s"


class Menu:
    __date_format = "%d/%m/%Y"
    __ad_list: List[Advertising] = []

    def __add_new_ad(self):
        """Menu de cadastrado de novo anuncio"""

        while True:
            clear_terminal_screen()
            try:
                print("Cadastre o novo anuncio:")
                name = input("nome: ").lower()
                client = input("cliente: ").lower()

                start_date = datetime.strptime(input("data de inicio (dd/mm/yyyy): "), self.__date_format).date()
                end_date = datetime.strptime(input("data de fim (dd/mm/yyyy): "), self.__date_format).date()
                budget_per_day = float(input("Investimento por dia (centavos separado por '.'): "))

                ad = Advertising(name, client, start_date, end_date, budget_per_day)
                assert ad.validate_ad(), "O anuncio não está válido!"
                self.__ad_list.append(ad)

                if not retry_function("Anuncio cadastrado! Deseja adicionar outro?"):
                    break

            except:
                if not retry_function("Houve um erro no cadastro de um novo anuncio. Deseja tentar novamente?"):
                    break

    def __report_filter(self):
        """Menu de filtro de relatório"""

        while True:
            clear_terminal_screen()
            try:
                print("RELATÓRIO DE ANUNCIOS")
                print("Favor indicar os filtros (podendo ser vazio):\n")

                client = input("Cliente: ")
                start_date = input("Data de início (dd/mm/yyyy): ")
                if start_date:
                    start_date = datetime.strptime(start_date, self.__date_format).date()

                end_date = input("Data de fim (dd/mm/yyyy): ")
                if end_date:
                    end_date = datetime.strptime(end_date, self.__date_format).date()

                ads_filtered = filter_ads(self.__ad_list, client=client, start_date=start_date, end_date=end_date)
                print("\n\n")
                create_report(ads_filtered)

                if not retry_function("\nDeseja realizar um novo relatório?", clear_screen=False):
                    break

            except:
                if not retry_function("Houve um erro no relatório de anuncios. Deseja tentar novamente?"):
                    break

    def main_menu(self):
        """Menu inicial"""

        while True:
            try:
                print("MENU INICIAL\n")
                print(f"Total de anuncios cadastrados: {len(self.__ad_list)} anuncios.\n")

                print("Escolha uma das opções abaixo:")
                print("1 - Cadastrar um novo anuncio")
                print("2 - Filtrar relatório")
                print("0 - Sair")

                option = int(input(">> "))

                if option == 0:
                    break
                if option == 1:
                    self.__add_new_ad()
                elif option == 2:
                    if len(self.__ad_list) == 0:
                        input("Não há anuncios cadastrados até momento! Digite qualquer tecla para continuar...")
                    else:
                        self.__report_filter()
                else:
                    print("Sua opção foi inválida!")
            except:
                print("Houve um erro na sua escolha de opção, favor digitar uma válida.")

            clear_terminal_screen()


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
