from flask_restful import Api, Resource, reqparse

class HelloApiHandler(Resource):
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Api Handler"
      }

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str)


    args = parser.parse_args()

    print(args)
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello user " + str(args.id)
    }