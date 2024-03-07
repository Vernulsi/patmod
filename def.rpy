init python:
    config.label_overrides.update({
        "kirinheadpat": "kirinheadpat_mod"
    })  
# image kirin_pat_say = Movie(play="mods/patmod/Images/Pat Say.webm", channel='movie', loop=True)
# image kirin_pat_pat = Movie(play="mods/patmod/Images/Pat.webm", channel='movie', loop=True)
# image kirin_pat_start = Movie(play="mods/patmod/Images/Start.webm", channel='movie', loop=True)
# image kirin_pat_finish = Movie(play="mods/patmod/Images/Pat.webm", channel='movie', loop=True)
define config.image_cache_size = 18 if not renpy.mobile else 12
define config.predict_statements = 7 if not renpy.mobile else 4

init:
    python:
        dissolvepat_mod = Dissolve(0.25)
    
    image Kirin_1_No_Hand_Silent = Movie(play="mods/patmod/Images/Kirin/1/1 No Hand Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_1_No_Hand_Talk = Movie(play="mods/patmod/Images/Kirin/1/1 No Hand Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_1_Start_Hand = Movie(play="mods/patmod/Images/Kirin/1/1 Start Hand.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_2_No_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/2/2 No Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_2_Start = Movie(play="mods/patmod/Images/Kirin/2/2 Start.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_2_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/2/2 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_2_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/2/2 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_3_Pat_Change = Movie(play="mods/patmod/Images/Kirin/3/3 Pat Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_3_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/3/3 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_4_Pat_Change = Movie(play="mods/patmod/Images/Kirin/4/4 Pat Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_4_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/4/4 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_4_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/4/4 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_5_Pat_Change = Movie(play="mods/patmod/Images/Kirin/5/5 Pat Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_5_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/5/5 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_5_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/5/5 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_6_Pat_Change = Movie(play="mods/patmod/Images/Kirin/6/6 Pat Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_6_Pat_Change_2 = Movie(play="mods/patmod/Images/Kirin/6/6 Pat Change 2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_6_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/6/6 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_6_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/6/6 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_7_Pat_Change = Movie(play="mods/patmod/Images/Kirin/7/7 Pat Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_7_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/7/7 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_7_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/7/7 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_8_Change = Movie(play="mods/patmod/Images/Kirin/8/8 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_8_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/8/8 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_8_Pat_Talk_Brow = Movie(play="mods/patmod/Images/Kirin/8/8 Pat-Talk Brow.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_8_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/8/8 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_9_Change = Movie(play="mods/patmod/Images/Kirin/9/9 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_9_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/9/9 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_9_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/9/9 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_10_Change = Movie(play="mods/patmod/Images/Kirin/10/10 Change V2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_10_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/10/10 Pat-Silent V2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_10_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/10/10 Pat-Talk V2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_11_Change = Movie(play="mods/patmod/Images/Kirin/11/11 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_11_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/11/11 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_11_Pat_Talk_Brow = Movie(play="mods/patmod/Images/Kirin/11/11 Pat-Talk Brow.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_11_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/11/11 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_12_Change = Movie(play="mods/patmod/Images/Kirin/12/12 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_12_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/12/12 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_12_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/12/12 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_13_Change = Movie(play="mods/patmod/Images/Kirin/13/13 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_13_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/13/13 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_13_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/13/13 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_13_Pat_Hand_Trace_1 = Movie(play="mods/patmod/Images/Kirin/13/13 Pat Hand Trace 1.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_13_Pat_Hand_Trace_2 = Movie(play="mods/patmod/Images/Kirin/13/13 Pat Hand Trace 2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_13_Pat_Hand_Trace_3 = Movie(play="mods/patmod/Images/Kirin/13/13 Pat Hand Trace 3.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_14_Change = Movie(play="mods/patmod/Images/Kirin/14/14 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_14_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/14/14 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_14_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/14/14 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_15_Change = Movie(play="mods/patmod/Images/Kirin/15/15 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_15_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/15/15 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image Kirin_16_Change = Movie(play="mods/patmod/Images/Kirin/16/16 Change.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_16_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/16/16 Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image Kirin_16_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/16/16 Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

    image 17_Change_1 = Movie(play="mods/patmod/Images/Kirin/17/17 Change 1(2.5).webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_Change_2 = Movie(play="mods/patmod/Images/Kirin/17/17 Change 2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_Change_3 = Movie(play="mods/patmod/Images/Kirin/17/17 Change 3.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_No_Pat_Silent = Movie(play="mods/patmod/Images/Kirin/17/17 No Pat-Silent.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_No_Pat_Talk = Movie(play="mods/patmod/Images/Kirin/17/17 No Pat-Talk.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_Pat_Silent_1 = Movie(play="mods/patmod/Images/Kirin/17/17 Pat-Silent 1.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_Pat_Silent_2 = Movie(play="mods/patmod/Images/Kirin/17/17 Pat-Silent 2.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)
    image 17_Pat_Talk_1 = Movie(play="mods/patmod/Images/Kirin/17/17 Pat-Talk 1.webm", channel='movie', loop=True, group='kirin', play_callback=play_callback)

