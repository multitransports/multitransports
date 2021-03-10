import os
import logging
from flask import Flask
from flask_cors import CORS
from back import route
from back.main import main
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig(
filename='log_app.log',
format='%(asctime)s %(message)s',
level=logging.DEBUG)

sched = BackgroundScheduler(daemon=True)
sched.add_job(main,'interval',seconds=59)
sched.start()

template_dir = os.path.abspath('./front/templates')
app = Flask(__name__, template_folder=template_dir)
CORS(app)
logging.debug("the db is going to initialize")
main()
logging.debug("the db is initialize")

app.add_url_rule('/', view_func=route.entry_point)
app.add_url_rule('/hello_world', view_func=route.hello_world)
app.add_url_rule('/<ville>/stations/<station>', view_func=route.nexttram)
app.add_url_rule('/<ville>/stations/', view_func=route.citystations)
app.add_url_rule('/<ville>/ligne/<ligne>', view_func=route.line_station)
app.add_url_rule('/<ville>/<station>/<ligne>/<direction>', view_func=route.next_to_direction)
app.add_url_rule('/<ville>/stationslike/<station>', view_func=route.station_like)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
