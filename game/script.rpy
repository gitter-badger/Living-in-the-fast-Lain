# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#BACKGROUND IS DONE BY @MrDetonia

define lain = Character('Lain', color="#c8ffc8", image="lain")
define stallman = Character('Stallman', color="#c8ffc8", image="stallman")
define unknown = Character('UNKNOWN', color="#c8ffc8")
define linus = Character("Linus", color="#c8ffc8", image="linus")

image bg uni = "resources/backgrounds/uni.jpg"
image bg dorm = "resources/backgrounds/dorm_hallway.jpg"
image bg bedroom dark = "resources/backgrounds/bedroom_dark.jpg"
image bg bedroom = "resources/backgrounds/bedroom.jpg"
image bg lecture_hall = "resources/backgrounds/lecture_hall.jpg"
image bg lecture_front = "resources/backgrounds/lecture_front.png"

image side lain = "resources/characters/lain/lain_relaxed_side.png"

image side stallman = "resources/characters/stallman/stallman_side.png"
image side stallman shocked = "resources/characters/stallman/stallman_shocked_side.png"
image side stallman embarrassed = "resources/characters/stallman/stallman_embarrassed_side.png"
image side stallman angry = "resources/characters/stallman/stallman_side_angry.png"

image side linus = "resources/characters/linus/linus_side.png"

image stallman relaxed = "resources/characters/stallman/stallman.png"
image stallman shocked = "resources/characters/stallman/stallman_shocked.png"
image stallman embarrassed = "resources/characters/stallman/stallman_embarrassed.png"
image stallman sicp = "resources/characters/stallman/stallman_sicp.png"
image stallman angry = "resources/characters/stallman/stallman_angry.png"

image linus relaxed = "resources/characters/linus/linus.png"
image linus angry = "resources/characters/linus/linus_angry.png"
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
            stallman "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
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
            "You've read SICP deep in to the night, until you drift off."
        "Fall asleep":
            "You lie down on the bed. Almost the second you do, you fall asleep. You must've needed it!"

    jump bedroom_morning

label bedroom_morning:
    show bg bedroom 
    with fade

    scene bg bedroom

    lain "*stretching* yaaawwwnnnnuuu!"
    "That was a refreshing sleep, maybe the most refreshing you've ever had."
    "You dreamt of him. You dreamt of him grabbing you and holding you close."
    "You wrapped your arms around him while he kissed your head..."

    "You stand up and brush the sleep from your eyes."
    "You check the time. 8:30??? YOU'RE GOING TO BE LATE!"
    show bg bedroom
    with fade

    "You're all ready now. Lets try and find Stallmanu."
    jump hall_morning

label hall_morning:
    scene bg dorm
    lain "H-hello? Is anyone there?"
    "Right as you said, he comes bursting out."
    show stallman relaxed
    with moveinright

    stallman "LAIN! YOU'RE HERE. WE'RE GOING TO EB LATE, LETS HURRY!!!"
    jump lecture_hall_1


label lecture_hall_1:
    show bg lecture_hall
    with fade

    scene bg lecture_hall
    "You arrive at the lecture hall quicker than you thought. In fact, hardly anyone is here."
    "You take your seat, and the lecturer starts speaking."

    scene bg lecture_front
    show linus relaxed
    linus "Hello! I am Linus Torvalds, and I will be teaching your 'systems programming' class."
    stallman "I hate this dick."
    show linus angry
    linus "FUCK YOU STALLMAN!"
    show linus relaxed
    stallman "FUCK YOU LINUS!"
    show linus angry
    linus "No, FUCK YOU STALLMAN!"
    show linus relaxed
    linus "Why are you even here? You graduated like 40 years ago."
    stallman "FUCK YOU!"
    show linus angry
    linus "Fuuuuuuuuuuuuckkkk yooooooooooooooooouuuuu"




