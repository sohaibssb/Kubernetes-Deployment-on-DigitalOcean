from quart import Quart
from blueprints.get_cars_blueprint import get_cars_blueprint
from blueprints.get_rentals_blueprint import get_rentals_blueprint
from blueprints.get_rental_blueprint import get_rental_blueprint
from blueprints.post_rental_blueprint import post_rentals_blueprint
from blueprints.delete_rental_blueprint import delete_rental_blueprint
from blueprints.post_rental_finish_blueprint import post_rental_finish_blueprint
from blueprints.health_check_blueprint import health_check_blueprint
from blueprints.login_blueprint import login_blurprint
from blueprints.statistique_blueprint import get_statistique_blurprint
from blueprints.post_cars_blueprint import post_car_blueprint
from blueprints.delete_car import delete_car_blueprint

from quart_cors import cors

app = Quart(__name__)

app = cors(app, allow_origin="*", allow_headers="*", allow_methods=["GET", "POST", "PUT", "DELETE"])

app.register_blueprint(get_cars_blueprint)
app.register_blueprint(get_rentals_blueprint)
app.register_blueprint(post_rentals_blueprint)
app.register_blueprint(delete_rental_blueprint)
app.register_blueprint(post_rental_finish_blueprint)
app.register_blueprint(get_rental_blueprint)
app.register_blueprint(health_check_blueprint)
app.register_blueprint(login_blurprint)
app.register_blueprint(get_statistique_blurprint)
app.register_blueprint(post_car_blueprint)
app.register_blueprint(delete_car_blueprint)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
