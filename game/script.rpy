define me = Character("[player_name]", color="2C2C2C")
define alex = Character("Alex", image="alex",)
define teacher = Character("Teacher", image="teacher")
define boss = Character("Boss", image="boss")

# school act 1
define s_subject_f = False
define s_subject_state = 0
define s_body_f = False
define s_act1_score = 0
# school act 2
define s_act2_score = 0

define school_score = 0

# office
define o_tone_f = False
define o_cc_f = False
define o_jf = 0
define office_score = 0

transform alex_adjust:
    zoom 0.46
    ypos 1250

transform alex_dual_adjust:
    xpos 1760

# The game starts here.

label start:
    python:
        player_name = renpy.input("What is your name?", length=32)
        player_name = player_name.strip()

        if not player_name:
            player_name = "You"

    jump s_act_one

label s_act_one:
    scene black

    "Today would be like every other day...{p=0.9}If it wasn't for the fact that your little sister, Alex, is starting school."

    "Now this would usually be a good thing, but there is one problem..."

    "{size=+20}Alex can't write emails...!!!{/size}" with vpunch

    scene bg bedroom
    with fade

    alex "Hey!"

    show alex at center, alex_adjust 
    with dissolve

    alex "[player_name], you know I {i}am{/i} starting school today, right?"
    alex "Hope you didn't forget you have to drop me off."

    me "How could I?{p=0.2}You wouldn't stop telling the entire neighbourhood about it.{p}I'm proud to be taking you to your first day of high school."
    me "You do have to tell me though, did you {i}finally{/i} learn how to write emails?"

    show alex angry

    alex "{size=+20}WHAT?{/size}{w=0.5}" with vpunch
    alex "Of course I've learned to write emails; how could you even ask me that?"

    me "Hey hey, I'm just asking. I trust you enough to believe that."

    show alex
    with dissolve

    alex "{i}Hmmph...{/i} let's go..."

    window hide

    scene bg school
    with fade

    window show

    me "Well we're finally here. Have a great first day, Alex!"

    alex "Thank you [player_name], I'll see you soon."

    "{i}She's definitely going to need help with emails, isn't she?{/i}"

    window hide

    scene black
    with fade

    show text "A few hours pass..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg school
    with fade

    window show

    show alex at center, alex_adjust
    with dissolve

    me "Hey Alex, how was your first day?"

    alex "It was {i}fine{/i}. Not much happened today."

    me "That's pretty normal for a first day. Not much is going to happen right away."

    show alex confused

    alex "Yeah, you're right...{p=0.8}Hey [player_name], I kind of need your help."

    me "Let me guess, you need to write an email, don't you?"

    alex "{i}Yeah...{/i}"

    me "I told you to learn about emails, didn't I?"

    show alex flustered

    alex "And I did!!"

    show alex confused

    alex "But I kind of forgot about it all."

    "{i}sigh...{/i}"

    me "Alright, let's go home. Then you can tell me what you need to do."

    window hide

    scene bg bedroom

    window show

    show alex at center, alex_adjust
    with dissolve

    alex "So you're going to help me with my emails, right?"

    me "Yeah, only if you promise you'll actually learn this time."

    alex "I promise, [player_name]."

    me "Alright, what do you need to do?"

    alex "So my homeroom teacher has asked all of us to send her an email introducing ourselves."

    me "Well, you know how to start, right?"

    alex "Yeah, you open up the email app...{nw=1.0}"

    me "Yeah yeah, what do you do {i}after{/i} that?"

    show alex angry

    alex "Aren't YOU supposed to be helping me with that?"

    me "Hey, calm down, you need to learn how to do this."

    show alex

    alex "You're right, sorry, what is the next step?"

    me "Well... firstly, you need to write out who the email is addressed to."

    alex "That would be my homeroom teacher, right?"

    me "Yep, you'd write that in the {color=#9C59D1}to:{/color} of the email."

    alex "Done! Next up is the subject line, right?\nI gotta tell the teacher what the email is about."

    alex "...Right?"

    me "You got that right. Do you know what you are going to write?"

    alex "Hmm, let me try...{p=1.0}"

    alex "I'm not sure actually, what should I actually write?"

    alex "[player_name], could you help me out please?"

    menu subject_line_menu:
        "What should Alex write?"

        "One word":
            me "You should write a one word subject line..."
            me "It keeps it clear and to the point."
            alex "Hmm, I'm not sure about that, but okay. I'll trust you on this one."
            alex "There.. {color=#9C59D1}\"Introduction\"{/color} that seems like a good enough subject line"

            $ s_subject_state = -1

        "All the details":
            me "You should write a subject line with every last detail..."
            me "It'll help your teacher understand what the email is about."
            alex "Hmm, I'm not sure about that, but okay. I'll trust you on this one."
            alex "There.. I wrote everything I think is important in the subject line, that looks pretty good."

            $ s_subject_state = 1

        "Just enough details":
            me "You should write a subject line with just enough details..."
            me "Like your {color=#9C59D1}name,{/color} and for what {color=#9C59D1}purpose{/color} you're writing."
            alex "Hmm, that sounds good. I'll trust you on this one."
            alex "There.. I wrote {color=#9C59D1}\"Introduction of Alex\"{/color}, that seems perfect."

            $ s_subject_f = True

    alex "Okay! Subject line done! What's next?"

    alex "Oh wait, I know, I have to write the body don't I?"

    me "Well, at least you remember {i}something{/i}."

    show alex angry

    alex "Hey! I haven't forgotten everything you know."

    me "Well, prove it then. What would be the proper {color=#9C59D1}greeting{/color}, {color=#9C59D1}sign-off{/color}, and way to write your {color=#9C59D1}name{/color}?"

    show alex flustered

    alex "Well, since I'm writing an email to my teacher, it would be..."

    alex "A formal greeting..."
    alex "A proper sign-off..."
    alex "And my proper name, no nicknames."

    me "Hey, whaddya know, maybe you do remember something after all."

    show alex

    alex "See I told you!"

    alex "But what exactly would each of those be...?"

    menu body_menu:
        "What should Alex write as her greeting, sign-off and name?"
        
        "Respected, Regards, Alex":
            alex "Respected teacher, Regards and Alex"
            alex "Okay that looks good!"
            
            $ s_body_f = True
            
        "What's up, Smell Ya Later, ~A":
            alex "What's up teach, Smell Ya Later and ~A"
            alex "This doesn't feel right, but okay..."
        
        "Dear, Regards, Al":
            alex "Dear teacher, Regards and Al"
            alex "There's something odd about this..."

    "Alex quickly types out a small introduction about herself in the email."

    alex "The email is now complete!"
    alex "Now to hit send...{w=0.6}and there we go!"
    alex "Thank you so much, [player_name]."

    me "You're welcome, Alex. I'm glad you're learning."

    "{i}I hope I told her the right things to write down{/i}"

    window hide

    scene black
    with fade
        
    show text "The next day, Alex heads to school" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg classroom
    with fade

    window show

    show alex at right, alex_adjust, alex_dual_adjust
    show teacher at left
    with dissolve

    teacher "Hey, Alex"

    alex "Yes, teacher?"

    if not s_subject_f and not s_body_f:
        $ s_act1_score = -1
        jump school_act_one_worst
    elif s_subject_f and not s_body_f:
        jump school_act_one_bad_body
    elif not s_subject_f and s_body_f:
        jump school_act_one_bad_subject
    else:
        $ s_act1_score = 1
        jump school_act_one_best

