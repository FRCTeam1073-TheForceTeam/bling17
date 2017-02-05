'''
Created on Feb 5, 2017

@author: ksthilaire
'''

import bibliopixel.colors as colors

#
# This is the set of color maps for the Bling. Each color map is made up of one or more
# colors as defined in the BiblioPixel color module. For solid colors, provide just one
# color in the list, but for complex color maps, provide as many colors as you want
#
color_map = {
    'RED': [ colors.Red ],
    'GREEN': [ colors.Green ],
    'YELLOW': [ colors.Yellow ],
    'BLUE': [ colors.Blue ],
    
    'TEAM_COLORS' : [ colors.Blue, colors.Orange ],
    'RAINBOW': [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Purple],

    # insert all color maps above this line to keep the error colors last    
    'ERROR': [colors.Red, colors.Green]
    }

#
# Function to get the list of colors that map to the color string.
# This function is used by those animations that require a list of colors to display (like RAINBOW)
#
# If the specified color string does not map to any colors, then the ERROR color list is returned to 
# make it obvious that the color string is unknown.
#
def get_colors( color_str ):
    color_str = color_str.upper()
    try:
        colors = color_map[color_str]
    except:
        colors = color_map['ERROR']
    return colors

#
# Function to get the first color from the list of colors that map to the color string.
# This function is used by those animations that require only one color instead of a list of colors
#
# If the specified color string does not map to any colors, then the first color from the ERROR color 
# list is returned to make it obvious that the color string is unknown.
#
def get_first_color( color_str ):
    color_str = color_str.upper()
    try:
        colors = color_map[color_str][0]
    except:
        colors = color_map['ERROR'][0]
    return colors
    
if __name__ == '__main__':
    pass