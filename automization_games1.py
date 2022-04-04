import pydirectinput 
import pyautogui
import time


print("WELCOME TO AUTO-SCRIPT")
#gotta input all the keys - reminder
keyb_and_mouse_arr = []

sorted_functions = []
sorted_keys = []
keys_in_use = []
keydown_last = []
keyboard_sleep = []

sorted_mouse_func = []
mouse_clicks = []
mouse_x = []
mouse_y = []
mouse_last = []


width, height = pydirectinput.size()
width_percent = width / 100
height_percent = height / 100
#pyautogui functions for keyboard - useful when in comes to storing variables in lists

press = pydirectinput.press
keydown = pydirectinput.keyDown
keyup = pydirectinput.keyUp
breakt = time.sleep

#keyboard functions for mouse 

mouse_move = pydirectinput.moveTo
move_for = pydirectinput.moveRel
right_click = pydirectinput.rightClick
click = pydirectinput.click
drag_to = pyautogui.dragTo

keyboard_functions = [press, keydown, breakt]
mouse_functions = [mouse_move, move_for, right_click, click, drag_to]

def check_is_digit(test_string):
    try: 
        float(test_string)
        return True
    except:
        pass
        


def hold_key_for_time (hold_time, key):
    start = time.time()
    while time.time() - start < hold_time:
        keydown(key)
        keyup(key)


#keyboard function for execution 
def run_script_keyboard(loop):
    print("__________________\n the script will begin in 5 seconds\n please click on the wanted window")
    time.sleep(5)
    num = 0
    count = 0
    sleep_count = 0
    key_count = 0
    while num < loop:
            for g in range(len(sorted_functions)):
                
                if sorted_functions[g] == keydown:
                    hold_key_for_time(keydown_last[count], sorted_keys[key_count])
                    count += 1
                    key_count += 1
                    continue
                
                elif sorted_functions[g] == breakt:
                    time.sleep(keyboard_sleep[sleep_count])
                    sleep_count += 1
                    continue

                sorted_functions[g](sorted_keys[key_count])
                key_count += 1

            count = 0
            key_count = 0
            sleep_count = 0    
            num += 1
            

def run_script_mouse(loop):
    time.sleep(10)
    
    num1 = 0
    click_count = 0
    x_and_y_count = 0
    sleep_count = 0
    while num1 < loop:
        
        for y in range(len(sorted_mouse_func)):
            
            if sorted_mouse_func[y] == mouse_move:
                sorted_mouse_func[y](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent), 1)
                x_and_y_count += 1

            elif sorted_mouse_func[y] == move_for:
                sorted_mouse_func[y](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent), 2)
                x_and_y_count += 1

            elif sorted_mouse_func[y] == right_click:
                sorted_mouse_func[y](int(mouse_x[x_and_y_count-1] * width_percent), int(mouse_y[x_and_y_count-1] * height_percent))
                
            
            elif sorted_mouse_func[y] == click:
                sorted_mouse_func[y]( mouse_clicks[click_count], interval = 0.25)
                click_count += 1
            
            elif sorted_mouse_func[y] == drag_to:
                sorted_mouse_func[y](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent), 0.1, button = "left")
                x_and_y_count += 1
            
            elif sorted_mouse_func[y] == breakt:
                time.sleep(mouse_last[sleep_count])
                sleep_count += 1
            
            else:
                print("error")
        sleep_count = 0
        x_and_y_count = 0
        click_count = 0
        num1 += 1
        
