#=======================================================================
#                        General Documentation
""" Stores information related to income breakdowns between cities.
"""

#-----------------------------------------------------------------------
#                       Additional Documentation
#
# Modification History:
# - 25 May, 2019  Original by Callie Bianco, UW Bothell.
#
# Notes:
# - Written for Python 3.7.2.
# - Part of larger I-405 Simulation
#
#=======================================================================
# https://datausa.io/profile/geo/everett-wa/#economy
# https://www.pewresearch.org/fact-tank/2018/09/06/
#       are-you-in-the-american-middle-class/
# income and city data based on 2016 data
"""
    @author CallieBianco
"""
import numpy as np

class Income_Data(object):
    """ Data to use for car income calculations
  
      Data fields:
          on_ramps_south = Entry points onto I-405 South and associated cities
          on_ramps_north = Entry points onto I-405 North and associated cities
          
      Constraints:
          * Our model is only going to analyze Lynnwood to Bothell and Bothell 
            to Lynnwood.
          * Any entry points south of Bothell will be ignored in on_ramps_south
    """
    def __init__(self):
        """ Initializes properties of Income Data
        """
      # ramp entry data will be used to determine income for a car      
        self.on_ramps_south = {'I5 North': 'Everett', 'I5 South1': 'Lynnwood', \
                               'I5 South2': 'Mountlake Terrace', 'Canyon Park':\
                               'Bothell', 'WA_522': 'Bothell'}                      
        self.on_ramps_north = {'Bellevue 4th St': 'Bellevue', 'Redmond Way':  \
                               'Redmond', 'Central Way': 'Kirkland', 'WA 527': \
                               'Bothell'}
    
        # income breakdown follows the wealth distribution for Washington State.
        # low-upper values will differ based on city data.    
        # income medians for average household (Pew Research): 
        #   low: <$40000
        #   mid low: $40k-$70k
        #   mid: $70k-$100k
        #   mid upper: $100k-$130k
        #   upper: <$130k
        # income breakdowns given in percentages
        self.income_breakdown = {'low': 9.89+11.1+13+12.2, 'low mid': 10.2+8.52+ \
                                7.34,'mid': 5.64+4.36+2.97, 'upper mid': 3.18+ \
                                1.83 +1.99, 'upper': 1.1+.872+1.09+.628+.506+.469+\
                                .141+2.93}
        
        self.everett_income = {'low': [22800, 39300], 'low mid': [39301, 51000], \
                            'mid': [51001, 68400], 'upper mid': [68401, 94500], \
                            'upper': [94501, 124000]}
                        
        self.lynnwood_income = {'low': [43400, 45700], 'low mid': [45701, 48700], \
                                'mid': [48701, 61200], 'upper mid': [61201, 64400],\
                                'upper': [64401, 67100]}
                                
        self.mterrace_income = {'low': [32100, 40400], 'low mid': [40401, 56500], \
                                'mid': [56501, 65700], 'upper mid': [65701, 71300],\
                                'upper': [71301, 75700]}
                                
        self.bothell_income = {'low': [59600, 70000], 'low mid': [70001, 80800], \
                            'mid': [80801, 92200], 'upper mid': [92201, 110000],\
                            'upper': [110001, 136000]}
                            
        self.bellevue_income = {'low': [45800, 80800], 'low mid': [80801, 98400], \
                                'mid': [98401, 117000], \
                                'upper mid': [117001, 143000],\
                                'upper': [143001, 160000]}
                                
        self.redmond_income = {'low': [68600, 94800], 'low mid': [94801, 115000], \
                                'mid': [115001, 147000], \
                                'upper mid': [147001, 200000],\
                                'upper': [200001, 209000]}
                                
        self.kirkland_income = {'low': [58600, 78400], 'low mid': [78401, 90900], \
                                'mid': [90901, 107000], \
                                'upper mid': [107001, 120000], \
                                'upper': [120001, 132000]}
                                          
    def ev_inc(self, iclass):
        """ Income if a driver lives in Everett  
            Parameters:
                iclass: a driver's income class
        """
        irange = self.everett_income[iclass] 
        return np.random.randint(irange[0], irange[1])

    def lynn_inc(self, iclass):
        """ Income if a driver lives in Lynnwood
            Parameters:
                iclass: a driver's income class
        """
        irange = self.lynnwood_income[iclass] 
        return np.random.randint(irange[0], irange[1])

    def mlt_inc(self, iclass):
        """ Income if a driver lives in Mountlake Terrace
            Parameters:
                iclass: a driver's income class
        """
        irange = self.mterrace_income[iclass] 
        return np.random.randint(irange[0], irange[1])
        
    def bot_inc(self, iclass):
        """ Income if a driver lives in Bothell
            Parameters:
                iclass: a driver's income class
        """
        irange = self.bothell_income[iclass] 
        return np.random.randint(irange[0], irange[1])
        
    def bell_inc(self, iclass):
        """ Income if a driver lives in Bellevue
            Parameters:
                iclass: a driver's income class
        """
        irange = self.bellevue_income[iclass] 
        return np.random.randint(irange[0], irange[1])
        
    def red_inc(self, iclass):
        """ Income if a driver lives in Redmond
            Parameters:
                iclass: a driver's income class
        """
        irange = self.redmond_income[iclass] 
        return np.random.randint(irange[0], irange[1])
        
    def kirk_inc(self, iclass):
        """ Income if a driver lives in Kirkland
            Parameters:
                iclass: a driver's income class
        """
        irange = self.kirkland_income[iclass] 
        return np.random.randint(irange[0], irange[1])
        
