# -*- coding: utf-8 -*-
from tdg_social import app, db
from tdg_social.crons import cron
from flask_script import Manager, Command, Option
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#manager.add_command("runserver", Server(use_debugger=app.config['DEBUG'], use_reloader=app.config['RELOAD'], host=app.config['HOST'], port=int(app.config['PORT'])))
manager.add_command('cron', cron)

if __name__ == "__main__":
    manager.run()
