# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#BACKGROUND IS DONE BY @MrDetonia

define lain = Character('Lain', color="#c8ffc8", image="lain")
define stallman = Character('Stallman', color="#c8ffc8", image="stallman")
define unknown = Character('UNKNOWN', color="#c8ffc8")
define torvalds = Character("torvalds", color="#c8ffc8", image="torvalds")
define jobs = Character("Steve Jobs", color="#c8ffc8", image="jobs")

#Scene backgrounds:
#Background of the Uni.
image bg uni = "resources/backgrounds/uni.jpg"
#Dorm background
image bg dorm = "resources/backgrounds/dorm_hallway.jpg"
#Lain's bedroom, only dark.
image bg bedroom dark = "resources/backgrounds/bedroom_dark.jpg"
#Lain's bedroom.
image bg bedroom = "resources/backgrounds/bedroom.jpg"
#The entrance of the lecture hall.
image bg lecture_hall = "resources/backgrounds/lecture_hall.jpg"
#The lecture hall from the perspective of Lain's seat.
image bg lecture_front = "resources/backgrounds/lecture_front.png"

#Side images are the small profiles when the character talks.
#Lain has only one picture.
image side lain = "resources/characters/lain/lain_relaxed_side.png"
image side torvalds = "resources/characters/torvalds/torvalds_side.png"
image side jobs = "resources/characters/jobs/jobs_side.jpg"


#Load all of RMS's side expressions.
image side stallman = "resources/characters/stallman/stallman_side.png"
image side stallman shocked = "resources/characters/stallman/stallman_shocked_side.png"
image side stallman embarrassed = "resources/characters/stallman/stallman_embarrassed_side.png"
image side stallman angry = "resources/characters/stallman/stallman_side_angry.png"

#All of Stallman's expressions.
image stallman relaxed = "resources/characters/stallman/stallman.png"
image stallman shocked = "resources/characters/stallman/stallman_shocked.png"
image stallman embarrassed = "resources/characters/stallman/stallman_embarrassed.png"
image stallman sicp = "resources/characters/stallman/stallman_sicp.png"
image stallman angry = "resources/characters/stallman/stallman_angry.png"

image torvalds relaxed = "resources/characters/torvalds/torvalds.png"
image torvalds angry = "resources/characters/torvalds/torvalds_angry.png"
image torvalds card = "resources/characters/torvalds/torvalds_card.png"

image jobs = "resources/characters/jobs/jobs.png"
image jobs gun = "resources/characters/jobs/jobs_gun.png"
image jobs gun fire = "resources/characters/jobs/jobs_gun_fire.png"

# The game starts here.
label start:
    $ gave_email = False

    #Stops the music from the menu playing.
    stop music
    play music "resources/music/outofsilencev2.ogg"
    scene bg uni
    #TODO: Make this better.
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

    #'with fade' kinda makes him flash a bit.
    show stallman sicp 
    with fade
    stallman "Here, you can have mine! Think of it as a gift between classmates, M'Lain-y."
    stallman "Just make sure to share it with anyone and everyone who asks!"
    lain "Thank you."

    stallman "I'm getting hungry. Follow me!"
    jump bakerhouse_1

#The first time you arrive at your dorm, bakerhouse.
label bakerhouse_1:
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
            #TODO: Add door slamming sound effect.

    "Even though he's been eccentric, you feel a strange affection for him."
    "You've never felt 'human' before, but around him you're alright with that."

    jump bedroom_night

#This is your bedroom at night, after your interaction with stallman.
label bedroom_night:
    show bg bedroom dark
    with fade

    scene bg bedroom dark

    "It's a lot nicer than you expected."
    "You sit on the bed, and although you're tired you want to read the book he gave you."

    menu:
        "Read SICP":
            #Opens your web browser at a HTML5 version of SICP.
            $ import webbrowser
            $ webbrowser.open("http://sarabander.github.io/sicp/html/index.xhtml")
            "If everything went to plan, your browser opened at SICP. Read it then!"
            "You've read SICP deep in to the night, until you drift off."
        "Fall asleep":
            stop music
            "You lie down on the bed. Almost the second you do, you fall asleep. You must've needed it!"

    jump bedroom_morning

