def vat(price, rate=0.2):
    """Price including VAT."""
    return round(price * rate, 2)
