import justpy as jp
from webapp import layout
import sys
sys.path.append('/Users/chriskim/Desktop/Programming/python/files/App-8-Instant-Dictionary-Webapp/webapp')
import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Home Page")

        return wp
