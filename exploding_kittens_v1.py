import random

whole_deck = [ 
    "Attack","Attack","Attack","Attack","Attack",
    "Skip","Skip","Skip","Skip","Skip",
    "Shuffle","Shuffle","Shuffle","Shuffle","Shuffle",
    "Favor","Favor","Favor","Favor","Favor",
    "nAC - Melon","nAC - Melon","nAC - Melon","nAC - Melon",
    "nAC - Beard", "nAC - Beard", "nAC - Beard", "nAC - Beard", 
    "nAC - Potato","nAC - Potato","nAC - Potato","nAC - Potato",
    "nAC - Taco","nAC - Taco","nAC - Taco","nAC - Taco",
    "nAC - Rainbow","nAC - Rainbow","nAC - Rainbow","nAC - Rainbow"
    ]

# print(len(whole_deck))

# shuffle the original deck
random.shuffle(whole_deck)

# deal cards
# to AI
hand_AI = whole_deck[0:4]
hand_AI.append("Defuse")
# print("\n",hand_AI)
del whole_deck[0:4]

# to player
hand_player = whole_deck[0:4]
hand_player.append("Defuse")
# print("\n",hand_player)
del whole_deck[0:4]

# now the deck constists of only remaining cards + 1 exploding kitten
whole_deck.append("Exploding kitten")
random.shuffle(whole_deck)
# print("\n", whole_deck)
# print(len(whole_deck))

# values of cards
Exploding_kitten_val = -20
Defuse_val = 15
nAC_val = 5
Favor_val = 10
Shuffle_val = 2
Att_val = 10
Sk_val = 10


# init discard pile
discard_pile = []

# function, which takes card from deck and gives it to selected player
def draw_card(subject,deck):
    card = deck[0]
    subject.append(card)
    del deck[0]


