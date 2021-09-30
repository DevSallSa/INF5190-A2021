def calculate_tax(article_tax):
    """
    Return article tax keywork as tax rate
    """
    tax = 0
    if article_tax == "FP":
        tax = 1.14975
    elif article_tax == "F":
        tax = 1.05
    elif article_tax == "P":
        tax = 1.09975
    else:
        tax = 1
    return tax
