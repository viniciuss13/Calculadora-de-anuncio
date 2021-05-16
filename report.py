from datetime import date
from typing import List, Any, Dict

from ad import Advertising


def filter_ads(ad_list: List[Advertising], client: str = None,
               start_date: date = None, end_date: date = None) -> List[Advertising]:
    """
    Filtra uma lista de anuncios segundo os parametros opcionais fornecidos.

    :param ad_list: List de anuncios
    :param client: Nome do cliente
    :param start_date: Data inicial
    :param end_date: Data final
    :return: Lista filtrada dos anuncios
    """

    ad_list_filtered = []
    for ad in ad_list:
        if client and ad.client.lower() != client.lower():
            continue
        elif start_date and ad.start_date < start_date:
            continue
        elif end_date and ad.end_date > end_date:
            continue
        else:
            ad_list_filtered.append(ad)

    return ad_list_filtered


def create_report(ad_list: List[Advertising], print_out=True) -> Dict[str, Any]:
    """
    Escreve no terminal um relatório total da lista de anuncios contendo:

    - Total investido
    - Quantidade máxima de visualizações
    - Quantidade máxima de cliques
    - Quantidade máxima de compartilhamentos

    :param ad_list: Lista de anuncios
    :param print_out: Se verdade irá mostrar no terminal
    :return: Dicionário com os dados escritos no terminal
    """

    total_investment = 0
    total_views = 0
    total_clicks = 0
    total_shares = 0

    for ad in ad_list:
        total_investment += ad.total_investment
        total_clicks += ad.total_clicks
        total_views += ad.total_views
        total_shares += ad.total_shares

    report_dict = {
        "investment": total_investment,
        "clicks": total_clicks,
        "views": total_views,
        "shares": total_shares
    }

    if print_out:
        print("Relatório de anuncios:")
        print(f"Total investido: R$ {total_investment}")
        print(f"Quantidade máxima de visualizações: {total_views} visualizações")
        print(f"Quantidade máxima de cliques: {total_clicks} cliques")
        print(f"Quantidade máxima de compartilhamentos: {total_shares} compartilhamentos")

    return report_dict
