import feedparser
import mysql.connector as sql


def parse_rss(rss_url):
    return feedparser.parse(rss_url)


# Function grabs the rss feed headlines (titles) and returns them as a list
def get_headlines(rss_url):
    headlines = []
    feed = parse_rss(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines


# A list to hold all headlines
allheadlines = []

# List of RSS feeds that we will fetch and combine
# 1
politicsURL = {
    'farsnews': 'https://www.farsnews.com/rss/politics',
    'isna': 'https://www.isna.ir/rss/tp/14',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/1/%D8%B3%DB%8C%D8%A7%D8%B3%DB%8C',
    'yjc': 'https://www.yjc.ir/fa/rss/3',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/7',
    'tabnak': 'https://www.tabnak.ir/fa/rss/1/2',
    'irna': 'https://www.irna.ir/rss/tp/5',
    'econews': 'http://econews.ir/fa/news/feed/764',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/1',
    'asriran': 'https://www.asriran.com/fa/rss/1/1',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/2',
    'entekhab': 'https://www.entekhab.ir/fa/rss/2',
    'jahannews': 'http://www.jahannews.com/rssci.uy2-s2tuu-5b1,ydk.8al2as.2.xml',
    'alef': 'https://www.alef.ir/rss/latest/politics.xml',
    'ana': 'http://ana.ir/fa/rss/service/12',
    'imna': 'https://www.imna.ir/rss/tp/28',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=1&l=fa-ir',
    'iqna': 'http://iqna.ir/en/rss/3/mostvisited',
    'iribnews': 'http://www.iribnews.ir/fa/rss/5'
}
# 2
economyURL = {
    'farsnews': 'https://www.farsnews.com/rss/economy',
    'isna': 'https://www.isna.ir/rss/tp/34',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/7/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%DB%8C',
    'yjc': 'https://www.yjc.ir/fa/rss/6',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/25',
    'tabnak': 'https://www.tabnak.ir/fa/rss/6',
    'irna': 'https://www.irna.ir/rss/tp/20',
    'econews': 'http://econews.ir/fa/news/feed/991',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/2',
    'asriran': 'https://www.asriran.com/fa/rss/1/4',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/16',
    'entekhab': 'https://www.entekhab.ir/fa/rss/5',
    'jahannews': 'http://www.jahannews.com/rssew.skj1zjyss1rhx2k4m.ib9jbx.j.xml',
    'alef': 'https://www.alef.ir/rss/latest/economy.xml',
    'ana': 'http://ana.ir/fa/rss/service/22',
    'imna': 'https://www.imna.ir/rss/tp/5',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=4&l=fa-ir',
    'iribnews': 'http://www.iribnews.ir/fa/rss/6'
}
# 3
worldURL = {
    'farsnews': 'https://www.farsnews.com/rss/world',
    'isna': 'https://www.isna.ir/rss/tp/17',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/8/%D8%A8%DB%8C%D9%86-%D8%A7%D9%84%D9%85%D9%84%D9%84',
    'yjc': 'https://www.yjc.ir/fa/rss/9',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/8',
    'tabnak': 'https://www.tabnak.ir/fa/rss/17',
    'irna': 'https://www.irna.ir/rss/tp/1',
    'econews': 'http://econews.ir/fa/news/feed/784',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/5',
    'asriran': 'https://asriran.com/fa/rss/1 /3',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/5',
    'entekhab': 'https://www.entekhab.ir/fa/rss/3',
    'jahannews': 'http://www.jahannews.com/rssir.,ltizt4,,ik1pxlne.2cbtcy.t.xml',
    'alef': 'https://www.alef.ir/rss/latest/world.xml',
    'ana': 'http://ana.ir/fa/rss/service/20',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=3&l=fa-ir',
    'iqna': 'http://iqna.ir/en/rss/services/7',
    'iribnews': 'http://www.iribnews.ir/fa/rss/5'
}
# 4
socialURL = {
    'farsnews': 'https://www.farsnews.com/rss/social',
    'isna': 'https://www.isna.ir/rss/tp/9',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/2/%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%DB%8C',
    'yjc': 'https://www.yjc.ir/fa/rss/5',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/6',
    'tabnak': 'https://www.tabnak.ir/fa/rss/3',
    'irna': 'https://www.irna.ir/rss/tp/32',
    'econews': 'http://econews.ir/fa/news/feed/767',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/4',
    'asriran': 'https://www.asriran.com/fa/rss/1/5',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/14',
    'entekhab': 'https://www.entekhab.ir/fa/rss/4',
    'jahannews': 'http://www.jahannews.com/rssf0.47wrywq44r,6mp73f.aigwij.w.xml',
    'alef': 'https://www.alef.ir/rss/latest/social.xml',
    'ana': 'http://ana.ir/fa/rss/service/21',
    'imna': 'https://www.imna.ir/rss/tp/3',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=5&l=fa-ir',
    'iqna': 'http://iqna.ir/en/rss/services/5',
    'iribnews': 'http://www.iribnews.ir/fa/rss/7',
}
# 5
sportsURL = {
    'farsnews': 'https://www.farsnews.com/rss/sports',
    'isna': 'https://www.isna.ir/rss/tp/24',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/3/%D9%88%D8%B1%D8%B2%D8%B4%DB%8C',
    'yjc': 'https://www.yjc.ir/fa/rss/8',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/9',
    'tabnak': 'https://www.tabnak.ir/fa/rss/2',
    'irna': 'https://www.irna.ir/rss/tp/14',
    'econews': 'http://econews.ir/fa/news/feed/766',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/6',
    'asriran': 'https://www.asriran.com/fa/rss/1/6',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/10',
    'entekhab': 'https://www.entekhab.ir/fa/rss/9',
    'jahannews': 'http://www.jahannews.com/rssdx.gmyefy,ggeltshmci.62ay2x.y.xml',
    'alef': 'https://www.alef.ir/rss/latest/sports.xml',
    'ana': 'http://ana.ir/fa/rss/service/24',
    'imna': 'https://www.imna.ir/rss/tp/7',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=6&l=fa-ir',
    'iqna': 'http://www.iribnews.ir/fa/rss/4',
    'iribnews': 'http://www.iribnews.ir/fa/rss/4'
}
# 6
scienceURL = {
    'farsnews': 'https://www.farsnews.com/rss/scientific-academic',
    'isna': 'https://www.isna.ir/rss/tp/5',
    'yjc': 'https://www.yjc.ir/fa/rss/7',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/5',
    'tabnak': 'https://www.tabnak.ir/fa/rss/1/72',
    'irna': 'https://www.irna.ir/rss/tp/180',
    'econews': 'http://econews.ir/fa/news/feed/768',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/7',
    'asriran': 'https://www.asriran.com/fa/rss/1/7',
    'mashreghnews': 'https://www.mashreghnews.ir/rss?pl=19',
    'entekhab': 'https://www.entekhab.ir/fa/rss/8',
    'alef': 'https://www.alef.ir/rss/latest/technology.xml',
    'imna': 'https://www.imna.ir/rss/tp/6',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=8&l=fa-ir',
    'iribnews': 'http://www.iribnews.ir/fa/rss/8/19',
}
# 7
cultureURL = {
    'farsnews': 'https://www.farsnews.com/rss/culture',
    'isna': 'https://www.isna.ir/rss/tp/20',
    'tasnimnews': 'https://www.tasnimnews.com/fa/rss/feed/0/7/4/%D9%81%D8%B1%D9%87%D9%86%DA%AF%DB%8C',
    'yjc': 'https://www.yjc.ir/fa/rss/4',
    'mehrnews': 'https://www.mehrnews.com/rss/tp/2',
    'tabnak': 'https://www.tabnak.ir/fa/rss/21',
    'irna': 'https://www.irna.ir/rss/tp/41',
    'econews': 'http://econews.ir/fa/news/feed/765',
    'khabaronline': 'https://www.khabaronline.ir/rss/tp/3',
    'asriran': 'https://www.asriran.com/fa/rss/1/8',
    'mashreghnews': 'https://www.mashreghnews.ir/rss/tp/4',
    'entekhab': 'https://www.entekhab.ir/fa/rss/18',
    'jahannews': 'http://www.jahannews.com/rssgx.dja5qa6dd51kwvjoe.4rparn.a.xml',
    'alef': 'https://www.alef.ir/rss/latest/culture.xml',
    'ana': 'http://ana.ir/fa/rss/service/23',
    'imna': 'https://www.imna.ir/rss/tp/4',
    'aryanews': 'http://www.aryanews.com/Feed.aspx?svc=7&l=fa-ir',
    'iqna': 'http://iqna.ir/en/rss/services/6',
    'iribnews': 'http://www.iribnews.ir/fa/rss/8/28'
}


def start_db(host, user, passwd, db_name):
    conn = sql.connect(
        host="localhost",
        user="root",
        passwd="7221974",
    )
    # cur = conn.courser()
    # cur.execute(f'CREATE {db_name} IF NOT EXISTS RSSFEED')
    # cur.execute(f'USE {db_name}')
    # return conn, cur


# Iterate over the feed urls
for key, url in sportsURL.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend(get_headlines(url))

# Iterate over the all headlines list and print each headline
for hl in allheadlines:
    print(hl)

# end of code
