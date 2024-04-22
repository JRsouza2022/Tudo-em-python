from instapy import InstaPy

# Configurar e iniciar a sessão do InstaPy
session = InstaPy(username='seu_usuario', password='sua_senha')
session.login()

# Automatizar curtidas em postagens com a hashtag #python
session.like_by_tags(['python'], amount=5)

# Encerrar a sessão do InstaPy
session.end()
