@app.route('/reset_password', methods=['POST'])
def reset_password():
    username = request.form['username']
    # 验证用户名
    # 发送重置链接到用户邮箱
    return "密码重置链接已发送"
