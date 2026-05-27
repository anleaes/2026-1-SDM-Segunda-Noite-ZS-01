# 2026-1-SDM-Segunda-Noite-ZS-01

Usuário:
URL: http://127.0.0.1:8000/usuarios/
http://127.0.0.1:8000/usuarios/login/
<br>VIEW: UsuarioViewSet
<br>SERIALIZER: UsuarioSerializer

MVT:

Cliente
http://127.0.0.1:8000/clientes/cadastrar
http://localhost:8000/clientes/escolher/
http://localhost:8000/clientes/comprar/14/

Admin
http://127.0.0.1:8000/administrador/filmes/

Admin (rotas MVT completas)
http://127.0.0.1:8000/administrador/
http://127.0.0.1:8000/administrador/cadastrar/
http://127.0.0.1:8000/administrador/filmes/
http://127.0.0.1:8000/administrador/filmes/cadastrar/
http://127.0.0.1:8000/administrador/filmes/<pk>/editar/
http://127.0.0.1:8000/administrador/filmes/remover/<pk>/
http://127.0.0.1:8000/administrador/sessoes/
http://127.0.0.1:8000/administrador/sessoes/cadastrar/
http://127.0.0.1:8000/administrador/sessoes/<pk>/editar/
http://127.0.0.1:8000/administrador/sessoes/<pk>/inativar/
http://127.0.0.1:8000/administrador/salas/
http://127.0.0.1:8000/administrador/salas/cadastrar/
http://127.0.0.1:8000/administrador/salas/<pk>/editar/
http://127.0.0.1:8000/administrador/salas/<pk>/inativar/
http://127.0.0.1:8000/administrador/salas/<sala_pk>/assentos/criar/
http://127.0.0.1:8000/administrador/salas/<sala_pk>/assentos/ativar/
http://127.0.0.1:8000/administrador/salas/<sala_pk>/assentos/inativar/
http://127.0.0.1:8000/administrador/generos/
http://127.0.0.1:8000/administrador/generos/cadastrar/
http://127.0.0.1:8000/administrador/generos/<pk>/editar/
http://127.0.0.1:8000/administrador/generos/<pk>/remover/

Assentos (templates)
http://127.0.0.1:8000/assentos/assentos/listar
http://127.0.0.1:8000/assentos/assentos/criar
http://127.0.0.1:8000/assentos/assentos/<id>/mudar-status/

Pedido (templates)
http://127.0.0.1:8000/pedido/cadastrar/

Ingresso (templates)
http://127.0.0.1:8000/ingresso/listar/
http://127.0.0.1:8000/ingresso/detalhe/<ingresso_id>/
http://127.0.0.1:8000/ingresso/validar/<ingresso_id>/

API (MVC)
http://127.0.0.1:8000/usuarios/usuarios/
http://127.0.0.1:8000/usuarios/usuarios/<pk>/
http://127.0.0.1:8000/clientes/clientes/
http://127.0.0.1:8000/clientes/clientes/<pk>/
http://127.0.0.1:8000/administrador/administrador/
http://127.0.0.1:8000/administrador/administrador/<pk>/
http://127.0.0.1:8000/salas/
http://127.0.0.1:8000/salas/<pk>/
http://127.0.0.1:8000/filmes/
http://127.0.0.1:8000/filmes/<pk>/
http://127.0.0.1:8000/pedido/api/
http://127.0.0.1:8000/pedido/api/<pk>/
http://127.0.0.1:8000/sessoes/
http://127.0.0.1:8000/sessoes/<pk>/
http://127.0.0.1:8000/assentos/assentos/
http://127.0.0.1:8000/assentos/assentos/<pk>/
http://127.0.0.1:8000/pagamento/api/
http://127.0.0.1:8000/pagamento/api/<pk>/
http://127.0.0.1:8000/ingresso/api/
http://127.0.0.1:8000/ingresso/api/<pk>/
http://127.0.0.1:8000/generos/
http://127.0.0.1:8000/generos/<pk>/
