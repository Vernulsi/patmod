#Кирин
label kirinheadpat_mod:
    $ sessionpats = 0
    scene black
    # $ renpy.free_memory()
    show Kirin_1_No_Hand_Silent with dissolvepat_mod
    pause 1.9
    show Kirin_1_No_Hand_Talk with dissolvepat_mod
    hide Kirin_1_No_Hand_Silent
    ki "Эмм... могу я тебе чем-то помочь?"
    ki "Не совсем нормально, когда кто-то встает перед тем, с кем он тусуется."
    show Kirin_1_No_Hand_Silent with dissolvepat_mod
    hide Kirin_1_No_Hand_Talk
    menu kirinpatmenu1_mod:
        "Поглаживать":
            pass
        "Не гладить":
            "Что мне делать вместо этого?"
            jump kirininvmenu
    show Kirin_1_Start_Hand with dissolvepat_mod
    hide Kirin_1_No_Hand_Silent
    pause 1.9
    show Kirin_2_No_Pat_Silent with dissolvepat_mod
    hide Kirin_1_Start_Hand
    ki "И это не совсем нормально - просто класть ему руку на голову..."
    show Kirin_2_Start with dissolvepat_mod
    hide Kirin_2_No_Pat_Silent
    menu:
        "Начать гладить":
            pass
        "Не гладить":
            "Что мне делать вместо этого?"
            jump kirininvmenu
    show Kirin_2_Pat_Silent with dissolvepat_mod
    hide Kirin_2_Start
    pause 1.9
    show Kirin_2_Pat_Talk with dissolvepat_mod
    hide Kirin_2_Pat_Silent
    ki "Не буду врать, мне сейчас невероятно неуютно."
    ki "Это ролевая игра? Я должна что-то делать?"
    show Kirin_3_Pat_Change with dissolvepat_mod
    hide Kirin_2_Pat_Talk
    pause 1.9
    show Kirin_3_Pat_Silent with dissolvepat_mod
    hide Kirin_3_Pat_Change
    pause 1.9
    show Kirin_4_Pat_Change with dissolvepat_mod
    hide Kirin_3_Pat_Silent
    pause 1.9
    show Kirin_4_Pat_Talk with dissolvepat_mod
    hide Kirin_4_Pat_Change
    ki "Я не понимаю. Зачем ты это делаешь?"
    ki "Может вместо этого тебе бы понравилось целоваться или что-то в таком роде?"
    ki "Для меня это реально странно. Я не совсем тот человек, которому нравятся такие милые вещи."
    show Kirin_4_Pat_Silent with dissolvepat_mod
    hide Kirin_4_Pat_Talk
    ki "..."
    pause 2.4
    show Kirin_5_Pat_Change with dissolvepat_mod
    hide Kirin_4_Pat_Silent
    pause 1.9
    show Kirin_5_Pat_Silent with dissolvepat_mod
    hide Kirin_5_Pat_Change
    pause 4.3
    show Kirin_5_Pat_Talk with dissolvepat_mod
    hide Kirin_5_Pat_Silent
    ki "Я знаю, что это твоя комната, так что я не буду, типа.. давать тебе указания или типа того."
    ki "Но не считай себя обязанным делать для меня такие вещи."
    ki "Мне достаточно просто быть с тобой... как бы неловко это ни звучало."
    show Kirin_6_Pat_Change with dissolvepat_mod
    hide Kirin_5_Pat_Talk
    pause 1.9
    show Kirin_6_Pat_Change_2 with dissolvepat_mod
    hide Kirin_6_Pat_Change
    pause 1.9
    show Kirin_6_Pat_Silent with dissolvepat_mod
    hide Kirin_6_Pat_Change_2
    pause 1.9
    ki "..."
    show Kirin_6_Pat_Talk with dissolvepat_mod
    hide Kirin_6_Pat_Silent
    ki "Так тебе нравится... делать это и с другими девушками?"
    ki "Не могу же я быть единственной, которую ты... поглаживаешь по голове... или как там это называется."
    ki "Я не разбираюсь в любви. Это заставляет меня чувствовать себя... не в своей тарелке."
    show Kirin_6_Pat_Silent with dissolvepat_mod
    hide Kirin_6_Pat_Talk
    pause 4.3
    show Kirin_7_Pat_Change with dissolvepat_mod
    hide Kirin_6_Pat_Silent
    pause 1.9
    show Kirin_7_Pat_Silent with dissolvepat_mod
    hide Kirin_7_Pat_Change
    pause 4.3
    show Kirin_7_Pat_Talk with dissolvepat_mod
    hide Kirin_7_Pat_Silent
    ki "Эй, ты {i}правда{/i} так хочешь провести наше время вместе?"
    ki "Мы не так уж много общаемся, и мне кажется, что это пустая трата времени - просто... гладить голову."
    ki "...Правда?"
    ki "Я имею в виду, мне не {i}не нравится{/i} это, но... почему?"
    show Kirin_7_Pat_Silent with dissolvepat_mod
    hide Kirin_7_Pat_Talk
    pause 4.3
    show Kirin_8_Change with dissolvepat_mod
    hide Kirin_7_Pat_Silent
    pause 1.9
    show Kirin_8_Pat_Silent with dissolvepat_mod
    hide Kirin_8_Change
    ki "Мм..."
    show Kirin_8_Pat_Talk with dissolvepat_mod
    hide Kirin_8_Pat_Silent
    ki "[kirinmaster]..."
    show Kirin_8_Pat_Silent with dissolvepat_mod
    hide Kirin_8_Pat_Talk
    pause 4.3
    ki "..."
    show Kirin_8_Pat_Talk with dissolvepat_mod
    hide Kirin_8_Pat_Silent
    ki "Возможно, если такое будет случаться время от времени, это никому не навредит."
    ki "Но это не значит, что я не считаю это странным."
    show Kirin_8_Pat_Talk_Brow with dissolvepat_mod
    hide Kirin_8_Pat_Talk
    pause 1.9
    show Kirin_8_Pat_Talk with dissolvepat_mod
    hide Kirin_8_Pat_Talk_Brow
    ki "Очень странным."
    ki "Типа... ты... странный. Или как-то так."
    ki "Я не знаю. Сейчас мне трудно мыслить трезво."
    show Kirin_9_Change with dissolvepat_mod
    hide Kirin_8_Pat_Talk
    pause 1.9
    show Kirin_9_Pat_Talk with dissolvepat_mod
    hide Kirin_9_Change
    ki "Знаешь, что еще более странно, чем твоя внезапная навязчивая идея погладить меня по голове?"
    ki "Тот факт, что ты ни разу не прервал зрительный контакт со мной."
    ki "По крайней мере, постарайся сделать так, чтобы девушка чувствовала себя комфортно, если ты собираешься ставить ее в ситуацию, к которой она не привыкла."
    ki "Так что... да. Успокой меня, [kirinmaster]."
    show Kirin_9_Pat_Silent with dissolvepat_mod
    hide Kirin_9_Pat_Talk
    pause 4.3
    show Kirin_10_Change with dissolvepat_mod
    hide Kirin_9_Pat_Silent
    pause 1.9
    show Kirin_10_Pat_Talk with dissolvepat_mod
    hide Kirin_10_Change
    ki "Ну... эмм..."
    ki "Я определенно начинаю чувствовать себя комфортно, но..."
    ki "Не совсем так, как я ожидала."
    ki "Это ведь не какой-то... фетиш на стыд или что-то такое, да?"
    ki "Потому что, если ты заводишься, проводя пальцами по моим волосам и..."
    ki "Наблюдая, как я начинаю становиться все... более возбуждённой и взволнованной..."
    show Kirin_10_Pat_Silent with dissolvepat_mod
    hide Kirin_10_Pat_Talk
    pause 1.9
    show Kirin_10_Pat_Talk with dissolvepat_mod
    hide Kirin_10_Pat_Silent
    ki "...Блядь."
    ki "Да. Определенно возбуждённой."
    show Kirin_10_Pat_Silent with dissolvepat_mod
    hide Kirin_10_Pat_Talk
    pause 4.3
    show Kirin_11_Change with dissolvepat_mod
    hide Kirin_10_Pat_Silent
    pause 1.9
    show Kirin_11_Pat_Talk with dissolvepat_mod
    hide Kirin_11_Change
    ki "{i}Ух... правда, Кирин?{/i}"
    ki "{i}Промокнуть от малейшего внимания?...{/i}"
    ki "{i}Что с тобой происходит?...{/i}"
    show Kirin_11_Pat_Silent with dissolvepat_mod
    hide Kirin_11_Pat_Talk
    pause 4.3
    ki "Нгх..."
    show Kirin_11_Pat_Talk with dissolvepat_mod
    hide Kirin_11_Pat_Silent
    ki "[kirinmaster]..."
    ki "Если ты собираешься продолжать это делать, можешь хотя бы позволить мне... сесть к тебе на колени?"
    show Kirin_11_Pat_Talk_Brow with dissolvepat_mod
    hide Kirin_11_Pat_Talk
    pause 1.9
    show Kirin_11_Pat_Talk with dissolvepat_mod
    hide Kirin_11_Pat_Talk_Brow
    ki "Звучит забавно... правда?"
    show Kirin_11_Pat_Silent with dissolvepat_mod
    hide Kirin_11_Pat_Talk
    pause 4.3
    show Kirin_12_Change with dissolvepat_mod
    hide Kirin_11_Pat_Silent
    pause 1.9
    show Kirin_12_Pat_Talk with dissolvepat_mod
    hide Kirin_12_Change
    ki "Хехех..."
    ki "Ты прекрасно проводишь время, да?"
    show Kirin_12_Pat_Silent with dissolvepat_mod
    hide Kirin_12_Pat_Talk
    "Кирин вытягивает ноги вперед и умудряется обхватить ногами мои колени, используя пятки, чтобы притянуть меня ближе."
    pause 4.3
    show Kirin_12_Pat_Talk with dissolvepat_mod
    hide Kirin_12_Pat_Silent 
    ki "Насколько ты сейчас крепкий, [kirinmaster]?"
    ki "Это ведь часть твоего плана, верно?"
    ki "Взбесить меня небольшой капелькой внимания, чтобы я позволила тебе кончить на моё милое личико..."
    ki "Ты ведь этого хочешь, верно?"
    show Kirin_12_Pat_Silent with dissolvepat_mod
    hide Kirin_12_Pat_Talk
    "Все, чего я хочу - гладить тебя по голове."
    pause 4.3
    show Kirin_13_Change with dissolvepat_mod
    hide Kirin_12_Pat_Silent
    pause 1.89
    show Kirin_13_Pat_Talk with dissolvepat_mod
    hide Kirin_13_Change
    ki "Нгх... дерьмо..."
    ki "Теперь я действительно начинаю это чувствовать..."
    show Kirin_13_Pat_Silent with dissolvepat_mod
    hide Kirin_13_Pat_Talk
    "Давление пяток Кирин, впивающихся в мои ноги, ослабевает, когда она раздвигает колени и начинает тереть себя через юбку."
    pause 4.3
    show Kirin_13_Pat_Talk with dissolvepat_mod
    hide Kirin_13_Pat_Silent
    ki "Думаю, я не против мастурбировать перед тобой, если ты этого хочешь..."
    ki "Я просто надеюсь, что больше никого нет дома. Я могу стать немного громкой, когда кончаю."
    ki "И мы же не хотим, чтобы у тебя были неприятности?"
    show Kirin_13_Pat_Silent with dissolvepat_mod
    hide Kirin_13_Pat_Talk
    pause 4.3
    ki "Хах... хах... нгах..."
    show Kirin_13_Pat_Talk with dissolvepat_mod
    hide Kirin_13_Pat_Silent
    ki "Ты уверен, что... не хочешь... подрочить мне сам, [kirinmaster]?..."
    ki "Где веселье в... таком странном фетише, как этот, если... ты не можешь закончить его хорошим, старомодным способом..."
    ki "Я вся разогрелась для тебя..."
    if brony == True:
        show Kirin_13_Pat_Silent with dissolvepat_mod
        hide Kirin_13_Pat_Talk
        "Я содрогаюсь при мысли о том, каково было бы, если бы она была пони и у нее были бы копыта."
        "Но мне нельзя показывать ей виду, иначе я не смогу завершить свою миссию."
        "..."
        "Но... Как же она была бы хороша в образе Эплджек.."
    show Kirin_13_Pat_Hand_Trace_1 with dissolvepat_mod
    if brony == True:
        hide Kirin_13_Pat_Silent
    else:
        hide Kirin_13_Pat_Talk
    pause 1.9
    show Kirin_13_Pat_Hand_Trace_2 with dissolvepat_mod
    hide Kirin_13_Pat_Hand_Trace_1
    pause 1.9
    show Kirin_13_Pat_Hand_Trace_3 with dissolvepat_mod
    hide Kirin_13_Pat_Hand_Trace_2
    pause 1.9
    show Kirin_13_Pat_Silent with dissolvepat_mod
    hide Kirin_13_Pat_Hand_Trace_3
    "Кирин протягивает ко мне руку и проводит указательным пальцем по контуру моего члена."
    if brony == True:
        "На секунду у меня привстал, но всё прошло, потому что Кирин дотронулась до моего члена рукой, а не копытом..."
    show Kirin_13_Pat_Talk with dissolvepat_mod
    hide Kirin_13_Pat_Silent
    ki "Да ладно тебе... [kirinmaster]..."
    ki "Давай немного повеселимся... по-другому..."
    show Kirin_13_Pat_Silent with dissolvepat_mod
    hide Kirin_13_Pat_Talk
    pause 4.3
    show Kirin_14_Change with dissolvepat_mod
    hide Kirin_13_Pat_Silent
    pause 1.9
    show Kirin_14_Pat_Talk with dissolvepat_mod
    hide Kirin_14_Change
    ki "Блядь... [kirinmaster]..."
    ki "Ты правда... не собираешься мне вообще помогать?..."
    ki "Плевать... и так сойдет, наверное..."
    ki "Я думаю... гладить милую девушку по голове, пока она... не кончит на всю твою кровать, звучит довольно забавно..."    
    ki "Но не сердись на меня, если я... испорчу твои простыни..."
    ki "Возможно, они уже немного намокли..."
    show Kirin_14_Pat_Silent with dissolvepat_mod
    hide Kirin_14_Pat_Talk
    pause 4.3
    show Kirin_14_Pat_Talk with dissolvepat_mod
    hide Kirin_14_Pat_Silent
    ki "Нгх... бля..."
    show Kirin_14_Pat_Silent with dissolvepat_mod
    hide Kirin_14_Pat_Talk
    pause 4.3
    show Kirin_14_Pat_Talk with dissolvepat_mod
    hide Kirin_14_Pat_Silent
    ki "Я собираюсь кончить, [kirinmaster]..."
    show Kirin_14_Pat_Silent with dissolvepat_mod
    hide Kirin_14_Pat_Talk
    "Я был так поглощен поглаживанием ее головы, что до сих пор не замечал, что юбка и трусики Кирин уже сняты и валяются на полу рядом со мной."
    "Я так впечатлен, что чуть не убрал руку с ее головы."
    pause 4.3
    show Kirin_14_Pat_Talk with dissolvepat_mod
    hide Kirin_14_Pat_Silent    
    ki "Тебе это нравится, да?"
    ki "Смотреть, как отчаявшаяся маленькая девочка теребит свою киску, пока ты гладишь ее по голове?"
    ki "Ты тоже хочешь кончить, [kirinmaster]?"
    ki "Давай... вынимай его..."
    ki "Кончи на меня. Все в порядке."
    show Kirin_15_Change with dissolvepat_mod
    hide Kirin_14_Pat_Talk
    pause 1.9
    show Kirin_15_Pat_Silent with dissolvepat_mod
    hide Kirin_15_Change
    pause 4.3
    "К несчастью для Кирин, у меня есть дело, которое нужно закончить в первую очередь."
    pause 4.3
    show Kirin_16_Change with dissolvepat_mod
    hide Kirin_15_Pat_Silent
    pause 1.9
    show Kirin_16_Pat_Talk with dissolvepat_mod
    hide Kirin_16_Change
    ki "Срань господня... может быть, мне... нравится вот так смущаться?"
    ki "Я уже близко, [kirinmaster]..."
    ki "Очень близко..."
    ki "Просто... погладь меня еще несколько раз и..."
    show Kirin_16_Pat_Silent with dissolvepat_mod
    hide Kirin_16_Pat_Talk
    pause 4.3
    show 17_Change_1 with dissolvepat_mod
    hide Kirin_16_Pat_Silent
    pause 1.7
    with cumflash and hpunch
    show 17_Pat_Silent_1 with dissolvepat_mod
    hide 17_Change_1
    ki "ААХХХ!!! ХАХ... АХ... АХХХХХХХ!!!~~~ ЕБАТЬ!!!!"
    show 17_Pat_Talk_1 with dissolvepat_mod
    hide 17_Pat_Silent_1
    ki "Бля... бля! Хах..."
    ki "Боже мой... Боже мой... ебать..."
    show 17_Change_2 with dissolvepat_mod
    hide 17_Pat_Talk_1
    pause 1.9
    show 17_Pat_Silent_2 with dissolvepat_mod
    hide 17_Change_2
    pause 1.9
    show 17_Change_3 with dissolvepat_mod
    hide 17_Pat_Silent_2
    pause 1.9
    show 17_No_Pat_Silent with dissolvepat_mod
    hide 17_Change_3
    "Кирин перестает ласкать себя и вцепляется в простыню кровати, используя другую руку, чтобы схватить меня за мою."
    "Это мешает мне дальше поглаживать её, поэтому я немного расстроен."
    pause 1.9
    ki "Хах... хах..."
    show 17_No_Pat_Talk with dissolvepat_mod
    hide 17_No_Pat_Silent
    ki "Эй..."
    ki "Это был... гм..."
    ki "Интересный опыт..."
    show 17_No_Pat_Silent with dissolvepat_mod
    hide 17_No_Pat_Talk
    scene black with dissolve2
    stop music fadeout 10.0
    $ kirinpatgasm = True
    $ kirinpats += renpy.random.randint(501, 666)
    "Я так долго гладил Кирин по голове, что день подошел к концу, прежде чем я осознал это ..."
    "Но, по крайней мере, она хорошо провела время."
    "Возможно... {i}слишком хорошо{/i}..."
    if day < 6:
        jump endofweekday
    else:
        jump endofsat
    jump kirininvmenu
