# Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
def gg(a):
    if not a: # pirvel rigshi  vnaxulobs staitrod a atris tu arta
        print( " ")
    
    start = a[0] # mere prefixsis pirvel asos vaketebt rom momavalsvi vnaxot sxva indexsebic
    for i in a[1::]: # for it i vuvlit a inxexsi  1 dan blom d a 
        while i[0:len(start)] != start and start: # sanam es cheni i o idan dawyebuli sigwamden indexsamede imushgaos am kodma
            start = start[:-1] # mere tu es piroba marlai cveni statis in dexi xdeba bolo elementi
            if not start: # mere tu indeqsi ar aris 
                print( " ") # carieli stringi daaburons
        print( start)
gg(["ola","olo","oli"])





#2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"
