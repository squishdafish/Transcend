import random
import time

players = []
rows = 20
cols = 20
space_size = 25
background_color = 0, 0, 0
running = True
turn = 0
print("--T-R-A-N-C-E-N-D--")
start = input("Press enter to start")
if start == "":
    print("Loading...")

try:
    current_player = turn % int(len(players))
except ZeroDivisionError:
    current_player = 0

player = current_player

running = True


#--- CLASSES ---
class Player:

    def __init__(self, name, character, starting_cards):
        self.name = name  # <--- implemented
        self.character = character  # <--- mostly implemented
        self.space = 0  # <--- WORK ON TONIGHT AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH PANIC
        self.happiness = 0  # <--- should be good
        self.happiness_gained = 0  # <--- should be good
        self.happiness_to_gain_next_turn = 0  # <--- good unless there's a card that gains happiness every next turn
        self.extra_happiness = 0  # <--- SHOULD be good
        self.happy_loss_resist = 0  # <--- OH MY GOD WORK ON THIS TONIGHT AAAAH AAAAH OH NO
        self.happiness_lost = 0  # <--- ^^^^^^^
        self.happiness_to_lose_next_turn = 0
        self.nature_buff = 0  # <--- implemented i hope
        self.number_of_cards = 0  # <---- I dont know what this is
        self.cards_to_play = 2  # <---- not implemented need to do the turn logic
        self.number_of_conform = 0  # <---- AAAAAAAAAAA OH GOD THIS ISNT IMPLEMENTED D: AAAAAAAH
        self.number_of_reliance = 0  # <---- transcendence can also be a tonight thing right?
        self.number_of_nature = 0
        self.conform_threshold = 3  # <---- CONFORMITY CONFORMITY AAAAH CONFORMITY WALDEN AAH
        self.cards_to_draw = 1
        self.double_counter = 0
        self.extra_counter = 0
        self.hand = []
        self.transcended = False
        self.happy_multiplier_turn = False
        self.conformed = False
        self.lost = False
        self.egotistic = False
        self.half_multiplier = False
        self.double_multiplier = False
        self.triple_multiplier = False
        self.conform_immune = False
        self.lost_immune = False
        self.garden_nature = False
        self.garden_reliance = False
        self.nature_played = False
        self.Forest = False
        self.Nature = False
        self.in_conformity = False
        self.nonconformity = False
        self.conformity_effects = []
        self.envied = False
        self.transparent = False
        self.transcend_threshold = 20
        self.location = "Roots"
        self.game_over = False
        self.happiness_loss_resist = 0
        self.mountains = False
        self.marked = False
        self.conform_threshold = 3
        self.conformity_threshold = 5

    def __str__(self):
        return f"""{self.name} ({self.character.name})
        Character Effects: {self.character.effects}
        Starting cards: {self.character.starting_cards}
        Space: {self.space}, 
        Happiness: {self.happiness}, 
        Happiness to Gain Next Turn: {self.happiness_to_gain_next_turn}, 
        Number of Cards: {self.number_of_cards}, 
        Cards to Play: {self.cards_to_play}, 
        Number of Conform: {self.number_of_conform}, 
        Number of Reliance: {self.number_of_reliance}, 
        Conform Threshold: {self.conform_threshold}, 
        Cards to Draw: {self.cards_to_draw},    
        Transcended: {self.transcended}, 
        Conformed: {self.conformed}, 
        Lost: {self.lost}, 
        Egotistic: {self.egotistic}, 
        Half Multiplier: {self.half_multiplier}, 
        Double Multiplier: {self.double_multiplier}, 
        Triple Multiplier: {self.triple_multiplier}, 
        Conform Immune: {self.conform_immune}, 
        Garden (Nature): {self.garden_nature}, 
        Garden (Reliance): {self.garden_reliance},
        Nature Card played: {self.nature_played},
        Forest card effect in play: {self.Forest},
        Nature card effect in play: {self.Nature},
        Nonconformity card effect in play: {self.nonconformity}, 
        Mountains card in play: {self.mountains},
        In conformity: {self.in_conformity},
        Currently envied: {self.envied},
        Nature deck Transparent Eyeball shuffled: {self.transparent},
        Amount of cards played needed to transcend: {self.transcend_threshold},
        Location: {self.location},
        Happiness loss resist: {self.happiness_loss_resist},
        Marked: {self.marked},
        Amount of conform cards needed to gain CONFORMED: {self.conform_threshold},
        Amount of conform cards needed to go to CONFORMITY: {self.conformity_threshold},"""

    #I dont think effects are removed if they aren't timed but that's fine thats not a problem
    def conform_check(self):
        turns_past = 0
        for i in range(len(players)):

            #checks for lingering envy
            for effects in range(len(players[i].conformity_effects)):
                if "Envy" not in players[i].conformity_effects[effects].name:
                    players[i].envied = False
            #Social media (half happiness, 50 - 50 to either half or double happiness gained next turn)
                if "Social Media" in players[i].conformity_effects[
                        effects].name:
                    last_turn = turn
                    old_happiness = self.happiness_gained
                    if old_happiness < self.happiness_gained:
                        coin = random.randint(1, 2)
                        if coin == 1:
                            difference = self.happiness_gained - old_happiness
                            self.happiness_gained += difference
                        elif coin == 2:
                            difference = self.happiness_gained - old_happiness
                            difference /= 2
                            self.happiness_gained -= difference
                            self.happiness_gained
                    if turn > last_turn:
                        self.happiness /= 2
                        turns_past += 1
                    if turns_past == 1:
                        self.conformity_effects.remove("Social Media")
                if "New Wardrobe" in players[i].conformity_effects[
                        effects].name:
                    for card in range(len(self.hand)):
                        discard_decks[f"{players[i].hand[card].type}"].append(
                            card)
                    self.hand = []
                    deck = input(f"{self.name}, choose your first card type.")
                    draw_given(player, deck)

                    deck2 = input(
                        f"{self.name}, choose your second card type.")
                    draw_given(player, deck2)
                #makes player transcended once again, after conformity effect is lost
                if self.marked == True and not "New Wardrobe" or "Plastic Surgery" in players[
                        i].conformity_effects[effects].name:
                    self.transcended = True
                #envy is checked in the effects_check function
                if "Extortion" in players[i].conformity_effects[effects].name:
                    try:
                        card = random.choice(players[i].hand)
                        players[i].hand.remove(card)
                    except:
                        players[i].happiness_lost += 3
                if "Insult" in players[i].conformity_effects[effects].name:
                    old_happiness = players[i].happiness_gained
                    if players[i].happiness_gained > old_happiness:
                        difference = players[i].happiness_gained - old_happiness
                        difference /= 2
                        players[i].happiness_gained -= difference
                if "Lose Self" in players[i].conformity_effects[effects].name:
                    for i in range(len(players)):
                        for effect in self.character.effects:
                            if effect == "CONFORM resist":
                                self.conform_threshold -= 1
                    if players[i].character == "The Fool":
                        self.double_multiplier = False
                    elif players[i].character == "The Egotist":
                        self.egotistic = True
                        self.conform_threshold -= 1
                if "Office Job" in players[i].conformity_effects[effects].name:
                    last_turn = turn
                    if turn > last_turn:
                        players[i].happiness_lost += 3
                if "Plastic Surgery" in players[i].conformity_effects[
                        effects].name:
                    old_happiness = players[i].happiness_gained
                    if players[i].happiness_gained > old_happiness:
                        difference = players[i].happiness_gained - old_happiness
                        difference /= 2
                        players[i].happiness_gained -= difference
                if "Dependency" in players[i].conformity_effects[effects].name:
                    players[i].cards_to_play -= 1
                if "Manipulate" in players[i].conformity_effects[effects].name:
                    if players[i].hand != []:
                        card = random.choice(players[i].hand)
                        players[i].hand.remove(card)
                if "Manipulate Neo" in players[i].conformity_effects[
                        effects].name:
                    if players[i].hand != []:
                        card = random.choice(players[i].hand)
                        players[i].hand.remove(card)
                if "CONFORM" in players[i].conformity_effects[effects].name:
                    last_turn = turn
                    players[i].cards_to_draw -= 1
                    if turn > last_turn:
                        players[i].conformity_effects.remove("CONFORM")

                if len(players[i].conformity_effects
                       ) > players[i].conform_threshold:
                    players[i].conformed = True
                if len(players[i].conformity_effects
                       ) > players[i].conformity_threshold:
                    players[i].in_conformity = True

    def effects_check(self):
        for card in cards_played:
            #double happiness check
            if self.double_multiplier or self.egotistic:
                old_happiness = self.happiness_gained
                if self.happiness_gained > old_happiness:
                    difference = self.happiness_gained - old_happiness

                    if self.character.name == "The Fool":
                        difference *= 2
                        print("You fool, you doubled your happiness gained.")
                    if self.egotistic:
                        difference *= 2
                        print(
                            "Egotistic jerk. You doubled your happiness gained. Bet you feel real smug."
                        )

                    self.happiness_gained += difference
                    print(f"{self.name}'s happiness gained has been doubled.")
                    self.happiness += self.happiness_gained
                    self.happiness_gained = 0

                    if self.character.name == "The Fool" or self.egotistic:
                        return
                    else:
                        self.double_multiplier = False
                        print(
                            f"{self.name}'s double multiplier has been lost.")

            if self.triple_multiplier:
                self.happiness_gained *= 3
                self.happiness += self.happiness_gained
                self.happiness_gained = 0
                self.triple_multiplier = False
                print(
                    f"{self.name}'s happiness gained was tripled. They no longer have a triple multipler."
                )

            if self.extra_happiness > 0:
                old_happiness = self.happiness_gained
                if self.happiness_gained > old_happiness:
                    self.happiness_gained += self.extra_happiness
                    print(
                        f"Effects have caused {self.name} to gain {self.extra_happiness} extra happiness."
                    )

            if self.conform_immune:
                old_effects = self.conformity_effects
                if len(self.conformity_effects) > len(old_effects):
                    self.conformity_effects.remove(self.conformity_effects[-1])
                    print(
                        f"{self.name} avoided a conformity effect. They no longer avoid conformity effects."
                    )

            if self.lost_immune:
                if self.lost:
                    self.lost = False
                    self.lost_immune = False
                    print(
                        f"{self.name} avoided getting lost. They no longer are lost immune."
                    )
            #happiness gained upon start of turn check
            if self.happiness_to_gain_next_turn > 0:
                last_turn = turn
                if turn > last_turn:
                    self.happiness_gained += self.happiness_to_gain_next_turn
                    self.happiness_to_gain_next_turn = 0
                    print(
                        f"{self.happiness_to_gain_next_turn} happiness has been gained due to effects last turn."
                    )
            #nature has increased happiness check
            if self.nature_buff > 0:
                old_happiness = self.happiness_gained
                if card.type == "Nature":
                    self.happiness_gained += self.nature_buff
                    print(
                        f"Amount of happiness gained by nature cards has been increased by {self.nature_buff}"
                    )
                    show_happiness(self)

            #theres a better way to do this for sure, but check for forest effect
            if self.Forest:
                last_turn = turn
                if turn > last_turn:
                    if not self.nature_played:
                        self.happiness_lost -= 3
                        print(
                            f"The forest has taken {self.name}. They lose 3 happiness"
                        )

            #adding back happiness gained at start of turns
            if self.garden_nature:
                if self.happiness_to_gain_next_turn == 0:
                    self.happiness_to_gain_next_turn += 1
                    print(f"{self.name} will gain 1 happiness next turn.")
            if self.Nature:
                if self.happiness_to_gain_next_turn == 0:
                    self.happiness_to_gain_next_turn += 1
                    print(f"{self.name} will gain 1 happiness next turn.")
                    if self.transcended:
                        self.happiness_to_gain_next_turn += 4
                        print(f"{self.name} will gain 4 happiness next turn.")
            #happy multiplier for whole turn
            if self.happy_multiplier_turn:
                last_turn = turn
                if card.name == "Oasis" and last_turn == turn:
                    return
                old_happiness = self.happiness_gained
                if self.happiness_gained > old_happiness:
                    difference = self.happiness_gained - old_happiness
                    self.happiness_gained += difference * 2
                    self.happiness += self.happiness_gained
                    self.happiness_gained = 0
                    old_happiness = 0
                    print("Happiness gained has been doubled.")
                    show_happiness(self)
                if turn > last_turn:
                    if card == "Camp":
                        self.double_counter += 1
                        if self.double_counter == 2:
                            self.double_counter = 0
                            self.happy_multiplier_turn = False
                            print("Camp double multiplier is now lost.")
                    else:
                        self.happy_multipler_turn = False
                        print("Double multiplier has been lost.")
            if self.nonconformity:
                old_effects = self.conformity_effects
                if old_effects != self.conformity_effects:
                    if self.transcended:
                        target = select_target(card)
                        print(
                            f"The conformity effect has been deflected to {target.name}"
                        )
                        target.conformity_effects.append(
                            self.conformity_effects[-1])
                        self.nonconformity = False
                    elif not self.transcended:
                        for i in range(len(players)):
                            checks = 0
                            if any(players[i].number_of_reliance >=
                                   players[checks].number_of_reliance):
                                checks += 1
                                continue
                            else:
                                print(
                                    f"The conformity effect has been deflected to {players[checks].name}"
                                )
                                players[checks].conformity_effects.append(
                                    self.conformity_effects[-1])
                                self.nonconformity = False

            if self.envied:
                old_happiness = self.happiness_gained
                if self.happiness > old_happiness:
                    for player in players:
                        for effect in player.conformity_effects:
                            if effect.name == "Envy" and self.name in effect.name:
                                player.happiness_lost += 2
                                print(f"{player.name} has lost two happiness.")

            if self.happiness_lost > 0:
                happiness_lost = self.happiness_lost - self.happiness_loss_resist
                self.happiness -= happiness_lost
                show_happiness(self)
            if self.mountains:
                answer = input("Would you like to activate mountains? (y/n)")
                if answer == "y":
                    self.happiness_gained += 4
                    coin = random.randint(1, 2)
                    if coin == 1:
                        self.lost = True
                        print(
                            "The mountains led you astray! You are now lost.")
                    else:
                        print(
                            "You found your way through the mountains! (Not lost)"
                        )
                else:
                    continue

    def transcend_check(self):
        if self.number_of_reliance + self.number_of_nature >= self.transcend_threshold:
            self.transcended = True
            print(f"{self.name} is now transcended!")
        else:
            print(
                f"{self.name} is {self.transcend_threshold - (self.number_of_reliance + self.number_of_nature)} away from transcending."
            )

            #ALSO REMEMBER MORE IMPORTANT DO NOT DROP CONFORMITY EFFECSTS THERE IS A DIFFERENT ARRAY FOR THAT MAYBE


