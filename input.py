letter=''' <|NAME|>
 Good Morning
 <|DATE|>'''
name=input("enter your name")
date=input("enter date")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
