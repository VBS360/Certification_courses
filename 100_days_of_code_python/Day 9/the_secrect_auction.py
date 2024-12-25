print("Welcome to the secret auction program.")

bid_details = {}

def bid(name,bid_val):
    name = input("What is your name?: ")
    bid_val = int(input("What is your bid?: $"))
    
    bid_details[name] = bid_val # Push data in the dictionary
    
    other_bid = input("Are there any other bidder? Type 'Yes' or 'No'.: ")
    if other_bid == "Yes":
#         print("\n"*100)                 #To clear screen
        return bid(name,bid_val)
    else:
#         print("\n"*100)                 #To clear screen
        return highest_bid()
    
    

def highest_bid():
    largest_bidder = max(bid_details, key=bid_details.get)   # Gets the key of max value
    largest_bid = bid_details[largest_bidder]                # Gets the highest value
    print(f"The winner is {largest_bidder} with a bid of ${largest_bid}.")
    
bid("",0)
