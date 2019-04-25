#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

from googletrans import Translator
translator = Translator()


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    
sentencetext1=translator.translate(("මෙම චිත්රපටය ඉතාමත් නරකයි")).text
sentencetext2=translator.translate(("මෙම චිත්රපටය නරකයි")).text
sentencetext3=("Bumblebee is an incredibly nice breath of fresh air compared to the previous Transformers movies. If you have been scarred or turned off by the Michael Bay version of the franchise, then this movie is certainly a welcomed change of pace.")
sentencetext4=translator.translate(("වීඩියෝ බලනවා. ඒවා හොඳයි..ඒත් මේකනම් චාටර් බං")).text

sentiment_analyzer_scores(sentencetext1)
sentiment_analyzer_scores(sentencetext2)
sentiment_analyzer_scores(sentencetext3)
sentiment_analyzer_scores(sentencetext4)


# In[ ]:





# In[ ]:




