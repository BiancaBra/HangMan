import random
words_list = ['management', 'country', 'movie', 'boyfriend', 'freedom', 'marriage',
              'success', 'moment', 'shopping', 'office', 'population', 'opportunity',
              'performance', 'message', 'grandmother', 'imagination', 'personality',
              'employment', 'drama', 'atmosphere', 'comparison', 'feedback', 'childhood',
              'church', 'database', 'village', 'professor', 'supermarket', 'diamond',
              'experience', 'company']




class Game:
    def __init__(self, player_name, word):
        self.player_name = player_name
        self.secret_word = word
        self.guess = {}
        self.mistakes = 0

        for secret_letter in range(0, len(self.secret_word)):
            self.guess[secret_letter] = '_'


    def show_details(self):
        for x in self.guess.values():
            print(x, end='')
        print()

    def check_letter(self, letter):
        if self.secret_word.find(letter) == -1:
            self.update_mistakes()
            self.print_mistakes()
        else:
            for x in range(0, len(self.secret_word)):
                if self.secret_word[x] == letter:
                    self.guess[x] = letter


    def update_mistakes(self):
        self.mistakes += 1


    def check_underscore(self):
        all_letters = True
        for x in self.guess.values():
           if x == '_':
               all_letters = False
               break
        return all_letters


    def continue_game(self):
        if self.mistakes == 6:
            print("You were hanged! The word was:", self.secret_word)
            return False
        elif self.check_underscore():
            print("You win!")
            return False
        else:
            return True


    def print_mistakes_1(self):
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    def print_mistakes_2(self):
        print("   _____ \n"
              "  |     |\n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    def print_mistakes_3(self):
        print("   _____ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    def print_mistakes_4(self):
        print("   _____ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    def print_mistakes_5(self):
        print("   _____ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /|\ \n"
              "  |      \n"
              "__|__\n")

    def print_mistakes_6(self):
        print("   _____ \n"
              "  |     |\n"
              "  |     |\n"
              "  |     |\n"
              "  |     O\n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")

    def print_mistakes(self):
        print("The chosen letter is not found in the secret word.")
        print("The number of remaining attempts is: ", 6 - self.mistakes)
        if self.mistakes == 1:
            self.print_mistakes_1()
        elif self.mistakes == 2:
            self.print_mistakes_2()
        elif self.mistakes == 3:
            self.print_mistakes_3()
        elif self.mistakes == 4:
            self.print_mistakes_4()
        elif self.mistakes == 5:
            self.print_mistakes_5()
        else:
            self.print_mistakes_6()


print('Welcome to HangMan Game!')

playing = True
name = input('Please enter your name: ')
game = Game(name, random.choice(words_list))
print(game.player_name,',your secret word is below:')

while playing:

    game.show_details()
    print()
    letter = input("Choose a letter:")
    game.check_letter(letter)
    playing = game.continue_game()






