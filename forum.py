@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    content = request.form['content']
    # 存储帖子信息到数据库
    return "帖子发布成功"
