# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#BACKGROUND IS DONE BY @MrDetonia

define lain = Character('Lain', color="#c8ffc8", image="lain")
define stallman = Character('Stallman', color="#c8ffc8", image="stallman")
define unknown = Character('UNKNOWN', color="#c8ffc8")

image bg uni = "resources/backgrounds/uni.jpg"
image bg dorm = "resources/backgrounds/dorm_hallway.jpg"
image bg bedroom dark = "resources/backgrounds/bedroom_dark.jpg"
image bg bedroom = "resources/backgrounds/bedroom.jpg"

image side lain = "resources/characters/lain/lain_relaxed_side.png"

image side stallman = "resources/characters/stallman/stallman_side.png"
image side stallman shocked = "resources/characters/stallman/stallman_shocked_side.png"
image side stallman embarrassed = "resources/characters/stallman/stallman_embarrassed_side.png"
image side stallman angry = "resources/characters/stallman/stallman_side_angry.png"

image stallman relaxed = "resources/characters/stallman/stallman.png"
image stallman shocked = "resources/characters/stallman/stallman_shocked.png"
image stallman embarrassed = "resources/characters/stallman/stallman_embarrassed.png"
image stallman sicp = "resources/characters/stallman/stallman_sicp.png"
image stallman angry = "resources/characters/stallman/stallman_angry.png"

# The game starts here.
label start:
    $ gave_email = False

    stop music
    scene bg uni
    "This is it. Your first day at the famous MIT!"
    "It's been a long day at orientation, and you want nothing more than to sleep."
    "Though you're not entirely sure where you live..."

    show stallman relaxed
    with dissolve
    lain "W-would you happen to know where Baker house is?"

    show stallman shocked
    unknown "Baker house?!?!? YOU'RE IN BAKER HOUSE TOO?"

    show stallman embarrassed
    unknown "Oy vey... I apologise for that outburst! It's just we don't get many girls living there."
    unknown "Especially not as goodlooking as you!"

    show stallman relaxed
    stallman "Oh jeeze, I've forgotten to introduce myself. I'm Richard Stallman, you might have heard of me?"
    menu:
        "Yes - I have heard of you!":
            stallman "Ah good! What religion are you?"
            lain "R-religion?!"
            ## TODO: MAKE MULTIPLE CHOICE ON WHAT EDITOR LAIN USES. *****************************
            stallman "Yeah! The Church of EMACS or the dirty Cult of VI?"
            lain "N-neither... We used Sublime Text at my last university."
            show stallman shocked
            stallman "WHAT???? YOU DID W-WHAT?"
            show stallman embarrassed
            stallman "Again, I'm sorry for my outburst. I've high functioning autism and I find it hard to control myself."
        "No - Sorry, I haven't heard of you.":
            show stallman relaxed
            stallman "Fine, bitch."
            lain "W-what? I don't understand en gu lish very well."
            stallman "I said your hair's nice baby."

    stallman "And your name is?"

    lain "It's Lain. Lain I-iwakura."

    stallman "Say Lain... What course are you doing?"
    lain "Computer science."
    show stallman shocked
    stallman "COMPUTER SCIENCE??"
    show stallman embarrassed
    stallman "Then you should have your textbook 'The Structure and Interpretation of Computer Programs'?"
    lain "No, sorry. I could not afford it."

    show stallman sicp 
    with fade
    stallman "Here, you can have mine! Think of it as a gift between classmates, M'Lain-y."
    stallman "Just make sure to share it with anyone and everyone who asks!"
    lain "Thank you."

    stallman "I'm getting hungry. Follow me!"
    jump bakerhouse

label bakerhouse:
    play sound "resources/sounds/door-open.wav"
    scene bg dorm
    "The dorm was only a short walk from where you met Stallman, but he seems to be having trouble breathing."
    play sound "resources/sounds/breathing.ogg"
    "Plus, now that you think about it he's a little old to be an undergrad."

    show stallman relaxed
    with fade
    stallman "Here we are. Bakerhouse dorm! Remember, our first lecture is tomorrow!"
    stallman "Also, before I leave. Can I have your E-Mail address?"

    menu:
        "Yes - Sure you can!":
            $ gave_email = True
            "You read ouy your email, and stallman quickly scribbles it down."
            stallman "Thanks!"
            "Before you can even say anything, he scurries away in to his room."
            hide stallman relaxed
            with moveoutright
        "No - No, I'm sorry.":
            show stallman angry
            stallman "LISTEN HERE YOU FUCKING BITCH!"
            stallman "I WROTE THE FUCKING COMPILER THAT RUNS THE FUCKING WORLD."
            stallman "THIS IS ALWAYS WHAT HAPPENS TO NICE GUYS, WE FINISH LAST."
            stallman "FUCK YOU, 'Lame Iwa-ching-cong' OR WHATEVER THE FUCK YOU'RE CALLED!"
            stallman "I GAVE YOU MY COPY OF SICP AND THIS IS HOW YOU TREAT ME? SUCK A DICK."
            hide stallman angry
            with moveoutright
            #Add door slamming sound effect.

    "Even though he's been eccentric, you feel a strange affection for him."
    "You've never felt 'human' before, but around him you're alright with that."


    jump bedroom_night

label bedroom_night:
    show bg bedroom dark
    with fade

    scene bg bedroom dark

    "It's a lot nicer than you expected."
    "You sit on the bed, and although you're tired you want to read the book he gave you."

    menu:
        "Read SICP":
            $ import webbrowser
            $ webbrowser.open("http://sarabander.github.io/sicp/html/index.xhtml")
            "If everything went to plan, your browser opened at SICP. Read it then!"
        "Fall asleep":
            "You lie down on the bed. Almost the second you do, you fall asleep. You must've needed it!"

