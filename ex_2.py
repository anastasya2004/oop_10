class NavalBattle:
    """
    This class represents a naval battle game with playing field and methods to play the game.
    """
    playing_field = None
    
    def __init__(self, player):
        """
        Initialize the player for the game.
        """
        self.plyer = player

    @staticmethod
    def show():
        """
        Display the current state of the playing field.
        """
        for row in NavalBattle.playing_field:
            for place in row:
                if place == 0 or place == 1:
                    print('~', end='')
                else:
                    print(place, end='')
            print()

    def shot(self, x, y):
        """
        Perform a shot at the specified coordinates on the playing field.
        """
        x -= 1
        y -= 1
        if NavalBattle.playing_field[y][x] == 1:
            print('попал')
            NavalBattle.playing_field[y][x] = self.plyer
        if NavalBattle.playing_field[y][x] == 0:
            print('мимо')
            NavalBattle.playing_field[y][x] = 'o'


