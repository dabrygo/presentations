# Compares versions of the Gettysburg address
# http://www.abrahamlincolnonline.org/lincoln/speeches/gettysburg.htm

import difflib
import textwrap
import sys

def gettysburg(version, width=65):    
    with open(f'gettysburg_{version}.txt') as f:
        text = f.read()
        sentences = text.split('.')
        stripped = [s.strip() for s in sentences if s]
        speech = []
        for sentence in stripped:
            wrapped = textwrap.wrap(sentence, width)
##            wrapped[-1] = wrapped[-1] + '.'
            for clause in wrapped:
                speech.append(clause)
        return speech

bancroft = gettysburg('bancroft')
bliss = gettysburg('bliss')
everett = gettysburg('everett')
hay = gettysburg('hay')
nicolay = gettysburg('nicolay')

differ = difflib.Differ()
diff = differ.compare(bliss, everett)

print('\n'.join(diff))
