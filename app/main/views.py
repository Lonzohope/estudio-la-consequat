from flask import render_template
from . import main
# from ..request import get_sources



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('index.html', title=title)

@main.route('/potrait')
def potrait():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('potrait.html', title=title)


@main.route('/steve')
def steve():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('steve.html', title=title)


@main.route('/zhang')
def zhang():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('zhang.html', title=title)

@main.route('/manny')
def manny():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('manny.html', title=title)

@main.route('/lisa')
def lisa():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('lisa.html', title=title)

@main.route('/david')
def david():

    '''
    View root page function that returns the index page and its data
    '''
    # sources=get_sources()
    # Getting popular news
    # popular_photos= get_photo("top-photos")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best Photo Hub Website Online'
    return render_template('david.html', title=title)

