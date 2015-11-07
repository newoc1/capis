class Alignment:
    def __init__(self, chaotic, evil, good, lawful):
        self.chaotic = chaotic
        self.evil = evil
        self.good = good
        self.lawful = lawful

    def meets_threshold(self, alignment):
        if (self.chaotic >= alignment.chaotic and self.evil >= alignment.evil
            and self.good >= alignment.good and self.lawful >= alignment.lawful):
            return True
        else:
            return False
