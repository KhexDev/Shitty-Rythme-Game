class Conductor:
    def __init__(self):
        self.songPosition = 0
        self.bpm = 120
        self.crochet = (self.bpm / 60)