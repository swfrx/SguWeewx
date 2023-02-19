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
VERSION = "2.0"
loginf("sguweewx.py Version %s" % VERSION)


class getData(SearchList):
    def __init__(self, generator):
        SearchList.__init__(self, generator)

# Function to return DokuWiki-style table cell plus delimiter
# Needs to strip '.txt' from filename
    @staticmethod
    def do_link( noaa_namespace, file, text ):
        if os.path.isfile(file):
            link = os.path.splitext( file )[0]
            return '[[' + noaa_namespace + link + '|' + text + ']]|'
        else:
            return '  -  |'

    def get_extension_list(self, timespan, db_lookup):
        """
        Return a string that contains a DokuWiki table containing links
        to the NOAA Yearly & Monthly summaries
        """

# Debugging?
        weewx.debug = int(self.generator.config_dict.get('debug', 0))

        noaa_namespace = self.generator.skin_dict['Extras'].get(
            'sguweewx.noaa_namespace', 'weather:noaa:')
        noaa_year = self.generator.skin_dict['Extras'].get(
            'sguweewx.noaa_year', 'noaa-2[0-9][0-9][0-9].txt' )

# Month number & short name
        months=[('01','Jan'),('02','Feb'),('03','Mar'),('04','Apr'),('05','May'),('06','Jun'),('07','Jul'),('08','Aug'),('09','Sep'),('10','Oct'),('11','Nov'),('12','Dec')]

# Find the right HTML ROOT
        if "HTML_ROOT" in self.generator.skin_dict:
            html_root = os.path.join(
                self.generator.config_dict["WEEWX_ROOT"],
                self.generator.skin_dict["HTML_ROOT"],
            )
        else:
            html_root = os.path.join(
                self.generator.config_dict["WEEWX_ROOT"],
                self.generator.config_dict["StdReport"]["HTML_ROOT"],
            )

        noaa_directory = os.path.join( html_root , "dokuwiki", "pages", "weather", "noaa" )
        loginf("noaa_directory = %s" % noaa_directory)

# Directory with NOAA files becomes cwd
# If this is a new installation the directory might not exist
# so skip the following
        try:
            os.chdir( noaa_directory )

# Get names of the year files
            years =  glob.glob( noaa_year )

            if len(years) == 0:
                noaa_table = 'No NOAH year files found in ' + noaa_directory
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
                        month_file = yyyy + '-' + month[0] + '.txt'
                        month_name = month[1]
                        row = row + self.do_link ( noaa_namespace, month_file, month_name )

                    noaa_table = noaa_table + row + os.linesep
        except:
            noaa_table = 'NOAA directory ' + noaa_directory + ' does not exist'

# all years processed - finished - build the search list extension
        search_list_extension = {
            'noaa_table'     : noaa_table,
            'noaa_directory' : noaa_directory,
            'noaa_namespace' : noaa_namespace,
            'noaa_year'      : noaa_year
            }

        # Finally, return our extension as a list:
        return [search_list_extension]
