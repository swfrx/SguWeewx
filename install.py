# installer for the 'SguWeewx' skin
# June 2022, Sally Woolrich

from weecfg.extension import ExtensionInstaller

#-------- extension info -----------

VERSION      = "0.2"
NAME         = 'SguWeewx'
DESCRIPTION  = 'A highly bespoke skin used to interface the SGU weather station with the Pilot\'s Wiki'
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
#                        'HTML_ROOT': 'dokuwiki',
#                        'unit_system': 'metricwx'
                    },
                    'PolarWindPlot': {
                        'skin': 'PolarWindPlot',
                        'enable' : 'True',
#                        'HTML_ROOT': 'media/weather',
#                        'lang': 'en',
#                        'unit_system': 'metricwx'
                    }
                }
            },
            files=[('bin/user', ['bin/user/sguweewx.py', 'bin/user/polarwindplot.py']),
                ('skins/SguWeewx',
                 ['skins/SguWeewx/font/FreeMonoBold.ttf',
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
