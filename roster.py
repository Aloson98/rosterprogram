"""
Welcome to the new roster version, where all the updated knowledge will be implied to improve the previous versions
                                By Aloson98
"""

import numpy as np
import pandas as pd

from rosterfeed import *

class Roster():
    def __init__(self, staff, special_names):
        self.staff = [staff.title() for staff in staff]
        self.special_names = special_names
        self.weekdays = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    
    def roster(self):
        #Method that innitite roster dataframe
        roster_df = pd.DataFrame(columns=self.weekdays, index=self.staff)
        
        for k,v in self.special_names.items():
            roster_df.loc[k.title(), "Mon"] = v
        self.roster_df = roster_df
        return self.roster_df
    
    def sd_check(self):
        #Methid that lookup for the sleeping days, then provide Dayoff next day to it.
        self.roster()
        sd_position = self.roster_df[self.roster_df=="SD"].stack().index
        for item in sd_position:
            sd_index = self.weekdays.index(item[1])
            do_index = sd_index + 1
            staff = item[0]
            
            if do_index < 7:
                self.roster_df.loc[staff, self.weekdays[do_index]] = 'DO'
        return self.roster_df
    
    def en_check(self):
        #Method that look for Evening night shift then provide Sleeping day and day off the next coming days
        en_position = self.roster_df[self.roster_df=="EN"].stack().index
        for item in en_position:
            en_index = self.weekdays.index(item[1])
            sd_index = en_index + 1
            do_index = en_index + 2
            staff = item[0]
            
            if sd_index < 7:
                self.roster_df.loc[staff, self.weekdays[sd_index]] = 'SD'
            
            if do_index < 7:
                self.roster_df.loc[staff, self.weekdays[do_index]] = 'DO'
        return self.roster_df
    
    def night_shift(self):
        #Method that provide required night shift duty to staff
        required_en = (len(self.staff) * 1) // 5
        print(required_en)
        trial = 1000
        weekly_night = []
        for index, row in self.roster_df.transpose().iterrows():
            filled = list(self.roster_df[row=="EN"].index.union(self.roster_df[row=="SD"].index).union(self.roster_df[row=="DO"].index))
            en_filled = list(self.roster_df[row=="EN"].index)
            new_filling = []
            
            while len(new_filling) < required_en and trial > 0:
                y = np.random.choice(self.staff)
                if y not in filled and y not in weekly_night:
                    self.roster_df.loc[y, index] = "EN"
                    new_filling.append(y)
                    weekly_night.append(y)
                trial -= 1
            self.en_check()
        return self.roster_df
    
    def morning_shift(self):
        #Method that provide required morning shift for each day of the week
        required_m = (len(staff) * 4) // 15
        trial = 1000
        
        for index, row in self.roster_df.transpose().iterrows():
            filled = list(self.roster_df[row=="EN"].index.union(self.roster_df[row=="SD"].index).union(self.roster_df[row=="DO"].index))
            morning_duties =[]
            
            while len(morning_duties) < required_m and trial > 0:
                y = np.random.choice(self.staff)
                if y not in morning_duties and y not in filled:
                    self.roster_df.loc[y, index] = "M"
                    morning_duties.append(y)
                    trial -= 1
        print(self.roster_df)
        return self.roster_df
    
    def do_check(self):
        #Method that insure every staff has two days for resting each week
        #do_indices = [self.roster_df[self.roster_df=="DO"].stack().index]
        
        for index, row in self.roster_df.iterrows():
            do_indices = list(row[row=="DO"].index)
            loop = 500
            
            while len(do_indices) < 2 and loop > 0:
                filled_spaces = list(row[row=="EN"].index.union(row[row=="SD"].index).union(row[row=="DO"].index.union(row[row=="M"].index)))
                items = [item for item in self.weekdays if item not in filled_spaces]
                if items:
                    x = np.random.choice(items)
                    self.roster_df.loc[index, x] = "DO"
                loop -= 1
        print(self.roster_df)
        
    def extra_duties(self):
        #Method that check for the incomplete requirements and provide extra duties to few workers
        pass


instance = Roster(staff, special_names)
instance.sd_check()
instance.night_shift()
instance.morning_shift()
instance.do_check()