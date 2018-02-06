# -*- coding: utf-8 -*-

class Book:
  def __init__(self, name, author, release, price, type, genre, info, img):
    self.name = name
    self.author = author
    self.release = release
    self.price = price
    self.type = type
    self.genre = genre
    self.info = info
    self.img = img
    self.all = [self.name, self.author, self.release, self.price,
                self.type, self.genre, self.info, self.img]


booklist = [
  Book( "Side Hustle: From Idea to Income in 27 Days",
        "Chris Guillebeau",
        "September 19, 2017",
        14.76,
        "Hardcover",
        "Business & Money",
        "For some people, the thought of quitting their day job to pursue the entrepreneurial "\
        "life is exhilarating. For many others, it’s terrifying. After all, a stable job that delivers "\
        "a regular paycheck is a blessing. And not everyone has the means or the desire to take on the "\
        "risks and responsibilities of working for themselves. But what if we could quickly and easily create "\
        "an additional stream of income without giving up the security of a full-time job? Enter the side hustle. "\
        "Chris Gullibeau is no stranger to this world, having launched more than a dozen side hustles over his "\
        "career. Here, he offers a step-by-step guide that takes you from idea to income in just 27 days. "\
        "Designed for the busy and impatient, this detailed roadmap will show you how to select, launch, "\
        "refine, and make money from your side hustle in under a month.",
        "https://images-na.ssl-images-amazon.com/images/I/517vq64xnCL._SX330_BO1,204,203,200_.jpg"
  ),
  Book( "Create Or Hate: Successful People Make Things",
        "Dan Norris",
        "October 1, 2016",
        7.99,
        "Paperback",
        "Business & Money",
        "Most of us have always wanted to make something, but for any number of reasons haven’t. "\
        "Maybe you used to make things as a child, but stopped some time into adulthood. "\
        "What is that something for you? Writing a book? Creating a blog? Learning photography? "\
        "Starting a podcast? Launching a business? This book exists for only one reason, to help "\
        "you create that something. We are all creative ― there is a creator in you. But there "\
        "is also a force called Hate, which will work against your creativity and stop you from "\
        "making things. Hate can be controlled, and overpowered and your creative side can be "\
        "nurtured and grown. This book will show you how.",
        "https://images-na.ssl-images-amazon.com/images/I/41g%2BWGHUyGL._SX359_BO1,204,203,200_.jpg"
  ),
  Book( "The 7 Day Startup: You Don't Learn Until You Launch",
        "Dan Norris",
        "September 29, 2014",
        14.99,
        "Paperback",
        "Business & Money",
        "From generating ideas to gaining your first paying customers, The 7 Day Startup is the "\
        "bootstrapper’s bible for launching your next product. In it, you will learn: 1. "\
        "Why validation isn’t the answer 2. How to evaluate your business idea 3. How to choose a "\
        "business name, fast 4. How to build a website in 1 day for under $100 5. 10 proven "\
        "ways to market a business quickly And much, much more.",
        "https://images-na.ssl-images-amazon.com/images/I/51lYzDLnOOL._SX332_BO1,204,203,200_.jpg"
  )
]
