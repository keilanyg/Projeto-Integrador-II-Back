from django.contrib import admin

# from auditlog.models import LogEntry
from livros.models import Categoria, Editora, Autor, Livro, Emprestimo, Devolucao

admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
admin.site.register(Devolucao)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

    # visualização de logs
    # actions = ['ver_logs_de_auditoria']

    # def ver_logs_de_auditoria(self, request, queryset):
    #     # for categoria in queryset:
    #         # logs = LogEntry.objects.filter(object_id=categoria.id, content_type__model='categoria')
    #         # for log in logs:
    #         #     changes = log.changes_dict
    #         #     if 'nome' in changes:
    #         #         nome_antigo = changes['nome'][0]  # valor antigo
    #         #         nome_novo = changes['nome'][1]    # valor novo
    #         #         self.message_user(request, f"Categoria '{categoria.nome}': Nome antigo: {nome_antigo}, Nome novo: {nome_novo}")
    # ver_logs_de_auditoria.short_description = "Ver Logs de Auditoria"


class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)

    # visualização de logs
    # actions = ['ver_logs_de_auditoria']

    # def ver_logs_de_auditoria(self, request, queryset):
    #     for editora in queryset:
    #         logs = LogEntry.objects.filter(object_id=editora.id, content_type__model='editora')
    #         for log in logs:
    #             changes = log.changes_dict
    #             if 'nome' in changes:
    #                 nome_antigo = changes['nome'][0]  # valor antigo
    #                 nome_novo = changes['nome'][1]    # valor novo
    #                 self.message_user(request, f"Editora '{editora.nome}': Nome antigo: {nome_antigo}, Nome novo: {nome_novo}")
    # ver_logs_de_auditoria.short_description = "Ver Logs de Auditoria"


class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)

    # visualização de logs
    actions = ["ver_logs_de_auditoria"]

    # def ver_logs_de_auditoria(self, request, queryset):
    #     for autor in queryset:
    #         logs = LogEntry.objects.filter(object_id=autor.id, content_type__model='autor')
    #         for log in logs:
    #             changes = log.changes_dict
    #             if 'nome' in changes:
    #                 nome_antigo = changes['nome'][0]  # valor antigo
    #                 nome_novo = changes['nome'][1]    # valor novo
    #                 self.message_user(request, f"Autor '{autor.nome}': Nome antigo: {nome_antigo}, Nome novo: {nome_novo}")
    # ver_logs_de_auditoria.short_description = "Ver Logs de Auditoria"


class LivroAdmin(admin.ModelAdmin):
    list_display = ("nome",)

    # visualização de logs
    actions = ["ver_logs_de_auditoria"]

    # def ver_logs_de_auditoria(self, request, queryset):
    #     for livro in queryset:
    #         logs = LogEntry.objects.filter(object_id=livro.id, content_type__model='livro')
    #         for log in logs:
    #             changes = log.changes_dict
    #             if 'nome' in changes:
    #                 nome_antigo = changes['nome'][0]  # valor antigo
    #                 nome_novo = changes['nome'][1]    # valor novo
    #                 self.message_user(request, f"Livro '{livro.nome}': Nome antigo: {nome_antigo}, Nome novo: {nome_novo}")

    # ver_logs_de_auditoria.short_description = "Ver Logs de Auditoria"
