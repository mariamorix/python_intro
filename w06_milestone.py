from tracemalloc import start
from wsgiref.util import shift_path_info


input ("""Welcome to Adventure Game!

In this text-based adventure game, you will be presented with a scenario with different options. 
Depending on the option they choose, they have different consequences, which in turn present different choices for the next action. 

Good luck! 

PRESS ENTER""")

scenario = input ("""
Please choose your scenario: 

Castle
Forest

""")

if scenario.lower() == "castle" :
   print("""
                     Starting Castle Simulation

   """)
   first_question = input("""   
You are trapped in an old castle, you must retrive the key to open the door and leave. 
Otherwise, you will stay in this castle FOREVER! MUAHAHAHAHA!!!!!!!! 
Choose an item: FLASHLIGHT OR A MATCH. """)
   if first_question.lower() == "flashlight" :
        second_question = input("""
You pick up the flashlight and turn it on. You are in the living room of the castle and it's huge! But just a few 
things call your attention: a door, a stair and ... wait! There is a message in the wall! 
Will you OPEN THE DOOR, CLIMB THE STAIRS or READ THE MESSAGE?  """)
        if second_question.lower() in ("open the door","open","door","open door") :
            third_question = input ("""
The door leads you to a hallway that gives you access to the kitchen.
You notice some objects on the table, among them are: a KNIFE, a NOTE, a CAT'S RATTLE. 
What will you pick up? """)
            if third_question.lower() in ("knife", "a knife") :
                fourth_question = input("""
This knife doesn't seem very special, but at least you feel safe! You keep exploring and as you do, the ghost of the Queen's made shows up in front of you!
Will you use the knife to DEFEND yourself, RUN, or try to CONTACT her?""")
                if fourth_question.lower() == "defend" :
                    print("""
Did you really believe that a knife would help you fight a ghost? 
The ghost of the Queen's made is offended and because of that she will never allow you to scape. You will be trapped here FOREVER!! 

*********GAME OVER*********""")
                if fourth_question.lower() == "run" :
                    fifth_question = input("""
You are running scared, it feels like your heart is going to get out of your chest. 
You reach the end of the hall, there is no scape from the ghost except for two doors. One on the LEFT and the other on the RIGHT. Which door will you open?""")
                    if fifth_question.lower() == "left" :
                        print("""
You feel safe for a few seconds, but this castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                    if fifth_question.lower() == "right" :  
                        sixth_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                        if sixth_question.lower() == "play" :
                            seventh_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if seventh_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if seventh_question.lower() == "talk" :
                                eighth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if eighth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "contact" :
                    fifth_question = input ("""
You were brave and talked to the Queen's made ghost. She told you that the spirit of the Queen is still at the Castle taking care of her beloved white cat!
Maybe if you find the cat, you can use him to get into the Queen's graces and leave the castle! 
Are you ready to try? YES or NO. """)
                    if fifth_question.lower() == "yes":
                        sixth_question = input("""
You started to look everywhere, trying to find the Queen's cat! You reach the end of the hall, there's only two doors: one in your left and the other in your right.
Which door will you open? LEFT OR RIGHT? """)
                        if sixth_question.lower() == "left" :
                            print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input(""" 
Congratulations! You've found it, 3 cats: a black, a brown and a white!
Will you PLAY with them or will you IGNORE them?""")
                            if seventh_question.lower() == "play":
                                eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                if eighth_question.lower() == "close" :
                                   print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                if eighth_question.lower()  == "talk" :
                                    ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                    if  ninth_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "brown" :
                                       print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "white" :
                                       print("""
Correct! 

*********GAME OVER*********""")
                            if seventh_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no":   
                        sixth_question = input("""
If that is your decision, okay! But be aware the Queen's ghost is walking freely in the Castle! Will you keep exploring? YES or NO. """)
                        if sixth_question.lower() == "yes" :
                            seventh_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open? """)
                            if seventh_question.lower == "left" :
                                print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if seventh_question.lower == "right" :
                                eighth_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                                if eighth_question.lower() == "play" :
                                    ninth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if ninth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "talk" :
                                        tenth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if tenth_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower == "brown" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower == "white":
                                             print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                                if eighth_question.lower() == "ignore" :
                                     print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                        if sixth_question.lower() == "no" :
                            print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER*********""")
            if third_question.lower() in ("note", "a note") :
                fourth_question = input("""""
You pick up the note and realize that it belongs to the Queen's made. It says:

                The Queen is sick, she doesn't have much time. She wants to say goodbye to her beloved cat: Dave. 
                I have to find him!

Even though the Queen's death was expected, it happened sunddenly. She wasn't able to say goodbye to her cat!
Now her sprit is wandering the Castle, looking for the beloved Cat. 
Will you look for the cat, so she can rest in peace finally? YES or NO  """"")
                if fourth_question.lower() == "yes" :
                    fifth_question = input("""
You start looking everywhere until you reach the end of a hall. There are two doors: one in the RIGHT and the other in the LEFT. 
Which will you open? """)
                    if fifth_question.lower() == "left" :
                        print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                    if fifth_question.lower() == "right" :
                        sixth_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if sixth_question.lower() == "play" :
                            seventh_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if seventh_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if seventh_question.lower() == "talk" :
                                eighth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if eighth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "no" : 
                    fifth_question = input("""
You get rid of the note without even reading it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                    if fifth_question.lower() == "yes" :
                        sixth_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                        if sixth_question.lower() == "left" :
                            print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if seventh_question.lower() == "play" :
                            eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if eighth_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if eighth_question.lower() == "talk" :
                                ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if ninth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no" :
                        print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
            if third_question.lower() in ("a cat's rattle", "cat's rattle","rattle") :
                fourth_question = input("""
What an weird thing to be found in a kitchen. Will you RING it or will you TOSS it on the trash?""")
                if fourth_question.lower() == "ring" :
                    fifth_question = input("""
You ring the cat's rattle and 3 cats comes into your direction. One is black, the other is brown and the third cat is white.
They come to you and are now waiting for you to play with them.
Will you PLAY with them or will you IGNORE them?""")
                    if fifth_question.lower() == "play" :
                        sixth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?""")
                        if sixth_question.lower() == "close" :
                             print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                        if sixth_question.lower() == "talk" :
                            seventh_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                            if  seventh_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                            if seventh_question.lower()  == "brown" :
                                       print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                            if seventh_question.lower()  == "white" :
                                       print("""
Correct! 

*********GAME OVER*********""")
                    if fifth_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "toss" :
                    fifth_question = input("""
You get rid of the rattle, it's seems stupid keep it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                    if fifth_question.lower() == "yes" :
                        sixth_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                        if sixth_question.lower() == "left" :
                            print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if seventh_question.lower() == "play" :
                            eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if eighth_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if eighth_question.lower() == "talk" :
                                ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if ninth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no" :
                        print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
        if second_question.lower() in ("climb the stairs","climb","stairs","climb stairs") :
            third_question = input("""
You climb the stairs and get into the King's bedroom. It's huge! You see right in front of you a big window and next to it, a paiting. 
Will try to flee by using the WINDOW or will you look at the PAITING? """)
            if third_question.lower() == "window" :
                print("""
OH NO!!! The fall is too high! We warned you that the only way to scape was by retriving the key!
You are now a ghost is the castle!
*********GAME OVER********* """)
            if third_question.lower() == "paiting" :
                fourth_question = input("""
You go take a look at the King's paiting. He seemed a weird guy! While you are looking at it, something crazy happens! 
The King's ghost show up! After the initial shock, you must decide: will IGNORE this crazy situation or will you TALK to him? """)
                if fourth_question.lower() == "ignore" :
                    print("""
The King is not used to be ignored! He feels really offended by it!
He is never going to let you leave!
You will be locked up here FOREVER!
*********GAME OVER********* """)
                if fourth_question.lower() == "talk" :
                    fifth_question = input("""
The King seems weird, but he is a nice guy after all! Well ... a nice ghost!
He is willing to let you go, but first you must answer a riddle!
The riddle? “What has four legs in the morning, two at noon, and three in the evening?” DOG, MEN OR DRAGON? """)
                    if fifth_question.lower() == "dog" :
                        print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                    if fifth_question.lower() == "dragon" :
                        print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                    if fifth_question.lower() == "men" :
                        print("""
"My Dear Friend, that is right! A deal is a deal, you are free to go! Here is the key! " - The King says to you.

Congratulations! You've reached the end of this game!
""")
        if second_question.lower() in ("read the message","read", "message", "read message") :
            print("""
||||||||| GHOSTS ARE CRAZY AND SCARY |||||||||
|||||||||||||| ARE THEY TELLING THE TRUTH? ||||||||||||||
||||||||||||||||||| ONLY THE TRULY BRAVE WILL FIND OUT! |||||||||||||||||||""")
            third_question = input("""
This message is creepy! But because of it, you can have an idea of what to expect. 
Will you continue your adventure by opening the DOOR or taking the STAIRS?""")
            if third_question.lower() == "door" :
                 fourth_question = input ("""
The door leads you to a hallway that gives you access to the kitchen.
You notice some objects on the table, among them are: a KNIFE, a NOTE, a CAT'S RATTLE. 
What will you pick up? """)
                 if fourth_question.lower() in ("knife", "a knife") :
                    fifth_question =  input("""
This knife doesn't seem very special, but at least you feel safe! You keep exploring and as you do, the ghost of the Queen's made shows up in front of you!
Will you use the knife to DEFEND yourself, RUN, or try to CONTACT her?""")
                    if fifth_question.lower() == "defend" :
                        print("""
Did you really believe that a knife would help you fight a ghost? 
The ghost of the Queen's made is offended and because of that she will never allow you to scape. You will be trapped here FOREVER!! 

*********GAME OVER*********""")
                    if fifth_question.lower() == "run" :
                        sixth_question = input("""
You are running scared, it feels like your heart is going to get out of your chest. 
You reach the end of the hall, there is no scape from the ghost except for two doors. One on the LEFT and the other on the RIGHT. Which door will you open?""")
                        if sixth_question.lower() == "left" :
                         print("""
You feel safe for a few seconds, but this castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                            if seventh_question.lower() == "ignore" :
                                print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                            if seventh_question.lower() == "play" : 
                                eighth_question =  input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                if eighth_question == "close" :
                                    print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                if eighth_question.lower == "talk" :
                                    ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                    if ninth_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""") 
                                    if ninth_question.lower() == "brown" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""") 
                                    if ninth_question.lower() == "white" :
                                        print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                    if fifth_question.lower() == "contact" :
                        sixth_question = input ("""
You were brave and talked to the Queen's made ghost. She told you that the spirit of the Queen is still at the Castle taking care of her beloved white cat!
Maybe if you find the cat, you can use him to get into the Queen's graces and leave the castle! 
Are you ready to try? YES or NO. """)
                        if  sixth_question.lower() == "yes":
                            seventh_question = input("""
You started to look everywhere, trying to find the Queen's cat! You reach the end of the hall, there's only two doors: one in your left and the other in your right.
Which door will you open? LEFT OR RIGHT? """)
                            if  seventh_question.lower() == "left" :
                                print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if  seventh_question.lower() == "right" :
                                eighth_question = input(""" 
Congratulations! You've found it, 3 cats: a black, a brown and a white!
Will you PLAY with them or will you IGNORE them?""")
                                if  eighth_question.lower() == "play":
                                    ninth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if ninth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if ninth_question.lower()  == "talk" :
                                        tenth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if  tenth_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "brown" :
                                             print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "white" :
                                            print("""
Correct! 

*********GAME OVER*********""")
                            if eighth_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if sixth_question.lower() == "no":   
                        seventh_question = input("""
If that is your decision, okay! But be aware the Queen's ghost is walking freely in the Castle! Will you keep exploring? YES or NO. """)
                        if seventh_question.lower() == "yes" :
                            eighth_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open? """)
                            if eighth_question.lower() == "left" :
                                print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if eighth_question.lower() == "right" :
                                ninth_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                                if ninth_question.lower() == "play" :
                                    tenth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if tenth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if tenth_question.lower() == "talk" :
                                        eleventh_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if eleventh_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if eleventh_question.lower() == "brown" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if eleventh_question.lower() == "white":
                                             print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                                if ninth_question.lower() == "ignore" :
                                     print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                        if seventh_question.lower() == "no" :
                            print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER*********""")
                 if fourth_question.lower() in ("note", "a note") :
                    fifth_question = input("""""
You pick up the note and realize that it belongs to the Queen's made. It says:

                The Queen is sick, she doesn't have much time. She wants to say goodbye to her beloved cat: Dave. 
                I have to find him!

Even though the Queen's death was expected, it happened sunddenly. She wasn't able to say goodbye to her cat!
Now her sprit is wandering the Castle, looking for the beloved Cat. 
Will you look for the cat, so she can rest in peace finally? YES or NO  """"")
                    if fifth_question.lower() == "yes" :
                        sixth_question = input("""
You start looking everywhere until you reach the end of a hall. There are two doors: one in the RIGHT and the other in the LEFT. 
Which will you open? """)
                        if sixth_question.lower() == "left" :
                            print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                            if seventh_question.lower() == "play" :
                                eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                if eighth_question.lower() == "close" :
                                    print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                if eighth_question.lower() == "talk" :
                                    ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                    if ninth_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "brown" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "white" :
                                        print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                            if seventh_question.lower() == "ignore" :   
                                print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no" : 
                        sixth_question = input("""
You get rid of the note without even reading it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                        if sixth_question.lower() == "yes" :
                            seventh_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                            if seventh_question.lower() == "left" :
                                print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if seventh_question.lower() == "right" :
                                eighth_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                                if eighth_question.lower() == "play" :
                                    ninth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if ninth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "talk" :
                                        tenth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if tenth_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "brown" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "white" :
                                            print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                                if eighth_question.lower() == "ignore" :   
                                    print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                        if sixth_question.lower() == "no" :
                            print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
                 if fourth_question.lower() in ("a cat's rattle", "cat's rattle", "rattle") :
                    fifth_question = input("""
What an weird thing to be found in a kitchen. Will you RING it or will you TOSS it on the trash?""")
                    if fifth_question.lower() == "ring" :
                        sixth_question = input("""
You ring the cat's rattle and 3 cats comes into your direction. One is black, the other is brown and the third cat is white.
They come to you and are now waiting for you to play with them.
Will you PLAY with them or will you IGNORE them?""")
                        if sixth_question.lower() == "play" :
                            seventh_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?""")
                            if seventh_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if seventh_question.lower() == "talk" :
                                eighth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if   eighth_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if  eighth_question.lower()  == "brown" :
                                       print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if  eighth_question.lower()  == "white" :
                                       print("""
Correct! 

*********GAME OVER*********""")
                        if sixth_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "toss" :
                        sixth_question = input("""
You get rid of the rattle, it's seems stupid keep it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                        if sixth_question.lower() == "yes" :
                            seventh_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                            if seventh_question.lower() == "left" :
                                print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if seventh_question.lower() == "right" :
                                eighth_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                                if  eighth_question.lower() == "play" :
                                    ninth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if ninth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "talk" :
                                        tenth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if tenth_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "brown" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower() == "white" :
                                            print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                                if  eighth_question.lower() == "ignore" :   
                                    print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                        if sixth_question.lower() == "no" :
                            print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
            if third_question.lower() == "stairs" :
                fourth_question =  input("""
You climb the stairs and get into the King's bedroom. It's huge! You see right in front of you a big window and next to it, a paiting. 
Will try to flee by using the WINDOW or will you look at the PAITING? """)
                if fourth_question.lower() == "window" :
                    print("""
OH NO!!! The fall is too high! We warned you that the only way to scape was by retriving the key!
You are now a ghost is the castle!
*********GAME OVER********* """)
                if fourth_question.lower() == "paiting" :
                    fifth_question = input("""
You go take a look at the King's paiting. He seemed a weird guy! While you are looking at it, something crazy happens! 
The King's ghost show up! After the initial shock, you must decide: will IGNORE this crazy situation or will you TALK to him? """)
                    if fifth_question.lower() == "ignore" :
                        print("""
The King is not used to be ignored! He feels really offended by it!
He is never going to let you leave!
You will be locked up here FOREVER!
*********GAME OVER********* """)
                    if fifth_question.lower() == "talk" :
                        sixth_question = input("""
The King seems weird, but he is a nice guy after all! Well ... a nice ghost!
He is willing to let you go, but first you must answer a riddle!
The riddle? “What has four legs in the morning, two at noon, and three in the evening?” DOG, MEN OR DRAGON? """)
                        if sixth_question.lower() == "dog" :
                            print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                        if sixth_question.lower() == "dragon" :
                            print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                        if sixth_question.lower() == "men" :
                             print("""
"My Dear Friend, that is right! A deal is a deal, you are free to go! Here is the key! " - The King says to you.

Congratulations! You've reached the end of this game!
""")
   if first_question.lower() in ("a match", "match") :
       second_question = input("""
You pick up the match and strike it, and for an instant, the room around you is illuminated. You are in the living room of the castle and it's huge! 
Quickly you notice a door and a stair. But as fast as the room was illuminated, it goes back to be completly dark. You try to remember the path!
What path will you follow: DOOR or STAIRS. """)
       if second_question.lower() in ("door") :
            third_question = input ("""
The door leads you to a hallway that gives you access to the kitchen.
You notice some objects on the table, among them are: a KNIFE, a NOTE, a CAT'S RATTLE. 
What will you pick up? """)
            if third_question.lower() in ("knife", "a knife") :
                fourth_question = input("""
This knife doesn't seem very special, but at least you feel safe! You keep exploring and as you do, the ghost of the Queen's made shows up in front of you!
Will you use the knife to DEFEND yourself, RUN, or try to CONTACT her?""")
                if fourth_question.lower() == "defend" :
                    print("""
Did you really believe that a knife would help you fight a ghost? 
The ghost of the Queen's made is offended and because of that she will never allow you to scape. You will be trapped here FOREVER!! 

*********GAME OVER*********""")
                if fourth_question.lower() == "run" :
                    fifth_question = input("""
You are running scared, it feels like your heart is going to get out of your chest. 
You reach the end of the hall, there is no scape from the ghost except for two doors. One on the LEFT and the other on the RIGHT. Which door will you open?""")
                    if fifth_question.lower() == "left" :
                        print("""
You feel safe for a few seconds, but this castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                    if fifth_question.lower() == "right" :  
                        sixth_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                        if sixth_question.lower() == "play" :
                            seventh_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if seventh_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if seventh_question.lower() == "talk" :
                                eighth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if eighth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "contact" :
                    fifth_question = input ("""
You were brave and talked to the Queen's made ghost. She told you that the spirit of the Queen is still at the Castle taking care of her beloved white cat!
Maybe if you find the cat, you can use him to get into the Queen's graces and leave the castle! 
Are you ready to try? YES or NO. """)
                    if fifth_question.lower() == "yes":
                        sixth_question = input("""
You started to look everywhere, trying to find the Queen's cat! You reach the end of the hall, there's only two doors: one in your left and the other in your right.
Which door will you open? LEFT OR RIGHT? """)
                        if sixth_question.lower() == "left" :
                            print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input(""" 
Congratulations! You've found it, 3 cats: a black, a brown and a white!
Will you PLAY with them or will you IGNORE them?""")
                            if seventh_question.lower() == "play":
                                eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                if eighth_question.lower() == "close" :
                                   print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                if eighth_question.lower()  == "talk" :
                                    ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                    if  ninth_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "brown" :
                                       print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "white" :
                                       print("""
Correct! 

*********GAME OVER*********""")
                            if seventh_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no":   
                        sixth_question = input("""
If that is your decision, okay! But be aware the Queen's ghost is walking freely in the Castle! Will you keep exploring? YES or NO. """)
                        if sixth_question.lower() == "yes" :
                            seventh_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open? """)
                            if seventh_question.lower == "left" :
                                print("""
You are in a dark room, then you feel a strong breath right in front of you!
This castle has many secrets and one of them is a beast hidden! The fear takes control of you, but then... peace!
Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                            if seventh_question.lower == "right" :
                                eighth_question = input("""
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down it's only tree cats: a black cat, a brown cat and a white cat. Will you PLAY with them or will you IGNORE them?""")
                                if eighth_question.lower() == "play" :
                                    ninth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                                    if ninth_question.lower() == "close" :
                                        print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                                    if ninth_question.lower() == "talk" :
                                        tenth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                        if tenth_question.lower() == "black" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower == "brown" :
                                            print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                        if tenth_question.lower == "white":
                                             print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                                if eighth_question.lower() == "ignore" :
                                     print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                        if sixth_question.lower() == "no" :
                            print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER*********""")
            if third_question.lower() in ("note", "a note") :
                fourth_question = input("""""
You pick up the note and realize that it belongs to the Queen's made. It says:

                The Queen is sick, she doesn't have much time. She wants to say goodbye to her beloved cat: Dave. 
                I have to find him!

Even though the Queen's death was expected, it happened sunddenly. She wasn't able to say goodbye to her cat!
Now her sprit is wandering the Castle, looking for the beloved Cat. 
Will you look for the cat, so she can rest in peace finally? YES or NO  """"")
                if fourth_question.lower() == "yes" :
                    fifth_question = input("""
You start looking everywhere until you reach the end of a hall. There are two doors: one in the RIGHT and the other in the LEFT. 
Which will you open? """)
                    if fifth_question.lower() == "left" :
                        print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                    if fifth_question.lower() == "right" :
                        sixth_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if sixth_question.lower() == "play" :
                            seventh_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if seventh_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if seventh_question.lower() == "talk" :
                                eighth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if eighth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eighth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "no" : 
                    fifth_question = input("""
You get rid of the note without even reading it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                    if fifth_question.lower() == "yes" :
                        sixth_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                        if sixth_question.lower() == "left" :
                            print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if seventh_question.lower() == "play" :
                            eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if eighth_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if eighth_question.lower() == "talk" :
                                ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if ninth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no" :
                        print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
            if third_question.lower() in ("a cat's rattle", "cat's rattle") :
                fourth_question = input("""
What an weird thing to be found in a kitchen. Will you RING it or will you TOSS it on the trash?""")
                if fourth_question.lower() == "ring" :
                    fifth_question = input("""
You ring the cat's rattle and 3 cats comes into your direction. One is black, the other is brown and the third cat is white.
They come to you and are now waiting for you to play with them.
Will you PLAY with them or will you IGNORE them?""")
                    if fifth_question.lower() == "play" :
                        sixth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. 
You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?""")
                        if sixth_question.lower() == "close" :
                             print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                        if sixth_question.lower() == "talk" :
                            seventh_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                            if  seventh_question.lower() == "black" :
                                        print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                            if seventh_question.lower()  == "brown" :
                                       print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                            if seventh_question.lower()  == "white" :
                                       print("""
Correct! 

*********GAME OVER*********""")
                    if fifth_question.lower() == "ignore" :
                                 print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                if fourth_question.lower() == "toss" :
                    fifth_question = input("""
You get rid of the rattle, it's seems stupid keep it. You look around the kitchen, but there is nothing there that will help you leave the castle.
Will you keep exploring? YES or NO. """)
                    if fifth_question.lower() == "yes" :
                        sixth_question = input("""
You keep exploring, until you reach the end of the hall. 
Now you only have two options, two doors, one in the LEFT and the other in the RIGHT.
Which one will you open?""")
                        if sixth_question.lower() == "left" :
                            print("""
You entered in a dark room, and unexpectedly you feel a breathing closer to your face! You can't see a thing! 
This castle has many secrets and one of them is a beast hidden in this same room. 
The fear grows inside of you, but then...peace. Everything ends so fast that you don't even notice! 
You are now a ghost in this castle! 

*********GAME OVER********* """)
                        if sixth_question.lower() == "right" :
                            seventh_question = input("""
You enter the room and you feel so tired! You've been looking for hours!
You breath deep trying to regain your strenghts, but then you feel something in your legs!
Calm down! It's only tree cats: a black cat, a brown cat and a white cat.
Maybe one of them is the Queen's cat!
Will you PLAY with them or will you IGNORE them?""")
                        if seventh_question.lower() == "play" :
                            eighth_question = input("""
While you playing with the cats, the ghost of the Queen shows up. You can't scape, will you CLOSE your eyes and pretend the she is not there or will you face your fears and TALK to her?  """)
                            if eighth_question.lower() == "close" :
                                print("""
The Queen is not used to be ignored! She is so angry! She will never allow you to leave!
You are going to be trapped here FOREVER!

*********GAME OVER*********""")
                            if eighth_question.lower() == "talk" :
                                ninth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if ninth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if ninth_question.lower() == "white" :
                                    print("""
Correct! You are free to go!
Congratulations, you've finished this game!""")    
                        if sixth_question.lower() == "ignore" :   
                            print("""
Ignored, the cats started to meow. They wanted to play with someone, they are alone for such a long time! Their crying caught the attention of the Queen's ghost!
She is mad that her cat is sad! She is never going to let you leave!

*********GAME OVER*********""")
                    if fifth_question.lower() == "no" :
                        print("""
Only an adventurous spirit will find the way out!
You are going to be stuck here forever!
*********GAME OVER********* """)
       if second_question.lower() in ("stairs") :
            third_question = input("""
You climb the stairs and get into the King's bedroom. It's huge! You see right in front of you a big window and next to it, a paiting. 
Will try to flee by using the WINDOW or will you look at the PAITING? """)
            if third_question.lower() == "window" :
                print("""
OH NO!!! The fall is too high! We warned you that the only way to scape was by retriving the key!
You are now a ghost is the castle!
*********GAME OVER********* """)
            if third_question.lower() == "paiting" :
                fourth_question = input("""
You go take a look at the King's paiting. He seemed a weird guy! While you are looking at it, something crazy happens! 
The King's ghost show up! After the initial shock, you must decide: will IGNORE this crazy situation or will you TALK to him? """)
                if fourth_question.lower() == "ignore" :
                    print("""
The King is not used to be ignored! He feels really offended by it!
He is never going to let you leave!
You will be locked up here FOREVER!
*********GAME OVER********* """)
                if fourth_question.lower() == "talk" :
                    fifth_question = input("""
The King seems weird, but he is a nice guy after all! Well ... a nice ghost!
He is willing to let you go, but first you must answer a riddle!
The riddle? “What has four legs in the morning, two at noon, and three in the evening?” DOG, MEN OR DRAGON? """)
                    if fifth_question.lower() == "dog" :
                        print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                    if fifth_question.lower() == "dragon" :
                        print("""
"My Dear Friend, that is not right!" - The King says to you.
Unfortunately he doesn't give second chances! You will stay here FOREVER! 
At least you will have a new friend!
*********GAME OVER*********""")
                    if fifth_question.lower() == "men" :
                        print("""
"My Dear Friend, that is right! A deal is a deal, you are free to go! Here is the key! " - The King says to you.

Congratulations! You've reached the end of this game!
""")
elif scenario.lower() == "forest" :
    print("""
                     Forest Simulation is Under Development!
                     Please try Castle Simulation or come back later!

   """)
else:
    print("""
                     Simulation not available!
                     Try the options available or come back later!

   """)