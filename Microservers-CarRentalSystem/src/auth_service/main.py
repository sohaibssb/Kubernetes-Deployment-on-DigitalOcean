from quart import Quart
from blueprints.models.user_model import UserModel
from blueprints.models.user_token import Usertoken
from blueprints.create_user import post_user_details_from_api
from blueprints.get_user import get_all_users
from blueprints.token_check import get_check_tokne
# from blueprints.callback_api import post_callback

from quart_cors import cors

app = Quart(__name__)

app = cors(app, allow_origin="*", allow_headers="*", allow_methods=["GET", "POST", "PUT", "DELETE"])

app.register_blueprint(post_user_details_from_api)
app.register_blueprint(get_all_users)
app.register_blueprint(get_check_tokne)
# app.register_blueprint(post_callback)




def create_tables():
    Usertoken.drop_table()
    UserModel.drop_table()
    UserModel.create_table()
    Usertoken.create_table()


if __name__ == '__main__':
    create_tables()
    # create_tokne()
    app.run(host='0.0.0.0', port=8090)
