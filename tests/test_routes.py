import unittest  # Importa o módulo unittest para criação de testes

from app import create_app, db  # Importa a função create_app e o objeto db do SQLAlchemy
from app.models import User  # Importa o modelo User


class TestRoutes(unittest.TestCase):  # Define a classe de teste que herda de unittest.TestCase

    def setUp(self):
        """Configura o ambiente de teste."""
        self.app = create_app()  # Cria uma instância da aplicação Flask para o teste
        self.app_context = self.app.app_context()  # Cria um contexto de aplicação
        self.app_context.push()  # Ativa o contexto de aplicação
        db.create_all()  # Cria todas as tabelas no banco de dados

    def tearDown(self):
        """Limpa o ambiente de teste."""
        db.session.remove()  # Remove a sessão do banco de dados
        db.drop_all()  # Remove todas as tabelas do banco de dados
        self.app_context.pop()  # Desativa o contexto de aplicação

    def test_cadastrar_usuario_get(self):
        """Testa a rota /cadastrar com método GET."""
        with self.app.test_client() as client:  # Cria um cliente de teste para simular requisições
            response = client.get('/cadastrar')  # Faz uma requisição GET para a rota /cadastrar
            self.assertEqual(response.status_code, 200)  # Verifica se o código de status da resposta é 200 (OK)

    def test_cadastrar_usuario_post(self):
        """Testa a rota /cadastrar com método POST."""
        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.post('/cadastrar', data={'nome': 'Novo Usuário'})  # Faz uma requisição POST com dados do formulário
            self.assertEqual(response.status_code, 302)  # Verifica se o código de status da resposta é 302 (redirecionamento)
            self.assertTrue(response.location.endswith('/listar'))  # Verifica se o redirecionamento é para a rota /listar

    def test_listar_usuarios(self):
        """Testa a rota /listar."""
        user1 = User(nome="Usuário 1")  # Cria um usuário
        user2 = User(nome="Usuário 2")  # Cria outro usuário
        db.session.add_all([user1, user2])  # Adiciona os usuários à sessão
        db.session.commit()  # Salva os usuários no banco de dados

        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get('/listar')  # Faz uma requisição GET para a rota /listar
            data = response.get_data(as_text=True)  # Obtém o conteúdo da resposta como texto

        self.assertIn("Usuário 1", data)  # Verifica se o nome do usuário 1 está presente na resposta
        self.assertIn("Usuário 2", data)  # Verifica se o nome do usuário 2 está presente na resposta

    def test_obter_usuario_por_id_existente(self):
        """Testa a rota /usuario/<int:id> com um ID existente."""
        user = User(nome="Usuário Teste")  # Cria um usuário
        db.session.add(user)  # Adiciona o usuário à sessão
        db.session.commit()  # Salva o usuário no banco de dados

        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get(f'/usuario/{user.id}')  # Faz uma requisição GET para a rota /usuario/<id>
            data = response.get_data(as_text=True)  # Obtém o conteúdo da resposta como texto

        self.assertIn("Usuário Teste", data)  # Verifica se o nome do usuário está presente na resposta

    def test_obter_usuario_por_id_inexistente(self):
        """Testa a rota /usuario/<int:id> com um ID inexistente."""
        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get('/usuario/999')  # Faz uma requisição GET para a rota /usuario/999 (ID inexistente)
            self.assertEqual(response.status_code, 302)  # Verifica se o código de status da resposta é 302 (redirecionamento)
            self.assertTrue(response.location.endswith('/listar'))  # Verifica se o redirecionamento é para a rota /listar

    def test_editar_usuario_get(self):
        """Testa a rota /editar/<int:id> com método GET."""
        user = User(nome="Usuário Teste")  # Cria um usuário
        db.session.add(user)  # Adiciona o usuário à sessão
        db.session.commit()  # Salva o usuário no banco de dados

        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get(f'/editar/{user.id}')  # Faz uma requisição GET para a rota /editar/<id>
            self.assertEqual(response.status_code, 200)  # Verifica se o código de status da resposta é 200 (OK)

    def test_editar_usuario_post(self):
        """Testa a rota /editar/<int:id> com método POST."""
        user = User(nome="Usuário Teste")  # Cria um usuário
        db.session.add(user)  # Adiciona o usuário à sessão
        db.session.commit()  # Salva o usuário no banco de dados

        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.post(f'/editar/{user.id}', data={'nome': 'Nome Editado'})  # Faz uma requisição POST com dados do formulário
            self.assertEqual(response.status_code, 302)  # Verifica se o código de status da resposta é 302 (redirecionamento)
            self.assertTrue(response.location.endswith('/listar'))  # Verifica se o redirecionamento é para a rota /listar

    def test_excluir_usuario_existente(self):
        """Testa a rota /excluir/<int:id> com um ID existente."""
        user = User(nome="Usuário Teste")  # Cria um usuário
        db.session.add(user)  # Adiciona o usuário à sessão
        db.session.commit()  # Salva o usuário no banco de dados

        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get(f'/excluir/{user.id}')  # Faz uma requisição GET para a rota /excluir/<id>
            self.assertEqual(response.status_code, 302)  # Verifica se o código de status da resposta é 302 (redirecionamento)
            self.assertTrue(response.location.endswith('/listar'))  # Verifica se o redirecionamento é para a rota /listar

    def test_excluir_usuario_inexistente(self):
        """Testa a rota /excluir/<int:id> com um ID inexistente."""
        with self.app.test_client() as client:  # Cria um cliente de teste
            response = client.get('/excluir/999')  # Faz uma requisição GET para a rota /excluir/999 (ID inexistente)
            self.assertEqual(response.status_code, 302)  # Verifica se o código de status da resposta é 302 (redirecionamento)
            self.assertTrue(response.location.endswith('/listar'))  # Verifica se o redirecionamento é para a rota /listar

if __name__ == '__main__':
    unittest.main()  # Executa os testes se o script for executado diretamente