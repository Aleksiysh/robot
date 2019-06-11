#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    N=0
    move_right()

    while True:
        for i in range(N):
            if wall_is_on_the_right():
                return 
            else:
                move_right() 
        fill_cell()
        N+=1        
              





if __name__ == '__main__':
    run_tasks()