class Actions:
    '''Possible actions of a subject, according to one's hand'''

    # init all states in hand and names of players
    def __init__(self,subject,hand):
        self.hand = hand
        self.subject = subject
        
        # init possible actions
        self.can_defuse = False
        self.can_attack = False
        self.can_skip = False
        self.can_favor = False
        self.can_shuffle = False
        self.must_draw = True

        if "Defuse" in self.hand:
            self.can_defuse = True        
        else: 
            self.can_defuse = False 
        
        if "Attack" in self.hand:
            self.can_attack = True
        else: 
            self.can_attack = False     
        
        if "Skip" in self.hand:
            self.can_skip = True
        else: 
            self.can_skip = False 
        
        if "Shuffle" in self.hand:
            self.can_shuffle = True
        else: 
            self.can_shuffle = False 
        
        if "Favor" in self.hand:
            self.can_favor = True   
        else: 
            self.can_favor = False

    # rewrite all possible actions based on hand
    def rewrite_possibilities(self):
        self.must_draw = True
        # rewrite possible actions based on hand
        if "Defuse" in self.hand:
            self.can_defuse = True        
        else: 
            self.can_defuse = False 
        
        if "Attack" in self.hand:
            self.can_attack = True
        else: 
            self.can_attack = False     
        
        if "Skip" in self.hand:
            self.can_skip = True
        else: 
            self.can_skip = False 
        
        if "Shuffle" in self.hand:
            self.can_shuffle = True
        else: 
            self.can_shuffle = False 
        
        if "Favor" in self.hand:
            self.can_favor = True   
        else: 
            self.can_favor = False      

    # reveal all cards in hand
    def reveal_hand(self):
        print("Hi, I'm {} and in my hand is {}".format(self.subject,self.hand))

    # print possible actions based on hand
    def possible_actions(self):
        if "Defuse" in self.hand:
            print("I can defuse!")       

        if "Attack" in self.hand:
            print("I can attack!")
        
        if "Skip" in self.hand:
            print("I can skip a round.")

        if "Shuffle" in self.hand:
            print("I can shuffle the deck.")

        if "Favor" in self.hand:
            print("I can take a card from opponent.")

    # function representing action of drawing a card from deck      FUNGUJE
    def draw_card(self,deck):
        drawn_card = deck[0]
        self.hand.append(drawn_card)
        del deck[0]

        # rewrite possible actions based on hand taking into consideration newly drawn card
        self.rewrite_possibilities()

        # scenario where you draw exploding kitten
        if drawn_card == "Exploding kitten" and self.can_defuse == True:
            print("You must defuse the exploding kitten!")
            # using Defuse
            played_card = self.hand.index("Defuse")
            del self.hand[played_card]
            discard_pile.append("Defuse")
            # putting back exploding kitten
            new_position = random.randint(0,len(deck))
            deck.insert(new_position,"Exploding kitten")
            # delete E.K. from hand
            EK_index = self.hand.index("Exploding kitten")
            del self.hand[EK_index]

        elif drawn_card == "Exploding kitten" and self.can_defuse == False:
            print("The kitten exploded in {} hands.\nGame over.\n---------".format(self.subject))
            discard_pile.append("Exploding kitten")
            EK_index = self.hand.index("Exploding kitten")
            del self.hand[EK_index]
            
    
    # CHCE ROZPRACOVAT VARIANTA, KDY SE PLAYER MUZE BRANIT KARTE ATTACK REDIRECTNUTIM ATTACKU NA OPONENTA
    #def being_attacked(self,subject2,deck):
    #   # chceck whether subject1 can defend itself, aka redirect attack back at subject2
    #   if self.can_attack == True:

    # function representing playing an ATTACK card on opponent      FUNGUJE
    def card_attack(self,subject2,deck):
        if self.can_attack == True:
            print("You attack!")
            # call draw_card function on opposing player
            draw_card(subject2,whole_deck)

            ####### being_attacked(subject2,deck)

            # find index of played Attack card
            played_card = self.hand.index("Attack")
            # delete said Attack card
            del self.hand[played_card]
            # put said Attack card into discard pile
            discard_pile.append("Attack")
        else:
            print("You cannot attack.")
    
    # function representing playing a SKIP card         NOT YET
    def card_skip(self):
        if self.can_skip == True:
            self.must_draw = False
            
            # discarding Skip card
            played_card = self.hand.index("Skip")
            del self.hand[played_card]
            discard_pile.append("Skip")
        else:
            print("You cannot skip this round.")
    
    # function representing playing a SHUFFLE card      FUNGUJE
    def card_shuffle(self,deck):
        if self.can_shuffle == True:
            random.shuffle(deck)
            
            # discarding Shuffle card
            played_card = self.hand.index("Shuffle")
            # delete said Shuffle card
            del self.hand[played_card]
            # put said Shuffle card into discard pile
            discard_pile.append("Shuffle")
        else:
            print("You cannot shuffle.")

    # function representing playing a FAVOR card        FUNGUJE
    def card_favor(self,subject2):
        if self.can_favor == True:
            card_position = random.randint(0,len(subject2.hand)-1)     # random integer in range 0 to length of enemy hand - 1
            print(card_position)
            card = subject2.hand[card_position]
            self.hand.append(card)
            del subject2.hand[card_position]

            # discarding Favor card
            played_card = self.hand.index("Favor")
            del self.hand[played_card]
            discard_pile.append("Favor")

            # rewrite possibilities with new card in hand 
            self.rewrite_possibilities()
        else:
            print("You cannot ask for a card.")


    enemy_defuse = 1
    def enemy_defuse_check(self,subject2):
        if "Defuse" in discard_pile and "Defuse" in self.hand:
            subject2.enemy_defuse = 0
        else:
            subject2.enemy_defuse = 1

    my_defuse = 1
    def my_defuse_check(self):
        if "Defuse" in self.hand:
            self.my_defuse = 1
        else:
            self.my_defuse = 0

    EK_in_deck = 1
    def deck_EK_check(self):
        if "Exploding kitten" in discard_pile:
            self.EK_in_deck = 0
        else:
            self.EK_in_deck = 1

    # calculate probabilities of drawing every card from deck
    def draw_probabilities(self,subject2,deck):

        self.enemy_defuse_check(subject2)
        self.deck_EK_check()
        # probability of drawing exploding kitten from deck
        self.draw_prob_EK = self.EK_in_deck/(len(deck))
        print(len(deck))
        # probability of drawing attack from deck
        att_in_hand = self.hand.count("Attack")
        print("I have {} Attack".format(att_in_hand))

        att_in_disc = discard_pile.count("Attack")
        self.draw_prob_attack =  (5 - att_in_hand - att_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing skip from deck
        skip_in_hand = self.hand.count("Skip")
        print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        self.draw_prob_skip = (5 - skip_in_hand - skip_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing shuffle from deck
        sh_in_hand = self.hand.count("Shuffle")
        print("I have {} Shuffle".format(sh_in_hand))

        sh_in_disc = discard_pile.count("Shuffle")
        self.draw_prob_shuffle = (5 - sh_in_hand - sh_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing favor from deck
        f_in_hand = self.hand.count("Favor")
        print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        self.draw_prob_favor = (5 - f_in_hand - f_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing a non action card from deck
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        print("I have {} nAC".format(nac_in_hand))

        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        self.draw_prob_nAC = (20 - nac_in_hand - nac_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)
    
    # function calculating probabilities of drawing cards from enemy hand and deck
    def draw_probabilities_with_favor(self,subject2,deck):
        # not sure if this math works tho
        # probability of drawing defuse
        self.enemy_defuse_check(subject2)
        self.draw_prob_defuse = subject2.enemy_defuse / (len(subject2.hand))

        self.deck_EK_check()
        # probability of drawing exploding kitten from deck
        self.draw_prob_EK = self.EK_in_deck/(len(deck))

        # probability of drawing attack from deck and enemy hand
        att_in_hand = self.hand.count("Attack")
        # print("I have {} Attack".format(att_in_hand))

        att_in_disc = discard_pile.count("Attack")
        self.draw_prob_attack_w_Favor = 2 * (5 - att_in_hand - att_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing skip from deck
        skip_in_hand = self.hand.count("Skip")
        # print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        self.draw_prob_skip_w_Favor = 2 * (5 - skip_in_hand - skip_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing shuffle from deck
        sh_in_hand = self.hand.count("Shuffle")
        # print("I have {} Shuffle".format(sh_in_hand))

        sh_in_disc = discard_pile.count("Shuffle")
        self.draw_prob_shuffle_w_Favor = 2 * (5 - sh_in_hand - sh_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing favor from deck
        f_in_hand = self.hand.count("Favor")
        # print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        self.draw_prob_favor_w_Favor = 2 * (5 - f_in_hand - f_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

        # probability of drawing a non action card from deck
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        # print("I have {} nAC".format(nac_in_hand))

        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        self.draw_prob_nAC_w_Favor = 2 * (20 - nac_in_hand - nac_in_disc) / (len(deck) + len(subject2.hand) - subject2.enemy_defuse)

    # this function computes probabilites, with which the opposing player draws cards from deck and my hand
    def enemy_draw_probabilities_with_favor(self,subject2,deck):

        # chance of enemy taking my defuse
        self.my_defuse_check()
        subject2.draw_prob_defuse = self.my_defuse / (len(self.hand))

        subject2.deck_EK_check()
        # probability of drawing exploding kitten from deck
        subject2.draw_prob_EK = subject2.EK_in_deck/(len(deck))

        # probability of drawing attack from deck and my hand
        att_in_hand = self.hand.count("Attack")
        # print("I have {} Attack".format(att_in_hand))
        att_in_disc = discard_pile.count("Attack")
        subject2.draw_prob_attack_w_Favor = ((5 - att_in_hand - att_in_disc) / (len(deck) + len(self.hand) - self.enemy_defuse)) + (att_in_hand / len(self.hand))

        # probability of drawing skip from deck and my hand
        skip_in_hand = self.hand.count("Skip")
        # print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        subject2.draw_prob_skip_w_Favor = ((5 - skip_in_hand - skip_in_disc) / (len(deck) + len(self.hand) - self.enemy_defuse)) + (skip_in_hand / len(self.hand))

        # probability of drawing shuffle from deck and my hand
        sh_in_hand = self.hand.count("Shuffle")
        # print("I have {} Shuffle".format(sh_in_hand))

        sh_in_disc = discard_pile.count("Shuffle")
        subject2.draw_prob_shuffle_w_Favor = ((5 - sh_in_hand - sh_in_disc) / (len(deck) + len(self.hand) - self.enemy_defuse)) + (sh_in_hand / len(self.hand))

        # probability of drawing favor from deck and my hand
        f_in_hand = self.hand.count("Favor")
        # print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        subject2.draw_prob_favor_w_Favor = ((5 - f_in_hand - f_in_disc) / (len(deck) + len(self.hand) - self.enemy_defuse)) + (f_in_hand / len(self.hand))

        # probability of drawing a non action card from deck and my hand
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        # print("I have {} nAC".format(nac_in_hand))
        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        subject2.draw_prob_nAC_w_Favor = ((20 - nac_in_hand - nac_in_disc) / (len(deck) + len(self.hand) - self.enemy_defuse)) + (nac_in_hand / len(self.hand))

    # creates variables, which represent subjective value (probability * value) of drawing different cards from deck
    def eval_draw(self):
        # creates variables, which represent subjective value (probability * value) of drawing different cards from deck
        self.expl_kitten_value = Exploding_kitten_val * self.draw_prob_EK
        self.skip_value = Sk_val * self.draw_prob_skip
        self.shuffle_value = Shuffle_val * self.draw_prob_shuffle
        self.favor_value = Favor_val * self.draw_prob_favor
        self.nAC_value = nAC_val * self.draw_prob_nAC
        self.attack_value = Att_val * self.draw_prob_attack

    # creates variables, which represent subjective value (probability * value) of drawing different cards from deck and with favor
    def eval_draw_favor(self):
        self.expl_kitten_value_f = Exploding_kitten_val * self.draw_prob_EK
        self.skip_value_f = Sk_val * self.draw_prob_skip_w_Favor
        self.shuffle_value_f = Shuffle_val * self.draw_prob_shuffle_w_Favor
        self.favor_value_f = Favor_val * self.draw_prob_favor_w_Favor
        self.nAC_value_f = nAC_val * self.draw_prob_nAC_w_Favor
        self.attack_value_f = Att_val * self.draw_prob_attack_w_Favor
        self.defuse_value = Defuse_val * self.draw_prob_defuse
    

    def eval_probabilities(self):
        self.eval_draw()
        self.eval_draw_favor()

        self.value_of_draw = self.expl_kitten_value + self.skip_value + self.shuffle_value + self.favor_value + self.nAC_value + self.attack_value
        self.value_of_draw_w_Favor = self.expl_kitten_value_f + self.skip_value_f + self.shuffle_value_f + self.favor_value_f + self.nAC_value_f + self.attack_value_f + self.defuse_value
        self.value_of_shuffle_draw = self.value_of_draw
        # later add value of attack, skip.. or maybe just keep values of draw + whatever and add separate function of attacking and so

    # evaluates different cards enemy can draw with favor from deck and me based on probability and card value
    def eval_draw_favor_enemy(self,subject2):

        subject2.expl_kitten_value_f = Exploding_kitten_val * subject2.draw_prob_EK
        subject2.skip_value_f = Sk_val * subject2.draw_prob_skip_w_Favor
        subject2.shuffle_value_f = Shuffle_val * subject2.draw_prob_shuffle_w_Favor
        subject2.favor_value_f = Favor_val * subject2.draw_prob_favor_w_Favor
        subject2.nAC_value_f = nAC_val * subject2.draw_prob_nAC_w_Favor
        subject2.attack_value_f = Att_val * subject2.draw_prob_attack_w_Favor
        subject2.defuse_value = Defuse_val * subject2.draw_prob_defuse

    # values of different actions enemy can take, put into list, final value of his turn is min of said list
    def eval_enemy(self,subject2):

        subject2.eval_draw_favor_enemy(subject2)

        subject2.value_of_draw = self.value_of_draw
        subject2.value_of_draw_w_Favor = subject2.expl_kitten_value_f + subject2.skip_value_f + subject2.shuffle_value_f + subject2.favor_value_f + subject2.nAC_value_f + subject2.attack_value_f + subject2.defuse_value
        subject2.value_of_shuffle_draw = subject2.value_of_draw

        list_enemy_vals = [subject2.value_of_draw, subject2.value_of_draw_w_Favor, subject2.value_of_shuffle_draw]

        self.value_of_enemy = min(list_enemy_vals)

PlayerOne = Actions("PlayerOne",hand_player)
#PlayerOne.reveal_hand()
PlayerTwo = Actions("AI",hand_AI)
#PlayerTwo.reveal_hand()

'''
PlayerOne.draw_probabilities_with_favor(PlayerTwo, whole_deck)
print("Total of chances:",(PlayerOne.draw_prob_defuse + PlayerOne.draw_prob_EK + PlayerOne.draw_prob_attack_w_Favor + PlayerOne.draw_prob_skip_w_Favor + PlayerOne.draw_prob_shuffle_w_Favor + PlayerOne.draw_prob_favor_w_Favor + PlayerOne.draw_prob_nAC_w_Favor))
print("Chances of drawing D, EK, Att, SK, Sh, F, nAC for P1 are\n",(PlayerOne.draw_prob_defuse,PlayerOne.draw_prob_EK,PlayerOne.draw_prob_attack_w_Favor,PlayerOne.draw_prob_skip_w_Favor,PlayerOne.draw_prob_shuffle_w_Favor,PlayerOne.draw_prob_favor_w_Favor, PlayerOne.draw_prob_nAC_w_Favor))
'''

PlayerOne.draw_probabilities(PlayerTwo,whole_deck)
PlayerOne.draw_probabilities_with_favor(PlayerTwo,whole_deck)

PlayerOne.eval_probabilities()
print(PlayerOne.value_of_draw, PlayerOne.value_of_draw_w_Favor, PlayerOne.value_of_shuffle_draw)

PlayerOne.enemy_draw_probabilities_with_favor(PlayerTwo,whole_deck)
# player one calls function which evaluates player two from p1 perspective
PlayerOne.eval_enemy(PlayerTwo)

print("Evaluation of my possibilities:",PlayerOne.value_of_draw, PlayerOne.value_of_draw_w_Favor, PlayerOne.value_of_shuffle_draw,"Enemy move:", PlayerOne.value_of_enemy)
print("Evaluation of enemy possibilities:",PlayerTwo.value_of_draw,PlayerTwo.value_of_draw_w_Favor,PlayerTwo.value_of_shuffle_draw)


'''
i = 0
while len(whole_deck) > 0:
    PlayerOne.draw_card(whole_deck)
    PlayerOne.draw_probabilities(PlayerTwo,whole_deck)
    PlayerOne.reveal_hand()
    PlayerTwo.reveal_hand()
    print("\n",whole_deck)
    print("\n",discard_pile)

    print("Total of chances:",PlayerOne.draw_prob_EK + PlayerOne.draw_prob_attack + PlayerOne.draw_prob_skip + PlayerOne.draw_prob_shuffle + PlayerOne.draw_prob_favor + PlayerOne.draw_prob_nAC)
    print("Chances of drawing EK, Att, SK, Sh, F, nAC for P1 are\n",(PlayerOne.draw_prob_EK,PlayerOne.draw_prob_attack,PlayerOne.draw_prob_skip,PlayerOne.draw_prob_shuffle,PlayerOne.draw_prob_favor, PlayerOne.draw_prob_nAC))
    i += 1
    PlayerTwo.draw_card(whole_deck)
'''
    
# print("Discard pile is {} cards".format(len(discard_pile)))
# print("In the deck is {} remaining cards".format(len(whole_deck)))
