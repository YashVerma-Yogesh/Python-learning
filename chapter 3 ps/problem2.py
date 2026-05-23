# wap to fill in a letter template given below with name and date
# letter = Dear <|name|>,
# yoy are selected !
# <|date|>

letter = ''' Dear <|name|>,
 You Are Selected
 <|Date|>
 '''
print(letter.replace("<|name|>","Yash").replace("<|Date|>", "24 june 2024"))