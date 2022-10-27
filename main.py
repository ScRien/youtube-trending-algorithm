from dis import dis


def main():
    def raiting():
        global like
        global dislike
        global raitingdeger
        try:
            like = int(input("Videonun Like Sayısını giriniz: "))
        except ValueError:
            print("Lütfen Sayı Giriniz!")
            raiting()
        try:
            dislike = int(input("Videonun Dislike Sayısını giriniz: "))
        except ValueError:
            print("Lütfen Sayı Giriniz!")
            raiting()
        try:
            grtlnmsrs = int(input("Videonun Görüntülenme Sayısını Giriniz: "))
        except ValueError:
            print("Lütfen Bir Sayı Giriniz!")
            raiting()

        raitingdeger = (like / (like + dislike)) * 100
        
        global raitingdegervalue

        raitingdegervalue = ""

        if raitingdeger > 75 and like > 10000 and dislike < 3000:
            raitingdegervalue = "Videonuz %90 ihtimalle trendler de olacaktır."
        elif raitingdeger > 50 and like > 5000 and dislike < 4225:
            raitingdegervalue = "Videonuz %70 ihtimalle trendler de olacaktır."
        elif raitingdeger > 25 and like > 2500 and dislike < 5250:
            raitingdegervalue = "Videonuz %50 ihtimalle trendler de olacaktır."
        elif raitingdeger > 10 and like > 1000 and dislike < 7500:
            raitingdegervalue = "Videonuz %30 ihtimalle trendler de olacaktır."
        elif raitingdeger > 5 and like > 500 and dislike < 10000:
            raitingdegervalue = "Videonuz %10 ihtimalle trendler de olacaktır."
        elif raitingdeger > 2 and like > 75 and dislike < 150000:
            raitingdegervalue = "Videonuz %-10 ihtimalle trendler de olacaktır."
        elif raitingdeger == 1 or raitingdeger < 0 and like > 25 and dislike < 200000:
            raitingdegervalue = "Videonuz %-30 ihtimalle trendler de olacaktır."

        print("""
        Video Beğenilme Sayısı: {like_}
        Video Beğenilmeme Sayısı: {dislike_}
        Video Görüntülenme Süresi: {grtlnmsrs_}
        
        Raiting'iniz: {raiting_}

        Trend İstatistikleri:
        {trend}
        """.format(like_ = like, dislike_ = dislike, grtlnmsrs_ = grtlnmsrs, raiting_ = raitingdeger, trend = raitingdegervalue))
    raiting()


main()