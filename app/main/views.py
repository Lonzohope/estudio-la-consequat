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
