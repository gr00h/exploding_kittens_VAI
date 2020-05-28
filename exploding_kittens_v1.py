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
Defuse_val = 20
nAC_val = 5
Favor_val = 10
Shuffle_val = 5
Att_val = 12
Sk_val = 10


# init discard pile
discard_pile = []

# function, which takes card from deck and gives it to selected player

'''
def draw_card(subject,deck):
    card = deck[0]
    subject.append(card)
    del deck[0]
'''


class Actions:
    '''Possible actions of a subject, according to one's hand'''
    
    # init all states in hand and names of players
    def __init__(self,subject,hand):

        # prepare class of enemy information
        class Enemy_Intel:
            def __init__(self):
                pass      

        self.hand = hand
        self.subject = subject
        self.enemy_intel = Enemy_Intel()
        
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
            
    # function representing playing an ATTACK card on opponent      FUNGUJE
    def card_attack(self,subject2,deck):
        if self.can_attack == True:
            print("You attack!")
            # call draw_card function on opposing player ----- REEEwrtite this to incorporate DEFENSIVE TACTICS
            subject2.draw_card(whole_deck)

            self.must_draw = False
            ####### being_attacked(subject2,deck)

            # find index of played Attack card
            played_card = self.hand.index("Attack")
            # delete said Attack card
            del self.hand[played_card]
            # put said Attack card into discard pile
            discard_pile.append("Attack")
        else:
            print("You cannot attack.")
    
    # function representing playing a SKIP card         FUNGUJE
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

    # check whether I can defend myself
    def can_counter_attack(self):
        self.rewrite_possibilities()
        if self.can_attack == True:
            self.I_can_counter_attack = True
        else:
            self.I_can_counter_attack = False

    # calculate probability of enemy defending himself with countering attack card
    def enemy_can_counter_attack(self,subject2,deck):
        self.draw_probabilities(subject2,deck)
        # chance of enemy having an attack card == possibility of random card being attack * number of cards in his hand
        self.enemy_intel.enemy_has_att_prob = len(subject2.hand) * self.draw_prob_attack
        print(self.enemy_intel.enemy_has_att_prob)


    #enemy_intel.enemy_defuse = 1
    def enemy_defuse_check(self):
        if "Defuse" in discard_pile and "Defuse" in self.hand:
            self.enemy_intel.enemy_defuse = 0
        else:
            self.enemy_intel.enemy_defuse = 1

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

        self.enemy_defuse_check()
        self.deck_EK_check()
        # probability of drawing exploding kitten from deck
        self.draw_prob_EK = self.EK_in_deck/(len(deck))
        print(len(deck))
        # probability of drawing attack from deck
        att_in_hand = self.hand.count("Attack")
        # print("I have {} Attack".format(att_in_hand))

        att_in_disc = discard_pile.count("Attack")
        self.draw_prob_attack =  (5 - att_in_hand - att_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing skip from deck
        skip_in_hand = self.hand.count("Skip")
        # print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        self.draw_prob_skip = (5 - skip_in_hand - skip_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing shuffle from deck
        sh_in_hand = self.hand.count("Shuffle")
        # print("I have {} Shuffle".format(sh_in_hand))

        sh_in_disc = discard_pile.count("Shuffle")
        self.draw_prob_shuffle = (5 - sh_in_hand - sh_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing favor from deck
        f_in_hand = self.hand.count("Favor")
        # print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        self.draw_prob_favor = (5 - f_in_hand - f_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing a non action card from deck
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        # print("I have {} nAC".format(nac_in_hand))

        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        self.draw_prob_nAC = (20 - nac_in_hand - nac_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)
    
    # function calculating probabilities of drawing cards from enemy hand and deck
    def draw_probabilities_with_favor(self,subject2,deck):
        # not sure if this math works tho
        # probability of drawing defuse
        self.enemy_defuse_check()
        self.draw_prob_defuse = self.enemy_intel.enemy_defuse / (len(subject2.hand))

        self.deck_EK_check()
        # probability of drawing exploding kitten from deck
        self.draw_prob_EK = self.EK_in_deck/(len(deck))

        # probability of drawing attack from deck and enemy hand
        att_in_hand = self.hand.count("Attack")
        # print("I have {} Attack".format(att_in_hand))

        att_in_disc = discard_pile.count("Attack")
        self.draw_prob_attack_w_Favor = 2 * (5 - att_in_hand - att_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing skip from deck
        skip_in_hand = self.hand.count("Skip")
        # print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        self.draw_prob_skip_w_Favor = 2 * (5 - skip_in_hand - skip_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing shuffle from deck
        sh_in_hand = self.hand.count("Shuffle")
        # print("I have {} Shuffle".format(sh_in_hand))

        sh_in_disc = discard_pile.count("Shuffle")
        self.draw_prob_shuffle_w_Favor = 2 * (5 - sh_in_hand - sh_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing favor from deck
        f_in_hand = self.hand.count("Favor")
        # print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        self.draw_prob_favor_w_Favor = 2 * (5 - f_in_hand - f_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

        # probability of drawing a non action card from deck
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        # print("I have {} nAC".format(nac_in_hand))

        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        self.draw_prob_nAC_w_Favor = 2 * (20 - nac_in_hand - nac_in_disc) / (len(deck) + len(subject2.hand) - self.enemy_intel.enemy_defuse)

    # this function computes probabilites, with which the opposing player draws cards from deck and my hand
    def enemy_draw_probabilities_with_favor(self,subject2,deck):

        # chance of enemy taking my defuse
        self.my_defuse_check()
        self.enemy_intel.draw_prob_defuse = self.my_defuse / (len(self.hand))

        # no need to check, game would be over
        # subject2.deck_EK_check()
        # probability of drawing exploding kitten from deck
        self.enemy_intel.draw_prob_EK = self.EK_in_deck/(len(deck))

        # probability of drawing attack from deck and my hand
        att_in_hand = self.hand.count("Attack")
        # print("I have {} Attack".format(att_in_hand))
        att_in_disc = discard_pile.count("Attack")
        self.enemy_intel.draw_prob_attack_w_Favor = ((5 - att_in_hand - att_in_disc) / (len(deck) + len(self.hand) - self.enemy_intel.enemy_defuse)) + (att_in_hand / len(self.hand))

        # probability of drawing skip from deck and my hand
        skip_in_hand = self.hand.count("Skip")
        # print("I have {} Skip".format(skip_in_hand))
        skip_in_disc = discard_pile.count("Skip")
        self.enemy_intel.draw_prob_skip_w_Favor = ((5 - skip_in_hand - skip_in_disc) / (len(deck) + len(self.hand) - self.enemy_intel.enemy_defuse)) + (skip_in_hand / len(self.hand))

        # probability of drawing shuffle from deck and my hand
        sh_in_hand = self.hand.count("Shuffle")
        # print("I have {} Shuffle".format(sh_in_hand))
        sh_in_disc = discard_pile.count("Shuffle")
        self.enemy_intel.draw_prob_shuffle_w_Favor = ((5 - sh_in_hand - sh_in_disc) / (len(deck) + len(self.hand) - self.enemy_intel.enemy_defuse)) + (sh_in_hand / len(self.hand))

        # probability of drawing favor from deck and my hand
        f_in_hand = self.hand.count("Favor")
        # print("I have {} Favor".format(f_in_hand))
        f_in_disc = discard_pile.count("Favor")
        self.enemy_intel.draw_prob_favor_w_Favor = ((5 - f_in_hand - f_in_disc) / (len(deck) + len(self.hand) - self.enemy_intel.enemy_defuse)) + (f_in_hand / len(self.hand))

        # probability of drawing a non action card from deck and my hand
        all_nac_in_hand = [s for s in self.hand if "nAC" in s]
        nac_in_hand = len(all_nac_in_hand)
        # print("I have {} nAC".format(nac_in_hand))
        all_nac_in_disc = [s for s in discard_pile if "nAC" in s]
        nac_in_disc = len(all_nac_in_disc)
        self.enemy_intel.draw_prob_nAC_w_Favor = ((20 - nac_in_hand - nac_in_disc) / (len(deck) + len(self.hand) - self.enemy_intel.enemy_defuse)) + (nac_in_hand / len(self.hand))

    # creates variables, which represent subjective value (probability * value) of drawing different cards from deck
    # function called in eval_probabilities
    def eval_draw(self,subject2,deck):
        # call function draw_probabilities to calculate unknowns
        self.draw_probabilities(subject2,deck)

        # creates variables, which represent subjective value (probability * value) of drawing different cards from deck
        self.expl_kitten_value = Exploding_kitten_val * self.draw_prob_EK
        self.skip_value = Sk_val * self.draw_prob_skip
        self.shuffle_value = Shuffle_val * self.draw_prob_shuffle
        self.favor_value = Favor_val * self.draw_prob_favor
        self.nAC_value = nAC_val * self.draw_prob_nAC
        self.attack_value = Att_val * self.draw_prob_attack

        # total value of draw
        self.value_of_draw = self.expl_kitten_value + self.skip_value + self.shuffle_value + self.favor_value + self.nAC_value + self.attack_value


    # creates variables, which represent subjective value (probability * value) of drawing different cards from deck and with favor
    # function called in eval_probabilities
    def eval_draw_favor(self,subject2,deck):
        # calculate unknowns
        self.draw_probabilities_with_favor(subject2,whole_deck)

        self.expl_kitten_value_f = Exploding_kitten_val * self.draw_prob_EK
        self.skip_value_f = Sk_val * self.draw_prob_skip_w_Favor
        self.shuffle_value_f = Shuffle_val * self.draw_prob_shuffle_w_Favor
        self.favor_value_f = Favor_val * self.draw_prob_favor_w_Favor
        self.nAC_value_f = nAC_val * self.draw_prob_nAC_w_Favor
        self.attack_value_f = Att_val * self.draw_prob_attack_w_Favor
        self.defuse_value = Defuse_val * self.draw_prob_defuse

        self.value_of_draw_w_Favor = self.expl_kitten_value_f + self.skip_value_f + self.shuffle_value_f + self.favor_value_f + self.nAC_value_f + self.attack_value_f + self.defuse_value


    # evaluate, whether its good to attack
    def eval_attack(self,subject2,deck):
        self.eval_draw(subject2,whole_deck)
        if self.value_of_draw < 5 and self.can_attack == True:
            self.enemy_can_counter_attack(subject2,deck)
            if self.enemy_intel.enemy_has_att_prob < 0.5:
                self.should_I_attack = True
                # increase the value of attack if oponent is probably defenseless
                self.value_of_attack = self.value_of_draw + 10
            else:
                self.should_I_attack = False
                # decrease if enemy is not defenseless
                self.value_of_attack = self.value_of_draw - 10
        else:
            self.should_I_attack = False
            self.value_of_attack = self.value_of_draw - 10
            
    # evaluate possibilities: draw, draw with favor, play attack, shuffle and draw, skip and enemy options
    def eval_options(self,subject2,deck):
        
        self.eval_draw(subject2,whole_deck)
        self.eval_draw_favor(subject2,whole_deck)
        self.eval_enemy(subject2,whole_deck)
        self.eval_attack(subject2,deck)

        # these values are already calculated in functions called above
        # self.value_of_draw = self.expl_kitten_value + self.skip_value + self.shuffle_value + self.favor_value + self.nAC_value + self.attack_value
        # self.value_of_draw_w_Favor = self.expl_kitten_value_f + self.skip_value_f + self.shuffle_value_f + self.favor_value_f + self.nAC_value_f + self.attack_value_f + self.defuse_value
        self.value_of_shuffle_draw = self.value_of_draw
        
        # skip == enemy can play whatever they want
        self.value_of_skip = self.enemy_intel.value_of_enemy

        # write to console current values of possible actions
        print(self.value_of_draw, self.value_of_draw_w_Favor, self.value_of_shuffle_draw, self.value_of_skip, self.value_of_attack, self.enemy_intel.value_of_enemy)

        # create list of possible actions and their values ----- POSSIBLY ADD MORE ACTIONS (MORE CARDS? MORE MOVES?)
        self.list_options = [self.value_of_draw, self.value_of_draw_w_Favor, self.value_of_shuffle_draw, self.value_of_skip, self.value_of_attack, self.enemy_intel.value_of_enemy]

    # evaluates different cards enemy can draw with favor from deck and me based on probability and card value
    def eval_draw_favor_enemy(self,subject2,deck):
        self.enemy_draw_probabilities_with_favor(subject2,whole_deck)

        self.enemy_intel.expl_kitten_value_f = Exploding_kitten_val * self.enemy_intel.draw_prob_EK
        self.enemy_intel.skip_value_f = Sk_val * self.enemy_intel.draw_prob_skip_w_Favor
        self.enemy_intel.shuffle_value_f = Shuffle_val * self.enemy_intel.draw_prob_shuffle_w_Favor
        self.enemy_intel.favor_value_f = Favor_val * self.enemy_intel.draw_prob_favor_w_Favor
        self.enemy_intel.nAC_value_f = nAC_val * self.enemy_intel.draw_prob_nAC_w_Favor
        self.enemy_intel.attack_value_f = Att_val * self.enemy_intel.draw_prob_attack_w_Favor
        self.enemy_intel.defuse_value = Defuse_val * self.enemy_intel.draw_prob_defuse

    # values of different actions enemy can take, put into list, final value of his turn is min of said list
    def eval_enemy(self,subject2,deck):

        # hodnota draw pro enemy == hodn. draw pro me samotneho; hodnota draw+favor je jina
        self.eval_draw_favor_enemy(subject2,deck)
        self.enemy_intel.value_of_draw = self.value_of_draw
        # kombo DRAW + card
        self.enemy_intel.value_of_draw_w_Favor = self.enemy_intel.expl_kitten_value_f + self.enemy_intel.skip_value_f + self.enemy_intel.shuffle_value_f + self.enemy_intel.favor_value_f + self.enemy_intel.nAC_value_f + self.enemy_intel.attack_value_f + self.enemy_intel.defuse_value
        self.enemy_intel.value_of_shuffle_draw = self.enemy_intel.value_of_draw

        list_enemy_vals = [self.enemy_intel.value_of_draw, self.enemy_intel.value_of_draw_w_Favor, self.enemy_intel.value_of_shuffle_draw]

        self.enemy_intel.value_of_enemy = min(list_enemy_vals)



class GameFlow:

    # init players of game
    def __init__(self):
        self.round = 0

        self.player = Actions("PlayerOne",hand_player)
        self.AI = Actions("AI",hand_AI)

        self.current_player = self.player

    # moznosti hrace
    def player_turn(self):
        self.player.must_draw = True
        # show player his hand to let him choose a card to play
        self.player.reveal_hand()
        self.player.wanna_play = input("\nDo you want to play a card? [y/n]: ")

        if self.player.wanna_play == "y":

            print("\nWhat card do you I want to play? \nNote, that only action cards can currently be played (cards which do NOT start with 'nAC')")
            self.card_was_played = False

            while(self.card_was_played == False):
                self.player.desired_card=input("Write name of card or 'Back', if you changed your mind: ")
                
                # check what was written and possibly execute card
                if self.player.desired_card == "Attack":
                    if self.player.can_attack == True:
                        self.player.card_attack(self.AI,whole_deck)
                        self.card_was_played = True
                    else:
                        self.player.desired_card=input("Please select another card: ")

                elif self.player.desired_card == "Favor":
                    if self.player.can_favor == True:
                        self.player.card_favor(self.AI)
                        self.card_was_played = True
                    else:
                        self.player.desired_card=input("Please select another card: ")

                elif self.player.desired_card == "Shuffle":
                    if self.player.can_shuffle == True:
                        self.player.card_shuffle(whole_deck)
                        self.card_was_played = True
                    else:
                        self.player.desired_card=input("Please select another card: ")

                elif self.player.desired_card == "Skip":
                    if self.player.can_skip == True:
                        self.player.card_skip()
                        self.card_was_played = True
                    else:
                        self.player.desired_card=input("Please select another card: ")

                elif self.player.desired_card == "Back":
                    break

                else:
                    print("Invalid card.")
        
        # konec tahu - tj pokud se nezmeni podminka tak musi tahnout
        if self.player.must_draw == True:
            self.player.draw_card(whole_deck)

    # moznosti / algoritmus AI
    def AI_turn(self):
        self.AI.rewrite_possibilities()
        self.AI.must_draw = True
        # calculate possible moves heren
        self.AI.eval_options(self.player,whole_deck)

        self.AI.did_something = False
        # choose best action
        while self.AI.did_something == False:
            # find best action
            # self.AI.best_action = max(self.AI.list_options)
            # print(self.AI.best_action)
            self.AI.best_action_index = self.AI.list_options.index(max(self.AI.list_options))
            print(self.AI.best_action_index)

            if self.AI.best_action_index == 0:
                self.AI.draw_card(whole_deck)
                self.AI.must_draw = False
                self.AI.did_something = True
            elif self.AI.best_action_index == 1 and self.AI.can_favor == True:
                self.AI.card_favor(self.player)
                self.AI.did_something = True
            elif self.AI.best_action_index == 2 and self.AI.can_shuffle == True:
                self.AI.card_shuffle(whole_deck)
                self.AI.did_something = True
            elif self.AI.best_action_index == 3 and self.AI.can_skip == True:
                self.AI.card_skip()
                self.AI.did_something = True
            elif self.AI.best_action_index == 4 and self.AI.can_attack == True:
                self.AI.card_attack(self.player,whole_deck)
                self.AI.did_something = True
            else: 
                self.AI.list_options[self.AI.best_action_index] = 0
                print("list after delete:",self.AI.list_options)

    def turn(self):
        # subject 1 == player, subject 2 == AI
        self.round = self.round + 1
        print(f"Round: {self.round}")
        print(f"It's {self.current_player.subject}'s turn")

        # tady odpalit funcki hrani hrace anebo AI
        # self.player_turn()
        # self.AI_turn()

        # end turn
        if self.current_player == self.player:
            self.player_turn()
            self.current_player = self.AI
        elif self.current_player == self.AI:
            self.AI_turn()
            self.current_player = self.player
    
    def complete_game(self):
        while "Exploding kitten" in whole_deck:
            self.turn()





PlayerOne = Actions("PlayerOne",hand_player)
#PlayerOne.reveal_hand()
PlayerTwo = Actions("AI",hand_AI)
#PlayerTwo.reveal_hand()


# PlayerOne.enemy_can_counter_attack(PlayerTwo,whole_deck)
'''

# TEST PROBABILITIES

PlayerOne.draw_probabilities_with_favor(PlayerTwo, whole_deck)
print("Total of chances:",(PlayerOne.draw_prob_defuse + PlayerOne.draw_prob_EK + PlayerOne.draw_prob_attack_w_Favor + PlayerOne.draw_prob_skip_w_Favor + PlayerOne.draw_prob_shuffle_w_Favor + PlayerOne.draw_prob_favor_w_Favor + PlayerOne.draw_prob_nAC_w_Favor))
print("Chances of drawing D, EK, Att, SK, Sh, F, nAC for P1 are\n",(PlayerOne.draw_prob_defuse,PlayerOne.draw_prob_EK,PlayerOne.draw_prob_attack_w_Favor,PlayerOne.draw_prob_skip_w_Favor,PlayerOne.draw_prob_shuffle_w_Favor,PlayerOne.draw_prob_favor_w_Favor, PlayerOne.draw_prob_nAC_w_Favor))


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

Gametest = GameFlow()
#Gametest.turn()
Gametest.complete_game()



PlayerOne.reveal_hand()
PlayerTwo.reveal_hand()

'''

# TEST OF DRAWING CARDS

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
