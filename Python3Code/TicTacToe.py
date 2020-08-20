

#defining Functions

def update_turn(current_turn):
    return current_turn + 1


def update_data(turn, selected_list_position, display_data):
    #print 'Current turn: ',  turn
    if turn %2 == 0:
        player_token ='X'
    else:
        player_token ='O'
    
    if turn == 0:
        pass
    else:
        #print 'attempting to update master list'
        display_data[selected_list_position] = player_token
    #print  display_data   
    return display_data

def display_board(display_data):
    list1 = display_data[0]+' | '+display_data[1]+' | '+display_data[2]
    list2 = display_data[3]+' | '+display_data[4]+' | '+display_data[5]
    list3 = display_data[6]+' | '+display_data[7]+' | '+display_data[8]
    print list1
    print '---------'
    print list2
    print '---------'
    print list3
    
    
#def player_input(display_data,turn):
def player_input(display_data):
    valid_numbers = ['1','2','3','4','5','6','7','8','9']   
    valid = False
    while valid == False:  
        player_choice = raw_input("Make a choice Bozo (1-9)")
        for char in valid_numbers :
            if player_choice == char:
                list_position = int(player_choice) -1
                if  display_data[list_position] == ' ':
                    print 'Thank you'
                    valid = True
                else:
                    print 'that selection is taken, try again'
            else:
                pass
        if valid == False:
            print 'invalid - Please enter a number between 1-9'
    return list_position

def game_won_check(display_data, player_token):
    #this is the main function that gets run
    result = False
    turn_data_as_binary = get_players_selections(display_data, player_token)
    result = result + evaluate_line(turn_data_as_binary,0,1,2)
    result = result + evaluate_line(turn_data_as_binary,3,4,5)
    result = result + evaluate_line(turn_data_as_binary,6,7,8)
    result = result + evaluate_line(turn_data_as_binary,0,3,6)
    result = result + evaluate_line(turn_data_as_binary,1,4,7)
    result = result + evaluate_line(turn_data_as_binary,2,5,8)
    result = result + evaluate_line(turn_data_as_binary,0,4,8)
    result = result + evaluate_line(turn_data_as_binary,2,4,6)                      
    return result

def get_players_selections(display_data,player_token):
    #Create a list with just ones and zeros per player ('X' or 'O')
    result = [0,0,0,0,0,0,0,0,0]
    position_number = 0
    
    for item in display_data:
        if item == player_token:
            #print position_number
            result[position_number] = 1
            position_number = position_number + 1
        else:
            #print position_number
            result[position_number] = 0
            position_number = position_number + 1
    #print result
    return result

def evaluate_line(players_turn_data,pos1,pos2,pos3):
    result = 0
    evalution_line = []
    evalution_line = players_turn_data[pos1]+players_turn_data[pos2]+players_turn_data[pos3]
    if evalution_line == 3:
        result = 1
    else:
        #result = False
        pass
    return result
        


# set starting variables
#Initialize variables

turn = 0
user_input = 0
list_position = 0
game_end = False
display_data = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# update_display_data(UserInputNumber, turn)
display_data = update_data(turn, list_position,display_data)
display_board(display_data)

# THIS IS THE LOOP
while game_end == False:
    selected_list_position = player_input(display_data)
    turn = update_turn(turn)
    new_display_data = update_data(turn, selected_list_position, display_data)
    display_board(new_display_data)
    token_x_won = game_won_check(display_data,'X')
    if token_x_won == 1:
        print 'X wins'
        game_end = True
    token_o_won = game_won_check(display_data,'O')
    if token_o_won == 1:
        print 'O wins'
        game_end = True
    #print token_x_won
print 'Game end'