def keyboard_and_mouse_run(loop):
    num4 = 0
    time.sleep(10)
    keyb_count = 0
    key_count = 0
    sleep_count = 0

    x_and_y_count = 0
    click_count = 0
   
    while num4 < loop:
        for ž in range(len(keyb_and_mouse_arr)):
            
            if keyb_and_mouse_arr[ž] == keydown:
                hold_key_for_time(keydown_last[keyb_count], sorted_keys[key_count])
                keyb_count += 1
                key_count += 1
                continue
                
            elif keyb_and_mouse_arr[ž] == breakt:
                time.sleep(keyboard_sleep[sleep_count])
                sleep_count += 1
                continue
            
            elif keyb_and_mouse_arr[ž] ==mouse_move:
                keyb_and_mouse_arr[ž](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent),0)
                x_and_y_count += 1
                continue
            
            elif keyb_and_mouse_arr[ž] == move_for:
                keyb_and_mouse_arr[ž](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent), 0)
                x_and_y_count += 1
                continue
            
            elif keyb_and_mouse_arr[ž] == right_click:
                keyb_and_mouse_arr[ž](int(mouse_x[x_and_y_count-1] * width_percent), int(mouse_y[x_and_y_count-1] * height_percent))
                continue
                
            elif keyb_and_mouse_arr[ž] == click:
                keyb_and_mouse_arr[ž]( mouse_clicks[click_count], interval = 0.25)
                click_count += 1
                continue
            
            elif keyb_and_mouse_arr[ž] == drag_to:
                keyb_and_mouse_arr[ž](int(mouse_x[x_and_y_count] * width_percent), int(mouse_y[x_and_y_count] * height_percent), 0.1, button = "left")
                x_and_y_count += 1
                continue
                
            elif keyb_and_mouse_arr[ž] == press:
                keyb_and_mouse_arr[ž](sorted_keys[key_count])
                key_count += 1
            
            else:
                print("error")
       
        
        click_count = 0
        x_and_y_count = 0

        keyb_count = 0
        key_count = 0
        sleep_count = 0
        num4 += 1
            

              

