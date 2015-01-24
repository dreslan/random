############################################################################
# Number of days between 2 dates
############################################################################
### this program takes 2 days in the format: mm:dd:yyyy, and returns the ###
### number of days between the two days, not including the end date      ###
### leap years are taken into consideration                              ###
############################################################################
### this code is working as of 03:14:2014                                ###
############################################################################

def days_in_feb(year):
  if year % 400 == 0:
    return 29
  elif year % 100 == 0:
    return 28
  elif year % 4 == 0:
    return 29
  else:
    return 28

# no error checking built in, so type the date correctly!
def get_date(s):
  return int(s[0:2]), int(s[3:5]), int(s[6:])

def days_elapsed(start_date, end_date):
  # once I learn how, the days in each month will be defined at the beginning as constants
  days_in_jan = 31
  # days_in_feb calculated during execution
  days_in_mar = 31
  days_in_apr = 30
  days_in_may = 31
  days_in_jun = 30
  days_in_jul = 31
  days_in_aug = 31
  days_in_sep = 30
  days_in_oct = 31
  days_in_nov = 30
  days_in_dec = 31
  
  current_month, current_day, current_year = get_date(start_date)
  end_month, end_day, end_year = get_date(end_date)
  
  total_days = 0
  
  while (current_month != end_month) or (current_day != end_day) or (current_year != end_year):
    if current_month == 1:
      if current_day < days_in_jan:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 2:
      if current_day < days_in_feb(current_year):
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 3:
       if current_day < days_in_mar:
         current_day = current_day + 1
       else:
         current_month = current_month + 1
         current_day = 1
       total_days = total_days + 1 
    elif current_month == 4:
      if current_day < days_in_apr:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 5:
      if current_day < days_in_may:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 6:
      if current_day < days_in_jun:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 7:
      if current_day < days_in_jul:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 8:
      if current_day < days_in_aug:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 9:
      if current_day < days_in_sep:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 10:
      if current_day < days_in_oct:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 11:
      if current_day < days_in_nov:
        current_day = current_day + 1
      else:
        current_month = current_month + 1
        current_day = 1
      total_days = total_days + 1
    elif current_month == 12:
      if current_day < days_in_dec:
        current_day = current_day + 1
      else:
        current_year = current_year + 1
        current_month = 1
        current_day = 1
      total_days = total_days + 1
    else:
      return "Error"
  return total_days