class Board:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)]
                     for _ in range(rows)]  # 2D grid
        self.players_positions = {}  # Track players on the board

# def set_space(self, row, col, space_type):
# """Define a type of space on the board."""
#self.grid[row][col] = space_type

    def move_player(self, player_name, roll):
        if player_name not in self.players_positions:
            print(f"Player {player_name} not found on the board.")
            return
        player_name.space += roll  # <--- should work

        #current_position = self.players_positions[player_name]
        #new_position = (current_position[0], (current_position[1] + steps) % self.cols)  # Move horizontally for simplicity
        #self.players_positions[player_name] = new_position

        # Check the type of space landed on
        space_type = roots[
            players[player].space]  #again, need more than just player 1
        print(f"{player_name} landed on a {space_type} space.")
        self.trigger_space(player_name, space_type)

    def add_player(self, player_name, start_position):
        """Add a player to the board."""
        self.players_positions[player_name] = start_position

    def trigger_space(self, space_type,
                      player):  # <--- added "player" SHOULD be fine
        if space_type == "nature":
            i = random.randint(0, len(questions) - 1)
            answer = input(f"Answer this question: {questions[i]}")
            if answer.strip().lower() in answers[i].strip().lower():
                draw_nature(player)
        elif space_type == "conformity":
            i = random.randint(0, len(questions) - 1)
            answer = input(f"Answer this question: {questions[i]}")
            if answer.strip().lower() in answers[i].strip().lower():
                draw_conformity(player)
        elif space_type == "reliance":
            i = random.randint(0, len(questions) - 1)
            answer = input(f"Answer this question: {questions[i]}")
            if answer.strip().lower() in answers[i].strip().lower():
                draw_reliance(player)
        elif space_type == "empty":
            print("You landed on an empty space.")
            return

        # Add other space effects

    def display_board(self):
        for row in self.grid:
            print(" | ".join(space if space else "Empty" for space in row))
        print("\n")


