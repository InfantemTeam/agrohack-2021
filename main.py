#!/usr/bin/env python3
# AgroHack 2021

import time, random, string, asyncio
from quart import *

app = Quart(__name__)

@app.route('/')
async def index():
	return await render_template('index.html')

@app.route('/upload', methods=('POST',))
async def upload():
	id = str().join(random.choices(string.ascii_lowercase, k=8))

	app.complete[id] = (int(time.time()) + 2)  # simulate some processing

	return id

@app.route('/result')
async def result():
	try: id = request.args['id']
	except KeyError as ex: return abort(400, ex)

	try: t = app.complete[id]
	except KeyError as ex: return abort(404, ex)

	await asyncio.sleep(t - time.time())

	return 'OK'

@app.before_serving
def before_serving():
	app.complete = dict()

def main():
	app.env = 'development'
	app.run('unix', '///tmp/agrohack.sock', debug=True)

if (__name__ == '__main__'): exit(main())

# by InfantemTeam, 2021
# infantemteam@sdore.me
