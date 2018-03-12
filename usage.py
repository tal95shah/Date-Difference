dte = #date to be compared with now() date
t_flag = ['s'] # default flag 
time_check=timediff_custom(dte,t_flag) # returns difference and changes t_flag
if t_flag[0] == 's':
    retVal="Updated {} seconds ago.".format(time_check)
elif t_flag[0] == 'm':
    retVal="Updated {} minutes ago.".format(time_check)
elif t_flag[0] == 'h':
    retVal="Updated {} hours ago.".format(time_check)
elif t_flag[0] == 'd':
    retVal="Updated {} days ago.".format(time_check)
#return retVal