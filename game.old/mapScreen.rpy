screen mapScreen:
    add "banquet_hall.png"

    # Повернутись до трапези
    imagebutton:
        xpos 100
        ypos 100
        idle "eat_idle.png"
        hover "eat_hover.png"
        action Jump("feast")
    
    # Поговорити із чоловіком навпроти
    if not is_talk_andriy:
        imagebutton:
            xpos 200
            ypos 200
            idle "andriy_idle.png"
            hover "andriy_hover.png"
            action Jump("talk_with_andriy")
    
    # Поговорити із хлопчиком біля дверей
    if not is_talk_sasha:
        imagebutton:
            xpos 300
            ypos 300
            idle "sasha_idle.png"
            hover "sasha_hover.png"
            action Jump("talk_with_sasha")
    
    # Поговорити із дівчиною з краю столу
    if not is_talk_anna:
        imagebutton:
            xpos 400
            ypos 400
            idle "anna_idle.png"
            hover "anna_hover.png"
            action Jump("talk_with_anna")
    
    # Поговорити із Айлою та Мікко
    imagebutton:
        xpos 500
        ypos 500
        idle "elf_idle.png"
        hover "elf_hover.png"
        action Jump("talk_with_elf")