class Space:

    def __init__(self, name, effect):
        self.name = name
        self.type = type
        self.effect = effect


class Card:

    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

    def play(self, player):
        if player.cards_to_play == 0:
            return
        effect = self.effect
        #self.append(cards_played)
        for i in players:
            print(f"{player.name} played {self.name}: {self.effect}")
            player.cards_to_play -= 1
            if self.type == "Self Reliance":
                if self.name == "Greatness":
                    player.double_multiplier = True
                    player.remove_multipler = True
                    draw_any(player)
                    player.number_of_reliance += 1
                elif self.name == "Rest":
                    remove_conformity2(player)
                    player.conformed = False
                    if player.transcended:
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
                elif self.name == "Study":
                    player.nature_buff += 3
                    draw_any(player)
                    if player.transcended:
                        draw_any(player)
                    player.number_of_reliance += 1
                elif self.name == "Intuition":
                    player.lost_immune = True
                    player.extra_happiness += 1
                    #drop the extra happiness next turn somehow <--- not sure if ive done this, check th
                    player.number_of_reliance += 1
                elif self.name == "Nonconformity":
                    effect = random.choice(player.conformity_effects)
                    player.conformity_effects.remove(effect)
                    player.conform_immune = True
                    player.nonconformity = True
                    player.number_of_reliance += 1
                elif self.name == "Sense of self":
                    if player.happiness < 5:
                        player.conform_immune = True
                        player.triple_multipler = True
                        draw_any(player)
                        player.number_of_reliance += 1
                elif self.name == "Therapy":
                    num = random.randint(1, 3)
                    if num == 1:
                        if player.egotistic:
                            player.egotistic = False
                        elif player.conformed:
                            player.conformed = False
                        elif player.lost:
                            player.lost = False
                    elif num == 2:
                        if player.lost:
                            player.lost = False
                        elif player.conformed:
                            player.conformed = False
                        elif player.egotistc:
                            player.conformed = False
                    elif num == 3:
                        if player.conformed:
                            player.conformed = False
                        elif player.egotistic:
                            player.egotistic = False
                        elif player.lost:
                            player.lost = False
                    remove_conformity2(player)
                    player.number_of_reliance += 1
                elif self.name == "Garden":
                    player.garden_reliance = True
                    player.happiness_to_gain_next_turn += 1
                    if player.garden_nature:
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
                elif self.name == "Search for self":
                    player.space = 0
                    draw_reliance(player)
                    draw_reliance(player)
                    player.number_of_reliance += 1
                elif self.name == "Budget":
                    player.happiness_loss_resist += 1
                    if player.transcended:
                        player.happiness_loss_resist += 2
                    player.number_of_reliance += 1
                elif self.name == "Self Reliant":
                    if player.conformity_effedcts != []:
                        effect = random.choice(player.conformity_effects)
                        player.conformity_effects.remove(effect)
                        player.conformed = False
                    player.double_multiplier = True
                    draw_any(player)
                    if player.transcended:
                        player.cards_drawn += 1
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
            if self.type == "Conformity":
                ask_question()
                if True:
                    target = select_target(self)
                    if self.name == "Social Media":
                        target.happiness *= 2
                        target.conformity_effects.append(self)
                    if self.name == "New Wardrobe":
                        for card in target.hand:
                            deck = card.type
                            target.hand.remove(card)
                            discard_decks[deck].append(card)
                        target.hand = []
                        get_characters(target)
                        if player.transcended:
                            target.transcend = False
                        player.marked = True
                        target.conformity_effects.append(self)
                    if self.name == "Envy":
                        player.envied = True
                        self.caster = player.name
                        target.conformity_effects.append(self)
                    if self.name == "Extortion":
                        try:
                            card = random.choice(target.hand)
                            target.hand.remove(card)
                        except:
                            target.happiness_lost += 3
                        target.conformity_effects.append(self)
                    if self.name == "Insult":
                        target.happiness_lost += 3
                        target.conformity_effects.append(self)
                    if self.name == "Lose self":
                        target.lost = True
                        target.cards_to_play -= 1
                        target.conformity_effects.append(self)
                    if self.name == "Office job":
                        target.happiness_to_lose_next_turn += 3
                        target.conformity_effects.append(self)
                    if self.name == "Plastic Surgery":
                        for card in target.hand:
                            deck = card.type
                            target.hand.remove(card)
                            discard_decks[deck].append(card)

                        target.hand = []

                        get_characters(target)

                        if player.transcended:
                            target.transcended = False
                        target.conformity_effects.append(self)
                    if self.name == "Dependency":
                        for card in target.hand:
                            if card.type == "Self Reliance":
                                target.hand.remove(card)
                                discard_reliance.append(card)
                        target.egotistical = False
                        target.conformity_effects.append(self)
                    if self.name == "Mainpulate":
                        if player.transcended:
                            manipulate_neo = Card("Manipulate Neo",
                                                  "Conformity", effect)
                            target.conformity_effects.append(manipulate_neo)
                        else:
                            target.conformity_effects.append(self)
                    if self.name == "Fad Diet":
                        target.space = 0
                        card = random.choice(target.hand)
                        card2 = random.choice(target.hand)
                        target.hand.remove(card)
                        target.hand.remove(card2)
                        deck = card.type
                        deck2 = card.type
                        discard_decks[deck].append(card)
                        discard_decks[deck2].append(card)
                    if self.name == "Peer Pressure":
                        target.happiness_lost += 5
                    if self.name == "CONFORM":
                        target.conformed = True
                        target.in_conformity = True
                        if player.transcended:
                            card = random.choice(target.hand)
                            card2 = random.choice(target.hand)
                            target.hand.remove(card)
                            target.hand.remove(card2)
                            deck = card.type
                            deck2 = card.type
                            discard_decks[deck].append(card)
                            discard_decks[deck2].append(card)
                            target.cards_to_draw -= 1
                            target.conformity_effects.append(self)
            if self.type == "Nature":
                if self.name == "Forest":
                    player.happiness_gained += 5
                    player.nature_played = True
                    player.number_of_nature += 1
                elif self.name == "Night Sky":
                    if player.conformity_effects != []:
                        effect = random.choice(player.conformity_effects)
                        player.conformity_effects.remove(effect)
                    player.happiness_gained += 2
                    player.nature_played = True
                    player.cards_to_play += 1
                    check = random.randint(1, 2)
                    if check == 1:
                        player.lost = True
                    player.number_of_nature += 1
                elif self.name == "Beach":
                    player.conformed = False
                    player.happiness_gained += 2
                    player.nature_played = True
                    player.number_of_nature += 1
                elif self.name == "Flower Field":
                    player.happiness_gained += 3
                    if player.transcended:
                        player.happiness_gained += 1
                    player.nature_played = True
                    player.number_of_nature += 1
                elif self.name == "River":
                    player.happiness_gained += 2
                    player.happiness_to_gain_next_turn += 2
                    player.nature_played = True
                    player.number_of_nature += 1
                elif self.name == "Transparent Eyeball":
                    temp_deck = []
                    player.transparent = True
                    choosing = True
                    for iterations in range(5):
                        card = random.choice(decks["nature"])
                        temp_deck.append(card)
                        y = 10
                    for i in range(len(temp_deck)):
                        while choosing:
                            print(f"Card {i}: {temp_deck[i].name}")
                            answer = input(f"Which card is #{i}")
                            if answer == 1:
                                eye_cards.append(temp_deck[0])
                            elif answer == 2:
                                eye_cards.append(temp_deck[1])
                            elif answer == 3:
                                eye_cards.append(temp_deck[2])
                            elif answer == 4:
                                eye_cards.append(temp_deck[3])
                            elif answer == 5:
                                eye_cards.append(temp_deck[4])
                            if len(eye_cards) == 5:
                                choosing = False
                                for card in range(len(eye_cards)):
                                    print(
                                        f"New next 5 nature cards: {eye_cards[card].name}"
                                    )
                    draw_nature(player)
                    player.lost_immune = True
                    if player.transcended:
                        draw_nature(player)
                    player.nature_played = True
                    player.number_of_nature += 1
                elif self.name == "Mountains":
                    player.mountains = True
                    player.number_of_nature += 1
                elif self.name == "Park":
                    player.happiness_gained += 2
                    if player.conformed:
                        player.happiness_gained += 3
                    player.nature_played = True
                elif self.name == "Garden":
                    player.garden_nature = True
                    player.happiness_to_gain_next_turn += 1
                    if player.garden_reliance:
                        player.cards_to_play += 1
                        player.nature_played = True
                elif self.name == "Camp":
                    player.happy_multiplier_turn = True
                    player.space = 0
                    player.nature_played = True
                elif self.name == "Oasis":
                    player.happiness_gained += 4
                    player.happy_multiplier_turn = True
                    player.happiness_to_gain_next_turn += 4
                    player.nature_played = True
                elif self.name == "Nature":
                    player.happiness_to_gain_next_turn += 1
                    if player.transcended:
                        player.happiness_to_gain_next_turn += 4
                        draw_any(player)
                    player.Nature = True
                    player.nature_played = True
            if self.type == "Chance":
                if self.name == "Take a hike!":
                    coin = random.randint(1, 2)
                    if coin == 1:
                        draw_nature(player)
                        draw_nature(player)
                    else:
                        player.lost = True
                elif self.name == "Trust Yourself":
                    coin = random.randint(1, 2)
                    if coin == 1:
                        draw_reliance(player)
                    else:
                        effect = random.choice(player.conformity_effects)
                        player.conformity_effects.remove(effect)
                elif self.name == "Get Builled":
                    card = draw_conformity(player)
                    card.play(player)
                elif self.name == "Go back to your roots":
                    player.space = 0
                    player.extra_happiness = 0  # <--- SHOULD be good
                    player.happy_loss_resist = 0  # <--- OH MY GOD WORK ON THIS TONIGHT AAAAH AAAAH OH NO
                    player.nature_buff = 0  # <--- implemented i hope
                    player.cards_to_play = 2
                    #player.number_of_conform = 0
                    player.number_of_reliance = 0
                    player.conform_threshold = 3
                    player.cards_drawn = 1
                    player.double_counter = 0
                    player.extra_counter = 0
                    player.hand = []
                    player.transcended = False
                    player.happy_multiplier_turn = False
                    player.conformed = False
                    player.lost = False
                    player.egotistic = False
                    player.half_multiplier = False
                    player.double_multiplier = False
                    player.triple_multiplier = False
                    player.conform_immune = False
                    player.lost_immune = False
                    player.garden_nature = False
                    player.garden_reliance = False
                    player.Forest = False
                    player.Nature = False
                    player.in_conformity = False
                    player.character.draw_starting_cards(player)
                elif self.name == "Meditate":
                    undiscard_all()
                    draw_any(player)
                elif self.name == "Trip":
                    roll = roll_dice()
                    roll *= -1
                    move_player(roll)
                    player.happiness_lost += roll
                elif self.name == "Jump for joy!":
                    roll = roll_dice()
                    move_player(roll)
                    player.happiness_gained += roll
                elif self.name == "Mirror":
                    player.egotistical = True
                elif self.name == "Therapy":
                    #Lose negative effect
                    #lose up to two conformity effects
                    print("MAKE NEGATIVE EFFECTS!!!")
                elif self.name == "Get Lost!":
                    player.lost = True
                elif self.name == "Find a coin":
                    player.happiness_gained += 1
                elif self.name == "CONFORM!":
                    player.in_conformity = True
                    player.conformed = True
                elif self.name == "Go goth":
                    draw_any(player)
                    player.conformed = False
                    player.in_conformity = False
                elif self.name == "Map":
                    player.lost = False
                elif self.name == "Chance":
                    coin = random.randint(1, 2)
                    if coin == 1:
                        draw_chance(player)
                        draw_philosophy(player)
                        draw_nature(player)
                        draw_reliance(player)
                        draw_conformity(player)
                    if coin == 2:
                        nature_removed = 0
                        for card in player.hand:
                            if card.type == "Self Reliance":
                                player.hand.remove(card)
                                discard_reliance.append(card)
                            if card.type == "Nature":
                                if nature_removed != 0:
                                    return
                                else:
                                    player.hand.remove(card)
                                    discard_nature.append(card)
                                    nature_removed += 1
            if self.type == "Philosophy":
                if self.name == "Communism":
                    for i in range(len(players)):
                        players[i].happiness = 5
                        while players[i].hand < 3:
                            card = random.choice(players[i].hand)
                            players[i].hand.remove(card)
                        while players[i].hand > 3:
                            draw_any(players[i])
                        print(
                            "All players now have the same amount of cards. 3."
                        )
                if self.name == "Captialism":
                    for i in range(len(players)):
                        checks = 0
                        if any(players[i].happiness >=
                               players[checks].happiness):
                            checks += 1
                            continue
                        else:
                            player.happiness *= 2
                            player.happiness_gained += players[i].happiness // 2
                            players[i].happiness /= 2
                            show_happiness(players[i])
                if self.name == "Transcendentalism":
                    player.transcend_threshold += 1
                    player.transcend_check()
                    player.transcend_threshold -= 1
                    if player.transcended:
                        draw_any(player)
                if self.name == "Absurdism":
                    number = roll_dice()
                    for i in range(len(players)):
                        while players[i].hand > number:
                            card = random.choice(player.hand)
                            players[i].hand.remove(card)
                        while players[i].hand < number:
                            draw_any(players[i])
                if self.name == "Nihilism":
                    player.lost = True
                    player.space = 0
                if self.name == "Creationism":
                    undiscard_all()
                    draw_any(player)
                if self.name == "Realism":
                    question = random.randint(1, 20)
                    answer = input(questions[question])
                    if answer in answers[question]:
                        player.happiness_gained += 5
                    else:
                        player.happiness_lost += 5
                if self.name == "Optimism":
                    player.happiness_gained += 4
                if self.name == "Pessimism":
                    player.happiness_lost += 4
                if self.name == "Confucianism":
                    player.conformed = True
                    player.in_conformity = True
                if self.name == "Chance, Philosophy of":
                    draw_chance(player)
                if self.name == "Spiritualism":
                    roll = roll_dice()
                    if roll in (2, 4, 6):
                        draw_nature(player)
                if self.name == "Atheism":
                    roll = roll_dice()
                    if roll in (1, 3, 5):
                        draw_reliance(player)
                if self.name == "Existentialism":
                    draw_any(player)
                    player.conformed = False
                    player.in_conformity = False
                    draw_reliance(player)
                    draw_reliance(player)


