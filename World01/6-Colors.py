# Command to color texts -- \033['style';'color-txt';'background'm --

# For style:
# 0 - none | 1 - bold | 4 - underline | 7 - negative

# For color-text:
# Begin 30 until 37 without library [white|red|green|yellow|blue|purple|cyan|gray]

# For background:
# Begin 40 until 47 without library [white|red|green|yellow|blue|purple|cyan|gray]

# Testing -------------------------------------------------------------------------------------------------------
colors = {'clear':'\033[m',
          'red':'\033[31m',
          'purple':'\033[35m'};

name = 'David';
print('Welcome {0}{1}{2}'.format(colors['blue'], name, colors['clear']));