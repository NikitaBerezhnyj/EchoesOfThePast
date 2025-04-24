init python:
    def get_main_menu_background():
        # Перевіряємо значення persistent.game_status і повертаємо відповідний фон
        if persistent.game_status == 1:
            return "gui/main_menu_1.png"
        elif persistent.game_status == 2:
            return "gui/main_menu_2.png"
        else:
            return "gui/main_menu.png"