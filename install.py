# installer for the 'SguWeewx' skin
# February 2023, Sally Woolrich

from weecfg.extension import ExtensionInstaller

#-------- extension info -----------

VERSION      = "2.2"
NAME         = 'SguWeewx'
DESCRIPTION  = 'A bespoke skin used to interface the Scottish Gliding Center weather station with the Pilot\'s Wiki'
AUTHOR       = "Sally Woolrich"
AUTHOR_EMAIL = "https://github.com/swfrx/sguweewx"

#-------- main loader -----------

def loader():
    return SguWeewxInstaller()

class SguWeewxInstaller(ExtensionInstaller):
    def __init__(self):
        super(SguWeewxInstaller, self).__init__(
            version=VERSION,
            name=NAME,
            description=DESCRIPTION,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            config={
                'StdReport': {
                    'SguWeewxReport': {
                        'skin': 'SguWeewx',
                        'enable' : 'True',
                        'lang': 'en',
                        HTML_ROOT=/var/www/html/weewx/dokuwiki,
                    },
                    'PolarWindPlot': {
                        'skin': 'PolarWindPlot',
                        'enable' : 'True',
                        HTML_ROOT=/var/www/html/weewx/dokuwiki,
                    },
                    'Defaults': {
                        'Units': {
                            'Groups': {
                                'group_altitude': 'meter',
                                'group_pressure': 'hPa',
                                'group_rain': 'mm',
                                'group_rainrate': 'mm_per_hour',
                                'group_temperature': 'degree_C',
                                'group_speed': 'knot',
                                'group_speed2': 'knot2',
                                'unused': 'unused',
                            },
                        },
                    },
                },
            },
            files=[('bin/user', ['bin/user/sguweewx.py', 'bin/user/polarwindplot.py']),
                ('skins/SguWeewx',
                 ['skins/SguWeewx/font/FreeMonoBold.ttf',
                  'skins/SguWeewx/font/OpenSans-Regular.ttf',
                  'skins/SguWeewx/font/OpenSans-Bold.ttf',
                  'skins/SguWeewx/lang/en.conf',
                  'skins/SguWeewx/dokuwiki/pages/weather/noaa/noaa-YYYY.txt.tmpl',
                  'skins/SguWeewx/dokuwiki/pages/weather/noaa/noaa-YYYY-MM.txt.tmpl',
                  'skins/SguWeewx/dokuwiki/pages/weather/weather_stats_incl.txt.tmpl',
                  'skins/SguWeewx/dokuwiki/sguweewx.html.tmpl',
                  'skins/SguWeewx/skin.conf',
                  ]),
                ('skins/PolarWindPlot',
                 ['skins/PolarWindPlot/font/OpenSans-Bold.ttf',
                  'skins/PolarWindPlot/skin.conf',]),
            ]
        )
