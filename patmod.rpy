init -1 python:
    def play_callback(old, new):

        renpy.music.play(new._play, channel=new.channel, loop=new.loop, synchro_start=True)

        if new.mask:
            renpy.music.play(new.mask, channel=new.mask_channel, loop=new.loop, synchro_start=True)