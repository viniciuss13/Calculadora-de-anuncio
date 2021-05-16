def clicks_views(views: float) -> float:
    """
    A cada 100 pessoas que visualizam o anúncio 12 clicam nele.

    :param views: Quantidade de visualizações
    :return: Quantidade de cliques por visualizações
    """

    return views / 100 * 12


def shares_clicks(clicks: float) -> float:
    """
    A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.

    :param clicks: Quantidade de cliques
    :return: Quantiade de compartilhamentos
    """

    return clicks / 20 * 3


def views_shares(shares: float) -> float:
    """
    Cada compartilhamento nas redes sociais gera 40 novas visualizações.

    :param shares: Quantidade de Compartilhamentos
    :return: Quantidade de visualizações
    """

    return shares * 40


def views_budget(budget: float) -> float:
    """
    30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.

    :param budget: Valor orçado
    :return: Visualizações recebidas
    """

    return budget * 30


def views_multiplier(views: float) -> float:
    """
    o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
    (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)

    :param views: Visualizações
    :return: Visualizações considerando compartilhamentos em sequência
    """

    return views * 4


def total_views(budget: float) -> int:
    """
    Calcula o total de visualizações considerando compartilhamentos e o valor orçado

    :param budget: Valor orçado
    :return: Quantidade aproximada de visualizações
    """

    views = views_budget(budget)
    clicks = clicks_views(views)
    shares = shares_clicks(clicks)
    views += views_shares(shares)
    views = views_multiplier(views)

    return int(views)
