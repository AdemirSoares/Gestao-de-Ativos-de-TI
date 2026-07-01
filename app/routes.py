from app.database import db
from app.models import Ativo
from flask import render_template, request, redirect, url_for, flash

def init_app(app):

    @app.route("/")
    def dashboard():

        total_ativos = Ativo.query.count()

        ativos_ativos = Ativo.query.filter_by(status="Ativo").count()
        ativos_em_uso = Ativo.query.filter_by(status="Em uso").count()
        ativos_manutencao = Ativo.query.filter_by(status="Manutenção").count()
        ativos_inativos = Ativo.query.filter_by(status="Inativo").count()

        ultimos_ativos = Ativo.query.order_by(Ativo.id.desc()).limit(3).all()

        return render_template(
            "dashboard.html",
            pagina="dashboard",
            total_ativos=total_ativos,
            ativos_ativos=ativos_ativos,
            ativos_em_uso=ativos_em_uso,
            ativos_manutencao=ativos_manutencao,
            ativos_inativos=ativos_inativos,
            ultimos_ativos=ultimos_ativos
        )

    @app.route("/ativos")
    def listar_ativos():

        pesquisa = request.args.get("pesquisa", "").lower()

        if pesquisa:
            ativos_filtrados = Ativo.query.filter(
                (Ativo.patrimonio.ilike(f"%{pesquisa}%")) |
                (Ativo.hostname.ilike(f"%{pesquisa}%")) |
                (Ativo.tipo.ilike(f"%{pesquisa}%")) |
                (Ativo.sistema.ilike(f"%{pesquisa}%")) |
                (Ativo.responsavel.ilike(f"%{pesquisa}%"))
            ).all()
        else:
            ativos_filtrados = Ativo.query.all()

        total_ativos = Ativo.query.count()

        return render_template(
            "ativos.html",
            pagina="ativos",
            ativos=ativos_filtrados,
            pesquisa=pesquisa,
            total_ativos=total_ativos
        )

    @app.route("/ativos/novo", methods=["GET", "POST"])
    def novo_ativo():

        if request.method == "POST":

            patrimonio = request.form.get("patrimonio")
            hostname = request.form.get("hostname")
            tipo = request.form.get("tipo")
            sistema = request.form.get("sistema")
            responsavel = request.form.get("responsavel")
            status = request.form.get("status")
            localizacao = request.form.get("localizacao")

            if not patrimonio or not hostname or not tipo or tipo == "Selecione...":
                return render_template(
                    "form_ativo.html",
                    pagina="ativos",
                    titulo="Novo Ativo",
                    subtitulo="Cadastre as informações completas do ativo de TI",
                    erro="Preencha os campos obrigatórios: patrimônio, hostname e tipo."
                )

            ativo = Ativo(
                patrimonio=patrimonio,
                hostname=hostname,
                tipo=tipo,
                sistema=sistema,
                responsavel=responsavel,
                status=status,
                localizacao=localizacao
            )

            db.session.add(ativo)
            db.session.commit()

            flash("Ativo cadastrado com sucesso!", "success")
            return redirect(url_for("listar_ativos"))

        return render_template(
            "form_ativo.html",
            pagina="ativos",
            titulo="Novo Ativo",
            subtitulo="Cadastre as informações completas do ativo de TI"
        )
    
    @app.route("/ativos/<int:id>/editar", methods=["GET", "POST"])
    def editar_ativo(id):

        ativo = Ativo.query.get_or_404(id)

        if request.method == "POST":
            ativo.patrimonio = request.form.get("patrimonio")
            ativo.hostname = request.form.get("hostname")
            ativo.tipo = request.form.get("tipo")
            ativo.sistema = request.form.get("sistema")
            ativo.responsavel = request.form.get("responsavel")
            ativo.status = request.form.get("status")
            ativo.localizacao = request.form.get("localizacao")

            db.session.commit()

            flash("Ativo atualizado com sucesso!", "success")
            return redirect(url_for("listar_ativos"))

        return render_template(
            "form_ativo.html",
            pagina="ativos",
            titulo="Editar Ativo",
            subtitulo="Altere as informações do ativo selecionado",
            ativo=ativo
        )
        
    @app.route("/ativos/<int:id>/excluir")
    def excluir_ativo(id):

        ativo = Ativo.query.get_or_404(id)

        db.session.delete(ativo)
        db.session.commit()

        flash("Ativo excluído com sucesso!", "success")
        return redirect(url_for("listar_ativos"))