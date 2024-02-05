class Piece:
    def __init__(self, nom):
        self.nom = nom

class PlateauDeJeu:
    def __init__(self):
        self.cases = {(i, j): None for i in range(8) for j in range(8)}
        self.initialiser_pieces()

    def initialiser_pieces(self):
        # Ajouts des pieces sur le plateau
        # Les blancs
        # Ligne des pions 
        self.cases[(1, 0)] = Piece('Pion')
        self.cases[(1, 1)] = Piece('Pion')
        self.cases[(1, 2)] = Piece('Pion')
        self.cases[(1, 3)] = Piece('Pion')
        self.cases[(1, 4)] = Piece('Pion')
        self.cases[(1, 5)] = Piece('Pion')
        self.cases[(1, 6)] = Piece('Pion')
        self.cases[(1, 7)] = Piece('Pion')
        # Ligne du roi
        self.cases[(0, 0)] = Piece('Tour')
        self.cases[(0, 1)] = Piece('Cavalier')
        self.cases[(0, 2)] = Piece('Fou')
        self.cases[(0, 3)] = Piece('Reine')
        self.cases[(0, 4)] = Piece('Roi')
        self.cases[(0, 5)] = Piece('Fou')
        self.cases[(0, 6)] = Piece('Cavalier')
        self.cases[(0, 7)] = Piece('Tour')

        # Les noirs
        # Ligne des pions 
        self.cases[(6, 0)] = Piece('Pion')
        self.cases[(6, 1)] = Piece('Pion')
        self.cases[(6, 2)] = Piece('Pion')
        self.cases[(6, 3)] = Piece('Pion')
        self.cases[(6, 4)] = Piece('Pion')
        self.cases[(6, 5)] = Piece('Pion')
        self.cases[(6, 6)] = Piece('Pion')
        self.cases[(6, 7)] = Piece('Pion')
        # Ligne du roi
        self.cases[(7, 0)] = Piece('Tour')
        self.cases[(7, 1)] = Piece('Cavalier')
        self.cases[(7, 2)] = Piece('Fou')
        self.cases[(7, 3)] = Piece('Reine')
        self.cases[(7, 4)] = Piece('Roi')
        self.cases[(7, 5)] = Piece('Fou')
        self.cases[(7, 6)] = Piece('Cavalier')
        self.cases[(7, 7)] = Piece('Tour')


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
            
        #deplacement Tour :
        elif piece.nom == 'Tour':
            return origine[0] == destination[0] or origine[1] == destination[1]
        
        #deplacement Cavalier :
        elif piece.nom == 'Cavalier':
            # Cavalier en L
            delta_x = abs(destination[0] - origine[0])
            delta_y = abs(destination[1] - origine[1])
            return (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)
        
        #deplacement fou : 
        elif piece.nom == 'Fou':
            # Fou se déplace en diagonale
            return abs(destination[0] - origine[0]) == abs(destination[1] - origine[1])
        
        #deplacement Reine : 
        elif piece.nom == 'Reine':
            # Reine se déplace horizontalement verticalement et en diagonale
            return origine[0] == destination[0] or origine[1] == destination[1] or \
                   abs(destination[0] - origine[0]) == abs(destination[1] - origine[1]) or \
                   (origine[0] == destination[0] and origine[1] == destination[1])
        
        #deplacement Roi : 
        elif piece.nom == 'Roi':
            # Roi se déplace d'une case dans n'importe quelle sens
            delta_x = abs(destination[0] - origine[0])
            delta_y = abs(destination[1] - origine[1])
            return delta_x <= 1 and delta_y <= 1
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