label school_act_one_worst:
    show teacher angry
    
    teacher "I'm highly dissapointed in your email"
    teacher "I couldn't comprehend your subject line..."
    teacher "...and your body details were horrendous."

    show teacher
    show alex confused

    teacher "I understand this is your first year in high school, but I'm expecting better from you."

    alex "Ye-Yes.. teacher, I'm so sorry!"

    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home... I can hear her sobbing.{/i}"

    show alex confused at center, alex_adjust

    alex "[player_name], I thought you would help me write emails..."
    alex "...but you only ended up embarassing me in front of my teacher."

    me "Wait, what do you mean?"

    alex "She called my entire email \'horrendous\'. The subject line, even the body was wrong."

    "{i}Darn it, I thought I told her the right options, I need to apologise right away.{/i}"

    me "I'm so sorry Alex... I didn't realise I was doing so bad at emails either."

    alex "You were supposed to know this..."

    me "I know, I'm so sorry Alex, I promise you the next time I'll make sure everything is proper."

    show alex

    alex "Okay... I know you didn't mean to embarass me. But you better keep yourself in check."

    jump s_act_two

label school_act_one_bad_body:
    teacher "I was quite impressed by your email."
    teacher "Though I had a small nitpick.{w=0.2}I know I tell you guys to think of me as a friend, but the details of your body
    were just a little too casual."
    teacher "It would be best to keep a more formal tone for all of those in the future!"

    alex "Of course. Thank you!"
    
    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home...{/i}"

    show alex at center, alex_adjust

    alex "Hey, [player_name]! My teacher said she was impressed by my email."

    show alex confused

    alex "Though she did say the body was a little informal."

    show alex

    alex "That's okay though, I can always correct small mistakes...{w}Even if you made them!"

    me "Hey now, that's amazing; good job!"

    "{i}Darn, seems like my skills weren't as sharp as I thought they would be.{/i}"

    jump s_act_two

