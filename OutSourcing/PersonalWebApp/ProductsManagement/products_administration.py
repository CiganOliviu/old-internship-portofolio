from .models import (
    PlannedProduct,
    ActiveWorkingProduct,
    FinishedProduct,
)


def save_data_into_finished_product(product):
    return FinishedProduct(id=product.id,
                           product_name=product.product_name,
                           product_description=product.product_description,
                           list_of_functionalities=product.list_of_functionalities,
                           type=product.type,
                           date=product.date,
                           price=product.price
                           )


def is_data_in_finished_product(product):
    return FinishedProduct.objects.filter(product_name=product.product_name,
                                          product_description=product.product_description,
                                          list_of_functionalities=product.list_of_functionalities,
                                          type=product.type,
                                          date=product.date,
                                          price=product.price).exists()


def save_data_into_active_working_product(product):
    return ActiveWorkingProduct(id=product.id,
                                product_name=product.product_name,
                                product_description=product.product_description,
                                list_of_functionalities=product.list_of_functionalities,
                                type=product.type,
                                price=product.price,
                                percent_done=product.percent_done,
                                ready_for_delivery=product.ready_for_delivery,
                                date=product.date
                                )


def save_data_into_planned_product(product):
    return PlannedProduct(id=product.id,
                          product_name=product.product_name,
                          product_description=product.product_description,
                          list_of_functionalities=product.list_of_functionalities,
                          type=product.type,
                          price=product.price,
                          working_status=product.working_status,
                          date=product.date)


def save_product_from_active_products_in_finished_products():

    products_query = ActiveWorkingProduct.objects.all()

    for product in products_query:
        if product.ready_for_delivery:
            if not is_data_in_finished_product(product):

                save_to_database = save_data_into_finished_product(product)

                save_to_database.save()

                query_active_products = save_data_into_active_working_product(product)

                query_active_products.delete()

                query_planned_products = save_data_into_planned_product(product)

                query_planned_products.delete()


def is_data_in_active_working_product(product):
    return ActiveWorkingProduct.objects.filter(product_name=product.product_name,
                                               product_description=product.product_description,
                                               list_of_functionalities=product.list_of_functionalities,
                                               type=product.type,
                                               price=product.price,
                                               date=product.date).exists()


def save_data_in_active_working_product(product):
    return ActiveWorkingProduct(id=product.id,
                                product_name=product.product_name,
                                product_description=product.product_description,
                                list_of_functionalities=product.list_of_functionalities,
                                type=product.type,
                                price=product.price,
                                date=product.date)


def save_product_from_planned_products_in_active_products():

    products_query = PlannedProduct.objects.all()

    for product in products_query:
        if product.working_status == 'Current Working at':
            if not is_data_in_active_working_product(product):

                save_to_database = save_data_in_active_working_product(product)

                save_to_database.save()

