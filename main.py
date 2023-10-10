def tones():
    print("This program can convert octave/pitchclass pairs\n into their appropriate Hertz values.It uses the tempered scale conversions")
    is_ok=0
    while is_ok<=2:
        if is_ok==1:
            print("Lets do that again shall we")
        elif is_ok==2:
            print("One more time")  

        octave=int(input("Give me an octave:"))
        o=octave-4
        pitch_class=int(input("Give me a pitch class:"))
        m=pitch_class-9
        C=440*2**(o+(m/12))
        print(f"{octave}.{pitch_class} equals {C}")
        is_ok+=1
    print("Thanks for using my program")    
tones()