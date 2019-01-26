import urllib2, json
from collections import defaultdict
from random import randint, seed

CANVAS_WIDTH = 3000
CANVAS_HEIGHT = 1700
CITY_STRING = "waterloo,can" # city,ISO3106 country code
FILENAME = 'weather.png'

def get_current_weather():
    global CITY_STRING
    # pulls weather data from openweathermap and makes a nice defaultdict
    r = urllib2.urlopen("https://api.openweathermap.org/data/2.5/weather?q={}&appid=20792534fde4527fc5fd1c6c7bd168e5".format(CITY_STRING)).read()
    r = json.loads(r)
    weather = defaultdict(int)

    weather['temp'] = r['main']['temp']
    if 'wind' in r:
        weather['wind'] = r['wind']['speed']
    if 'rain' in r:
        weather['rain'] = r['rain']['1h']
    if 'snow' in r:
        weather['snow'] = r['snow']['1h']
    if 'clouds' in r:
        weather['clouds'] = r['clouds']['all']
        
    return weather
    
def map_ranges(weather): 
    # maps all our weather values to the ranges we want to work with for our drawing
    rain_depth = map(weather['rain'], 0, 15, 0, 6)
    weather['rain'] = rain_depth
    temp_range = (map(weather['temp'], 255, 300, -170, -85))*-1
    weather['temp'] = temp_range
    cloudiness = ceil(map(weather['clouds'], 0, 100, 0, 10))
    weather['clouds'] = cloudiness
    windy = map(weather['wind'], 0, 33, 1, 5)
    weather['wind'] = windy
    return weather

def chevrons(l, r, c, h, tc):
    # when there's no snow or rain in the weather data our drawing is p boring
    # add some chevrons with the temperature color (tc) 
    stroke(tc[0], tc[1], tc[2])
    strokeWeight(2)
    d = 0
    while d < h:
        line(l, d, c, d+100)
        line(c, d+100, r, d)
        d = d + 100
        

def make_it_rain(x, y, d, h, w):
    # makes a tree rooted at x,y with depth d over height h, width w
    # tree depth based on how much rain has fallen in the past 1h
    if d == 0:
        return
    elif h <= 0:
        return
    else:
        line(x, y, x, y+(h/d))
        line(x, y+(h/d), x-(w/2), y+(h/d))
        line(x, y+(h/d), x+(w/2), y+(h/d))
        make_it_rain(x+(w/2), y+(h/d), d-1, h-(h/d), w/2)
        make_it_rain(x-(w/2), y+(h/d), d-1, h-(h/d), w/2)
        
def make_it_cloudy_and_snow(num, snow, tc, left, right, h):
    # make some random sized circles at random locations.
    # the cloudier it is the more circles we get
    if num != 0:
        adj = int(h/num)
        
    while num > 0:    
        fill(tc[0], 107+tc[1], tc[2], 128)
        r = randint(50, 200)
        x = randint(left+r, right-r)
        y = randint(adj*num, (adj*num)+adj)
        noStroke()
        ellipse(x, y, r*2, r*2)
        num = num - 1
        if snow and (num%2 == 0):
            stroke(149, 178, 201)
            strokeWeight(2)
            noFill()
            ellipse(x, y, r/3, r/3)
            ellipse(x, y, r/1.1, r/1.1)
            line(x-r, y, x+r, y)
            line(x, y-r, x, y+r)
            line(x-(r*(sqrt(2)/2)), y-(r*(sqrt(2)/2)), x+(r*(sqrt(2)/2)), y+(r*(sqrt(2)/2)))
            line(x-(r*(sqrt(2)/2)), y+(r*(sqrt(2)/2)), x+(r*(sqrt(2)/2)), y-(r*(sqrt(2)/2)))

# Borrowed and modified from https://learn.adafruit.com/florabrella/test-the-neopixel-strip
def colorwheel(n):
    # map a single int n to a 3D RGB vector
    if n < 85:
        return [n*3, 255 - n*3, 0]
        
    elif n < 170:
        n = n - 85
        return [255 - n*3, 0, n*3]
        
    else:
        n = n - 170
        return [0, n*3, 255 - n*3]
        
def setup():
    global CANVAS_WIDTH
    global CANVAS_HEIGHT
    size(CANVAS_WIDTH, CANVAS_HEIGHT)
    noLoop()
    alpha(100)

    noFill()

def draw():
    global CANVAS_WIDTH
    global CANVAS_HEIGHT
    # black background for classy
    background(0)
    
    # real weather is boring. some fun fake weathers to test with
    # a tropical rain storm:
    # weather = {'rain': 4, 'wind': 4, 'clouds': 9, 'temp': 130, 'snow': 0}
    # a snow storm
    # weather = {'rain': 0, 'wind': 5, 'clouds': 10, 'temp': 170, 'snow': 1}
    # a windy rain and snow combination (welcome to waterloo)
    # weather = {'rain': 3, 'wind': 5, 'clouds': 10, 'temp': 150, 'snow': 1}
    # a monsoon day in mumbai
    # weather = {'rain': 6, 'wind': 4, 'clouds': 7, 'temp': 87, 'snow': 0}
    weather = get_current_weather()
    weather = map_ranges(weather)
    
    tc = colorwheel(weather['temp'])
    
    # the windier it is, the more tiles we get in our drawing
    sections = ceil(weather['wind'])
    section_width = float(CANVAS_WIDTH)/float(sections)
    while sections > 0:
        right = sections*section_width
        left = right - section_width
        center = float(section_width)/float(2) + left
        if not weather['rain'] and not weather['snow']:
            chevrons(left, right, center, CANVAS_HEIGHT, tc)
        
        # clouds and snow done together
        make_it_cloudy_and_snow(weather['clouds'], weather['snow'], 
                                tc, left, right, CANVAS_HEIGHT)
        # a line at each tile division
        stroke(tc[0], tc[1], tc[2])
        strokeWeight(3)
        line(left, 0, left, 1700)
        # if it's raining we make it rain
        strokeWeight(7)
        make_it_rain(center, 0, weather['rain'], 1700, section_width/2)
        sections = sections - 1
        
    save(FILENAME)
    
