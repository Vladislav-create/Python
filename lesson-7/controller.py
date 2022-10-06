import views
import model

def select_user_menu():
    res = views.user_menu()
    if res == 1:
        views.views_show_users(model.show_users())
    elif res == 2:
        model.create_user(views.user_data_entry())
    elif res == 3:
        views.views_show_users(model.show_users())
        model.delete_user(views.user_num_for_delete())
        views.views_show_users(model.show_users())
    else:
        views.views_show_users(model.show_users())
        model.apdate_user(views.user_num_for_update(), model.show_users())
        views.views_show_users(model.show_users())