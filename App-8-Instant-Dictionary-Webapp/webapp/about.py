import justpy as jp
import page

from webapp import layout


class About(page.Page):
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container)
        jp.Div(a=div, text="About Page")

        return wp