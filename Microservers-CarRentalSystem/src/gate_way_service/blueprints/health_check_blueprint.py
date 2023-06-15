from quart import Blueprint, Response
from .auth_handler import token_required


health_check_blueprint = Blueprint('health_check', __name__, )


@health_check_blueprint.route('/manage/health', methods=['GET'])
@token_required
async def health_check() -> Response:
    return Response(
        status=200
    )