label school_act_one_bad_subject:
    teacher "I was quite impressed by your email."
    teacher "Though I had a small nitpick.{w=0.2}It was a bit hard for me to figure out what you wanted to say in your subject line."

    if s_subject_state == -1:
        teacher "It felt like there was too little, I couldn't figure out what the email was about, from that one word subject."
    elif s_subject_state == 1:
        teacher "It felt like there was too much, I couldn't figure out what the email was about among all those details."

    teacher "It would be best to stick to the necessary details in the future!"

    alex "Of course. Thank you!"

    
    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home...{/i}"

    show alex at center, alex_adjust

    alex "Hey, [player_name]! My teacher said she was impressed by my email."

    show alex confused

    alex "Though she did say the subject line needed some work."

    show alex

    alex "That's okay though, I can always correct small mistakes...{w}Even if you made them!"

    me "Hey now, that's amazing; good job!"

    "{i}Darn, seems like my skills weren't as sharp as I thought they would be.{/i}"

    jump s_act_two

label school_act_one_best:
    show teacher happy
    
    teacher "I'm highly impressed, I simply loved your email!"
    teacher "The subject line was just right, and all the body details were prim and proper."
    teacher "You're shaping up to be a promising young student!"

    show alex

    alex "Thank you teacher! That means a lot to me!"

    
    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home... I can hear her giggling.{/i}"

    show alex at center, alex_adjust

    alex "[player_name], my teacher loved my email!"

    me "Really? That's amazing Alex, I'm so happy for you!"

    alex "It's all thanks to you! Oh you're such a great sibling"

    "{i}Great! Looks like I got everything just right. I'm glad Alex is also happy.{/i}"

    jump s_act_two

label s_act_two:
    window hide

    scene black
    with fade

    show text "A few months pass.. Alex continues her journey at high school.." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg bedroom 
    with fade

    alex "{size=+20}[player_name!u]!!!{/size}" with vpunch

    show alex at center, alex_adjust
    with dissolve

    me "What happened? Why are you screaming?"

    alex "I need help again..."

    me "And you needed to yell my name out for the entire world to hear, to let me know that?"

    alex "{i}Yes...{/i}"

    "{i}Sigh... She'll never change, will she?{/i}"

    me "Alright, what is it this time?"

    alex "Well, my teacher has asked me to write an email to the mayor."

    me "The mayor? That's impressive! What for?"

    alex "Well, my teacher knew I was interested in learning more about being digitally literate..."
    alex "So, she asked me to reach out to Mayor George."

    me "Wow, that's amazing! So, what are you afraid of then?"

    alex "Well...{w=0.4}It's just that I've mostly been writing emails to my friends now."
    alex "I haven't even written that often to my teacher."

    show alex confused

    alex "So I'm just not sure what I should write."

    me "I see. You're afraid of saying the wrong things to the mayor?"

    alex "Yeah, that's exactly it."

    me "Don't worry, I'll help you out!"

    show alex

    alex "Oh thank you, I knew you'd help me out."

    alex "Now to write this email."
    alex "You got any ideas?"

    menu etiquette_menu:
        "How should Alex write this email?"

        "Completelely unrestrained":
            me "I think you should go all out"
            me "Let the mayor know everything. Don't hold anything back!"

            show alex confused

            alex "Hmmm, are you sure I should be talking to the mayor like that?"

            me "Of course, they'd wanna know how excited you are!"

            show alex

            alex "Alright, if you say so."

            $ s_act2_score = -1

        "Hold her horses and think about it":
            me "I think you should think about it."
            me "They're the mayor, right? You don't wanna let the fact that your interaction is online, make you think differently."

            alex "You're right, I think I'll word my thoughts carefully and let them know about how I want to learn!"

            $ s_act2_score = 1

    "{i}I hope I told her the right things to write down.{/i}"

    window hide

    scene black
    with fade
        
    show text "The next day, Alex heads to school" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg classroom
    with fade

    window show

    show alex at right, alex_adjust, alex_dual_adjust
    show teacher at left
    with dissolve

    teacher "Hey Alex, have you got a minute?"

    alex "Yes, teacher, of course."

    teacher "I wanted to talk to you about the email you wrote to the mayor."

    if s_act2_score == -1:
        jump school_act_two_bad
    elif s_act2_score == 1:
        jump school_act_two_good

