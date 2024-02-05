#hello first commit 

import unittest
from echecs import PlateauDeJeu 

class TestPlateauDeJeu(unittest.TestCase):
    def test_initialisation_plateau(self):
        plateau = PlateauDeJeu()
        self.assertEqual(len(plateau.cases), 64)  # Le plateau comporte 64 cases. 8 cases à l'horizontal et 8 cases à la verticale.
        self.assertTrue(plateau.case_occupee((0, 0)))  # Vérification de la case (O,O Tour) spécifique est occupée pour initialisation de la game

    def test_deplacement_pion(self):
        plateau = PlateauDeJeu()
        plateau.deplacer_piece((1, 0), (3, 0))  # Déplace un pion vers le haut
        self.assertEqual(plateau.cases[(3, 0)].nom, 'Pion')  # Vérifie que la pièce déplacée est un pion
        self.assertFalse(plateau.case_occupee((1, 0)))  # Vérifie que la case d'origine n'est plus occupée

if __name__ == '__main__':
    unittest.main()
