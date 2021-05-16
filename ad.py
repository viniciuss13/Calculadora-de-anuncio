from datetime import date

from utils import *


class Advertising:
    """Classe de cadatro de anúncios"""

    name: str
    client: str
    start_date: date
    end_date: date
    budget_per_day: float

    def __init__(self, name: str, client: str, start_date: date, end_date: date, budget_per_day: float):
        """
        Cria uma nova instância de anuncio.

        :param name: Nome do anuncio
        :param client: Nome do cliente
        :param start_date: Data inicial da campanha
        :param end_date: Data final da campanha
        :param budget_per_day: Investimento por dia
        """

        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.budget_per_day = budget_per_day

    def validate_ad(self) -> bool:
        """Valida se o anuncio possui todos os dados."""

        return all([
            bool(self.name),
            bool(self.client),
            self.start_date <= self.end_date,
            self.budget_per_day >= 0
        ])

    @property
    def total_investment(self) -> float:
        """
        Calcula o investimento total considerando o intervalo.

        :return: Total investido durante o intervalo
        """

        return (self.end_date - self.start_date).days * self.budget_per_day

    @property
    def total_views(self) -> int:
        """
        Calcula o total de visualizações durante o intervalo.

        :return: Total de visualizações durante o intervalo.
        """

        return total_views(self.total_investment)

    @property
    def total_clicks(self) -> int:
        """
        Calcula o total de cliques durante o intervalo.

        :return: Total de cliques durante o intervalo
        """

        views = views_budget(self.total_investment)
        return int(clicks_views(views))

    @property
    def total_shares(self) -> int:
        """
        Calcula o total de compartilhamentos durante o intervalo.

        :return: Total de compartilhamentos durante o intervalo
        """

        views = views_budget(self.total_investment)
        clicks = clicks_views(views)
        shares = shares_clicks(clicks)

        return int(shares)
