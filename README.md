# SguWeewx
Bespoke skin to produce files &amp; images from WeeWx to go into the SGU Pilot's Wiki.  

The file & image names, and paths, are all specific to the Weather Stations page 
in the SGU Pilot's Wiki.  See https://pilots.scottishglidingcentre.co.uk/weather/weather_station.

The skin can be downloaded from...  and is installed in the usual way with 'wee_extension'.  

No configuration should be required.  The skin assumes that:  
  * Weewx is installed with setup.py into ``/home/weewx``
  * This skin places it's output in ``public_html/dokuwiki``
  * NOAA yearly & monthly summaries are generated in ``pages/weather/noaa``  
  * The correct namespace for the NOAA files in DokuWiki is ``weather:noaa:``  
  * The name format for NOAA yearly summaries is ``noaa-2[0-9][0-9][0-9].txt``
  
This skin produces the pages:  
  * pages/weather/weather_stats_incl.txt  
  * pages/weather/noaa/noaa-YYYY.txt.tmpl  
  * pages/weather/noaa/noaa-YYYY-MM.txt.tmpl  
  * sguweewx.html  
  
And in media/weather, it creates the PNG files:  
   * daybarometer-sgu & daybarometer-sgu-big 
   * dayrain-sgu & dayrain-sgu-big
   * daytempdew-sgu & daytempdew-sgu-big
   * daywind-sgu & daywind-sgu-big  
   * dayrose & dayspiral
 
The font - FreeMonoBold.ttf - used in the charts is included in the skin. 

The WindRose files are generated by the skin PolarWindPlotDemo  https://github.com/gjr80/weewx-polarwindplot which is a separate install.  Permission to include this was kindly granted by the author, who also gave a lot of help along the way.
