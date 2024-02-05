class Piece:
    def __init__(self, nom):
        self.nom = nom

class PlateauDeJeu:
    def __init__(self):
        self.cases = {(i, j): None for i in range(8) for j in range(8)}
        self.initialiser_pieces()

    def initialiser_pieces(self):
        # Ajouts des pièces sur le plateau
        
        # Ligne des pions 
        self.cases[(1, 0)] = Piece('Pion')
        # Ligne du roi
        self.cases[(0, 0)] = Piece('Tour')

    def case_occupee(self, position):
        return self.cases[position] is not None

    def deplacer_piece(self, origine, destination):
        piece = self.cases[origine]
        if piece:
            self.cases[destination] = piece
            self.cases[origine] = None
