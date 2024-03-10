# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Jeeth Joseph
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


# -----------------------------------------------------------------------

# ======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
# ======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
        #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
        #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret


# ======================
# Data structure design
# ======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):

    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


# ======================
# Triggers
# ======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        We assume that phrase does not have punctuation
        """
        # We should probably assert to check if phrase is trimmed, has punctuation or multiple spaces

        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        """
        Assumptions -
        Text is string.
        Returns -
        True if phrase is present entirely in text without trailing/starting alphabets
        string.punctuations and spaces are ignored as allowed fillers
        """
        allowed_fillers = string.punctuation + " "

        word_without_punctuation = ""
        # We first replave all punctuation with spaces. We should change definition of phrase if we want to add punctuation
        for char in text.lower():  # can we use map?
            if char not in string.punctuation:
                word_without_punctuation = word_without_punctuation + char
            else:
                word_without_punctuation = word_without_punctuation + " "
        cleaned_text = ""
        # Here we add one whitespace per word
        for word in word_without_punctuation.split():
            cleaned_text = cleaned_text + word + " "
        trimmed_cleaned_text = cleaned_text.strip()  # removing trailing whitespace
        if self.phrase in trimmed_cleaned_text:
            # Case where there are trailing or starting characters
            phrase_index = trimmed_cleaned_text.find(self.phrase)
            try:
                if (trimmed_cleaned_text[phrase_index - 1] not in allowed_fillers) and (
                        trimmed_cleaned_text[phrase_index + len(self.phrase)] not in allowed_fillers):
                    return False
            except IndexError:
                pass

            return True
        else:
            return False


# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, title_phrase):
        PhraseTrigger.__init__(self, title_phrase)

    def evaluate(self, story):
        title = story.get_title()
        return self.is_phrase_in(title)


# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, description_phrase):
        PhraseTrigger.__init__(self, description_phrase)

    def evaluate(self, story):
        story_description = story.get_description()
        return self.is_phrase_in(story_description)


# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, trigger_time):
        """
            Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S"
        """
        #DO NOT USE astimezone
        # self.trigger_time = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S").astimezone(pytz.timezone('EST'))
        # this create a change to the values. We should use replace
        # could have alternatively used replace to return datetime object with new timezone
        self.trigger_time = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S")
        self.trigger_time = self.trigger_time.replace(tzinfo=pytz.timezone("EST"))


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def __int__(self,trigger_time):
        TimeTrigger.__init__(self,trigger_time)

    def evaluate(self, story):

        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.trigger_time


class AfterTrigger(TimeTrigger):
    def __int__(self, trigger_time):
        TimeTrigger.__init__(self, trigger_time)

    def evaluate(self, story):
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.trigger_time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger_to_evaluate = trigger

    def evaluate(self, story):
        return not self.trigger_to_evaluate.evaluate(story)

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    def __init__(self, one_trigger, another_trigger):
        self.one_trigger_to_evaluate = one_trigger
        self.another_trigger_to_evaluate = another_trigger

    def evaluate(self, story):
        return  self.one_trigger_to_evaluate.evaluate(story) and self.another_trigger_to_evaluate.evaluate(story)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    def __init__(self, one_trigger, another_trigger):
        self.one_trigger_to_evaluate = one_trigger
        self.another_trigger_to_evaluate = another_trigger

    def evaluate(self, story):
        return  self.one_trigger_to_evaluate.evaluate(story) or self.another_trigger_to_evaluate.evaluate(story)


# ======================
# Filtering
# ======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    filtered = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                filtered.append(story)
    # print(filtered)
    return filtered


# ======================
# User-Specified Triggers
# ======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_class_dict = {"TITLE":TitleTrigger,
                    "DESCRIPTION":DescriptionTrigger,
                    "AFTER":AfterTrigger,
                    "BEFORE":BeforeTrigger,
                    "NOT":NotTrigger,
                    "AND":AndTrigger,
                    "OR":OrTrigger}
    all_triggers = {}
    trigger_list =[]
    for line in lines:
        if not line.startswith("ADD"):
            command_list = line.split(",")
            trigger_name = command_list[0]
            trigger_class_name = command_list[1]
            trigger_class = trigger_class_dict[trigger_class_name]
            print("trigger",trigger_class_name)

            if trigger_class_name in ("AND", "OR"):
                trigger_parameter1 = command_list[2]
                trigger_parameter2 = command_list[3]
                print(trigger_parameter1, trigger_parameter2)
                try:
                    all_triggers[trigger_name] = trigger_class(all_triggers[trigger_parameter1],all_triggers[trigger_parameter2])
                except NotImplementedError:
                    print("Ingredient not defined")

            else:
                trigger_parameter1 = command_list[2]
                all_triggers[trigger_name] = trigger_class(trigger_parameter1)
        else:
            command_list = line.split(",")
            for trigger_name in command_list[1:]:
                trigger_list.append(all_triggers[trigger_name])
    print(lines)
    print(trigger_list)
    return trigger_list





    # print(lines)  # for now, print it so you see what it contains!


SLEEPTIME = 120  # seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("bjp")
        t2 = DescriptionTrigger("nasa")
        t3 = DescriptionTrigger("astroid")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')

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

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title() + "\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")


            # Get stories from Yahoo's Top Stories RSS news feed
            # Commenting out to fix issue - 20240308 Jeeth
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)


            list(map(get_cont, stories))
            for story in stories:
                print(story.get_title())
            scrollbar.config(command=cont.yview)

            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