class Character:

    def __init__(self, name, effects, starting_cards):
        self.name = name
        self.effects = effects
        self.starting_cards = starting_cards

    def apply_special_effects(self, player):
        for i in range(len(players)):
            for effect in self.effects:
                if effect == "CONFORM resist":
                    player.conform_threshold += 1
                elif effect == "COFNORM weakness":
                    player.conform_threshold -= 1
                elif effect == "Starts lost":
                    player.lost = True
            if players[
                    i].character == "The Fool":  #make it cycle through checking each player - consider using player_name, that's what board uses
                #figure out how to give effect of 2 conformity cards
                player.lost = True
                player.egotistic = True
            elif players[i].character == "The Egotist":
                player.egotistic = True
                player.conform_threshold += 1

    def draw_starting_cards(self, player):
        if isinstance(player, int):
            player = players[player]
        if player.hand == []:
            if self.name == "The Influencer":
                draw_conformity(player)
                draw_conformity(player)
                draw_conformity(player)
            elif self.name == "The Philosopher":
                draw_philosophy(player)
                draw_reliance(player)
                draw_reliance(player)
            elif self.name == "The Hippie":
                draw_nature(player)
                draw_nature(player)
                draw_nature(player)
                draw_nature(player)
            elif self.name == "The Egotist":
                draw_reliance(player)
                draw_reliance(player)
                draw_reliance(player)
            elif self.name == "The Prisoner":
                print(f"{player.name} drew nothing.")
            elif self.name == "The Wild Card":
                draw_any(player)
                draw_any(player)
                draw_chance(player)
            elif self.name == "The Fool":
                draw_reliance(player)
                draw_reliance(player)
                draw_conformity(player)
            elif self.name == "The Activist":
                draw_nature(player)
                draw_nature(player)
                draw_philosophy(player)


