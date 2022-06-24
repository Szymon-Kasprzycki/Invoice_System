from panel.models import *
from django.db.models import Model


def get_client(name: str, surname: str):
    """Retrieves client from database

        Parameters
        ----------
        name : str
            The name of client
        surname : str
            The last name of client

        Returns
        -------
        Model
            Client object

        Raises
        ------
        Model.DoesNotExist
            If client with these credentials does not exist
        Model.MultipleObjectsReturned
            If more than one client with these credentials was found
        """
    try:
        client = Client.objects.get(first_name__iexact=name, last_name__iexact=surname)
        return client
    except Model.DoesNotExist:
        raise Model.DoesNotExist('That client does not exist in the database.')
    except Model.MultipleObjectsReturned:
        raise Model.MultipleObjectsReturned('We have more than one client for given credentials.')


def get_product(name: str, product_id: int = None):
    """Retrieves product from database

        Parameters
        ----------
        name : str
            The name of product
        product_id : int, optional
            The id of product

        Returns
        -------
        Model
            Product object

        Raises
        ------
        Model.DoesNotExist
            If product with this name does not exist
        Model.MultipleObjectsReturned
            If more than one product with this name was found
        """
    try:
        if not product_id:
            product = Product.objects.get(name__contains=name)
        else:
            product = Product.objects.get(name__contains=name, id=product_id)
        return product

    except Model.DoesNotExist:
        raise Model.DoesNotExist('This product does not exist in the database.')
    except Model.MultipleObjectsReturned:
        raise Model.MultipleObjectsReturned('We have more than one product for given attributes.')


def get_invoice(number: str):
    """Retrieves client from database

        Parameters
        ----------
        number : str
            The number of invoice

        Returns
        -------
        Model
            Invoice object

        Raises
        ------
        Model.DoesNotExist
            If invoice with this number does not exist in database
        Model.MultipleObjectsReturned
            If more than one invoice exist with this number
        """
    try:
        invoice = Invoice.objects.get(invoice_number__iexact=number)
        return invoice
    except Model.DoesNotExist:
        raise Model.DoesNotExist('That invoice does not exist in the database.')
    except Model.MultipleObjectsReturned:
        raise Model.MultipleObjectsReturned('We have more than one invoice with given number.')
