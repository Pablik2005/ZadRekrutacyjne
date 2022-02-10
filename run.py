from flask import Flask, jsonify

from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook


app = Flask(__name__)


@app.route("/api/v1/<classType>/<position>")
def list_available_moves(classType, position):

    figure = King(position)
    res = dict()
    res["availableMoves"] = []
    res["error"] = ""
    res["figure"] = str(classType)
    res["currentField"] = str(position)

    if (figure.x in figure.range) and (figure.y in figure.range):

        if str(classType).lower() == "bishop":
            figure = Bishop(position)
        elif str(classType).lower() == "king":
            figure = King(position)
        elif str(classType).lower() == "knight":
            figure = Knight(position)
        elif str(classType).lower() == "pawn":
            figure = Pawn(position)
        elif str(classType).lower == "queen":
            figure = Queen(position)
        elif str(classType).lower() == "rook":
            figure = Rook(position)
        else:
            res["error"] = "Figure does not exist."
            return (
                jsonify(
                    res,
                ),
                404,
            )

        res["error"] = "null"
        res["availableMoves"] = figure.list_available_moves()
        return jsonify(res), 200

    else:
        res["error"] = "Field does not exist."
        return jsonify(res), 409


@app.route("/api/v1/<classType>/<position>/<destPosition>")
def validate_move(classType, position, destPosition):

    figure = King(position)
    res = dict()
    res["move"] = ""
    res["figure"] = str(classType)
    res["error"] = ""
    res["currentField"] = str(position)
    res["destField"] = str(destPosition)

    tDestPosition = figure.translatePositionToNumeric(destPosition)

    if (
        (figure.x in figure.range)
        and (figure.x in figure.range)
        and (tDestPosition[0] in figure.range)
        and (tDestPosition[1] in figure.range)
    ):

        if str(classType).lower() == "bishop":
            figure = Bishop(position)
        elif str(classType).lower() == "king":
            figure = King(position)
        elif str(classType).lower() == "knight":
            figure = Knight(position)
        elif str(classType).lower() == "pawn":
            figure = Pawn(position)
        elif str(classType).lower == "queen":
            figure = Queen(position)
        elif str(classType).lower() == "rook":
            figure = Rook(position)
        else:
            res["error"] = "Figure does not exist."
            return (
                jsonify(
                    res,
                ),
                404,
            )

        if figure.validate_move(destPosition):
            res["move"] = "valid"
            res["error"] = "null"
            return jsonify(res), 200
        else:
            res["move"] = "invalid"
            res["error"] = "Current move is not permitted."
            return jsonify(res), 200

    else:
        res["error"] = "Field does not exist."
        return jsonify(res), 409

app.run()
