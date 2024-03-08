from mtTkinter import *


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("india")
        # t2 = DescriptionTrigger("nasa")
        # t3 = DescriptionTrigger("astroid")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        # triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        # def get_cont(newstory):
        #     if newstory.get_guid() not in guidShown:
        #         cont.insert(END, newstory.get_title() + "\n", "title")
        #         cont.insert(END, "\n---------------------------------------------------------------\n", "title")
        #         cont.insert(END, newstory.get_description())
        #         cont.insert(END, "\n*********************************************************************\n", "title")
        #         guidShown.append(newstory.get_guid())

        # while True:
        #     print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            # stories = process("http://news.google.com/news?output=rss")


            # Get stories from Yahoo's Top Stories RSS news feed
            # Commenting out to fix issue - 20240308 Jeeth
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            # stories = filter_stories(stories, triggerlist)


            # list(map(get_cont, stories))
            # for story in stories:
            #     print(story.get_title())
            # scrollbar.config(command=cont.yview)
            #
            # print("Sleeping...")
            # time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Test TK parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
