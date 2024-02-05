class Piece:
    def __init__(self, nom):
        self.nom = nom

class PlateauDeJeu:
    def __init__(self):
        self.cases = {(i, j): None for i in range(8) for j in range(8)}
        self.initialiser_pieces()

    def initialiser_pieces(self):
        # Ajouts des pieces sur le plateau

        # Ligne des pions 
        self.cases[(1, 0)] = Piece('Pion')
        self.cases[(1, 1)] = Piece('Pion')
        # Ligne du roi
        self.cases[(0, 0)] = Piece('Tour')

    def case_occupee(self, position):
        return self.cases[position] is not None
    
    def validite_deplacement(self,origine, destination ):
        piece = self.cases[origine]

        #les limites du plateau
        if not (0 <= destination[0] < 8 and 0 <= destination[1] < 8):
            return False

        #déplacement des pions 
        if piece.nom == 'Pion':
            
            if destination[0] == origine[0] + 1 and destination[1] == origine[1]:
                return True
            elif destination[0] == origine[0] + 1 and destination[1] == origine[1] + 1:
                return True
            elif destination[0] == origine[0] + 1 and destination[1] == origine[1] - 1:
                return True
        elif piece.nom == 'Tour':
            return origine[0] == destination[0] or origine[1] == destination[1]


        return False

    def deplacer_piece(self, origine, destination):
        piece = self.cases[origine]
        print(piece)
        if piece is not None:
            print(f"Déplacement autorisé de {origine} à {destination}")
            self.cases[destination] = piece
            self.cases[origine] = None
        else:
            print(f"Déplacement non autorisé de {origine} à {destination}")
