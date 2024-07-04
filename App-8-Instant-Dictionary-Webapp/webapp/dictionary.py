import justpy as jp

from webapp import layout

import requests
import page

"""
     classmethod is a method that gets the class that it belongs
     to as its attribute. Typical methods gets the instance of
     the class they belong to as its attribute usually.
     However, classmethod is used when the creation of the class instance
     is not required, but still the method needs to access the
     variables of the class, or when another object is passed to
     the class method, but the method stills need to keep the access
     of the class variables.
 """

"""
       staticmethod is an independent method from the class that
       it belongs to. This means that the method doesn't require
       anything from the class or the instance of the class. 
       However, the method belongs to a class for the purpose of
       organization and logic
"""


class Dictionary(page.Page):
    path = '/dictionary'


    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="Instant English Dictionary",
               classes="text-4xl m-2")
        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        input_box = jp.Input(a=input_div, placeholder="Enter a word...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded w-64 focus:bg-white focus:outline-none "
                                     "focus:border-purple-500 py-2 px-4",
                             outputdiv = output_div)
        input_box.on('input', cls.get_definition)

        # jp.Button(a=input_div, text="Get Definition",
        #           classes="border-2 text-gray-500",
        #           click=cls.get_definition,
        #           outputdiv=output_div,
        #           inputbox=input_box)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
        data = req.json()
        widget.outputdiv.text = " ".join(data['definition'])

