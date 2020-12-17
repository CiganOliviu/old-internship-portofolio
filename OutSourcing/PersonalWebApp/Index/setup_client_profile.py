from ClientsManagement.models import ClientsDetail


def create_user_in_client_detail(user):
    if not ClientsDetail.objects.filter(user=user):

        save_to_database = ClientsDetail(user=user)

        save_to_database.save()
