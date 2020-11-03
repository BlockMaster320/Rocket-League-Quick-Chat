import pynput

#Set Variables
inputString = "";
keyboard = pynput.keyboard.Controller();

#Add Pressed Number to the inputString
def on_key_press(key):
    global inputString;
    try:    #in case the pressed key cannot be represented as a string
        keyString = key.char;
        if keyString in '1234':
            inputString += keyString;
    except:
        pass;

#Write a Quick Chat Message Based on Pressed Numbers
def on_key_release(key):
    global inputString;
    outputString = '';
    if len(inputString) >= 2:     #choose the message
        if inputString[0] == '1':
            if inputString[1] == '1':
                outputString = 'I got it!';
            if inputString[1] == '2':
                outputString = 'Need boost!';
            if inputString[1] == '3':
                outputString = 'Take the shot!';
            if inputString[1] == '4':
                outputString = 'Defending...';
        if inputString[0] == '2':
            if inputString[1] == '1':
                outputString = 'Nice shot!';
            if inputString[1] == '2':
                outputString = 'Great pass!';
            if inputString[1] == '3':
                outputString = 'Thanks!';
            if inputString[1] == '4':
                outputString = 'What a save!';
        if inputString[0] == '3':
            if inputString[1] == '1':
                outputString = 'OMG!';
            if inputString[1] == '2':
                outputString = 'Noooo!';
            if inputString[1] == '3':
                outputString = 'Wow!';
            if inputString[1] == '4':
                outputString = 'Close one!';
        if inputString[0] == '4':
            if inputString[1] == '1':
                outputString = '$#@%!';
            if inputString[1] == '2':
                outputString = 'No problem.';
            if inputString[1] == '3':
                outputString = 'Whoops...';
            if inputString[1] == '4':
                outputString = 'Sorry!';
        if inputString[0] == '5':
            if inputString[1] == '1':
                outputString = 'On sa točí!';
            if inputString[1] == '2':
                outputString = 'Zabijak zapaty.';
            if inputString[1] == '3':
                outputString = 'POG';
            if inputString[1] == '4':
                outputString = "Today's video is sponsored by Raid Shadow Legends, one of the biggest mobile role-playing games of 2019 and it's totally free! Currently almost 10 million users have joined Raid over the last six months, and it's one of the most impressive games in its class with detailed models, environments and smooth 60 frames per second animations! All the champions in the game can be customized with unique gear that changes your strategic buffs and abilities! The dungeon bosses have some ridiculous skills of their own and figuring out the perfect party and strategy to overtake them's a lot of fun! Currently with over 300,000 reviews, Raid has almost a perfect score on the Play Store! The community is growing fast and the highly anticipated new faction wars feature is now live, you might even find my squad out there in the arena! It's easier to start now than ever with rates program for new players you get a new daily login reward for the first 90 days that you play in the game! So what are you waiting for? Go to the video description, click on the special links and you'll get 50,000 silver and a free epic champion as part of the new player program to start your journey! Good luck and I'll see you there!";

        keyboard.press(pynput.keyboard.Key.backspace);  #delete the typed numbers
        keyboard.release(pynput.keyboard.Key.backspace);
        keyboard.press(pynput.keyboard.Key.backspace);
        keyboard.release(pynput.keyboard.Key.backspace);

        keyboard.release(pynput.keyboard.Key.shift);    #write the message
        keyboard.type(outputString);
        keyboard.press(pynput.keyboard.Key.enter);
        keyboard.press(pynput.keyboard.Key.shift);
        inputString = '';

listener = pynput.keyboard.Listener(on_press = on_key_press, on_release = on_key_release);  #create a listener
with listener:
    listener.join();
