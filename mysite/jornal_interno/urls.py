from django.urls import path
from . import views

app_name = 'jornalinterno'
urlpatterns = [
    path(
        '', views.IndexView.as_view(),
        name='index'
    ),

    path(
        'listar_edicoes/', views.ListarEdicoesView.as_view(),
        name='listar_edicoes'
    ),

    path(
        'edicao/<int:pk>/', views.PaginaEdicaoView.as_view(),
        name='pagina_edicao'
    ),

    path(
        'noticia/<int:pk>/', views.PaginaNoticiaView.as_view(),
        name='pagina_noticia'
    ),

    path(
        'edicao/cadastrar/', views.AddEdView.as_view(),
        name='add_ed'
    ),

    path(
        'noticia/cadastrar/', views.AddNoticiaView.as_view(),
        name='add_noticia'
    ),

    path(
        'comentario/cadastrar/<int:noticia_id>/', views.AddComentView.as_view(),
        name='add_coment'
    ),
]