#functions class - used mainly for better organization
class doin_stuff:

                                                   

    def keyboard_use_in_intervals(self):
        print("you choose keyboard and access to time functions\n -keyboard\n -determine how long each function will last ( keydown - 5 seconds )\n_____________\n any key is available\n")     
        time.sleep(1) 
        num1 = 1
        
        

        print("-----------\n INSTRUCTIONS \n write the name of keys one by one \n you can type numbers, letters enter, space and left, right, up, down keys \n please write the letters in lowercase otherwise the script may not work \n")
        time.sleep(1)
        print("\n if you are asked to input time or set of times - input a number")
        print("________\nif you wrote all the keys type - done \nif you did a mistake and want to start over type - again ")
        #inputing the keys and storing them in list
        val2 = True
        while val2 == True:
            
            want_key = input("input the key you want the script to use: ")
            
            keys_in_use.append(want_key)

                       
            if want_key == "again":
                keys_in_use.clear()
                print("--starting again")
            
            #no unwanted elements in list
            elif "again" in keys_in_use or "done" in keys_in_use or keys_in_use.count(want_key) == 2 :
                del keys_in_use[-1]
            
            if want_key == "done":
                val2 = False   
        
                #prints the list
        print("___________\n the keys you will be using: ")
        
        

        for r in keys_in_use:
            print( num1, r)
            num1 += 1
        
        num1 = 1           

        #prints the list
        
        time.sleep(1)
        print("_____________\n press - pressses a button \n keydown - holds a certain key down \n break - how much time you would like between functions\n if you type keydown you also have to specify the number of seconds you wish to hold down")
        #prints the pydirectinput functions for keyboard
        
        time.sleep(1)        
        print("__________\n input the keys one by one and for each one input the key function\n you can use same keys multiple times \n when you are done type in both - done \n if you made a mistake type - again")
        
        
        
        val3 = True
        while val3 == True:
            
            key  = input("write the key you will use: ")
            key_function = input("write the key function you will use with that key: ")
            
            
            if key == "done" and key_function == "done":
                val3 = False
            
            elif key == "again" and key_function == "again":
                sorted_functions.clear()
                sorted_keys.clear()
                print("start again\n__________")
            
            elif key_function == "press" and key in keys_in_use:
                sorted_keys.append(key)
                sorted_functions.append(keyboard_functions[0])

            elif key_function == "keydown" and key in keys_in_use:
                value8 = True
                while value8 == True:
                   time_last = float(input("write how many seconds you wish it lasts: "))
                   if check_is_digit(time_last) == True:

                      keydown_last.append(time_last)
                      value8 = False
                   else:
                      print("error you did not input a number")

                sorted_keys.append(key)
                sorted_functions.append(keyboard_functions[1])

            
            elif key_function == "break" or key == "break":
                value202 = True
                while value202 == True:
                    time_last = float(input("input how many seconds you would like the function to pause: "))
                    if check_is_digit(time_last) == True:
                        keyboard_sleep.append(time_last)
                        value202 = False
                    
                    else:
                        print("error you did not input a whole number\n____________")
                sorted_functions.append(keyboard_functions[2])
                        
            else:
                print("key or key_function is not in the system... was not listed")
            
            
        
        #asks for times of looping and then executes the run function
        val10 = True
        while val10 == True: 

           num_loops = input("how many times do you wish this sript to loop\ninput a number: ")
           if check_is_digit(num_loops) == True:
                 run_script_keyboard(int(num_loops))
                 val10 = False
           else:
               print("error you did not input a whole number")

        sorted_functions.clear()
        sorted_keys.clear()
        keys_in_use.clear()
        keydown_last.clear()
        keyboard_sleep.clear()
        
    def mouse(self):
        print("______________\nso you decided on mouse - this functions serve mainly for clicking the same spot for a long time or, minimal moving without being time limited")
        time.sleep(1)
        print("INSTRUCTIONS\n input the names of functions you want \n input the number of times you want the script to loop\n_____________")
        print("\n if you are asked to input time or set of times - input a number")
        print("list of mouse functions:\n_________________ \nmouse_move - moves mouse to percentage of screen on x and y axis for example - moves mouse to 20% y axis and 30 percent on x axis\nmove_for - moves mouse relative to position, for example - moves mouse for 20 percent from current position")
        print("right_click - clicks right button on mouse\nclick - clicks the left button on mouse\ndrag_to - holds down a mouse button and drags it acros the screen \nbreak - pauses the script for a certain time")
        time.sleep(1)
        print("\nwhen you are done type - done\n if you made a mistake type - again\n_________________\n______________")

        
        val4 = True
        while val4 == True:
            mouse_func_choice = input("type which functions you want your mouse to use: ")
            

            if mouse_func_choice == "mouse_move": 
                value21 = True
                while value21 == True:

                     x = float(input("write the number of percents you want the mouse to move on the x axis: "))
                     y = float(input("write the number of percents you want the mouse to move on the y axis: "))
                     if check_is_digit(x) == True and check_is_digit(y) == True:
                         value21 =False
                     else:
                         print("you did not input a whole number")
                mouse_x.append(x)
                mouse_y.append(y)
                sorted_mouse_func.append(mouse_functions[0])
            
            elif mouse_func_choice == "move_for":
                value18 = True
                while value18 == True:

                      x1 = float(input("write the number of percents you want the mouse to move on the x axis from current position: "))
                      y1 = float(input("write the number of percents you want the mouse to move on the y axis from current position: "))
                      if check_is_digit(x1) == True and check_is_digit(y1) == True:
                          value18 = False
                      else:
                          print("you did not input a whole number")
                mouse_x.append(x1)
                mouse_y.append(y1)
                sorted_mouse_func.append(mouse_functions[1])
            
            elif mouse_func_choice == "right_click":
                sorted_mouse_func.append(mouse_functions[2])
            
            elif mouse_func_choice == "click":
                value12 = True
                while value12 == True:
                     num_of_clicks = int(input("write the number of times you want the mouse to be clicked: "))
                     if check_is_digit(float(num_of_clicks)) == True:
                        value12 = False
                        mouse_clicks.append(int(num_of_clicks))
                     else:
                         print("error you did not input a whole number")
                sorted_mouse_func.append(mouse_functions[3])
            
            elif mouse_func_choice == "drag_to":
                value13 = True
                while value13 == True:

                      x2 = float(input("write the number of percents on the x axis to which you drag mouse: "))
                      y2 = float(input("write the number of percents on the y axis to which you drag mouse: "))
                      if check_is_digit(x2) == True and check_is_digit(y2) == True:

                         mouse_x.append(x2)
                         mouse_y.append(y2)
                      else:
                          print("you did not input a whole number")
                sorted_mouse_func.append(mouse_functions[4])
            
            elif mouse_func_choice == "done":
                val4 = False
            
            elif mouse_func_choice == "again":
                sorted_mouse_func.clear()     

            elif mouse_func_choice =="break":
                value62 = True
                while value62 == True:
                    time_last = float(input("input how long: "))
                    if check_is_digit(time_last) == True:
                        value62 = False
                    else:
                        print("error")
                    mouse_last.append(time_last)


            else:
                print("function not found or incorrectly typed")
            
                    
        value10 = True
        while value10 == True:

              loop_mouse = int(input("how many times do you want the script to loop: "))
              if check_is_digit(float(loop_mouse)) == True:
                  value10 = False
              else:
                  print("you did not input a whole number")
            
        
        
        
        print("___________\nthe script will start in 10 seconds")
        run_script_mouse(loop_mouse)
        sorted_mouse_func.clear()
        mouse_clicks.clear()
        mouse_x.clear()
        mouse_y.clear()
        mouse_last.clear()

        
    def keyboard_and_mouse(self):
        print("so you decided on keyboard and mouse automatizations")
        print("_______________________")
        time.sleep(1)
        print("INSTRUCTIONS\n input the keyboard functions or mouse functions in the odrer you would like \n set the number of loops \n run the script")
        print("\n if you are asked to input time or set of times - input a number")
        time.sleep(1)
        print("\nkeyboard functions:")
        print("_____________\n press - pressses a button \n keydown - holds a certain key down \n if you type keydown you also have to specify the number of seconds you wish to hold down\n")
        time.sleep(1)
        
        print("list of mouse functions: \n__________________\nmouse_move - moves mouse to percentage of screen on x and y axis for example - moves mouse to 20% y axis and 30 percent on x axis\nmove_for - moves mouse relative to position, for example - moves mouse for 20 percent from current position")
        print("right_click - clicks right button on mouse\nclick - clicks the left button on mouse\ndrag_to - holds down a mouse button and drags it acros the screen ")
        time.sleep(1)
        print("\nwhen you are done type - done\n if you made a mistake type - again\n_________________\n______________")
        value6 = True
        while value6 == True:
            key_or_mouse_function = input("write a keyboard or mouse function: ")
            
            if key_or_mouse_function == "press":
                print("please write the keys in lowercase so that the script can run without errors")
                keyboard_key = input("input a key you want to use with this function: ")
                sorted_keys.append(keyboard_key)
                keyb_and_mouse_arr.append(keyboard_functions[0])
                
            
            elif key_or_mouse_function == "keydown":
                print("please write the keys in lowercase so that the script can run without errors")
                keyboard_key = input("input a key you want to use with this function: ")
                val15 = True
                while val15 == True:
                    key_time = float(input("input how long you want to hold down this key: "))
                    if check_is_digit(key_time) == True:
                        val15 = False
                    else:
                        print("error - you have to input a whole number")
                keydown_last.append(key_time)
                sorted_keys.append(keyboard_key)
                keyb_and_mouse_arr.append(keyboard_functions[1])
                
            
            elif key_or_mouse_function == "mouse_move":
                val69 = True
                while val69 == True:

                  x4 = float(input("write the number of percents you want the mouse to move on the x axis: "))
                  y4 = float(input("write the number of percents you want the mouse to move on the y axis: "))
                  if check_is_digit(x4) == True and check_is_digit(y4) == True:
                      val69 = False
                  else:
                      print("error - you have to input a whole number(decimal number)")
                mouse_x.append(x4)
                mouse_y.append(y4)
                keyb_and_mouse_arr.append(mouse_functions[0])
                
            
            elif key_or_mouse_function == "move_for":
                val42 = True
                while val42 == True:
                  x5 = float(input("write the number of percents you want the mouse to move on the x axis from current position: "))
                  y5 = float(input("write the number of percents you want the mouse to move on the y axis from current position: "))
                  if check_is_digit(x5) == True and check_is_digit(y5) == True:
                      val42 = False
                  else:
                      print("error - you have to input a number")
                mouse_x.append(x5)
                mouse_y.append(y5)
                keyb_and_mouse_arr.append(mouse_functions[1])
                
            
            elif key_or_mouse_function == "right_click":
                keyb_and_mouse_arr.append(mouse_functions[2])
                
            
            elif key_or_mouse_function == "click":
                val_doggy_style = True
                while val_doggy_style == True:

                  num_of_clicks2 = int(input("write the number of times you want the mouse to be clicked: "))
                  if check_is_digit(float(num_of_clicks2)) == True:
                      val_doggy_style = False
                  else:
                      print("error - you have to input a whole number")
                mouse_clicks.append(num_of_clicks2)
                keyb_and_mouse_arr.append(mouse_functions[3])
                

            elif key_or_mouse_function == "drag_to":
                val_delyy = True
                while val_delyy == True:
                  x7 = float(input("write the number of percents on the x axis to which you drag mouse: "))
                  y7 = float(input("write the number of percents on the y axis to which you drag mouse: "))
                  if check_is_digit(x7) == True and check_is_digit(y7):
                      val_delyy = False
                  else:
                      print("error - you have to input a number")
               
                    
                mouse_x.append(x7)
                mouse_y.append(y7)
                keyb_and_mouse_arr.append(mouse_functions[4])
                
            
            elif key_or_mouse_function == "done":
                value6 = False
            
            elif key_or_mouse_function =="break":
                val_luka = True
                while val_luka == True:

                  time_last1 = int(input("how much time do you want the script to pause: "))
                  if check_is_digit(float(time_last1)) == True:
                      val_luka = False
                  else:
                      print("error - you have to input a whole number")

                keyb_and_mouse_arr.append(keyboard_functions[2])
                keyboard_sleep.append(time_last1)
            
            elif key_or_mouse_function == "again":
                sorted_functions.clear()
                sorted_keys.clear()

                keydown_last.clear()
                keyboard_sleep.clear()

                sorted_mouse_func.clear()
                mouse_clicks.clear()
                mouse_x.clear()
                mouse_y.clear()
            
            
            
        
        value7 = True
        while value7 == True:    
          loop3 = int(input("how many times would you like to loop this script: "))
          if check_is_digit(float(loop3)) == True:

             print("the script will start in 10 seconds")
             keyboard_and_mouse_run(loop3)
             value7 = False
        
          else:
              print("error you have to input a whole number")
           
     
