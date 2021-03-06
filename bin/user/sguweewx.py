"""
Extension for the SguWeewx skin
This extension creates a DokuWiki format table for the NOAA year & month summaries
Sally Woolrich, June 2022
"""

import os
import glob
import weewx

# Logging
import weeutil.logger
import logging

log = logging.getLogger(__name__)

def logdbg(msg):
    log.debug(msg)

def loginf(msg):
    log.info(msg)

def logerr(msg):
    log.error(msg)

from weewx.cheetahgenerator import SearchList


# Print version in syslog for easier troubleshooting
VERSION = "1.0"
loginf("version %s" % VERSION)


class getData(SearchList):
    def __init__(self, generator):
        SearchList.__init__(self, generator)

# Function to return DokuWiki-style table cell plus delimiter
    @staticmethod
    def do_link( noaa_namespace, file, text ):
        if os.path.isfile(file):
            return '[[' +  noaa_namespace  + file + '|' + text + ']]|'
        else:
            return '  -  |'

    def get_extension_list(self, timespan, db_lookup):
        """
        Return a string that contains a DokuWiki table containing links
        to the NOAA Yearly & Monthly summaries

        Variables:
            noaa_files		where the NOAA summary files are
            noaa_namespace	the DokuWiki namespace they will be in
            noaaa_year		the pattern to match for the names of the year summary files
                month file namess are assuming to have '-mm' ammended to the year number

            these all have defaults but can be overriden in [Extras][sguweewx]
        """

# Debugging?
        weewx.debug = int(self.generator.config_dict.get('debug', 0))

        noaa_files = self.generator.skin_dict['Extras'].get(
            'sguweewx.noaa_files', '/home/weewx/public_html/dokuwiki/pages/weather/noaa' )
        noaa_namespace = self.generator.skin_dict['Extras'].get(
            'sguweewx.noaa_namespace', 'weather:noaa:')
        noaa_year = self.generator.skin_dict['Extras'].get(
            'sguweewx.noaa_year', 'noaa-2[0-9][0-9][0-9]' )

# Month number & short name
        months=[('01','Jan'),('02','Feb'),('03','Mar'),('04','Apr'),('05','May'),('06','Jun'),('07','Jul'),('08','Aug'),('09','Sep'),('10','Oct'),('11','Nov'),('12','Dec')]

# Directory with NOAA files becomes cwd
# If this is a new installation the directory might not exist
# so skip the following
        try:
            os.chdir( noaa_files )
        
# Get names of the year files
            years =  glob.glob( noaa_year )

            if len(years) == 0:
                noaa_table = 'No NOAH year files found ' + noaa_files
            else:

# We have to return the table as just one string variable which will be built
# row by row using the correct newline for the system
                noaa_table = ''
                row = ''
        
# process years from current to oldest
            for year in sorted(years, reverse = True):
                    yyyy = year.split('.')[0]
                    year_name = yyyy.split('-')[1] 
        
# Start the table output for this year
                    row = self.do_link( noaa_namespace, year, year_name )
                    row = "|" + row
            
# Append the link to each month's file plus the short month name,
# or a cell with just a hyphen if the month file doesn't exist
                    for month in months:
                        month_file = yyyy + '-' + month[0]
                        month_name = month[1]
                        row = row + self.do_link ( noaa_namespace, month_file, month_name )
    
                    noaa_table = noaa_table + row + os.linesep
        except:
            noaa_table = 'NOAA directory ' + noaa_files + ' does not exist'

# all years processed - finished - build the search list extension
        search_list_extension = {
            'noaa_table'    : noaa_table,
            'noaa_files'    : noaa_files,
            'noaa_namespace': noaa_namespace,
            'noaa_year'     : noaa_year
            }

        # Finally, return our extension as a list:
        return [search_list_extension]
        
