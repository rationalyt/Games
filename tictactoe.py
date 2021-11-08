a = [7,8,9]
b = [4,5,6]
c = [1,2,3]


def display_board():
    for x in a:
        print("{0}    ".format(x),end=" ")
    print("\n")
    for x in b:
        print("{0}    ".format(x),end=" ")
    print("\n")
    for x in c:
        print("{0}    ".format(x),end=" ")
    print("\n")
    

def check_rows():
    if (a[0] == a[1] and a[1]==a[2]):
        return True
    elif (b[0]==b[1] and b[1]==b[2]):
        return True
    elif (c[0]==c[1] and c[1]==c[2]):
        return True
    else:
        return False

def check_cols():

    if(a[0]==b[0] and b[0]==c[0]):
        return True
    elif(a[1]==b[1] and b[1]==c[1]):
        return True
    elif(a[2]==b[2] and b[2]==c[2]):
        return True
    else:
        return False

def check_diag():

    if a[0] == b[1] and b[1] == c[2]:
        return True
    elif a[2] == b[1] and b[1] == c[0]:
        return True
    else:
        return False

def check_space():
    for x in a:
        if isinstance(x,int) == True:
            return False
    for x in b:
        if isinstance(x,int) == True:
            return False
    for x in c:
        if isinstance(x,int) == True:
            return False
    return True

def check_game_on(input,coin):
    if input in a:
        a[a.index(input)] = coin
    if input in b:
        b[b.index(input)] = coin
    if input in c:
        c[c.index(input)] = coin
    game_check = check_rows()
    if game_check == False:
     game_check = check_cols()
    if game_check == False:
     game_check = check_diag()
    if game_check == True:
        return "FalseWin"
    else:    
        if(check_space() == False):
            return "True"
        else:
            return "FalseDraw"
 

def main():
    game_on = "True"
    print("")
    while game_on == "True":
     display_board()
     input1_check = False
     while input1_check == False:
      print("Player 1 input:")
      input1 = int(input())
      if input1 not in range(1,10):
          print("Invalid value")
          continue
      else:
          input1_check = True
          game_on = check_game_on(input1,'X')
     if game_on=="True":
         display_board()
         print("Player 2 input:")
         input2_check = False
         while input2_check == False:
          input_2 = int(input())
          if input_2 not in range(1,10):
           print("Invalid value")
           continue
          else:
           input2_check = True
           game_on = check_game_on(input_2,'O')
           if game_on=="FalseWin":
               display_board()
               print("Player 2 Won")
               break
           elif game_on=="FalseDraw":
               display_board()
               print("Its a draw")
               break
     elif game_on=="FalseWin":
         display_board()
         print("Player 1 Won")
         break
     elif game_on=="FalseDraw":
         display_board()
         print("Its a Draw")
         break

if __name__ == "__main__":
    main()
    
    



    