#main function - works as direction guide
def terminal():
  value = True
  while value == True :

      features = [ "keyboard_time", "mouse", "keyboard_mouse" ]   

      dict_with_features = {
          "mouse" : "for simple mouse functions, for example - clicking the same spot for a long time \n _____________",
          "keyboard_time" : "for keyboard functions that involve time, for example - hold key down for 10 seconds, press key1, hold key3 for 20 seconds \n _______________",
          "keyboard_mouse" : "for simple keyboard and mouse automatizations for example - press right, left keydown 10 seconds, move mouse 20% to the right"
          }  
      
      print("if you need help type - help \nif you want a list of options(features) type - options \nif you want explanation on functions type - explaine")
        
      dr = input("---------------\n<< ")
      
      a = 1
      č = 1

      if dr == 'help' :
        print("_________\n_____________")

        print("follow the guide: \n 1. select option of automating - script \n 2. Follow the instructions \n 3. run the script \n")                 
          
      elif dr == 'options':
        print("__________\n_________")
        for n in features:
            print(a, n)
            a += 1 
        
        
          #choices for various functions
        choice = input("write the name of the feature you want to try: ")  
        don = doin_stuff()

        if choice == "keyboard_time":
            don.keyboard_use_in_intervals()
            
        elif choice == "mouse":
            don.mouse()

        elif choice == "keyboard_mouse":
            don.keyboard_and_mouse()
          
        else:
            print("error - matching function not found")
      
         
      elif dr == "explaine" :
          for š in features:
            print(č, š)
            č += 1 
          dict_choice = input("write the name of the function you want brief explanation for: ")
          
          print("____________\n",dict_with_features[dict_choice])

terminal()


     
   

      
