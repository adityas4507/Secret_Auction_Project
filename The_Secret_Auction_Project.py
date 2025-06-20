logo = r'''
           __-----__              ||====================================================================||
      ..;;;--'~~~`--;;;..         ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
    /;-~IN GOD WE TRUST~-.\\      ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   //      ,;;;;;;;;      \\\     ||\\$//        ~         '------========--------'                \\$//||
 .//      ;;;;;    \       \\\    ||<< /        /$\              // ____ \\                         \ >>||
 ||       ;;;;(   /.|       ||    ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
 ||       ;;;;;;;   _\      ||    ||<<|        \\ //           || <||  >\  ||                        |>>||
 ||       ';;  ;;;;=        ||    ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
 ||LIBERTY | ''\;;;;;;      ||    ||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
  \\     ,| '\  '|><| 1995 //     ||>>|  12                     *\\/___\_//*   1989                  |<<||
   \\   |     |      \  A //      ||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
    `;.,|.    |      '\.-'/       ||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
      ~~;;;,._|___.,-;;;~'        ||(100)===================  ONE HUNDRED DOLLARS =================(100)||
          ''=--'                  ||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
                                  ||====================================================================||
'''

logo1 = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(f"{logo}{logo1}")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    lowest_bid = float('inf')  # Initialize with a very high number
    # print(lowest_bid)
    winner = ""
    lowest_bidder = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        elif bid_amount < lowest_bid:
            lowest_bid = bid_amount
            lowest_bidder = bidder
    print(f"The winner(highest bidder) is {winner} with a bid of ${highest_bid}")
    print(f"The lowest bidder is {lowest_bidder} with a bid of ${lowest_bid}")
    print("Goodbye!")

bids={}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = 0  # Avoid static warning: ensures price is always defined
    while True: # checking whether the price input is integer or not
        try:
            price = int(input("What is your bid?: $"))
            break  # exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    bids[name] = price
    # print(bids)

    another_bidder = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if another_bidder == "no":
        continue_bidding = False # or Here we can use (break) statement
        find_highest_bidder(bids)
    elif another_bidder == "yes":
        print("\n" * 20)
    else:
        while True:
            print("Invalid input!. Try again.")
            another_bidder1 = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
            if another_bidder1 == "no":
                continue_bidding = False
                find_highest_bidder(bids)
                break
            elif another_bidder1 == "yes":
                print("\n" * 20)
                break
