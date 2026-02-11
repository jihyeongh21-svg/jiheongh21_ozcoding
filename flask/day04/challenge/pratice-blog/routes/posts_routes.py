from flask import request,jsonify
from flask_smorest import Blueprint,abort

def create_post(mysql):
    posts_blp = Blueprint('posts',__name__,description='Operations on posts',url_prefix='/posts')

    @posts_blp.route('/',methods=['POST','GET'])
    def posts():
        cusor = mysql.connection.cursor()
        if request.method == 'POST':
            data = request.get_json()
            title = data['title']
            content = data['content']
            sql = "INSERT INTO posts(title,content) VALUES(%s,%s)"

            if not title or not content:
                abort(400,message= "제목 또는 내용이 비엇음")
            cusor.execute(sql,(title,content))
            mysql.connection.commit()
            cusor.close()
            return jsonify({"msg":"생성 완료"})
        
        elif request.method == 'GET':
            sql = "SELECT * FROM posts"
            cusor.execute(sql)
            posts = cusor.fetchall()
            cusor.close()
            posts_list = []
            for post in posts:
                post_dict = {
                    'id':post[0],
                    'title':post[1],
                    'content':post[2]
                }
                posts_list.append(post_dict)
            return jsonify(posts_list)
        

    @posts_blp.route('/<int:id>',methods=['GET','PUT','DELETE'])
    def post(id):
        cusor = mysql.connection.cursor()
        sql = "SELECT * FROM posts WHERE id = %s"
        cusor.execute(sql,(id, ))
        post = cusor.fetchone()
        
        if request.method == 'GET':
            if not post:
                abort(404,"찾는 포스트가 없습니다")
            return ({
                'id':post[0],
                'title':post[1],
                'content':post[2]
                })
        elif request.method == 'PUT':
            data = request.get_json()
            title = data['title']
            content = data['content']
            sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"

            if not title or not content:
                abort(400,message= "제목 또는 내용이 비엇음")
            
            if not post:
                abort(404,"찾는 포스트가 없습니다")
            
            cusor.execute(sql,(title,content,id))
            mysql.connection.commit()
            cusor.close()

            return jsonify({"msg":"수정 완료"})
        
        elif request.method == 'DELETE':
            if not post:
                abort(404,"찾는 포스트가 없습니다")

            sql = "DELETE FROM posts WHERE id = %s"
            cusor.execute(sql,(id,))
            mysql.connection.commit()
            cusor.close()

            return jsonify({"msg":"삭제 완료"})


    return posts_blp