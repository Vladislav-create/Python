import views
import model


def select_user_menu():
    res = views.user_menu()
    if res == 1:
        views.show_all_users(model.show_users())
    elif res == 2:
        model.add_user_model(views.add_user())
    elif res == 3:
        views.show_all_users(model.show_users())
        model.del_user_model(views.del_user())
        views.show_all_users(model.show_users())
    else:
        views.show_all_users(model.show_users())
        model.change_user(views.update_user())
        views.show_all_users(model.show_users())
