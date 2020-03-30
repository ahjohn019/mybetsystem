

def main():
    currentaccount = 100
    homemarksfirst = 0
    awaymarksfirst = 4

    while True:
        print("Your Current Account:", currentaccount)
        selection = input("Do You Want To Top Up ? 1. Yes 2. No 3. Start Bet 4. Results 5. Exit : ")

        if selection == "1":
            topup = input("How much ? :")
            total = currentaccount + int(topup)
            print("Your Total Amount is :", total)
            currentaccount += int(topup)
        elif selection not in ("1","2","3","4","5"):
            print("Your Input Is Wrong, Please Try Again")
        elif selection == "3":
            betselection = input("Select Your Bet Match : 1. A vs B 2. C vs D :")
            if betselection == '1':
                betteam = input('Select Your Bet Team : 1. A(0.11) 2. B(0.2) : ')
                if betteam == '1':
                    print("Your Bet Team : A(0.11)")
                else:
                    print("Your Bet Team : B(0.2)")
                betamount = input("How much for bet ? : ")
                print("Your Bet Amount : ", betamount)
                currentaccount -= int(betamount)
                
                print('Here Is Your Remain After Bet : ',currentaccount)
                print('A : ' + str(homemarksfirst) +' B:'+str(awaymarksfirst))

                if (homemarksfirst < awaymarksfirst):
                    print("Away Wins")
                elif(homemarksfirst == awaymarksfirst):
                    print("Draw")
                else:
                    print("Home Wins")
                
        elif selection == "5":
            print("Good Bye")
            break
        else:
            continue
        
    
if __name__ == "__main__":
    main()

