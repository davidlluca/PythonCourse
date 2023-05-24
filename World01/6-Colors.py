# Command to color texts -- \033['style';'color-txt';'background'm --

# For style:
# 0 - none | 1 - bold | 4 - underline | 7 - negative

# For color-text:
# Begin 30 until 37 without library [white|red|green|yellow|blue|purple|cyan|gray]

# For background:
# Begin 40 until 47 without library [white|red|green|yellow|blue|purple|cyan|gray]

# Testing -------------------------------------------------------------------------------------------------------
randomRhing = input('Write something: ');
print('\033[4;30;41m{0}\033[m'.format(randomRhing));