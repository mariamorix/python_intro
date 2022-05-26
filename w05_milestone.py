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
Choose an item: FLASHLIGHT OR 3 MATCHES. """)
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
                                eigth_question = input("""
The Queen is amazed by your courage! She is willing to let you go, but before you must answer her question:
Which of the 3 cats is hers? The BLACK, WHITE OR BROWN?""")
                                if eigth_question.lower() == "black" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eigth_question.lower() == "brown" :
                                    print("""
Wrong answer! You will never leave the castle!

*********GAME OVER*********""")
                                if eigth_question.lower() == "white" :
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
                    if fifth_question.lower() == "no":   
                        seventh_question = input("""
If that is your decision, okay! But be aware the Queen's ghost is walking freely in the Castle! Will you keep exploring? YES or NO. """)
                        if seventh_question.lower() == "yes":
                        if seventh_question.lower() == "no":   
            if third_question.lower() in ("note", "a note") : 
            if third_question.lower() in ("cat's rattle", "a cat's rattle", "rattle") :  
        if second_question.lower() in ("climb the stairs","climb","stairs","climb stairs") :
        if second_question.lower() in ("read the message","read","message","read message") :   
   if first_question.lower() in ("matches", "3 matches", "3") :
       input()