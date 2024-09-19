def calculate_love_score():
    num1 = 0
    num2 = 0
    word1 = ["T","R","U","E"]
    word2 = ["L","O","V","E"]
    for char in name1:
        if char in word1:
            num1 +=1
    for char in name1:
        if char in word1:
            num1 +=1
    for char in name2:
        if char in word2:
            num1 +=1
    for char in name2:
        if char in word2:
            num1 +=1
    print(f"{num1}{num2}")
   
name1 = "Angela Yu"
name1 = name1.upper()
name2 = "Jack Bauer"
name2 = name2.upper()

calculate_love_score()