def activity():
    global activity
    activity = input("""
    We are going to be convert:
    a Money
    b Measurement
    c Liquids
    d Exit program

    """)
activity()
if activity == "Money" or activity == "money" or activity == "a" or activity == "A":
    def converter():
        global what_convert
        what_convert = input("Do you want to convert a) ksh to usd or b) usd to ksh:  ")
    converter()

    if what_convert == "b":
        usd_cash = int(input("Enter how much dollars you want to convert: "))
        print("The amount you have inputed into kenya shilings = ",usd_cash * 108.59)
        def again():
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
                again()
        again()
    elif what_convert == "a":   
        ksd_cash = int(input("Enter how much kenya shillings you want to convert: "))
        print("The amount you have inputed into ud dolars = ",ksd_cash / 108.59)
        def again():
            again = input("Do you want to convert again Yes(y) or No(n):  ")
            if again == "y":
                converter()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
                again()
        again()
    else:
        print("I did not understand you")
        converter()
elif activity == "b":
    def activity_converting():
        global what_convert
        what_convert = input("""
        Do you want to convert
        a Km to m
        b M to km
        c M to cm
        d cm to M
        e Km to cm
        f Cm to Km
        g Go back to the top
        
        
        """)
    activity()
    if what_convert == "a":
        def km_m():

            km = float(input("Enter the amount in km:  "))
            print("The amount in meters is ",km * 1000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                km_m()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again()
        km_m()
    elif what_convert == "b":
        def m_km():
            m = float(input("Enter the amount in m:  "))
            print("The amount in km is ",m / 1000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                m_km()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again()
        m_km()
    elif what_convert == "c":
        def m_cm():
            m = float(input("Enter the amount in m:  "))
            print("The amount in centimeters is ",m * 1000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                m_cm()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again()
        m_cm()
    elif what_convert == "d":
        def cm_m():

            cm = float(input("Enter the amount in cm:  "))
            print("The amount in m is ", cm/1000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                cm_m()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again()
        cm_m()
    elif what_convert == "e":
        def km_cm():
            km = float(input("Enter the amount in km:  "))
            print("The amount in cm is ", km*1000000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                km_cm()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again_func()
        km_cm()
    elif what_convert == "f":
        def cm_km():

            cm = float(input("Enter the amount in cm:  "))
            print("The amount in km is ", cm/1000000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                cm_km()
            elif again == "n":
                activity_converting()
            else:
                print("I did not understand you")
                again_func()
        cm_km()
    elif what_convert == "g":
        activity_converting()
elif activity == "c":

    def converter():
        global what_convert
        what_convert = input("""These are the options of converting
        a L to ml
        b ml to l
        c dl to l
        d l to dl
        e Ml to dl
        f Dl to ml
        g Go back to the top
        
         """)
    converter()
    if what_convert == "a":
        def l_ml():
            l = int(input("Enter the amount in l:  "))
            print("The amound in ml is ",l*1000)
            def again_func():
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                activity()
        l_ml()
    elif what_convert == "b":
        def ml_l():
            ml = int(input("Enter the amount in ml:  "))
            print("The amound in l is ",ml/1000)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                converter()
            else:
                print("I did not understand you")
                again_func()
        ml_l()
    elif what_convert == "c":
        def dl_l():
            dl = int(input("Enter the amount in dl:  "))
            print("The amound in l is ",dl/10)
            def again_func():
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                converter()
            else:
                print("I did not understand you")
                again_func()
        dl_l()
    elif what_convert == "d":
        def l_dl():
            l = int(input("Enter the amount in l:  "))
            print("The amound in dl is ",l*10)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                converter()
            else:
                print("I did not understand you.")
                again_func()
        l_dl()
    elif what_convert == "e":
        def ml_dl():
            ml = int(input("Enter the amount in ml:  "))
            print("The amound in dl is ",ml/100)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                converter()
            else:
                print("I did not understand you")
                again_func()
        ml_dl()
    elif what_convert == "f":
        def dl_ml():
            dl = int(input("Enter the amount in dl:  "))
            print("The amound in ml is ",dl*10)
            def again_func():
                global again
                again = input("Do you want to convert again Yes(y) or No(n):  ")
            again_func()
            if again == "y":
                converter()
            elif again == "n":
                activity()
            else:
                print("I did not understand you")
                again_func()
        dl_ml()
    elif what_convert == "g":
        activity()
elif activity == "d":
    main_actvities()
else:
    print("I did not understand you")
    activity()