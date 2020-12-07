from .models import (
    PlannedProduct,
    ActiveWorkingProduct,
    FinishedProduct,
)


def save_product_from_active_products_in_finished_products():

    products_query = ActiveWorkingProduct.objects.all()

    for product in products_query:
        if product.ready_for_delivery:
            if not FinishedProduct.objects.filter(product_name=product.product_name,
                                                  product_description=product.product_description,
                                                  list_of_functionalities=product.list_of_functionalities,
                                                  type=product.type,
                                                  date=product.date,
                                                  price=product.price).exists():
                save_to_database = FinishedProduct(id=product.id,
                                                   product_name=product.product_name,
                                                   product_description=product.product_description,
                                                   list_of_functionalities=product.list_of_functionalities,
                                                   type=product.type,
                                                   date=product.date,
                                                   price=product.price
                                                   )

                save_to_database.save()

                query_active_products = ActiveWorkingProduct(id=product.id,
                                                             product_name=product.product_name,
                                                             product_description=product.product_description,
                                                             list_of_functionalities=product.list_of_functionalities,
                                                             type=product.type,
                                                             price=product.price,
                                                             percent_done=product.percent_done,
                                                             ready_for_delivery=product.ready_for_delivery,
                                                             date=product.date
                                                             )

                query_active_products.delete()

                query_planned_products = PlannedProduct(id=product.id,
                                                        product_name=product.product_name,
                                                        product_description=product.product_description,
                                                        list_of_functionalities=product.list_of_functionalities,
                                                        type=product.type,
                                                        price=product.price,
                                                        working_status=product.working_status,
                                                        date=product.date)

                query_planned_products.delete()


def save_product_from_planned_products_in_active_products():

    products_query = PlannedProduct.objects.all()

    for product in products_query:
        if product.working_status == 'Current Working at':
            if not ActiveWorkingProduct.objects.filter(product_name=product.product_name,
                                                       product_description=product.product_description,
                                                       list_of_functionalities=product.list_of_functionalities,
                                                       type=product.type,
                                                       price=product.price,
                                                       date=product.date).exists():

                save_to_database = ActiveWorkingProduct(id=product.id,
                                                        product_name=product.product_name,
                                                        product_description=product.product_description,
                                                        list_of_functionalities=product.list_of_functionalities,
                                                        type=product.type,
                                                        price=product.price,
                                                        date=product.date)

                save_to_database.save()