label school_act_two_bad:
    show teacher angry
    teacher "I am very displeased at the way you wrote that email to the mayor."
    teacher "The Mayor is not a friend of yours. You know that, right? You talked to them as if you've known each other a long time."
    teacher "Even if that were the case, there's only so much you should share, with someone like them."

    show alex confused

    alex "I.. I am so sorry teacher."
    
    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home... She doesn't sound happy.{/i}"

    show alex angry at center, alex_adjust
    with dissolve

    alex "Hey, [player_name], my teacher yelled at me today. She said I wrote a terrible email to the mayor."
    alex "And whose fault is that?"
    alex "YOURS!" with vpunch

    "{i}Darn it.{/i}"

    me "I'm so sorry Alex, I must've gotten caught up in the excitement."

    alex "Ugh.. Why do I keep listening to you."

    show alex sad

    alex "It's fine... I guess."

    jump intermission

label school_act_two_good:
    show teacher happy
    teacher "I loved the way you wrote that email to the mayor!"
    teacher "They even reached back out to me! They wanted to help the school out."
    teacher "You did a wonderful job, Alex!"

    alex "Thank you, teacher!"

    
    window hide

    scene bg bedroom
    with fade

    window show

    "{i}Alex returned home... She sounded very happy.{/i}"

    show alex at center, alex_adjust
    with dissolve

    alex "Hey, [player_name], my teacher praised me today. She said I wrote an amazing email to the mayor."
    alex "And who do I have to thank for that?"
    alex "YOU! Thank you so much!"

    "{i}I'm glad everything worked out.{/i}"

    me "I'm so happy for you, Alex! I'm glad everything is going your way."

    alex "I'm so happy too! Thanks, [player_name]!"

    jump intermission

label intermission:
    window hide

    scene black
    with fade

    show text "Years pass. Alex went through high school, writing even more emails." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "Now, as she's older, she's moving on..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    window show

    "Today is another important day."
    "Your sister, Alex, is beginning her first job."
    "Which would be amazing...{w=0.8}Except for one small detail..."
    "{size=+20}Alex {i}still{/i} can't write emails...!!!{/size}" with vpunch

    window hide

    scene bg bedroom
    with fade

    window show

    show alex office at center, alex_adjust
    with dissolve

    alex "Hey [player_name], I'll be heading off to work now!"

    "{i}The years may have passed.. but some things never change do they?{/i}"

    me "Aren't you forgetting something?"

    alex "No..?"

    me "I'm the one dropping you off, remember?"

    alex "Oh! I almost forgot! Let's go, then?"

    me "Hold on now just a moment. I should be asking you..."
    me "Have you finally learned how to write emails? I did teach you all those years go, didn't I?"

    alex "Sure I did! I made a promise to you."

    me "Alright..."

    "{i}Those were only the basics though, and she mainly sent emails to her friends. Does she plan on sending the same
    type of emails to her boss?{/i}"

    alex "Alright already, let's go!"

    window hide

    scene black
    with fade

    window show

    me "That was quite a lot of traffic. We managed to reach just in time."
    me "Anyways, have a great day! It's your very first day at your very first job!"

    alex "Thank you, [player_name]! Remember, you have to pick me up at 5, okay?"

    me "You got it! See you then."

    jump office_act_one