#CARDS AND DECKS AND STUFF AAAAAAAAAAAAAAAAAAAAAAAH
nature_cards = [
    Card(
        "Forest", "Nature",
        "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."
    ),
    Card(
        "Forest", "Nature",
        "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."
    ),
    Card(
        "Forest", "Nature",
        "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."
    ),
    Card(
        "Forest", "Nature",
        "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."
    ),
    Card(
        "Night Sky", "Nature",
        "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"
    ),
    Card(
        "Night Sky", "Nature",
        "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"
    ),
    Card(
        "Night Sky", "Nature",
        "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"
    ),
    Card(
        "Night Sky", "Nature",
        "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"
    ),
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"),
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"),
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature",
         "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("River", "Nature",
         "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature",
         "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature",
         "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature",
         "Gain 2 happiness now, and 2 happiness next turn."),
    Card(
        "Transparent Eyeball", "Nature",
        "Look at the top 5 cards of the nature deck, arrange them in any way, and draw a nature card. Can't get lost this turn. If transcended, draw 2 instead,"
    ),
    Card(
        "Transparent Eyeball", "Nature",
        "Look at the top 5 cards of the nature deck, arrange them in any way, and draw a nature card. Can't get lost this turn. If transcended, draw 2 instead,"
    ),
    Card(
        "Mountains", "Nature",
        "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."
    ),
    Card(
        "Mountains", "Nature",
        "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."
    ),
    Card(
        "Mountains", "Nature",
        "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."
    ),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card(
        "Garden)", "Nature",
        "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."
    ),
    Card(
        "Garden", "Nature",
        "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."
    ),
    Card(
        "Garden", "Nature",
        "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."
    ),
    Card(
        "Camp", "Nature",
        "Gain 2x happiness for the next 2 turns times gained, and go back to roots."
    ),
    Card(
        "Camp", "Nature",
        "Gain 2x happiness for the next 2 turns times gained, and go back to roots."
    ),
    Card(
        "Oasis", "Nature",
        "Gain 4 happiness, next turn can gain 4 again and double happiness gained that turn, but become lost."
    ),
    Card(
        "Oasis", "Nature",
        "Gain 4 happiness, next turn can gain 4 again and double happiness gained that turn, but become lost."
    ),
    Card(
        "Nature", "Nature",
        "Gain one happiness each turn. If transcended, gain 5 happiness and draw one each turn. "
    )
]

reliance_cards = [
    Card("Greatness", "Self Reliance",
         "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance",
         "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance",
         "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance",
         "Gain 2x happiness from next source. Draw one."),
    Card(
        "Rest", "Self Reliance",
        "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."
    ),
    Card(
        "Rest", "Self Reliance",
        "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."
    ),
    Card(
        "Rest", "Self Reliance",
        "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."
    ),
    Card(
        "Study", "Self Reliance",
        "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."
    ),
    Card(
        "Study", "Self Reliance",
        "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."
    ),
    Card(
        "Study", "Self Reliance",
        "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."
    ),
    Card(
        "Study", "Self Reliance",
        "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."
    ),
    Card(
        "Intuition", "Self Reliance",
        "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."
    ),
    Card(
        "Intuition", "Self Reliance",
        "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."
    ),
    Card(
        "Intuition", "Self Reliance",
        "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."
    ),
    Card(
        "Intuition", "Self Reliance",
        "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."
    ),
    Card(
        "Intuition", "Self Reliance",
        "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."
    ),
    Card(
        "Nonconformity", "Self Reliance",
        "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."
    ),
    Card(
        "Nonconformity", "Self Reliance",
        "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."
    ),
    Card(
        "Nonconformity", "Self Reliance",
        "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."
    ),
    Card(
        "Sense of self", "Self Reliance",
        "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."
    ),
    Card(
        "Sense of self", "Self Reliance",
        "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."
    ),
    Card(
        "Sense of self", "Self Reliance",
        "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."
    ),
    Card(
        "Therapy", "Self Reliance",
        "Lose one neegative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Self Reliance",
        "Lose one neegative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Self Reliance",
        "Lose one neegative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Self Reliance",
        "Lose one neegative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Self Reliance",
        "Lose one neegative status on player and up to two conformity effects."
    ),
    Card(
        "Garden", "Self Reliance",
        "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."
    ),
    Card(
        "Garden", "Self Reliance",
        "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."
    ),
    Card(
        "Garden", "Self Reliance",
        "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."
    ),
    Card("Search for self", "Self Reliance",
         "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance",
         "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance",
         "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance",
         "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance",
         "Send back to roots, draw 2 self reliance cards."),
    Card(
        "Budget", "Self Reliance",
        "When you lose happiness, you lose 1 less. If transcended, lose 3 less."
    ),
    Card(
        "Budget", "Self Reliance",
        "When you lose happiness, you lose 1 less. If transcended, lose 3 less."
    ),
    Card(
        "Budget", "Self Reliance",
        "When you lose happiness, you lose 1 less. If transcended, lose 3 less."
    ),
    Card(
        "Budget", "Self Reliance",
        "When you lose happiness, you lose 1 less. If transcended, lose 3 less."
    ),
    Card(
        "Self Reliant", "Self Reliance",
        "Lose one conformity effect, lose CONFORMED, gain 2x happiness next turn, and draw a card. If transcended, draw one at start of turn, and you can play an extra card."
    )
]