#Your bedroom when you wake up.
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

#Bakerhouse dorm hall, in the morning.
label hall_morning:
    scene bg dorm
    lain "H-hello? Is anyone there?"
    "Right as you said, he comes bursting out."
    show stallman relaxed
    with moveinright

    stallman "LAIN! YOU'RE HERE. WE'RE GOING TO EB LATE, LETS HURRY!!!"
    hide stallman
    jump lecture_hall_1

#First time Lain goes to a lecture.
label lecture_hall_1:
    show bg lecture_hall
    with fade

    scene bg lecture_hall
    "You arrive at the lecture hall quicker than you thought. In fact, hardly anyone is here."
    "You take your seat, and the lecturer starts speaking."

    scene bg lecture_front
    show torvalds relaxed
    torvalds "Hello! I am Linus Torvalds, and I will be teaching your 'systems programming' class."
    "Your sleep left you feeling strangely unrested. You can't keep your eyes open any longer."

    hide torvalds relaxed
    show bg lecture_front
    with fade
    #Add yawn
    "Oh shit. How long have you been asleep?"
    "You look around. Nobody is here. Even Stallman has left. Maybe it's time to go back."

    show bg lecture_hall
    with dissolve

    "As you try and leave, you hear a rushing sound from your side."
    show torvalds relaxed
    with moveinleft
    torvalds "It can't be! Lain?!?!"
    lain "How did you know my name?"
    torvalds "I saw you in the crowd!"
    torvalds "We can't talk here. Here's my card. Call me!"
    hide torvalds relaxed
    with moveoutright

    show torvalds card
    hide torvalds card
    with dissolve

    "This was too weird. You better go back and have a nap."
    jump jobs_rob_1

#The first time steve jobs robs you. Might happen more.
label jobs_rob_1:
    scene bg uni
    show jobs 
    "On your way back, you get stopped by a strange person."
    jobs "Hey kid, give me all your lunch money!"
    lain "I-i don't have any money."
    jobs "THEN PRAISE MR SKELETAL"
    lain "w-what?"
    jobs "SAY 'thank you mr skeletal' RIGHT FUCKING NOW."
    menu:
        "Thank you Mr Skeletal!":
            jobs "Good Lain. You can go now."
        "N-no I wont do it.":
            hide jobs
            show jobs gun
            jobs "You think this is a fucking joke?!?!"
            jobs "PRAISE MR SKELETAL OR I'LL BLOW YOUR FUCKING BRAINS OUT"
            menu:
                "THANK YOU MR SKELETAL":
                    jobs "You're real fucking lucky Lain. Get out of here."
                "NO!":
                    jobs "See you in hell, Lain."
                    lain "How did you know my -"
                    hide jobs gun
                    show jobs gun fire
                    "*BLAOW*"
                    hide jobs gun fire
                    show jobs gun
                    "You feel a burning sensation in your chest... you've been shot."
                    "This is it. You finally get to meet Mr Skeletal yourself."
                    "GG"
                    "No re."
                    return
    "You pick up your dropped books and quickly run back to your dorm."
    "How did he know your name?"
    jump bakerhouse_2

#The second time you arrive at Bakerhouse. This is where
#you make the important story line choice.
label bakerhouse_2:
    scene bg dorm

    show stallman relaxed
    stallman "Hey Lain! Is everything okay? You look scared."
    lain "Y-yeah. Just tired."
    stallman "Lain, I was wondering..."
    stallman "Would you like to go for lunch?"

    #This is where shit gets real.
    #You can choose to go to lunch with stallman, and that will cause the rest
    #of the game to follow the Stallman path. Or you can choose to go inside,
    #and phone Torvalds to start the torvalds fork.
    menu:
        "No - I'm sorry, I've something to do. (Go and phone Torvalds)":
        "Yes - That sounds great!":