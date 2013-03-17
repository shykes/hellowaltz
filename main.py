#!/usr/bin/python
#-*- coding: utf-8 -*-

import waltz
from waltz import track, render

urls = ('/analytics/?', 'waltz.modules.Analytics',
        '/?', 'Index')

sessions = {}
env = {}
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions, env=env)

class Index:
    @track
    def GET(self):
        return render().index()

if __name__ == "__main__":
    app.run()
