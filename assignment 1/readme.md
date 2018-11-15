**AO3 fandom dataset**
=
"Fandom is a subculture composed of fans characterized by a feeling of empathy and camaraderie with others who share a common interest.fanfiction (also abbreviated to fan fic, fanfic, fic or ff) is fiction about characters or settings from an original work of fiction, created by fans of that work rather than by its creator."(Source：wikipedia)

Achive of Our Own(AO3)is a famous website for fans to share their fanfictions.
This dataset is about to scrape the top5 popular original works in main media genres on the AO3.

Page：https://archiveofourown.org/media

**data fields**

genre - String. e.g.Anime & Manga

fanwork number - Int.e.g.36

original works name - String.e.g Haikyuu!!

**Data Volume**

56 row 3 column

**License**

MIT License


**reference**

https://github.com/hupili/python-for-data-and-media-communication-gitbook/issues/67

I used the following code bolck in this issue answer from @ChicoXYC.


**bonus part**

As a subculture, fandom works are positively related to the exposure on social media of the original works but in the AO3 it also accumulated considerable works on many old series like Stak Trek.So i would like to import twitter data（https://github.com/awesomedata/awesome-public-datasets#socialnetworks） to find the relationship between the popularity of original and number of fanworks. There is a famours myth that a high popularity and fanworks complement each other. I want find if it is true.
