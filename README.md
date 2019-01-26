# weatherpatterns
A small processing project to make pretty pictures from the current weather

To use weatherpatterns, you'll need to get set up Processing. You can install processing [here](https://processing.org/download/?processing). Getting Python mode for Processing is easy! A nice tutorial for it is [here](https://github.com/arocho/generative-art-workshop).

Edit the globals at the top of the file to match your specific parameters:

`CANVAS_HEIGHT = y`

`CANVAS_WIDTH = x`

`CITY_STRING = your_city`

`FILENAME = filename`

For the [OpenWeatherMap](https://openweathermap.org/api) API to work correctly, your city 
name has to be in the format `city,code` where code is the [ISO 3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

Otherwise, just hit "Run" to generate some pretty pictures!

Credits to [arocho's PyCarribean workshop](https://github.com/arocho/generative-art-workshop) for inspiration for this project.

Some examples of drawings that weatherpatterns generates:

A tropical rain storm
![a bubbly purple drawing representing tropical weather](https://raw.githubusercontent.com/fboxwala/weatherpatterns/master/drawings/tropical.png)

A snowy day
![a bubbly blue drawing representing snowy weather](https://raw.githubusercontent.com/fboxwala/weatherpatterns/master/drawings/snow_storm.png)

A sleet storm (rain and snow) classic Waterloo winter weather
![a bubbly blue drawing representing icky rain and snow](https://raw.githubusercontent.com/fboxwala/weatherpatterns/master/drawings/sleet_storm.png)

A monsoon in Mumbai (hot and rainy)
![a bubbly red drawing representing a warm rainy day](https://raw.githubusercontent.com/fboxwala/weatherpatterns/master/drawings/monsoon.png)

A cloudy day with no precipitation to speak of
![a bubbly purple drawing, representing temperate cloudy weather](https://raw.githubusercontent.com/fboxwala/weatherpatterns/master/drawings/cloudy.png)
