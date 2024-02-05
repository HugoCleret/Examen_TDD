class PlateauDeJeu:
    def __init__(self):
        self.cases = {(i, j): None for i in range(8) for j in range(8)}

    def case_occupee(self, position):
        return self.cases[position] is not None

    def deplacer_piece(self, origine, destination):
        self.cases[destination] = self.cases[origine]
        self.cases[origine] = None
