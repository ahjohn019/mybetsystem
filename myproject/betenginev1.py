

def main():
    currentaccount = 100
    dotanewbee = 4
    dotaliquid = 2
    homemarkssecond = 2
    awaymarkssecond = 3

    while True:
        print("Your Current Account:", currentaccount)
        selection = input("Do You Want To Top Up ? 1. Yes 2. No 3. Start Bet 4. Exit : ")

        if selection == "1":
            topup = input("How much ? :")
            total = currentaccount + int(topup)
            print("Your Total Amount is :", total)
            currentaccount += int(topup)
        elif selection not in ("1","2","3","4"):
            print("Your Input Is Wrong, Please Try Again")
        elif selection == "3":
            #pre match
            betselection = input("Select Your Bet Match : 1. Newbee vs Liquid 2. C vs D :")

            if betselection == '1':
                betteam = input('Select Your Bet Team : 1. Newbee(2.2) 2. Liquid(0.3) : ')
                if betteam == '1':
                    print("Your Bet Team : Newbee(2.2)")
                else:
                    print("Your Bet Team : Liquid(0.3)")

            if betselection == '2':
                betteam = input('Select Your Bet Team : 1. C(0.18) 2. D(3.0) : ')
                if betteam == '1':
                    print("Your Bet Team : C(0.18)")
                else:
                    print("Your Bet Team : D(3.0)")

            #after select odd, bet how much from currentaccount
            betamount = input("How much for bet ? : ")

            if (int(betamount) > currentaccount):
                print("Please try again")
            else:  
                print("Your Bet Amount : ", betamount)
                currentaccount -= int(betamount)
                print('Here Is Your Remain After Bet : ',currentaccount)

                if betselection == '1':
                    print(' Newbee : ' + str(dotanewbee) +' Liquid : '+str(dotaliquid))
                    if betteam == '1':
                        print("Newbee Wins")
                        awaywin = int(betamount)*2.2
                        print(awaywin)
                        currentaccount += awaywin
                    elif dotanewbee == dotaliquid:
                        print("Draw")
                        currentaccount += int(betamount)
                    else:
                        print("You Lose")
                        betamount = 0
                        currentaccount -= betamount
                else:
                    #post result
                    print('C : ' + str(homemarkssecond) +' D : '+str(awaymarkssecond))
                    if betteam == '2':
                        print("Away Wins")
                        awaywin = int(betamount)*3
                        print(awaywin)
                        currentaccount += awaywin
                    elif homemarkssecond == awaymarkssecond:
                        print("Draw")
                        currentaccount += int(betamount)
                    else:
                        print("You Lose")
                        betamount = 0
                        currentaccount -= betamount
                
        elif selection == "4":
            print("Good Bye")
            break
        else:
            continue
        
    
if __name__ == "__main__":
    main()

