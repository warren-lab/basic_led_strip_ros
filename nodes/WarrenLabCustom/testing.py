
import numpy as np

led_list = np.array([10, 32, 54, 76, 98, 120])
it_val = 1
led = 0
while it_val <= len(led_list): ## loop through 6 times..
    led_num = np.random.choice(led_list, replace = False)
    # delete the value that was developed...
    print(np.where(led_list == led_num))
   # led_list.pop()
    
    ## first would reference the led_num_on... and then call that and the we will set it to be on
    # 10, 32, 54, 76, 98, 120
    led = led_num
    print(led)
    # added a 5 seconds
    # slept based on rate
    # after iteration go to the next one..
    ## add 22...
    #led_num_on += increase_val
    ## add 1
    #print(it_val) 
    it_val += 1