conformity_cards = [
    Card(
        "Social Media", "Conformity",
        "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."
    ),
    Card(
        "Social Media", "Conformity",
        "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."
    ),
    Card(
        "Social Media", "Conformity",
        "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."
    ),
    Card(
        "Social Media", "Conformity",
        "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."
    ),
    Card(
        "New Wardrobe", "Conformity",
        "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."
    ),
    Card(
        "New Wardrobe", "Conformity",
        "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."
    ),
    Card(
        "New Wardrobe", "Conformity",
        "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."
    ),
    Card("Envy", "Conformity",
         "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity",
         "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity",
         "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity",
         "Player loses 2 happiness each time the user gains happiness."),
    Card(
        "Extortion", "Conformity",
        "Each turn the target discards a card, if no cards then lose 3 happiness."
    ),
    Card(
        "Extortion", "Conformity",
        "Each turn the target discards a card, if no cards then lose 3 happiness."
    ),
    Card(
        "Extortion", "Conformity",
        "Each turn the target discards a card, if no cards then lose 3 happiness."
    ),
    Card(
        "Insult", "Conformity",
        "Target a player; they lose 3 happiness. When they gain happiness, it's halved."
    ),
    Card(
        "Insult", "Conformity",
        "Target a player; they lose 3 happiness. When they gain happiness, it's halved."
    ),
    Card(
        "Insult", "Conformity",
        "Target a player; they lose 3 happiness. When they gain happiness, it's halved."
    ),
    Card(
        "Insult", "Conformity",
        "Target a player; they lose 3 happiness. When they gain happiness, it's halved."
    ),
    Card("Lose self", "Conformity",
         "Target gets lost this turn and has no positive character effects."),
    Card("Lose self", "Conformity",
         "Target gets lost this turn and has no positive character effects."),
    Card("Lose self", "Conformity",
         "Target gets lost this turn and has no positive character effects."),
    Card("Office job", "Conformity",
         "Target loses 3 happiness at start of turns."),
    Card("Office job", "Conformity",
         "Target loses 3 happiness at start of turns."),
    Card(
        "Plastic Surgery", "Conformity",
        "Change character, lose hand, half happiness gained while in effect. If transcended, untranscend target."
    ),
    Card(
        "Plastic Surgery", "Conformity",
        "Change character, lose hand, half happiness gained while in effect. If transcended, untranscend target."
    ),
    Card(
        "Dependency", "Conformity",
        "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."
    ),
    Card(
        "Dependency", "Conformity",
        "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."
    ),
    Card(
        "Dependency", "Conformity",
        "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."
    ),
    Card(
        "Dependency", "Conformity",
        "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."
    ),
    Card(
        "Manipulate", "Conformity",
        "Lose a card at start of turns, user chooses which type. If transcended, lose two."
    ),
    Card(
        "Manipulate", "Conformity",
        "Lose a card at start of turns, user chooses which type. If transcended, lose two."
    ),
    Card(
        "Manipulate", "Conformity",
        "Lose a card at start of turns, user chooses which type. If transcended, lose two."
    ),
    Card("Fad Diet", "Conformity", "Lose 2 cards and go back to roots."),
    Card("Fad Diet", "Conformity", "Lose 2 cards and go back to roots."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card(
        "CONFORM", "Conformity",
        "CONFORM player, send player to CONFORMITY, if transcended they lose two cards, and next turn they draw one less."
    )
]

chance_cards = [
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance",
         "50-50 chance to either draw 2 nature cards or get lost."),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card(
        "Trust Yourself", "Chance",
        "50-50 change to either draw a self reliance card or lose a conformity effect."
    ),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card(
        "Go back to your roots", "Chance",
        "Go back to bottom of the tree, with everything but happiness, character, and hand reset."
    ),
    Card(
        "Go back to your roots", "Chance",
        "Go back to bottom of the tree, with everything but happiness, character, and hand reset."
    ),
    Card(
        "Go back to your roots", "Chance",
        "Go back to bottom of the tree, with everything but happiness, character, and hand reset."
    ),
    Card(
        "Go back to your roots", "Chance",
        "Go back to bottom of the tree, with everything but happiness, character, and hand reset."
    ),
    Card(
        "Go back to your roots", "Chance",
        "Go back to bottom of the tree, with everything but happiness, character, and hand reset."
    ),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance",
         "Put discard piles back into their decks, draw one."),
    Card("Trip", "Chance",
         "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Trip", "Chance",
         "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Trip", "Chance",
         "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Jump for joy!", "Chance",
         "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Jump for joy!", "Chance",
         "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Jump for joy!", "Chance",
         "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card(
        "Therapy", "Chance",
        "Loses one negative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Chance",
        "Loses one negative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Chance",
        "Loses one negative status on player and up to two conformity effects."
    ),
    Card(
        "Therapy", "Chance",
        "Loses one negative status on player and up to two conformity effects."
    ),
    Card("Get Lost!", "Chance", "Get lost"),
    Card("Get Lost!", "Chance", "Get lost"),
    Card("Get Lost!", "Chance", "Get lost"),
    Card("Get Lost!", "Chance", "Get lost"),
    Card("Find a coin", "Chance", "Gain 1 happiness"),
    Card("Find a coin", "Chance", "Gain 1 happiness"),
    Card("Find a coin", "Chance", "Gain 1 happiness"),
    Card("Find a coin", "Chance", "Gain 1 happiness"),
    Card("Find a coin", "Chance", "Gain 1 happiness"),
    Card("CONFORM!", "Chance", "CONFORM GO TO CONFORMITY"),
    Card("CONFORM!", "Chance", "CONFORM GO TO CONFORMITY"),
    Card("Go goth", "Chance", "Gain card. Lose CONFORM and leave CONFORMITY."),
    Card("Go goth", "Chance", "Gain card. Lose CONFORM and leave CONFORMITY."),
    Card("Go goth", "Chance", "Gain card. Lose CONFORM and leave CONFORMITY."),
    Card("Go goth", "Chance", "Gain card. Lose CONFORM and leave CONFORMITY."),
    Card(
        "Map", "Chance",
        "Keep this card in your hand. You may play this at any time to un-get lost"
    ),
    Card(
        "Map", "Chance",
        "Keep this card in your hand. You may play this at any time to un-get lost"
    ),
    Card(
        "Map", "Chance",
        "Keep this card in your hand. You may play this at any time to un-get lost"
    ),
    Card(
        "Map", "Chance",
        "Keep this card in your hand. You may play this at any time to un-get lost"
    ),
    Card(
        "Map", "Chance",
        "Keep this card in your hand. You may play this at any time to un-get lost"
    ),
    Card(
        "Chance", "Chance",
        "50-50 to draw one of each card, or discard all self reliance and one nature."
    )
]

philosophy_cards = [
    Card(
        "Communism", "Philosophy",
        "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."
    ),
    Card(
        "Communism", "Philosophy",
        "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."
    ),
    Card(
        "Communism", "Philosophy",
        "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."
    ),
    Card(
        "Capitalism", "Philosophy",
        "When you draw this, if you have the most happiness, then take half of every other players' happiness."
    ),
    Card(
        "Capitalism", "Philosophy",
        "When you draw this, if you have the most happiness, then take half of every other players' happiness."
    ),
    Card(
        "Transcendentalism", "Philosophy",
        "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"
    ),
    Card(
        "Transcendentalism", "Philosophy",
        "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"
    ),
    Card(
        "Transcendentalism", "Philosophy",
        "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"
    ),
    Card(
        "Absurdism", "Philosophy",
        "Roll die. Draw/discard until the number of cards in hand matches that number."
    ),
    Card(
        "Absurdism", "Philosophy",
        "Roll die. Draw/discard until the number of cards in hand matches that number."
    ),
    Card(
        "Absurdism", "Philosophy",
        "Roll die. Draw/discard until the number of cards in hand matches that number."
    ),
    Card(
        "Absurdism", "Philosophy",
        "Roll die. Draw/discard until the number of cards in hand matches that number."
    ),
    Card(
        "Absurdism", "Philosophy",
        "Roll die. Draw/discard until the number of cards in hand matches that number."
    ),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy",
         "Put discard piles back into their decks, draw one"),
    Card(
        "Realism", "Philosophy",
        "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."
    ),
    Card(
        "Realism", "Philosophy",
        "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."
    ),
    Card(
        "Realism", "Philosophy",
        "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."
    ),
    Card(
        "Realism", "Philosophy",
        "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."
    ),
    Card(
        "Realism", "Philosophy",
        "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."
    ),
    Card("Optimism", "Philosophy", "Gain 4 happiness"),
    Card("Optimism", "Philosophy", "Gain 4 happiness"),
    Card("Optimism", "Philosophy", "Gain 4 happiness"),
    Card("Optimism", "Philosophy", "Gain 4 happiness"),
    Card("Optimism", "Philosophy", "Gain 4 happiness"),
    Card("Pessimism", "Philosophy", "Lose 4 happiness"),
    Card("Pessimism", "Philosophy", "Lose 4 happiness"),
    Card("Pessimism", "Philosophy", "Lose 4 happiness"),
    Card("Pessimism", "Philosophy", "Lose 4 happiness"),
    Card("Pessimism", "Philosophy", "Lose 4 happiness"),
    Card("Confucianism", "Philosophy", "CONFORM GO TO CONFORMITY"),
    Card("Confucianism", "Philosophy", "CONFORM GO TO CONFORMITY"),
    Card("Confucianism", "Philosophy", "CONFORM GO TO CONFORMITY"),
    Card("Chance, Philosopy of", "Philosophy", "Draw a chance card."),
    Card("Chance, Philosopy of", "Philosophy", "Draw a chance card."),
    Card("Chance, Philosopy of", "Philosophy", "Draw a chance card."),
    Card("Chance, Philosopy of", "Philosophy", "Draw a chance card."),
    Card("Chance, Philosopy of", "Philosophy", "Draw a chance card."),
    Card("Spiritualism", "Philosophy", "Roll. If even, draw nature."),
    Card("Spiritualism", "Philosophy", "Roll. If even, draw nature."),
    Card("Spiritualism", "Philosophy", "Roll. If even, draw nature."),
    Card("Spiritualism", "Philosophy", "Roll. If even, draw nature."),
    Card("Spiritualism", "Philosophy", "Roll. If even, draw nature."),
    Card("Atheism", "Philosophy", "Roll. If odd, draw self reliance."),
    Card("Atheism", "Philosophy", "Roll. If odd, draw self reliance."),
    Card("Atheism", "Philosophy", "Roll. If odd, draw self reliance."),
    Card("Atheism", "Philosophy", "Roll. If odd, draw self reliance."),
    Card("Atheism", "Philosophy", "Roll. If odd, draw self reliance."),
    Card("Existentialism", "Philosophy",
         "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy",
         "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy",
         "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy",
         "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards.")
]

cards_played = []

eye_cards = []

characters = [
    Character("The Influencer", "CONFORM weakness", "3 conformity cards"),
    Character("The Philosopher", "CONFORM resist",
              "1 philosophy card, 2 self reliance cards"),
    Character("The Hippie", "Starts lost", "4 nature cards"),
    Character("The Egotist", "Is egotistic, CONFORM resist",
              "3 self reliance cards"),
    Character("The Prisoner", "Starts lost", "No cards"),
    Character("The Wild Card", "CONFORM resist",
              "2 random cards, 1 chance card,"),
    Character(
        "The Fool",
        "Takes effect of 2 conformity cards, starts lost, is egotistic, gains double happiness",
        "2 self reliance, 1 conformity card"),
    Character("The Activist", "Nothing womp womp",
              "2 nature cards, 1 philosophy card")
]