label office_act_one:
    window hide

    scene bg office
    with fade

    window show

    show alex office at right, alex_adjust, alex_dual_adjust
    show boss at left

    boss "Ah.. you're the new hire. Nice to meet you, I'm Boss."

    alex "Uhm.. nice to m-meet you, Boss."

    boss "What's wrong? Cat got your tongue?"
    boss "Oh right I forgot, this is your first job."

    show alex office sad

    alex "Yeah, I guess you could say I'm a bit nervous ma'am."

    boss "That's fine, I don't expect much from you anyways."

    show alex office confused

    alex "Oh, okay. Thank you."

    boss "All I need from you is to draft and send a few emails for me. You think you can handle that?"

    show alex office

    alex "O-of course..!"

    show boss happy

    boss "Good. Still, we need to follow standard procedure..."
    boss "So I'll be asking you a question regarding procedures."

    show boss

    alex "Understood ma'am."

    boss "Here you go, which one of these is an acceptable way to address someone within our organisation?"

    menu trick_question:
        "Which one of these is an acceptable way to address someone within our organisation?"

        "Yo":
            pass

        "What's up":
            pass

        "Heyyyyyyyyyy":
            pass

    show boss angry

    boss "Hmm. Is that your choice? That is a bit..{w=0.5} concerning."

    show alex office confused

    alex "What do you mean? Is it wrong?"

    show boss

    boss "Very much so, if this is how you would address any of your coworkers, your first job will be a short one."

    alex "Wh-what?!"

    boss "Don't worry though, I'm sure you'll adapt in no time."

    window hide

    scene black
    with fade

    show text "A few hours later" with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
    scene bg bedroom
    with fade

    window show

    me "So we're back! What's up? You look upset."

    show alex office sad at center, alex_adjust

    alex "I don't wanna talk about it."

    me "Did you get told off already?"

    alex "How could you tell [player_name]?"

    me "Let me guess further, you wrote a bad email didn't you?"

    show alex office angry

    alex "How did you know???"

    me "I'm your sibling, I've watched you write atrocious emails my entire life."

    show alex office

    alex "I guess so..."
    alex "But I really need your help. My boss told me I need to sharpen my email-writing skills."

    me "And...?"

    show alex office angry

    alex "AND THAT I COULD BE FIRED IF I DON'T GET BETTER AT WRITING EMAILS!" with vpunch

    show alex office

    me "Well you should've seen this coming. I've been telling you the same thing since high school."

    alex "I remember..."

    if s_act1_score == -1 and s_act2_score == -1:
        alex "I also remember how you embarassed me in front of my teacher so many times."
    elif s_act1_score == 1 and s_act2_score == 1:
        alex "I also remember how you helped me through all the emails I had to write then."
    else:
        alex "I also remember how you yourself aren't a perfect genius when it comes to emails."

    alex "No matter though, I still need your help [player_name]. I cannot get fired!"

    me "Well okay, now that you're working, I think it's time you learn some things that even school wouldn't have taught you."

    alex "Like what?"

    me "Well for instance, the tone of your email."
    me "The way you write the content of your emails should change depending on who you're sending the email to."

    alex "So you're saying there's a difference between sending an email to a friend of mine and sending a mail to a colleague."

    me "Yeah exactly..."
    me "You can't be emailing your coworkers the same way you would friends."
    me "Which means no slang or abbreviations like \"LOL\" or \"omw\""

    alex "No nicknames or shortcuts either then?"

    me "Yep"

    alex "Alright, so no shortcuts, formal text and greetings, and no slang, got it."
    alex "Anything else I need to keep in mind?"

    me "Well tone won't matter if you send the email to the wrong people."
    me "You'll be sending emails to a lot more than just one person now."
    me "Say, have you ever seen the little {color=#9C59D1}cc:{/color} and {color=#9C59D1}bcc:{/color} fields underneath the
    {color=#9C59D1}to:{/color} field?"

    alex "I have, but I'm not sure what they're for. I've never had to use them."

    me "That's alright. So what you need to know is that CC stands for {color=#9C59D1}Carbon Copy{/color} and is used to loop people in."
    me "When you put someone's address in CC, everyone gets to know who got the message."
    me "You should use it when the information you're sending in your email is relevant to multiple people."

    alex "Got it! What about BCC?"

    me "That's {color=#9C59D1}Blind Carbon Copy{/color}. People in the BCC field get the email itself, but they have no clue about
    who else received it, not even other BCC participants."

    alex "So it's kind of like...{w=0.5}A secret copy?"

    me "Yeah exactly, it's for when you need to inform someone privately, or when you're emailing a group and want to maintain
    the group members' anonymity."

    alex "Got it... I think."

    me "That's alright, you'll take time to wrap your head around these."

    alex "Mhmm, thank you again [player_name]!"

    jump office_act_two

label office_act_two:
    window hide

    scene black
    with fade

    show text "A few days later..." with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    
    scene bg office
    with fade

    window show

    show alex office at right, alex_adjust, alex_dual_adjust
    show boss at left
    with dissolve

    boss "Hello Alex, today I need you to send out a few emails in the coming few days."
    boss "We have some new clients and we need to help out with the onboarding process."
    boss "We also have to send out that group survey."

    alex "Understood boss, I'll get on that right away!"

    window hide

    scene bg bedroom
    with fade

    window show

    show alex office at center, alex_adjust
    with dissolve

    me "Welcome back Alex, how was work today."

    alex "Work was fine. My boss asked me to send some emails out and I'm just not sure how to do it."

    "{i}Didn't I teach her how to do this a few days ago?{/i}"

    me "Alright, what do you need to do?"

    alex "Well first I need to send an email to a new client of ours..."
    alex "I know you said something about tone, but I can't seem to remember what to do."
    alex "Could you help me out [player_name]?"

    menu tone_menu:
        "How should Alex write this email?"

        "Take a casual tone":
            me "I think you should take a casual tone."
            me "It conveys a friendliness."

            alex "Hmm, I don't think that's right, I'll still trust you on this one"

        "Take a formal and serious tone":
            me "You need to maintain a formal tone with them remember?"
            me "They're not your friends."

            alex "You're right, a formal tone it is!"

            $ o_tone_f = True

    alex "That's the first email done..."
    alex "Now my boss told me to send out an email regarding a group survey."
    alex "I remember something about using the {color=#9C59D1}cc:{/color} and {color=#9C59D1}bcc:{/color} fields but I can't remember which one
    to use."
    
    menu cc_menu:
        "What field should Alex write the participant's emails in?"

        "BCC":
            me "Write it in the bcc field."
            me "It's important to maintain anonymity when it comes to surveys."

            alex "Of course! I remember you talking about this earlier now, okay!"

            $ o_cc_f = True

        "CC":
            me "Write it in the cc field."
            me "It's important for all of them to know each other and about the group."

            alex "I don't think that's right but okay.."

    alex "Alright, that's all the emails done!"
    alex "Thanks again [player_name]!"

    me "Of course Alex, anytime."

    "{i}I hope I made the right choices...{/i}"

    window hide

    scene black
    with fade

    show text "Alex returns to the office the next day..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg office
    with fade

    show alex office at right, alex_adjust, alex_dual_adjust
    show boss at left
    with dissolve

    if o_tone_f:
        jump office_good_tone
    else:
        jump office_bad_tone

label office_good_tone:
    boss "Hey Alex, our clients loved our pitch, you did an amazing job with that email!"

    alex "R-Really? Oh I mean, thank you so much boss!"

    $ o_jf = 1

    if o_cc_f:
        jump office_good_cc
    else:
        jump office_bad_cc

label office_bad_tone:
    show boss angry

    boss "Alex!!!" with vpunch
    
    show alex office confused

    alex "Y-yes boss?"

    boss "You did a terrible job with that email, we just lost our latest clients!"
    boss "What posssessed you to talk to them like you would friends?"

    alex "I-.. I'm so sorry boss"

    $ o_jf = -1

    if o_cc_f:
        jump office_good_cc
    else:
        jump office_bad_cc

label office_good_cc:
    if o_jf == 1:
        boss "And, you know what?"
        boss "That group survey was such a success."
        
        show boss happy

        boss "You did a great job Alex."

        alex "Thank you so much boss!"

        $ office_score = 2

        jump intermission_two

    else:
        boss "But about the group survey..."
        boss "You at least did good on that, our results were great."

        show alex office sad

        alex "Thank you boss"

        $ office_score = 1

        jump intermission_two

label office_bad_cc:
    if o_jf == 1:
        boss "But about the group survey..."
        boss "You messed up bad Alex"
        boss "You used the CC field and now we're getting complaints about people's emails being shared around."
        boss "This isn't good."

        show alex office sad

        alex "I'm so sorry boss"

        $ office_score = 1
    else:
        boss "And you even messed up the group survey"
        boss "You used the CC fields and now we're getting complains left, right and center about people's emails being shared."
        boss "You're on thin ice Alex."

        show alex office sad

        alex "I-I'm.. so sorry boss"

        $ office_score = -1

        jump intermission_two

label intermission_two:
    window hide

    scene black
    with fade

    show text "Alex returns home" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene bg bedroom
    with fade

    window show

    $ school_score = s_act1_score + s_act2_score

    if school_score == -2 and office_score == -1:
        jump ending_three
    elif school_score == 2 and office_score == 2:
        jump ending_one
    else:
        jump ending_two

label ending_one:
    # The good ending!

    show alex office at center, alex_adjust
    with dissolve

    alex "Hey [player_name]! You wanna know what happened today?"

    me "Yeah, of course, what's up?"

    alex "My boss complimented me!"
    alex "She said I did an amazing job at everything and now I'm possibly in line for a promotion even!"

    me "Wow Alex, that's amazing, I'm so happy for you"

    alex "It's all thanks to you [player_name]."
    alex "If you didn't teach me about emails across all those years, I wouldn't have been able to do it."
    alex "Thank you..."

    window hide

    scene black
    with fade

    show text "Ending 1: The Good Ending" with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    jump end

label ending_two:
    if office_score == -1 and school_score < 2:
        show alex office angry at center, alex_adjust
        with dissolve

        alex "Hey [player_name]! What is wrong with you?"

        me "What happened? What do you mean?"

        alex "You embarassed me in front of my boss.."
        alex "You told me all the wrong things!"

        me "What, wait I didn't mean to do that."

        alex "I'm at least glad you didn't mess up my school life completely."
        alex "Ugh"

    elif office_score == 2 and school_score == -2:
        show alex office at center, alex_adjust
        with dissolve

        alex "Hey [player_name]! You wanna know what happened today?"

        me "Yeah, of course, what's up?"

        alex "My boss complimented me!"
        alex "She said I did an amazing job at everything and now I'm possibly in line for a promotion even!"

        me "Wow Alex, that's amazing, I'm so happy for you"

        alex "It's all thanks to you."
        alex "Even though you embarassed me in high school, at least you pulled through now."

    else:
        show alex at center, alex_adjust
        with dissolve

        alex "Hey [player_name]! You wanna know what happened today?"
        
        me "Yeah, of course, what's up?"

        alex "My boss complimented me!"
        alex "But she also said I messed up a little. That's okay though, I know you aren't perfect.."

        if s_body_f:
            alex "You helped me get body details of an email right"
        else:
            alex "You got body details of an email wrong"

        if s_subject_f:
            alex "You helped me craft the ideal subject line"
        else:
            alex "You messed up even the subject lines of emails"

        if o_tone_f:
            alex "You helped me understand tone."
        else:
            alex "You confused me about tone."

        if o_cc_f:
            alex "You helped me know the different kinds of receivers"
        else:
            alex "You did a bad job of explaining receievers to me."

        alex "You're not perfect, but I wish you did better"

    window hide

    scene black
    with fade

    show text "Ending 2: The Neutral Ending" with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    jump end

label ending_three:
    show alex office sad at center, alex_adjust
    with dissolve

    alex "Hey [player_name]... I know I haven't been the best sister always.."
    alex "But did you really need to mess my life up and embarass me so much?"
    alex "All the way back in high school... and now even at work"
    alex "It seems like you're always telling me the wrong things."
    alex "I might as well be better off on my own.."
    alex "Goodbye [player_name]."

    window hide

    scene black
    with fade

    show text "Ending 3: The Bad Ending" with dissolve
    with Pause(5)

    hide text with dissolve
    with Pause(1)

    jump end

label end:
    # END (ME)
    return
