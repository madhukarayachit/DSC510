from string import punctuation as pun
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords
import re
import string
##breakdown = swn.senti_synset('breakdown.n.03')
##print (breakdown)

##from nltk.corpus import sentiwordnet as swn

def superNativeSentiment(review):
    reviewPolarity=0.0
    numExceptions=0
    #print('\n' in stopwords)

    for word in review.lower().split():
        weight=0.0
        p=0.0
        n=0.0
        i=0
        try:
            prettyword= ''.join(re.findall(r'\w+',word))
            #prettyword =  word.replace("b'","").strip('\n')
            #prettyword=prettyword.replace('"','')
            prettyword=prettyword.strip(string.punctuation)
            if word.lower() in stopwords:
                continue
            a=[]
            if list(swn.senti_synsets(prettyword)) == a:
                print(word,'  ', prettyword)
                continue
            common_meaning=list(swn.senti_synsets(prettyword))[0]
            p=common_meaning.pos_score()
            n=common_meaning.neg_score()
            if p> n:
                weight=weight+p
            elif n>p:
                weight=weight-n
        except Exception as ex:
            numExceptions+=1
            print('error {} {} {}'.format( ex,word,prettyword))

        ##print('word :{} weight {}  Pos {}  Neg {} '.format(word,str(weight)  ,str(p),str(n) ))
        reviewPolarity=reviewPolarity+weight
    #print('total words {} error count {}'.format(len(review.split()), numExceptions))
    return reviewPolarity

def GetReview(filePath):
    with open(filePath, "rb") as f:
        data = f.readlines()
    return data


def RunDiagnostic(reviewResult):
    posScore=reviewResult['positivescore']
    negScore=reviewResult['negativescore']

    pctTruePositive = posScore) / len(po))
    pctTrueNegative = f negScore) / len(negScore))

    TotalAccurate = float( sum(x > 0 for x in posScore)) + float(sum(x < 0 for x in negScore))
    total = len(posScore) + len(negScore)

    print('Accuracy on positive reviews :  {:.2f}%'.format(pctTruePositive * 100))
    print('Accuracy on negative reviews :  {:.2f}%'.format(pctTrueNegative * 100))
    print('Overall Accuracy             :  {:.2f}%'.format(TotalAccurate * 100 / total))



if __name__ == '__main__':
    posFile='SampleData/rt-polarity1.txt'
    negFile='SampleData/rt-polarity2.txt'
    stopwords = set(stopwords.words('english') + list(pun) +list('\n'))
    posReview = GetReview(posFile)
    negReview= GetReview(negFile)
    posScore=0
    negScore=0
    totalReviewScore=0
    ##review ="if you sometimes like to go to the movies to have fun , wasabi is a good place to start . "

    for r in posReview:
        totalReviewScore=superNativeSentiment(str(r))
        posScore+=totalReviewScore

    totalReviewScore=0

    for r in negReview:
        totalReviewScore = superNativeSentiment(str(r))
        negScore += totalReviewScore

    ScoreCalculator = {'positivescore': posScore, 'negativescore': negScore}

    print(posScore )
    #RunDiagnostic(ScoreCalculator)

