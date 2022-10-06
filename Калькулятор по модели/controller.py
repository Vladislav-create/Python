import views
import model
import logging

logging.basicConfig(level=logging.INFO, filename='logi.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M')


def process_data():
    user_select = views.show_menu()
    logging.info(f'варварварвар {user_select}')
    if user_select == 1:
        result = model.calculate(views.calc())
        views.output(result)
    elif user_select == 2:
        result = model.converter_model(views.converter_view())
        views.output_converter(result)
    else:
        exit()
