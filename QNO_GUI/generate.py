#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import QNO
from QNO import color

def main():
    deck = QNO.buildDeck()

    IMGDIR='img/cards'

    y = 1
    for card in deck:
        print(card)
        txt = f'{card[1]}\\n{card[0]}'
        outfile = f'card_{card[1]}_{card[0]}.png'
        outfile = os.path.join(IMGDIR, 'out', outfile)
        if card[0]=="|00>":
            infile = os.path.join(IMGDIR, 'blank_red.png')
            print(y, ")" ,  "[" , color.RED , color.BOLD , card[0] , "  " , card[1] , color.END , "]" )
        elif card[0]=="|01>":
            infile = os.path.join(IMGDIR, 'blank_yellow.png')
            print(y, ")" ,  "[" , color.YELLOW , color.BOLD , card[0] ,"  ", card[1] , color.END , "]" )
        elif card[0]=="|10>":
            infile = os.path.join(IMGDIR, 'blank_green.png')
            print(y, ")" ,  "[" , color.GREEN , color.BOLD , card[0] ,"  ", card[1] , color.END , "]" )
        elif card[0]=="|11>":
            infile = os.path.join(IMGDIR, 'blank_blue.png')
            print(y, ")" ,  "[" , color.BLUE , color.BOLD , card[0] ,"  ", card[1] , color.END , "]" )
        else:
            infile = os.path.join(IMGDIR, 'blank_white.png')
            print(y, ")" ,  "[" , color.BOLD , card[1] , color.END , color.RED , color.BOLD , "G" , color.END, color.YELLOW , color.BOLD , "A" ,color.END, color.GREEN , color.BOLD , "T", color.END, color.BLUE , color.BOLD , "E" , color.END , "]" )

        print(txt)
        print(infile)
        print(outfile)

        # convert blank.png -gravity North -pointsize 200 -annotate +0+100 'GATE\n|00>'  temp1.jpg
        # convert blank_white.png  -pointsize 50 -annotate +10+50 'GATE\n|00>' -gravity North -pointsize 200 -annotate +0+100 'SKIP\n|11>'   tmp.png
        # cmd = ['convert', infile, '-gravity', 'North', '-pointsize', '100' ,'-annotate', '+0+200', txt,  outfile]
        cmd = ['convert', infile,
               '-pointsize', '50' ,'-annotate', '+10+50', txt,
               '-gravity', 'North', '-pointsize', '100' ,'-annotate', '+0+200', txt,
               outfile]

        print(' '.join(cmd))
        subprocess.run(cmd)

        y+=1
        print("")

if __name__ == "__main__":
    main()
