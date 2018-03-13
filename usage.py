dte = #date to be compared with now() date
t_flag = ['s'] # default flag
p_flag=[False] # checks if plural value or not
time_check=timediff_custom(dte,t_flag,p_flag) # returns difference and changes t_flag
context = {}
if t_flag[0] == 's':
    if p_flag[0] == True:
        context['updated']="Updated {} seconds ago.".format(time_check)
    else:
        context['updated']="Updated {} second ago.".format(time_check)
elif t_flag[0] == 'm':
    if p_flag[0] == True:
        context['updated']="Updated {} minutes ago.".format(time_check)
    else:
        context['updated']="Updated {} minute ago.".format(time_check)
elif t_flag[0] == 'h':
    if p_flag[0] == True:
        context['updated']="Updated {} hours ago.".format(time_check)
    else:
        context['updated']="Updated {} hour ago.".format(time_check)
elif t_flag[0] == 'd':
    if p_flag[0] == True:
        context['updated']="Updated {} days ago.".format(time_check)
    else:
        context['updated']="Updated {} day ago.".format(time_check)
 # use this context  
