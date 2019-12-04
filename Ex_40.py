# Modlues, Classes and Objects

# mystuff = {'apple': "I AM APPLES!"}
# print(mystuff['apple'])


# class MyStuff(object):

#     def __init__(self):
#         self.tangerine = "And now a thousand years between"

#     def apple(self):
#         print("I AM CLASSY APPLES")


# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I dont want to get sued",
                    "So I stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



made_up_lyrics = Song(["I made up these lines",
                       "because I can and it rhymes",
                       "so it's okay and fine"])


made_up_lyrics.sing_me_a_song()


