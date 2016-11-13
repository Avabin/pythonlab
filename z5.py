class Song:
    lyrics = []

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me(self):
        ret = ""
        for line in self.lyrics:
            ret += "\n      " + str(line)
        return ret
