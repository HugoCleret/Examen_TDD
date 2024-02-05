#hello first commit 

import unittest
from echecs import PlateauDeJeu 

class TestPlateauDeJeu(unittest.TestCase):
    def test_initialisation_plateau(self):
        plateau = PlateauDeJeu()
        self.assertEqual(len(plateau.cases), 64)  # Le plateau comporte 64 cases. 8 cases à l'horizontal et 8 cases à la verticale.
        self.assertTrue(plateau.case_occupee((0, 0)))  # Vérification de la case (O,O Tour) spécifique est occupée pour initialisation de la game

    # Déplacement des pions : 
        
    def test_deplacement_pion(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((1, 0), (3, 0))  # pion vers le haut
        self.assertEqual(plateau.cases[(3, 0)].nom, 'Pion')  # Vérification que la piece déplacee est un pion
        self.assertFalse(plateau.case_occupee((1, 0)))  # Vérification que la case d'origine n'est plus occupee

    def test_deplacement_pion_vers_avant_droite(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((1, 0), (2, 1)) 
        self.assertEqual(plateau.cases[(2, 1)].nom, 'Pion')
        self.assertFalse(plateau.case_occupee((1, 0)))  

    def test_deplacement_pion_vers_avant_gauche(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((1, 1), (2, 0))  
        #print("Plateau apres déplacement du pion vers la gauche : ", plateau.cases)
        self.assertEqual(plateau.cases[(2, 0)].nom, 'Pion') 
        self.assertFalse(plateau.case_occupee((1, 1)))  

    #deplacement Tour :
    def test_deplacement_tour_horizontal(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((0, 0), (0, 4))  # Déplace la tour horizontalement
        self.assertEqual(plateau.cases[(0, 4)].nom, 'Tour')
        self.assertFalse(plateau.case_occupee((0, 0)))

    def test_deplacement_tour_vertical(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((0, 0), (4, 0))  # Déplace la tour verticalement
        self.assertEqual(plateau.cases[(4, 0)].nom, 'Tour')
        self.assertFalse(plateau.case_occupee((0, 0)))

    #deplacement Cavalier :
    def test_deplacement_cavalier(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((0, 1), (2, 0))  # Déplace le cavalier en L
        self.assertEqual(plateau.cases[(2, 0)].nom, 'Cavalier')
        self.assertFalse(plateau.case_occupee((0, 1)))

    #deplacement fou :
    def test_deplacement_fou_diagonale(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((0, 2), (2, 0))
        self.assertEqual(plateau.cases[(2, 0)].nom, 'Fou')
        self.assertFalse(plateau.case_occupee((0, 2)))

if __name__ == '__main__':
    unittest.main()