decks = {
    "nature": nature_cards,
    "reliance": reliance_cards,
    "conformity": conformity_cards,
    "chance": chance_cards,
    "philosophy": philosophy_cards,
    "eye": eye_cards
}

alt_decks = [nature_cards, reliance_cards, conformity_cards]

discard_nature = []

discard_reliance = []

discard_conformity = []

discard_philosophy = []

discard_chance = []

discard_decks = {
    "Chance": discard_chance,
    "Nature": discard_nature,
    "Self Reliance": discard_reliance,
    "Conformity": discard_conformity,
    "Philosophy": discard_philosophy
}

#SPACE TYPES
space_types = [
    Space("nature", "Trigger a question, draw a nature card"),
    Space("reliance", "Trigger a question, draw a reliance card"),
    Space("conformity", "Trigger a question, draw a conformity card"),
    Space("chance", "Trigger a chance event"),
    Space("philosophy", "Trigger a philosophy event")
]

first_10_questions = []

questions = [
    "What do transcendentalists believe an appreciation of nature achieves?",
    "Everything is connected. Humans on some deep instinctual level, adore nature.",
    "What event does Emerson claim would make people see what he does in the stars?",
    "Why do transcendentalists love nature so much?",
    "What is the connection between humans and nature, according to transcendentalists?"
    'In "Self-Reliance", Emerson lists many things that can make someone great. Name one of them.',
    'Why does Emerson think it so important to become self reliant?',
    'A certain unnamed transcendentalist went to Walden Pond for 2 years. Why did he do this?',
    "According to Emerson's ideas around conformity, if you have an opinion that goes against the mainstream, what should you do, regardless of the result."
    "Why do transcendentalists value nonconformity so much?"
    "Government bad. Why? (according to transcendentalism)",
    "Do transcendentalists agree with capitalism?",
    "How did transcendentalists feel about religious institutions?",
    "What is particularly notable about transcendentalism as it relates to American culture?",
    "When was transcendentalism going on?",
    "Name one, non Ralph Waldo Emerson, important transcendentalist.",
    "Which transcendentalist is well known for staying at Walden Pond for 2 years?",
    "What does the Transcendence in transcendentalism even mean?",
    'How would one go about "transcending"?',
    'What does the "transparent eyeball" that Emerson metaphorically became mean?',
]

answers = [
    "It helps you become happier and more strongly connected to the divine",
    "Everything is connected. Humans on some deep instinctual level, adore nature.",
    "Them only appearing once per thousand years.",
    "Nature is deeply connected to the divine. We like the divine.",
    "All humans are deeply connected to nature, because both have whatever divine entity within us.",
    "Trusting themselves, being true to their beliefs, not conforming, individualism",
    "It allowed peoples to access their inner truth and creativity, not hindered by conformity.",
    'He wanted to experiment on himself. He wrote that he, "wished to live deliberately". His goal was to determine the necessities of life.',
    "Profess it! Shout it out loud for all to hear!",
    'Mostly due to another thing they highly value, individualism. Also, it allows them to live an authentic life, which is what transcendentalism is all about.',
    'It is inherently not individualistic.',
    "No. Obviously not. It doesn't preserve nature, and they like nature. They also did not like institutions, which is what capitalism creates. And capitalism isn't incredibly individualistic either.",
    "Not great towards them. Bad. They want people to conform to one ideology, and disallow individualism far more than transcendentalists would like.",
    "It was the first wholly unique American intellectual movement.",
    "19th century. 1820s-1830s",
    "Just google the person they named. There's way too many. Henry David Thoreau, Margaret Fuller.",
    "Henry David Thoreau",
    "Transcendence is essentially what its says. Transcending. Going above the human plane of existence to reach an above.",
    "Nature. Nature is connected to the divine, and to us, so connecting to it helps further those ties to the divine.",
    "Viewing everything exactly as is. No filter.",
]

#BOARD
roots = [
    "birth", "empty", "empty", "nature", "reliance", "empty", "philosophy",
    "empty", "nature", "empty", "chance", "empty", "philosophy", "empty",
    "reliance", "empty", "nature", "empty", "conformity", "conformity",
    "chance", "reliance", "chance", "reliance", "empty", "conformity",
    "nature", "empty", "philosophy", "reliance"
]

nature_branch = [
    "nature", "empty", "nature", "chance", "nature", "empty", "nature",
    "philosophy", "nature", "reliance", "nature", "empty", "nature", "nature",
    "transcendence"
]

reliance_branch = [
    "reliance", "empty", "reliance", "chance", "reliance", "empty", "reliance",
    "philosophy", "reliance", "reliance", "reliance", "empty", "reliance",
    "reliance", "transcendence"
]

conformity_branch = [
    "conformity", "conformity", "conformity", "conformity", "conformity",
    "chance", "conformity", "empty", "empty", "philsophy", "conformity",
    "empty", "conformity", "conformity", "empty"
]
#empty spaces should = 30% the total spaces, philosophy being like 10%, chance being 10%, nature, reliance, and conformity being the other 50% (20, 20, and 10)

#make sure to check youre happy with the amount of conformance and nature and whatnot
branches = {
    "Nature": nature_branch,
    "Reliance": reliance_branch,
    "Conformity": conformity_branch
}


#BASIC FUNCTIONS RAAAAAAAAAAAH
def show_happiness(player):
    print(f"{player.name}'s happiness: {player.happiness}")


def select_target(card):
    num = 0
    for i in range(len(players)):
        num += 1
        print(players[i].name, num)
    target = int(input("Who would you like to target? (Enter a number)")) - 1
    target = players[target]
    print(f"{target.name} was targeted by {card.effect}")
    return target


def coin_flip():
    coin = random.randint(1, 2)
    return coin


def roll_dice():
    global roll
    roll = random.randint(1, 6)

    print(f"It's a {roll}")
    time.sleep(.5)
    return roll


def move_player(roll):
    board = Board(10, 20)
    if not players[current_player].in_conformity:
        players[current_player].space += int(roll)
        print(f"{players[current_player].name} moved {roll} spaces.")
        if players[current_player].space > 45:
            players[current_player].space = 45
        if players[current_player].space == 45:
            players[current_player].transcend_check()
            players[current_player].space = 0

    if players[current_player].in_conformity:
        print("Sorry, you're in conformity.")

    #makes sure those in roots are in roots
    if players[current_player].space <= 30:
        players[current_player].location = "Roots"

    #change location to a branch
    if players[current_player].space == 30:
        answer = input("Which branch would you like to go to? (1, 2, or 3)")
        if answer == 1:
            players[current_player].location = "Nature"
        elif answer == 2:
            players[current_player].location = "Reliance"
        elif answer == 3:
            players[current_player].location = "Conformity"
    #move player, grab space type
    try:
        if players[current_player].location == "Roots":
            space = players[current_player].space - 1
            space_type = roots[space]
        elif players[current_player].location != "Roots":
            space = players[current_player].space - 31
            space_type = branches[players[current_player].location[space]]

    #if player passed space 30, puts them in their branch
    except:
        if players[current_player].space > 30 and players[current_player].location == "Roots":
            answer = input("Which branch would you like to go to? (1, 2, or 3)?")
            if answer == 1:
                players[current_player].location = "Nature"
            elif answer == 2:
                players[current_player].location = "Reliance"
            elif answer == 3:
                players[current_player].location = "Conformity"
            space = players[current_player].space - 31
            space_type = branches[players[current_player].location[space]]

    board.trigger_space(space_type, player)


def draw_given(player, deck):
    if isinstance(player, int):
        player = players[player]
    if deck == []:
        undiscard(decks[f"{deck}"])
    drawn_card = random.choice(decks[f"{deck}"])

    decks[f"{deck}"].remove(drawn_card)
    player.hand.append(drawn_card)
    #show_hand(player)


def draw_any(player):
    if isinstance(player, int):
        player = players[player]
    deck = alt_decks[random.randint(0, 2)]
    if deck == []:
        undiscard(deck)
    drawn_card = random.choice(deck)

    deck.remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)
    #show_hand(player)


def draw_nature(player):
    if isinstance(player, int):
        player = players[player]
    # Clear the draw area
    deck = "nature"
    for i in range(len(players)):
        if players[i].transparent and decks["eye"] != []:
            deck = "eye"
    if decks[deck] == []:
        undiscard(deck)

    drawn_card = random.choice(decks[deck])

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)
    #show_hand(player)


