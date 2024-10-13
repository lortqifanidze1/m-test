#1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.-
def a(b):
    n = len(b) + 1 # vaketebtr cvlads romelic aris sigrde b argumentis + 1 
    sum1 = n * (n + 1 ) // 2  # shemdeg jam iu unda gavakeeot am vlcadi romelac vamravletbs mis 1 balatebul damgvavebul ayovil 2 ze
    print( sum1 - (sum(b))) # mere am cven sum  n vakleb t tviston am b test cases da vala shedegi
a([1,2,4])