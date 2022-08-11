import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from sympy import O

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
 @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  
#   @app.route('/books')
#   def retrieve_books():
#     selection = Book.query.order_by(Book.id).all()
#     current_books = paginate_books(request, selection)

#     if len(current_books) == 0:
#       abort(404)

#     return jsonify({
#       'success': True,
#       'books': current_books,
#       'total_books': len(Book.query.all())
#     })

#   @app.route('/books/<int:book_id>', methods=['PATCH'])
#   def update_book(book_id):

#     body = request.get_json()

#     try:
#       book = Book.query.filter(Book.id == book_id).one_or_none()
#       if book is None:
#         abort(404)

#       if 'rating' in body:
#         book.rating = int(body.get('rating'))

#       book.update()

#       return jsonify({
#         'success': True,
#       })
      
#     except:
#       abort(400)

#   @app.route('/books/<int:book_id>', methods=['DELETE'])
#   def delete_book(book_id):
#     try:
#       book = Book.query.filter(Book.id == book_id).one_or_none()

#       if book is None:
#         abort(404)

#       book.delete()
#       selection = Book.query.order_by(Book.id).all()
#       current_books = paginate_books(request, selection)

#       return jsonify({
#         'success': True,
#         'deleted': book_id,
#         'books': current_books,
#         'total_books': len(Book.query.all())
#       })

#     except:
#       abort(422)

#   @app.route('/books', methods=['POST'])
#   def create_book():
#     body = request.get_json()

#     new_title = body.get('title', None)
#     new_author = body.get('author', None)
#     new_rating = body.get('rating', None)

#     try:
#       book = Book(title=new_title, author=new_author, rating=new_rating)
#       book.insert()

#       selection = Book.query.order_by(Book.id).all()
#       current_books = paginate_books(request, selection)

#       return jsonify({
#         'success': True,
#         'created': book.id,
#         'books': current_books,
#         'total_books': len(Book.query.all())
#       })

#     except:
#       abort(422)

#   @app.errorhandler(404)
#   def not_found(error):
#     return jsonify({
#       "success": False, 
#       "error": 404,
#       "message": "resource not found"
#       }), 404

#   @app.errorhandler(422)
#   def unprocessable(error):
#     return jsonify({
#       "success": False, 
#       "error": 422,
#       "message": "unprocessable"
#       }), 422

#   @app.errorhandler(400)
#   def bad_request(error):
#     return jsonify({
#       "success": False, 
#       "error": 400,
#       "message": "bad request"
#       }), 400
      
#   @app.errorhandler(405)
#   def not_found(error):
#     return jsonify({
#       "success": False, 
#       "error": 405,
#       "message": "method not allowed"
#       }), 405
  
#   return app

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
@app.route('/categories')
def get_categories ():
    selection = Category.query.order_by (Category.id).all()
    current_category= paginate_questions(request, selection)
    abort(404)


@app.route('/questions')
def retrieve_questions ():
    selection = Question.query.order_by (Question.id).all()
    current_questions= paginate_questions(request, selection)
    if len (current_questions)==O:
    abort(404)

    return jsonify({
      'success': True,
      'books': current_books,
      'total_books': len(Question.query.all())

    })

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app

