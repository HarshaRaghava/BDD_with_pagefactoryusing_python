from Base.Browser import browser
# from Base.object import objects


def before_feature(context,feature):
    obj  = browser()
    obj.open_Chromebrowser("https://www.irctc.co.in/nget/train-search")
    # objects.createobjects(objects())
