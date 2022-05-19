
import numpy as np
import time

led_array = np.array([10, 32, 54, 76, 98, 120])
# randomly selected without replacement... basically just shuffling..
led_rand_array = np.random.choice(led_array,len(led_array), replace=False)
led = 0
for led_num in led_rand_array:  ## loop through the new random values//
    ## first would reference the led_num_on... and then call that and the we will set it to be on
    # 10, 32, 54, 76, 98, 120
    print(led_num)
    # added a 5 seconds
    # slept based on ra
    time.sleep(5)
