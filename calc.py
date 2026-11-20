def vat(price, rate=0.2):
    """Price including VAT."""
    return round(price * (1 + rate), 2)
