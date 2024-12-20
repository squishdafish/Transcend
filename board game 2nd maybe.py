import pygame
import random
import time
import sys
#TEXT AAAAH TEXT AH PANIC DADHAHS9 text for pygame in pygame
#text_surface = font.render(f"", True, (100, 100, 100))
#screen.blit(text_surface, (0, 10))
#pygame.display.flip()



pygame.init()
screen = pygame.display.set_mode((1920, 1080)) 
pygame.display.set_caption("Transcend")

players = []
font = pygame.font.SysFont('Comic Sans MS', 30) 
rows = 20
cols = 20
space_size = 25
background_color = 0, 0, 0
HAND_ZONE_Y = 950
MESSAGE_ZONE_Y = 10
CHARACTER_ZONE_Y = 50
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (100, 100, 100)
FONT_SIZE = 30
COLOR_ACTIVE = (150, 150, 150)
COLOR_INACTIVE = (50, 50, 50)
global turn 
turn = 0

try: 
    current_player = turn % int(len(players))
except:
    current_player = 0

player = current_player

running = True

#--- CLASSES ---
class Player:
    def __init__(self, name, character, starting_cards):
        self.name = name # <--- implemented
        self.character = character # <--- mostly implemented
        self.space = 0 # <--- WORK ON TONIGHT AAAAAAAAAAAAAAAAAAAAAAAAAAAAAH PANIC
        self.happiness = 0 # <--- should be good
        self.happiness_gained = 0 # <--- should be good
        self.happiness_to_gain_next_turn = 0 # <--- good unless there's a card that gains happiness every next turn
        self.extra_happiness = 0 # <--- SHOULD be good
        self.happy_loss_resist = 0 # <--- OH MY GOD WORK ON THIS TONIGHT AAAAH AAAAH OH NO
        self.happiness_lost = 0 # <--- ^^^^^^^
        self.happiness_to_lose_next_turn = 0
        self.nature_buff = 0 # <--- implemented i hope
        self.number_of_cards = 0 # <---- I dont know what this is
        self.cards_to_play = 2 # <---- not implemented need to do the turn logic
        self.number_of_conform = 0 # <---- AAAAAAAAAAA OH GOD THIS ISNT IMPLEMENTED D: AAAAAAAH
        self.number_of_reliance = 0 # <---- transcendence can also be a tonight thing right?
        self.number_of_nature = 0
        self.conform_threshold = 3 # <---- CONFORMITY CONFORMITY AAAAH CONFORMITY WALDEN AAH
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

    def __str__(self):
        return f"{self.name} ({self.character}) - Space: {self.space}, Happiness: {self.happiness}, Happiness to Gain Next Turn: {self.happiness_to_gain_next_turn}, Number of Cards: {self.number_of_cards}, Cards to Play: {self.cards_to_play}, Number of Conform: {self.number_of_conform}, Number of Reliance: {self.number_of_reliance}, Conform Threshold: {self.conform_threshold}, Cards to Draw: {self.cards_to_draw}, Hand: {self.hand}, Transcended: {self.transcended}, Conformed: {self.conformed}, Lost: {self.lost}, Egotistic: {self.egotistic}, Half Multiplier: {self.half_multiplier}, Double Multiplier: {self.double_multiplier}, Triple Multiplier: {self.triple_multiplier}, Conform Immune: {self.conform_immune}, Garden (Nature): {self.garden_nature}, Garden (Reliance): {self.garden_reliance}"

    #I dont think effects are removed if they aren't timed but that's fine thats not a problem
    def conform_check(self):
        for i in range(len(players)):
            #checks for lingering envy
            for effects in range(len(players[i].conformity_effects)):
                if "Envy" not in players[i].conformity_effects[effects].name:
                    players[i].envied = False
            #Social media (half happiness, 50 - 50 to either half or double happiness gained next turn)
                if "Social Media" in players[i].conformity_effects[effects].name:
                    last_turn = turn
                    old_happiness = self.happiness_gained
                    if old_happiness < self.happiness_gained:
                        coin = random.randint(1,2)
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
                if "New Wardrobe" in players[i].conformity_effects[effects].name:
                    for card in range(len(self.hand)):
                        discard_decks[f"{card.type}"].append(card)
                    self.hand = []
                    draw_card_message(f"{self.name}, choose your first card type.")
                    deck1 = choose_deck()
                    draw_given(deck1)

                    draw_card_message(f"{self.name}, choose your second card type.")
                    deck2 = choose_deck()
                    draw_given(deck2)
                #makes player transcended once again, after conformity effect is lost
                if self.marked == True and not "New Wardrobe" or "Plastic Surgery" in players[i].conformity_effects[effects].name:
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
                        for effect in self.effects:
                            if effect == "CONFORM resist":
                                player.conform_threshold -= 1
                if players[i].character == "The Fool":
                    player.double_multiplier = False
                elif players[i].character == "The Egotist":
                    player.egotistic = True
                    player.conform_threshold += 1


        #Lose self (no character effects)
        #office job -3 happiness each turn
        #plastic surgery (half happiness gained while in effect)
        #Dependency (one less card next turn)
        #manipulate / manipulate neo - lose card at start of turns, lose two cards at start of turns

    def effects_check(self):
        for card in cards_played:
            #double happiness check 
            if self.double_multiplier or self.egotistic:
                old_happiness = self.happiness_gained
                if self.happiness_gained > old_happiness:
                    difference = self.happiness_gained - old_happiness

                    if self.character.name == "The Fool":
                        difference *= 2
                    if self.egotistic:
                        difference *= 2

                    self.happiness_gained += difference

                    self.happiness += self.happiness_gained
                    self.happiness_gained = 0

                    if self.character.name == "The Fool":
                        return
                    else:
                        self.double_multiplier = False

            if self.triple_multiplier:
                self.happiness_gained *= 3
                self.happiness += self.happiness_gained
                self.happiness_gained = 0
                self.triple_multiplier = False

            if self.extra_happiness > 0:
                old_happiness = self.happiness_gained
                if self.happiness_gained > old_happiness:
                    self.happiness_gained += self.extra_happiness

            if self.conform_immune:
                old_effects = self.conformity_effects
                if len(self.conformity_effects) > len(old_effects):
                    self.conformity_effects.remove(self.conformity_effects[-1])

            if self.lost_immune:
                if self.lost:
                    self.lost = False
                    self.lost_immune = False
            #happiness gained upon start of turn check
            if self.happiness_to_gain_next_turn > 0:
                last_turn = turn
                if turn > last_turn:
                    self.happiness_gained += self.happiness_to_gain_next_turn
                    self.happiness_to_gain_next_turn = 0
            #nature has increased happiness check
            if self.nature_buff > 0:
                old_happiness = self.happiness_gained
                if card.type == "Nature":
                    self.happiness_gained += self.nature_buff

            #theres a better way to do this for sure, but check for forest effect
            if self.Forest:
                last_turn = turn
                if turn > last_turn:
                    if not self.nature_played:
                        self.happiness_lost -= 3


            #adding back happiness gained at start of turns
            if self.garden_nature:
                if self.happiness_to_gain_next_turn == 0:
                    self.happiness_to_gain_next_turn += 1
            if self.Nature:
                if self.happiness_to_gain_next_turn == 0:
                    self.happiness_to_gain_next_turn += 1
                    if self.transcended:
                        self.happiness_to_gain_next_turn += 4
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
                if turn > last_turn:
                    if card == "Camp":
                        self.double_counter += 1
                        if self.double_counter == 2:
                            self.double_counter = 0
                            self.happy_multiplier_turn = False
                    else: 
                        self.happy_multipler_turn = False
            if self.nonconformity:
                old_effects = self.conformity_effects
                if old_effects != self.conformity_effects:
                    if self.transcended:
                        target = choose_target(self)
                        text_surface = font.render(f"The conformity effect has been deflected to {target.name}", True, (100, 100, 100))
                        screen.blit(text_surface, (0,0))
                        pygame.display.flip()
                        target.conformity_effects.append(self.conformity_effects[-1])
                        self.nonconformity = False
                    elif not self.transcended:
                        for i in range(len(players)):
                            checks = 0
                            if any(players[i].number_of_reliance >= players[checks].number_of_reliance):
                                checks += 1
                                continue
                            else:
                                text_surface = font.render(f"The conformity effect has been deflected to {players[checks].name}", True, (100, 100, 100))
                                screen.blit(text_surface, (0,0))
                                pygame.display.flip()
                                players[checks].conformity_effects.append(self.conformity_effects[-1])
                                self.nonconformity = False
            if self.egotistic:
                if turn > 10 * len(players):
                    self.game_over = True

            if self.envied:
                old_happiness = self.happiness_gained
                if self.happinesss > old_happiness:
                    for player in players:
                        for effect in player.conformity_effects:
                            if effect.name == "Envy" and self.name in effect.name:
                                player.happiness_lost += 2
                            
            if self.happiness_lost > 0:
                happiness_lost = self.happiness_lost - self.happiness_loss_resist
                self.happiness -= happiness_lost
        #make the reliance and nature cards lasting effects add reliance_cards or just make it be all reliance and nature cards played
            if self.happiness_to_lose_next_turn > 0:
                last_turn = turn
                if turn > last_turn:
                    happiness_lost = self.happiness_lost - self.happiness_loss_resist
                    self.happiness -= happiness_lost
    
    def transcend_check(self):
        if self.number_of_reliance + self.number_of_nature >= self.transcend_threshold:
            self.transcended = True
                    
                    
            #ALSO REMEMBER MORE IMPORTANT DO NOT DROP CONFORMITY EFFECSTS THERE IS A DIFFERENT ARRAY FOR THAT MAYBE 
   
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]  # 2D grid
        self.players_positions = {}  # Track players on the board

    def render(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * space_size
                y = row * space_size 
                pygame.draw.rect(screen, (200, 200, 200), (x, y, space_size, space_size), 1)
                # Draw players if present
                for player_name, position in self.players_positions.items():
                    if position == (row, col):
                        pygame.draw.circle(screen, (255, 0, 0), (x + space_size // 2, y + space_size // 2), 20)  # Red circle



   # def set_space(self, row, col, space_type):
       # """Define a type of space on the board."""
        #self.grid[row][col] = space_type

    def move_player(self, player_name, roll):
        if player_name not in self.players_positions:
            print(f"Player {player_name} not found on the board.")
            return
        player_name.space += roll # <--- should work


        #current_position = self.players_positions[player_name]
        #new_position = (current_position[0], (current_position[1] + steps) % self.cols)  # Move horizontally for simplicity
        #self.players_positions[player_name] = new_position

        # Check the type of space landed on
        space_type = roots[players[player].space] #again, need more than just player 1
        print(f"{player_name} landed on a {space_type} space.")
        self.trigger_space(player_name, space_type)

    def add_player(self, player_name, start_position):
        """Add a player to the board."""
        self.players_positions[player_name] = start_position

    def trigger_space(self, space_type, player): # <--- added "player" SHOULD be fine
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

class Button:
    def __init__(self, x, y, width, height, text, color=(100, 100, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False

    def draw(self, screen):
        # Change color when hovered
        color = (150, 150, 150) if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, 2)  # 2 is border width
        
        # Render text
        text_surface = font.render(self.text, True, color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            # Update hover state
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if clicked
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
class Card:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect
    
    def play(self, player):
        result = False
        print(self.type, self.effect, self.name)
        if player.cards_to_play == 0:
            return
        effect = self.effect
        print(f"You played {self.name}: {self.effect}")
        for i in players:
            if self.type == "Self Reliance":
                if self.name == "Greatness":
                    player.double_multiplier = True
                    player.remove_multipler = True
                    draw_card_message(f"{player.name}'s next happiness gained will be doubled.")
                    draw_any(player)
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Rest":
                    player.remove_conformity2(player)
                    player.conformed = False
                    if player.transcended:
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Study":
                    player.nature_buff += 3 
                    draw_any(player)
                    if player.transcended:
                        draw_any(player)
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Intuition":
                    player.lost_immune = True
                    player.extra_happiness += 1
                    #drop the extra happiness next turn somehow <--- not sure if ive done this, check that
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Nonconformity":
                    player.conform_immune = True
                    player.nonconformity = True
                    player.number_of_reliance += 1
                    if player.conformity_effects == []:
                        return
                    effect = random.choice(player.conformity_effects)
                    player.conformity_effects.remove(effect)
                    result = True
                elif self.name == "Sense of self":
                    if player.happiness < 5:
                        player.conform_immune = True
                        player.triple_multipler = True
                        draw_any(player)
                        player.number_of_reliance += 1
                        result = True
                elif self.name == "Therapy":
                    num = random.randint(1,3)
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
                    player.remove_conformity2(player)
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Garden":
                    player.garden_reliance = True
                    player.happiness_to_gain_next_turn += 1
                    if player.garden_nature:
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Search for self":
                    player.space = 0
                    draw_reliance(player)
                    draw_reliance(player)
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Budget":
                    player.happiness_loss_resist += 1
                    if player.transcended:
                        player.happiness_loss_resist += 2
                    player.number_of_reliance += 1
                    result = True
                elif self.name == "Self Reliant":
                    effect = random.choice(player.conformity_effects)
                    player.conformity_effects.remove(effect)
                    player.conformed = False
                    player.double_multiplier = True
                    draw_any(player)
                    if player.transcended:
                        player.cards_drawn += 1
                        player.cards_to_play += 1
                    player.number_of_reliance += 1
                    result = True
            if self.type == "Conformity":
                target = choose_target(self)
                if self.name == "Social Media":
                    target.happiness *= 2
                    target.conformtiy_effects.append(self)
                    result = True 
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
                    result = True
                if self.name == "Envy":
                    player.envied = True
                    self.caster = player.name
                    target.conformity_effects.append(self)
                    result = True
                if self.name == "Extortion":
                    try:
                        card = random.choice(target.hand)
                        target.hand.remove(card)
                    except target.hand == []: 
                        target.happiness_lost += 3
                    target.conformity_effects.append(self)
                    result = True
                if self.name == "Insult":
                    target.happiness_lost += 3
                    target.conformity_effects.append(self)
                    result = True
                if self.name == "Lose self":
                    target.lost = True
                    target.cards_to_play -= 1
                    target.conformity_effects.append(self)
                    result = True
                if self.name == "Office job":
                    target.happiness_to_lose_next_turn += 3
                    target.conformity_effects.append(self)
                    result = True
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
                    result = True
                if self.name == "Dependency":
                    for card in target.hand:
                        if card.type == "Self Reliance":
                            target.hand.remove(card)
                            discard_reliance.append(card)
                    target.egotistical = False
                    target.conformity_effects.append(self)
                    result = True
                if self.name == "Mainpulate":
                    if player.transcended:
                        manipulate_neo = Card("Manipulate Neo", "Conformity", effect)
                        target.conformity_effects.append(manipulate_neo)
                    else: 
                        target.conformity_effects.append(self)
                    result = True
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
                    result = True
                if self.name == "Peer Pressure":
                    target.happiness_lost += 5
                    result = True
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
                    result = True
            if self.type == "Nature":
                if self.name == "Forest":
                    player.happiness_gained += 5
                    player.nature_played = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Night Sky":
                    if player.conformity_effects != []:
                        effect = random.choice(player.conformity_effects)
                        player.conformity_effects.remove(effect)
                    player.happiness.gained += 2
                    player.nature_played = True
                    player.cards_to_play += 1
                    check = random.randint(1,2)
                    if check == 1:
                        player.lost = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Beach":
                    player.conformed = False
                    player.happiness_gained += 2
                    player.nature_played = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Flower Field":
                    player.happiness_gained += 3
                    if player.transcended:
                        player.happiness_gained += 1
                    player.nature_played = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "River":
                    player.happiness_gained += 2
                    player.happiness_to_gain_next_turn += 2
                    player.nature_played = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Transparent Eyeball":
                    # Create temporary deck for viewing
                    temp_deck = decks["nature"][:5]
                    
                    # Display the cards
                    draw_card_message("Choose order for these cards (press 1-5 in desired order):")
                    y_pos = 400
                    for i, card in enumerate(temp_deck):
                        text_surface = font.render(f"{i+1}: {card.name}", True, TEXT_COLOR)
                        screen.blit(text_surface, (800, y_pos))
                        y_pos += 30
                    pygame.display.flip()
                    
                    # Get player input for card order
                    choosing = True
                    eye_cards = []
                    while choosing:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    eye_cards.append(temp_deck[0])
                                elif event.key == pygame.K_2:
                                    eye_cards.append(temp_deck[1])
                                elif event.key == pygame.K_3:
                                    eye_cards.append(temp_deck[2])
                                elif event.key == pygame.K_4:
                                    eye_cards.append(temp_deck[3])
                                elif event.key == pygame.K_5:
                                    eye_cards.append(temp_deck[4])
                                if len(eye_cards) == 5:
                                    choosing = False
                    
                    # Put cards back in order chosen
                    for i in range(5):
                        decks["nature"][i] = eye_cards[i]
                    
                    draw_nature(player)
                    player.lost_immune = True
                    if player.transcended:
                        draw_nature(player)
                    player.nature_played = True 
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Mountains":
                    # Create button
                    mountain_button = Button(1800, 900, 200, 40, "Mountains")
                    mountain_button.draw(screen)  # Draw the button
                    pygame.display.flip()  # Update display
                    
                    waiting_for_click = True
                    while waiting_for_click:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        
                            if mountain_button.handle_event(event):  # If button is clicked
                                player.happiness_gained += 4
                                coin = random.randint(1, 2)
                                if coin == 1:
                                    player.lost = True
                                    draw_card_message("The mountains led you astray! You are now lost.")
                                else:
                                    draw_card_message("You found your way through the mountains!")
                                waiting_for_click = False  # Exit the waiting loop
                                
                            # Update button hover state
                            mouse_pos = pygame.mouse.get_pos()
                            mountain_button.is_hovered = mountain_button.rect.collidepoint(mouse_pos)
                            mountain_button.draw(screen)
                            pygame.display.flip()
                        
                        player.number_of_nature += 1
                        player.nature_played = True
                        result = True
                elif self.name == "Park":
                    player.happiness_gained += 2
                    if player.conformed:
                        player.happiness_gained += 3 
                    player.nature_played = True
                    player.number_of_nature += 1
                    result = True
                elif self.name == "Garden":
                    player.garden_nature = True
                    player.happiness_to_gain_next_turn += 1
                    if player.garden_reliance:
                        player.cards_to_play += 1
                    player.nature_played = True
                    result = True
                    player.number_of_nature += 1
                elif self.name == "Camp":
                    player.happy_multiplier_turn = True
                    player.space = 0
                    player.nature_played = True
                    result = True
                    player.number_of_nature += 1
                elif self.name == "Oasis":
                    player.happiness_gained += 4
                    player.happy_multiplier_turn = True
                    player.happiness_to_gain_next_turn += 4
                    player.nature_played = True
                    result = True
                    player.number_of_nature += 1
                elif self.name == "Nature":
                    player.happiness_to_gain_next_turn += 1
                    if player.transcended:
                        player.happiness_to_gain_next_turn += 4
                        draw_any(player)
                    player.Nature = True
                    result = True
                    player.number_of_nature += 1
                    player.nature_played = True
            if self.type == "Chance":
                if self.name == "Take a hike!":
                    coin = random.randint(1,2)
                    if coin == 1:
                        draw_nature(player)
                        draw_nature(player)
                    else:
                        player.lost = True
                elif self.name == "Trust Yourself":
                    coin = random.randint(1,2)
                    if coin == 1:
                        draw_reliance(player)
                    else:
                        effect = random.choice(player.conformity_effects)
                        player.conformity_effects.remove(effect)
                elif self.name == "Get Builled":
                    card = draw_conformity()
                    card.play(player)
                elif self.name == "Go back to your roots":
                    player.space = 0
                    player.extra_happiness = 0 # <--- SHOULD be good
                    player.happy_loss_resist = 0 # <--- OH MY GOD WORK ON THIS TONIGHT AAAAH AAAAH OH NO
                    player.nature_buff = 0 # <--- implemented i hope
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
                    result = True
                elif self.name == "Chance":
                    coin = random.randint(1,2)
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
                if self.name == "Captialism":
                    for i in range(len(players)):
                        checks = 0
                        if any(players[i].happiness >= players[checks].happiness):
                            checks += 1
                            continue
                        else:
                            player.happiness *= 2
                            player.happiness_gained += players[i].happiness // 2
                            players[i].happiness /= 2
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
                    question = random.randint(1,20)
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
            if result:
                player.cards_to_play -= 1
                print(f"Remaining cards to play {player.cards_to_play}")
            text(draw_card_message, 500, 500)

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
            if players[i].character == "The Fool":  #make it cycle through checking each player - consider using player_name, that's what board uses
                #figure out how to give effect of 2 conformity cards
                player.lost = True
                player.egotistic = True
                player.double_multiplier = True
            elif players[i].character == "The Egotist":
                player.egotistic = True
                player.conform_threshold += 1

    def draw_starting_cards(self, player):
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
            text_surface = font.render(f"{player.name} drew nothing.", True, (100, 100, 100))
            screen.blit(text_surface, (0,0))
            pygame.display.flip()
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
    Card("Forest", "Nature", "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."),
    Card("Forest", "Nature", "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."),
    Card("Forest", "Nature", "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."),
    Card("Forest", "Nature", "Gain 5 happiness. If you do not play a nature card next turn, you are lost and lose 3 happiness. If transcended, you don't need to play a card next turn."),
    Card("Night Sky", "Nature", "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"),
    Card("Night Sky", "Nature", "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"),
    Card("Night Sky", "Nature", "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"),
    Card("Night Sky", "Nature", "Lose one conformity effect, gain 2 happiness, you can play another card this turn. 50-50 chance to get lost"),
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"), 
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"), 
    Card("Beach", "Nature", "Lose CONFORMED, gain 2 happiness"), 
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("Flower Field", "Nature", "Gain 3 happiness. If transcended, gain 4 instead."),
    Card("River", "Nature", "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature", "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature", "Gain 2 happiness now, and 2 happiness next turn."),
    Card("River", "Nature", "Gain 2 happiness now, and 2 happiness next turn."),
    Card("Transparent Eyeball", "Nature", "Look at the top 5 cards of the nature deck, arrange them in any way, and draw a nature card. Can't get lost this turn. If transcended, draw 2 instead,"), 
    Card("Transparent Eyeball", "Nature", "Look at the top 5 cards of the nature deck, arrange them in any way, and draw a nature card. Can't get lost this turn. If transcended, draw 2 instead,"), 
    Card("Mountains", "Nature", "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."),
    Card("Mountains", "Nature", "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."),
    Card("Mountains", "Nature", "Each turn, the user can choose to gain 4 happiness, but has a 50-50 chance to get lost."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Park", "Nature", "Gain 2 happiness if CONFORMED gain 5."),
    Card("Garden", "Nature", "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."),
    Card("Garden", "Nature", "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."),
    Card("Garden", "Nature", "Gain 1 at start of turns, if you have garden self reliance card in play then you can play another card."),
    Card("Camp", "Nature", "Gain 2x happiness for the next 2 turns times gained, and go back to roots."),
    Card("Camp", "Nature", "Gain 2x happiness for the next 2 turns times gained, and go back to roots."),
    Card("Oasis", "Nature", "Gain 4 happiness, next turn can gain 4 again and double happiness gained that turn, but become lost."),
    Card("Oasis", "Nature", "Gain 4 happiness, next turn can gain 4 again and double happiness gained that turn, but become lost."),
    Card("Nature", "Nature", "Gain one happiness each turn. If transcended, gain 5 happiness and draw one each turn. ")
]

reliance_cards = [
    Card("Greatness", "Self Reliance", "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance", "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance", "Gain 2x happiness from next source. Draw one."),
    Card("Greatness", "Self Reliance", "Gain 2x happiness from next source. Draw one."),
    Card("Rest", "Self Reliance", "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."),
    Card("Rest", "Self Reliance", "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."),
    Card("Rest", "Self Reliance", "Lose up to two conformity effects, lose CONFORMED. If transcended you can play an extra card this turn."),
    Card("Study", "Self Reliance", "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."),
    Card("Study", "Self Reliance", "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."),
    Card("Study", "Self Reliance", "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."),
    Card("Study", "Self Reliance", "Gain 2 extra happiness from nature cards. (Applies after multipliers, does NOT stack.) Draw one. If transcended, draw another card."),
    Card("Intuition", "Self Reliance", "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."),
    Card("Intuition", "Self Reliance", "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."),
    Card("Intuition", "Self Reliance", "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."),
    Card("Intuition", "Self Reliance", "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."),
    Card("Intuition", "Self Reliance", "You cannot get lost this and next turn. Gain 1 extra happiness from any source during those turns (applies after multipliers, does not stack). Draw one."),
    Card("Nonconformity", "Self Reliance", "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."),
    Card("Nonconformity", "Self Reliance", "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."),
    Card("Nonconformity", "Self Reliance", "Lose one conformity effect, next time player is targeted by a conformity card, the card will instead target the player with the least active self reliance cards. If transcended you choose who it targets."),
    Card("Sense of self", "Self Reliance", "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."),
    Card("Sense of self", "Self Reliance", "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."),
    Card("Sense of self", "Self Reliance", "Gain immunity to the next conformity card. Gain 3x happiness from next source. Play this card only if you have less than 5 happiness. Draw one."),
    Card("Therapy", "Self Reliance", "Lose one neegative status on player and up to two conformity effects."),
    Card("Therapy", "Self Reliance", "Lose one neegative status on player and up to two conformity effects."),
    Card("Therapy", "Self Reliance", "Lose one neegative status on player and up to two conformity effects."),
    Card("Therapy", "Self Reliance", "Lose one neegative status on player and up to two conformity effects."),
    Card("Therapy", "Self Reliance", "Lose one neegative status on player and up to two conformity effects."),
    Card("Garden", "Self Reliance", "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."),
    Card("Garden", "Self Reliance", "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."),
    Card("Garden", "Self Reliance", "Gain 1 at start of turns, if you have garden nature card in play then you can play another card."),
    Card("Search for self", "Self Reliance", "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance", "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance", "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance", "Send back to roots, draw 2 self reliance cards."),
    Card("Search for self", "Self Reliance", "Send back to roots, draw 2 self reliance cards."),
    Card("Budget", "Self Reliance", "When you lose happiness, you lose 1 less. If transcended, lose 3 less."),
    Card("Budget", "Self Reliance", "When you lose happiness, you lose 1 less. If transcended, lose 3 less."),
    Card("Budget", "Self Reliance", "When you lose happiness, you lose 1 less. If transcended, lose 3 less."),
    Card("Budget", "Self Reliance", "When you lose happiness, you lose 1 less. If transcended, lose 3 less."),
    Card("Self Reliant", "Self Reliance", "Lose one conformity effect, lose CONFORMED, gain 2x happiness next turn, and draw a card. If transcended, draw one at start of turn, and you can play an extra card.")
]

conformity_cards = [
    Card("Social Media", "Conformity", "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."),
    Card("Social Media", "Conformity", "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."),
    Card("Social Media", "Conformity", "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."),
    Card("Social Media", "Conformity", "Double a player's happiness, then half it next turn. Whenever happiness is gained, 50-50 it is either halved or doubled."),
    Card("New Wardrobe", "Conformity", "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."),
    Card("New Wardrobe", "Conformity", "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."),
    Card("New Wardrobe", "Conformity", "Change character, at start of turns discard hand. Replace with two of any type. If transcended, untranscend target."),
    Card("Envy", "Conformity", "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity", "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity", "Player loses 2 happiness each time the user gains happiness."),
    Card("Envy", "Conformity", "Player loses 2 happiness each time the user gains happiness."),
    Card("Extortion", "Conformity", "Each turn the target discards a card, if no cards then lose 3 happiness."),
    Card("Extortion", "Conformity", "Each turn the target discards a card, if no cards then lose 3 happiness."),
    Card("Extortion", "Conformity", "Each turn the target discards a card, if no cards then lose 3 happiness."),
    Card("Insult", "Conformity", "Target a player; they lose 3 happiness. When they gain happiness, it's halved."),
    Card("Insult", "Conformity", "Target a player; they lose 3 happiness. When they gain happiness, it's halved."),
    Card("Insult", "Conformity", "Target a player; they lose 3 happiness. When they gain happiness, it's halved."),
    Card("Insult", "Conformity", "Target a player; they lose 3 happiness. When they gain happiness, it's halved."),
    Card("Lose self", "Conformity", "Target gets lost this turn and has no positive character effects."),
    Card("Lose self", "Conformity", "Target gets lost this turn and has no positive character effects."),
    Card("Lose self", "Conformity", "Target gets lost this turn and has no positive character effects."),
    Card("Office job", "Conformity", "Target loses 3 happiness at start of turns."),
    Card("Office job", "Conformity", "Target loses 3 happiness at start of turns."),
    Card("Plastic Surgery", "Conformity", "Change character, lose hand, half happiness gained while in effect. If transcended, untranscend target."),
    Card("Plastic Surgery", "Conformity", "Change character, lose hand, half happiness gained while in effect. If transcended, untranscend target."),
    Card("Dependency", "Conformity", "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."),
    Card("Dependency", "Conformity", "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."),
    Card("Dependency", "Conformity", "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."),
    Card("Dependency", "Conformity", "Discard all self reliance cards, lose egotistical. Target plays one less card next turn."),
    Card("Manipulate", "Conformity", "Lose a card at start of turns, user chooses which type. If transcended, lose two."),
    Card("Manipulate", "Conformity", "Lose a card at start of turns, user chooses which type. If transcended, lose two."),
    Card("Manipulate", "Conformity", "Lose a card at start of turns, user chooses which type. If transcended, lose two."),
    Card("Fad Diet", "Conformity", "Lose 2 cards and go back to roots."),
    Card("Fad Diet", "Conformity", "Lose 2 cards and go back to roots."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("Peer Pressure", "Conformity", "Lose 5 happiness."),
    Card("CONFORM", "Conformity", "CONFORM player, send player to CONFORMITY, if transcended they lose two cards, and next turn they draw one less.")
]

chance_cards = [
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Take a hike!", "Chance", "50-50 chance to either draw 2 nature cards or get lost."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Trust Yourself", "Chance", "50-50 change to either draw a self reliance card or lose a conformity effect."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Get Bullied", "Chance", "A conformity card is played against you."),
    Card("Go back to your roots", "Chance", "Go back to bottom of the tree, with everything but happiness, character, and hand reset."),
    Card("Go back to your roots", "Chance", "Go back to bottom of the tree, with everything but happiness, character, and hand reset."),
    Card("Go back to your roots", "Chance", "Go back to bottom of the tree, with everything but happiness, character, and hand reset."),
    Card("Go back to your roots", "Chance", "Go back to bottom of the tree, with everything but happiness, character, and hand reset."),
    Card("Go back to your roots", "Chance", "Go back to bottom of the tree, with everything but happiness, character, and hand reset."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Meditate", "Chance", "Put discard piles back into their decks, draw one."),
    Card("Trip", "Chance", "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Trip", "Chance", "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Trip", "Chance", "Move back x spaces and lose x happiness. (x= dice roll)"),
    Card("Jump for joy!", "Chance", "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Jump for joy!", "Chance", "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Jump for joy!", "Chance", "Move forward x spaces and gain x happiness (x = dice roll)"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card("Mirror", "Chance", "Become egotistical"),
    Card("Therapy", "Chance", "Loses one negative status on player and up to two conformity effects."),
    Card("Therapy", "Chance", "Loses one negative status on player and up to two conformity effects."),
    Card("Therapy", "Chance", "Loses one negative status on player and up to two conformity effects."),
    Card("Therapy", "Chance", "Loses one negative status on player and up to two conformity effects."),
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
    Card("Map", "Chance", "Keep this card in your hand. You may play this at any time to un-get lost"),
    Card("Map", "Chance", "Keep this card in your hand. You may play this at any time to un-get lost"),
    Card("Map", "Chance", "Keep this card in your hand. You may play this at any time to un-get lost"),
    Card("Map", "Chance", "Keep this card in your hand. You may play this at any time to un-get lost"),
    Card("Map", "Chance", "Keep this card in your hand. You may play this at any time to un-get lost"),
    Card("Chance", "Chance", "50-50 to draw one of each card, or discard all self reliance and one nature.")
]

philosophy_cards = [
    Card("Communism", "Philosophy", "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."),
    Card("Communism", "Philosophy", "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."),
    Card("Communism", "Philosophy", "Everyone's happiness is set to 5 and they discard/draws cards till they have 3."),
    Card("Capitalism", "Philosophy", "When you draw this, if you have the most happiness, then take half of every other players' happiness."),
    Card("Capitalism", "Philosophy", "When you draw this, if you have the most happiness, then take half of every other players' happiness."),
    Card("Transcendentalism", "Philosophy", "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"),
    Card("Transcendentalism", "Philosophy", "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"),
    Card("Transcendentalism", "Philosophy", "Triggers effect of transcend space. +1 card needed for effect. If transcended, draw a card"),
    Card("Absurdism", "Philosophy", "Roll die. Draw/discard until the number of cards in hand matches that number."),
    Card("Absurdism", "Philosophy", "Roll die. Draw/discard until the number of cards in hand matches that number."),
    Card("Absurdism", "Philosophy", "Roll die. Draw/discard until the number of cards in hand matches that number."),
    Card("Absurdism", "Philosophy", "Roll die. Draw/discard until the number of cards in hand matches that number."),
    Card("Absurdism", "Philosophy", "Roll die. Draw/discard until the number of cards in hand matches that number."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Nihilism", "Philosophy", "Get lost, and go back to roots."),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Creationism", "Philosophy", "Put discard piles back into their decks, draw one"),
    Card("Realism", "Philosophy", "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."),
    Card("Realism", "Philosophy", "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."),
    Card("Realism", "Philosophy", "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."),
    Card("Realism", "Philosophy", "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."),
    Card("Realism", "Philosophy", "Ask a question. If correct, get 5 happiness. If incorrect, lose 5 happiness."),
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
    Card("Existentialism", "Philosophy", "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy", "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy", "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards."),
    Card("Existentialism", "Philosophy", "Lose CONFORM, leave CONFORMITY, and draw two self reliance cards.")
]

cards_played = []

eye_cards = []


characters = [
    Character("The Influencer", "CONFORM weakness", "3 conformity cards"),
    Character("The Philosopher", "CONFORM resist", "1 philosophy card, 2 self reliance cards"),
    Character("The Hippie", "Starts lost", "4 nature cards"), 
    Character("The Egotist", "Is egotistic, CONFORM resist", "3 self reliance cards"),
    Character("The Prisoner", "Starts lost", "No cards"),
    Character("The Wild Card", "CONFORM resist", "2 random cards, 1 chance card,"),
    Character("The Fool", "Takes effect of 2 conformity cards, starts lost, is egotistic, gains double happiness", "2 self reliance, 1 conformity card"),
    Character("The Activist", "Nothing womp womp", "2 nature cards, 1 philosophy card")
]

decks = {
"nature": nature_cards,
"reliance": reliance_cards,
"conformity": conformity_cards,
"chance": chance_cards,
"philosophy": philosophy_cards,
"eye": eye_cards
}

alt_decks = [
    nature_cards, reliance_cards, conformity_cards
]

discard_nature = []

discard_reliance = []

discard_conformity = []

discard_philosophy = []

discard_chance = []


discard_decks = {"chance": discard_chance, 
                 "nature": discard_nature, 
                 "reliance": discard_reliance, 
                 "conformity": discard_conformity, 
                 "philosophy": discard_philosophy}

#SPACE TYPES
space_types = [
    Space("nature", "Trigger a question, draw a nature card"),
    Space("reliance", "Trigger a question, draw a reliance card"),
    Space("conformity", "Trigger a question, draw a conformity card"),
    Space("chance", "Trigger a chance event"),
    Space("philosophy", "Trigger a philosophy event")
]

first_10_questions = [

]

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
    "birth", "empty", "empty", "nature", "reliance", "empty", "philosophy", "empty", "nature", "empty", "chance", "empty", "philosophy", "empty", "reliance",
"empty", "nature", "empty", "conformity", "conformity", "chance", "reliance", "chance", "reliance", "empty", "conformity", "nature", "empty", "philosophy", "reliance"
]

nature_branch = [
    "nature", "empty", "nature", "chance", "nature", "empty", "nature", "philosophy", "nature", "reliance", "nature", "empty", "nature", "nature", "transcendence"
]

reliance_branch = [
    "reliance", "empty", "reliance", "chance", "reliance", "empty", "reliance", "philosophy", "reliance", "reliance", "reliance", "empty", "reliance", "reliance", "transcendence"
]

conformity_branch = [
    "conformity", "conformity", "conformity", "conformity", "conformity", "chance", "conformity", "empty", "empty", "philsophy", "conformity", "empty", "conformity", "conformity", "empty"
]
#empty spaces should = 30% the total spaces, philosophy being like 10%, chance being 10%, nature, reliance, and conformity being the other 50% (20, 20, and 10)

#make sure to check youre happy with the amount of conformance and nature and whatnot
branches = {
    "Nature": nature_branch,
    "Reliance": reliance_branch,
    "Conformity": conformity_branch
}

#BASIC FUNCTIONS RAAAAAAAAAAAH
def choose_target(self):
    buttons = []
    y_pos = 0
    for player in players:
        buttons.append(Button(1800, y_pos, 200, 40, player.name))
        y_pos += 50  
    
    waiting_for_click = True
    selected_target = None  # Initialize target variable
    
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Check button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        selected_target = next(p for p in players if p.name == button.text)
                        draw_card_message(f"{selected_target.name} has been targeted with {self.name}: {self.effect}")
                        time.sleep(1)
                        waiting_for_click = False
                        break
        
        # Draw buttons
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

    return selected_target  # Return the selected target


def choose_deck():
    buttons = [
        Button(1600, 800, 200, 40, "Nature"),
        Button(1600, 850, 200, 40, "Self Reliance"),
        Button(1600, 900, 200, 40, "Conformity"),
        Button(1600, 950, 200, 40, "Philosophy"),
        Button(1600, 1000, 200, 40, "Chance")
    ]
    
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            for button in buttons:
                if button.handle_event(event):
                    deck_name = button.text.lower().replace(" ", "_")
                    waiting_for_click = False
                    return deck_name
        
        # Draw all buttons
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
    
def text(text, x, y, clear_height=30):
    # Clear the specific area
    clear_rect = pygame.Rect(x, y, SCREEN_WIDTH, clear_height)
    pygame.draw.rect(screen, background_color, clear_rect)
    
    # Render new text
    text_surface = font.render(str(text), True, TEXT_COLOR)
    screen.blit(text_surface, (x, y))
    pygame.display.flip()

def coin_flip():
    coin = random.randint(1,2)
    return coin

def draw_card_message(text):
    # Clear message area
    message_area = pygame.Rect(0, MESSAGE_ZONE_Y, SCREEN_WIDTH, 40)
    pygame.draw.rect(screen, BACKGROUND_COLOR, message_area)
    
    # Split long messages into multiple lines if needed
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        # Check if current line is too long
        test_surface = font.render(' '.join(current_line), True, TEXT_COLOR)
        if test_surface.get_width() > SCREEN_WIDTH - 20:  # Leave 20px margin
            lines.append(' '.join(current_line[:-1]))  # Add completed line
            current_line = [word]  # Start new line with current word
    
    if current_line:
        lines.append(' '.join(current_line))
    
    # Draw each line
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (10, MESSAGE_ZONE_Y + (i * 30)))  # 30px vertical spacing
    
    pygame.display.flip()
    message_area = pygame.Rect(0, MESSAGE_ZONE_Y, SCREEN_WIDTH, 40)
    pygame.draw.rect(screen, background_color, message_area)
    
    # Draw new message
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, (10, MESSAGE_ZONE_Y))
    pygame.display.flip()

def roll_dice():
    global roll
    roll = random.randint(1,6)
    buttons = []
    y_pos = 500
    for player in players:
        buttons.append(Button(1800, y_pos, 200, 40, player.name))
        y_pos += 50  
    
    waiting_for_click = True
    
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                            
            for button in buttons:
                if button.handle_event(event):
                    draw_card_message(f"{players[current_player].name} rolled a {roll}")
                    waiting_for_click = False
                        
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
    


    print(f"It's a {roll}")
    return roll
    
def move_player(roll):
    #conformity check
    if not players[current_player].in_conformity:
        players[current_player].space += int(roll)
        if players[current_player].space > 45:
            players[current_player].space = 45
        if players[current_player].space == 45:
            players[current_player].transcend_check() 
            players[current_player].space = 0

    if players[current_player].in_conformity:
        print("Sorry, you're in conformity.")
        text("{players[current_player.name]} is in conformity and cannot move.")

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
    except players[current_player].space > 30 and players[current_player].location == "Roots":
        answer = input("Which branch would you like to go to? (1, 2, or 3)?")
        if answer == 1:
            players[current_player].location = "Nature"
        elif answer == 2:
            players[current_player].location = "Reliance"
        elif answer == 3:
            players[current_player].location = "Conformity"
        space = players[current_player].space - 31
        space_type = branches[players[current_player].location[space]]
    text(f"{players[current_player].name} landed on a(n) {space_type} space", 500, 500)
    
    board.trigger_space(space_type, player)

def draw_given(player, deck):
    text("", 0, 10, 40)

    if deck == []:
        undiscard(decks[f"{deck}"])
    drawn_card = random.choice(decks[f"{deck}"]) 

    text(f"{player.name} drew {drawn_card.name}", 0, 10)

    decks[f"{deck}"].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()

def draw_any(player): 
    text("", 0, 10, 40)

    deck = alt_decks[random.randint(0,2)]
    if deck == []:
        undiscard(deck)
    drawn_card = random.choice(deck) 

    text(f"{player.name} drew {drawn_card.name}", 0, 10)

    deck.remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()

def draw_nature(player):
    # Clear the draw area
    text("", 0, 10, 40)
    
    deck = "nature"
    for i in range(len(players)):
        if players[i].transparent and decks["eye"] != []:
            deck = "eye" 
    if decks[deck] == []:
        undiscard(deck)
    
    drawn_card = random.choice(decks[deck])
    text(f"{player.name} drew {drawn_card.name}", 0, 10)
    
    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    
    if player == players[current_player]:
        show_hand()

def draw_reliance(player):
    text("", 0, 10, 40)


    deck = "reliance"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])
    text(f"{player.name} drew {drawn_card.name}", 0, 10)

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()
def draw_conformity(player):
    text("", 0, 10, 40)

    deck = "conformity"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    text(f"{player.name} drew {drawn_card.name}", 0, 10)

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()
def draw_chance(player):
    text("", 0, 10, 40)

    deck = "chance"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    text(f"{player.name} drew {drawn_card.name}", 0, 10)

    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()
def draw_philosophy(player):
    text("", 0, 10, 40)

    deck = "philosophy"
    if decks[deck] == []:
        undiscard(deck)
    drawn_card = random.choice(decks[deck])

    text(f"{player.name} drew {drawn_card.name}", 0, 10)
    
    decks[deck].remove(drawn_card)
    player.hand.append(drawn_card)
    time.sleep(1)
    if player == players[current_player]:
        show_hand()
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
    turn += 1
    for i in range(len(players)):
        players[i].happiness += players[i].happiness_gained
        players[i].happiness -= players[i].happiness_lost
        if players[i].extra_happiness > 0:
            players[i].extra_counter += 1
            if players[i].extra_counter == 2:
                players[i].extra_counter -= 1
        players[current_player].effects_check(cards_played) #this will almost certainly cause problems
        players[current_player].conform_check()

def take_turn(player):
    players[current_player].conform_check()
    players[current_player].effects_check()
    players[current_player].cards_to_play = 2  # Reset cards_to_play at start of turn
    draw_any(players[current_player])
    clickable_cards = show_hand()
    cards_played = []
    
    skip_button = Button(1600, 900, 200, 40, "Skip Playing Cards")
    skip_button.draw(screen)

    text_surface = font.render(f"Current Player: {players[current_player].name} Turn: {turn / len(players)} ({turn})", True, (100, 100, 100))
    screen.blit(text_surface, (0,0))
    pygame.display.flip()

    waiting_for_cards = True
    while waiting_for_cards and players[current_player].cards_to_play > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if skip_button.handle_event(event):
                player.cards_to_play = 0
                waiting_for_cards = False
                break   
            
            # Handle card playing
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_card = play_cards(clickable_cards, player)
                if clicked_card:
                    cards_played.append(clicked_card)
                    show_happiness()
                    clickable_cards = show_hand()  # Update the hand display

        # Update skip button hover state
        mouse_pos = pygame.mouse.get_pos()
        skip_button.is_hovered = skip_button.rect.collidepoint(mouse_pos)
        skip_button.draw(screen)
        pygame.display.flip()
               
        if players[current_player].cards_to_play == 0:
            waiting_for_cards = False
    
    roll = roll_dice()
    move_player(int(roll))
    pygame.display.flip()
    end_turn()

def play_cards(cards, player):
    if player.cards_to_play <= 0:
        draw_card_message("No more cards to play this turn!")
        return None
        
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]
    result = None
    if mouse_clicked:
        if players[current_player].cards_to_play <= 0:
            return
        for card_rect, card in cards:
            if card_rect.collidepoint(mouse_pos):
                result = card.play(player)  # Pass the player instead of current_player
                if result:  # Only remove card and decrement if play was successful
                    player.hand.remove(card)
                    discard_decks[card.type].append(card)
                    player.cards_to_play -= 1  # Decrement cards_to_play
                    draw_card_message(f"Played {card.name}: {card.effects} {player.cards_to_play} cards left to play.")
                    clickable_cards = show_hand()
                    return card
        
    return None

def get_characters(i):
    waiting_for_input = True
    display_character_options()  # Display options once at start
    
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    players[i].character = Character("The Influencer", "CONFORM weakness", "3 conformity cards")
                    waiting_for_input = False
                elif event.key == pygame.K_2:
                    players[i].character = Character("The Philosopher", "CONFORM resist", "2 self reliance cards, 1 philosophy card")
                    waiting_for_input = False
                elif event.key == pygame.K_3:
                    players[i].character = Character("The Hippie", "Starts lost", "4 nature cards")
                    waiting_for_input = False
                elif event.key == pygame.K_4:
                    players[i].character = Character("The Egotist", "Is egotistic, CONFORM resist", "3 self reliance cards")
                    waiting_for_input = False
                elif event.key == pygame.K_5:
                    players[i].character = Character("The Prisoner", "Starts lost", "No cards")
                    waiting_for_input = False
                elif event.key == pygame.K_6:
                    players[i].character = Character("The Wild Card", "CONFORM resist", "chance card, 2 random cards")
                    waiting_for_input = False
                elif event.key == pygame.K_7:
                    players[i].character = Character("The Fool", "Takes effect of 2 conformity cards, starts lost, is egotistic, gains double happiness", "2 self reliance, 1 conformity")
                    waiting_for_input = False
                elif event.key == pygame.K_8:
                    players[i].character = Character("The Activist", "Nothing womp womp", "2 nature cards, 1 philosophy card")
                    waiting_for_input = False

    # Clear the entire screen except hand area
    pygame.draw.rect(screen, background_color, (0, 0, SCREEN_WIDTH, HAND_ZONE_Y))
    
    # After character is selected
    text_surface = font.render(f"{players[i].name} chose {players[i].character.name}", True, (100, 100, 100))
    screen.blit(text_surface, (800, 540))
    pygame.display.flip()
    
    # Handle starting cards
    if players[i].character.starting_cards != "No cards":
        print(f"{players[i].name} drew:")
        players[i].character.draw_starting_cards(players[i])
    
    time.sleep(1)

def display_character_options():
    # Clear the middle section of the screen
    pygame.draw.rect(screen, background_color, (0, CHARACTER_ZONE_Y, SCREEN_WIDTH, HAND_ZONE_Y - CHARACTER_ZONE_Y))
    
    text = '''Choose which character you want to play as:    
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
   Cards: 2 nature cards, one philosophy card'''

    lines = text.split('\n')
    y_offset = CHARACTER_ZONE_Y
    for line in lines:
        text_surface = font.render(line, True, (100, 100, 100))
        screen.blit(text_surface, (100, y_offset))
        y_offset += 30
    
    pygame.display.flip()

def show_hand():
    # Clear the entire hand area
    hand_area = pygame.Rect(0, 950, SCREEN_WIDTH, 130)
    pygame.draw.rect(screen, background_color, hand_area)
    cards = []
    # Show player name
    text_surface = font.render(f"{players[current_player].name}'s Hand:", True, TEXT_COLOR)
    x = 10
    y = 1000
    screen.blit(text_surface, (x, y))
    
    # Show cards
    x += text_surface.get_width() + 20
    for card in players[current_player].hand:
        if x > SCREEN_WIDTH - 100:
            break
        card_name = card.name if hasattr(card, 'name') else str(card)
        text_surface = font.render(card_name, True, TEXT_COLOR)
        
        # Create clickable area for card
        card_rect = pygame.Rect(x, y, text_surface.get_width(), text_surface.get_height())
        cards.append((card_rect, card))
        
        # Draw card (with highlight if hovered)
        mouse_pos = pygame.mouse.get_pos()
        if card_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (150, 150, 150), card_rect, 1)
        
        screen.blit(text_surface, (x, y))
        x += text_surface.get_width() + 20
    
    pygame.display.flip()
    return cards

def show_happiness():
    hand_area = pygame.Rect(0, 950, SCREEN_WIDTH, 130)
    pygame.draw.rect(screen, background_color, hand_area)
    happiness = players[current_player].happiness + players[current_player].happiness_gained
    # Show player name
    text_surface = font.render(f"{players[current_player].name}'s Happiness:", True, TEXT_COLOR)
    x = 10
    y = 200
    screen.blit(text_surface, (x, y))
    
    
    text(players[current_player].happiness, 10, 250)
    
    pygame.display.flip()
    return happiness

def remove_conformity2(player):
    try:
        effect1 = random.choice(player.conformity_effects)
        effect2 = random.choice(player.conformity_effects)
        player.conformity_effects.remove(effect1)
        player.conformity_effects.remove(effect2)
    except:
        print("There are no conformity effects left")

def test(player):
    while running: 
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
            take_turn(player, board)
        if answer == 5:
            draw_any(player)
            draw_any(player)
        if answer == 6:
            draw_nature(player)
            draw_nature(player)
        if answer == 7:
            pygame.draw.rect(screen, (background_color), (0, 0, 1920, 30))
        if answer == 8:
            text_surface = font.render(f"{players[current_player].name}'s Hand: {str(players[current_player].hand)}", True, (100, 100, 100))
            screen.blit(text_surface, (0,100))
            pygame.display.flip()
        if answer == 9:
            player.character.draw_starting_cards(player)
        if answer == 10:
            for i in range(len(player.hand)):
                player.hand[i].play()
        if answer == 11:
            print(players[current_player].hand)

#get number of players and their names
def get_players():
    # Initialize variables
    input_text = ""
    num_players = 0
    getting_num = True
    current_player = 0
    
    while getting_num or current_player < num_players:
        screen.fill(background_color)
        
        # Show appropriate prompt
        if getting_num:
            prompt = "How many players?: "
        else:
            prompt = f"Enter name for Player {current_player + 1}: "
        
        text_surface = font.render(prompt + input_text, True, TEXT_COLOR)
        screen.blit(text_surface, (100, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key pressed
                    if getting_num:
                        try:
                            num_players = int(input_text)
                            if num_players > 0:  # Validate player count
                                getting_num = False
                                input_text = ""  # Reset for name input
                            else:
                                input_text = ""  # Reset if invalid number
                        except ValueError:
                            input_text = ""  # Reset if not a number
                    else:
                        if input_text.strip():  # If name isn't empty
                            players.append(Player(input_text.strip(), "none", "none"))
                            current_player += 1
                            input_text = ""  # Reset for next player
                            
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    # Only add valid characters
                    if len(input_text) < 20:  # Limit name length
                        if getting_num:
                            if event.unicode.isdigit():
                                input_text += event.unicode
                        else:
                            if event.unicode.isprintable():
                                input_text += event.unicode

    return players

players = get_players()

for i in range(len(players)):
    get_characters(i)
    print(f"{players[i].name} has chosen {players[i].character.name}")

    
#create the text that tells you what characters do
#ideally, update this to have character cards that tell you what they do when clicked


#test(players[current_player])
time.sleep(2)
screen.fill((background_color))
board = Board(rows, cols) 

screen.fill((background_color))  
#board.render(screen)
pygame.display.flip() 


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    if turn < 45:
        take_turn(players[current_player])
        current_player = (current_player + 1) % len(players)
    else:
        # Game end logic
        print("You have reached the end of the game! Congratulations!")
        winner = max(players, key=lambda p: p.happiness)
        text_surface = font.render(f"{winner.name} wins!", True, (100, 100, 100))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
        running = False

pygame.quit()

#What i have:
#cards in their respective decks, a list of the decks, basic die roll and card draw/shuffle mechanics
#player class for adding effects and happiness and such
#characters