def draw_reliance(player):
    if isinstance(player, int):
        player = players[player]
    deck = "reliance"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)


    #show_hand(player)
def draw_conformity(player):
    if isinstance(player, int):
        player = players[player]
    deck = "conformity"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)


    #show_hand(player)
def draw_chance(player):
    if isinstance(player, int):
        player = players[player]
    deck = "chance"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)


    #show_hand(player)
def draw_philosophy(player):
    if isinstance(player, int):
        player = players[player]
    deck = "philosophy"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(.5)
    #show_hand(player)


def shuffle_all():
    random.shuffle(decks["nature"])
    random.shuffle(decks["conformity"])
    random.shuffle(decks["chance"])
    random.shuffle(decks["reliance"])
    random.shuffle(decks["philosophy"])


def shuffle_nature():
    random.shuffle(decks["nature"])


def shuffle_reliance():
    random.shuffle(decks["nature"])


def shuffle_conformity():
    random.shuffle(decks["conformity"])


def shuffle_philosophy():
    random.shuffle(decks["philosophy"])


def shuffle_chance():
    random.shuffle(decks["chance"])


def undiscard_all():
    nature = random.shuffle(discard_decks["nature"])
    reliance = random.shuffle(discard_decks["reliance"])
    conformity = random.shuffle(discard_decks["conformity"])
    philosophy = random.shuffle(discard_decks["philosophy"])
    chance = random.shuffle(discard_decks["chance"])
    decks["nature"].append(nature)
    decks["reliance"].append(reliance)
    decks["conformity"].append(conformity)
    decks["philosophy"].append(philosophy)
    decks["chance"].append(chance)


def undiscard(deck):
    shuffled = random.shuffle(discard_decks[deck])
    decks[deck].append(shuffled)


def end_turn():
    global turn
    turn += 1
    for i in range(len(players)):
        players[i].happiness += players[i].happiness_gained
        players[i].happiness += players[i].happiness_lost
        if players[i].extra_happiness > 0:
            players[i].extra_counter += 1
            if players[i].extra_counter == 2:
                players[i].extra_counter -= 1
        players[current_player].effects_check()  #this will almost certainly cause problems
        players[current_player].conform_check()
    print(f"Turn {turn / len(players)} ended.")


def take_turn(player):
    try:
        global current_player
        current_player = turn % int(len(players))
    except ZeroDivisionError:
        current_player = 0
    print(f"{players[current_player].name}'s turn!")
    time.sleep(.5)
    for i in range(players[current_player].cards_to_draw):
        draw_any(player)
    show_hand(players[current_player])
    players[current_player].conform_check()
    players[current_player].effects_check()
    players[current_player].cards_to_play = 2
    answer = input("Would you like to see your player state right now? (y/n)")
    if answer == "y":
        see_stats(player)
    while players[current_player].cards_to_play > 0:
        play_cards()
    cards_played = []

    roll = roll_dice()

    move_player(int(roll))

    end_turn()


def get_characters(i):
    answer = int(input("Which character would you like? (1-8) ")) - 1

    try:
        players[i].character = characters[answer]
    except:
        print("try again.")
        players[i].character = characters[answer]


def show_hand(player):
    if isinstance(player, int):
        player = players[player]
    for card in range(len(player.hand)):
        print(f"{player.name}'s hand: {player.hand[card].name}")


def see_stats(player):
    if isinstance(player, object):
        player = players
    #print(f"{player[current_player].name}'s happiness: {player[current_player].happiness}")
    #for i in range(len(players[current_player].conformity_effects)):
    #print(f"{player[current_player].name}'s conformity effects: {player[current_player].conformity_effects[i].name}")
    #print(f"{player[current_player].name}'s space: {player[current_player].space}")
    #if player[current_player].in_conformity:
    #print(f"{player[current_player].name} is in conformity.")
    print(player[current_player])


def play_cards():
    if players[current_player].hand != []:
        # Ask once if they want to play cards
        answer = input("Would you like to play a card? (y/n)")
        
        if answer == "y":
            while players[current_player].cards_to_play > 0:
                pos = 0
                for i in range(len(players[current_player].hand)):
                    pos += 1
                    print(players[current_player].hand[i].name, str(pos))
                try:
                    card_played = int(
                        input("Which card? (Enter a number value)")) - 1
                except:
                    print("Try again.")
                    card_played = int(
                        input("Which card? (Enter a number value)")) - 1
                
                card = players[current_player].hand[card_played]
                card.play(players[current_player])
                players[current_player].hand.remove(card)
                discard_decks[str(card.type)].append(card)
                players[current_player].cards_to_play -= 1
                
                # If they have plays left, ask if they want to play another
                if players[current_player].cards_to_play > 0:
                    answer = input("Would you like to play another card? (y/n)")
                    if answer == "n":
                        players[current_player].cards_to_play = 0
        else:
            players[current_player].cards_to_play = 0
    else:
        print(
            f"Oh wow thats such a shame oh no {players[current_player].name}'s hand is empty (everyone laugh"
        )
        players[current_player].cards_to_play = 0
        return

        


def remove_conformity2(player):
    try:
        effect1 = random.choice(player.conformity_effects)
        effect2 = random.choice(player.conformity_effects)
        player.conformity_effects.remove(effect1)
        player.conformity_effects.remove(effect2)
    except:
        print("There are no conformity effects left")


def test(player):
    while player.name:
        answer = int(input("1-10"))
        if answer == 1:
            draw_nature(player)
            draw_chance(player)
            draw_conformity(player)
            draw_reliance(player)
            draw_philosophy(player)
        if answer == 2:
            shuffle_nature()
            shuffle_conformity()
            shuffle_chance()
            shuffle_reliance()
            shuffle_philosophy()
        if answer == 3:
            undiscard_all()
        if answer == 4:
            take_turn(player)
        if answer == 5:
            draw_any(player)
            draw_any(player)
        if answer == 6:
            draw_nature(player)
            draw_nature(player)
        if answer == 7:
            print("hello")
        if answer == 8:
            print("hi")
        if answer == 9:
            player.character.draw_starting_cards(player)
        if answer == 10:
            for i in range(len(player.hand)):
                player.hand[i].play()
        if answer == 11:
            print(players[current_player].hand)


#get number of players and their names
def get_players():
    answer = int(input("How many people are playing? "))
    for i in range(answer):
        name = input("What's your name?")
        players.append(Player(name, "None", "None"))
    return players


def ask_question():
    num = random.randint(0, len(questions) - 1)
    question = questions[num]
    correct_answer = answers[num]
    answer = input(question)
    if answer == correct_answer or answer in correct_answer:
        print("Quesiton answered correctly!")
        return True
    else:
        print("Oops. WRONG.")


get_players()

print('''Choose which character you want to play as:    
1) The Influencer: One less effect to become CONFORMED 
   Cards: 3 conformity cards  
2) The Philosopher: Takes one more effect to become CONFORMED 
   Cards: 2 self reliance cards, 1 philosophy card 
3) The Hippie: Starts lost 
   Cards: 4 Nature cards 
4) The Egotist: Is egotistic, takes one more effect to become CONFORMED 
   Cards: 3 Self Reliance cards 
5) The Prisoner: Starts lost 
   Cards: No cards 
6) The Wild Card: Takes one more effect to be conformed 
   Cards: One chance card, two random cards 
7) The Fool: Takes effect of 2 conformity cards, starts lost, is egotistic, gains double happiness
   Cards: 2 self reliance, 1 conformity 
8) The Activist: Nothing special 
   Cards: 2 nature cards, one philosophy card''')
for i in range(len(players)):
    get_characters(i)
    print(f"{players[i].name} has chosen {players[i].character.name}")
for player in range(len(players)):
    print("""
    """)
    players[player].character.draw_starting_cards(player)
    players[current_player].character.apply_special_effects(
        players[current_player])
    show_hand(player)

#create the text that tells you what characters do
#ideally, update this to have character cards that tell you what they do when clicked

#test(players[current_player])

#test(players[current_player])

while turn < 45:
    take_turn(players[current_player])

if turn >= 45:
    print("You have reached the end of the game! Congratulations!")
    for i in range(len(players)):
        players[i].end_game = True
        checks = 0
        if any(players[i].happiness >= players[checks].happiness):
            checks += 1
            continue
        else:
            print(f"{players[i].name} wins!")