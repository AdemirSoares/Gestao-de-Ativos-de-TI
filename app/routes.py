from flask import render_template, request, redirect, url_for, flash

ativos = []
proximo_id = 1

def init_app(app):

    @app.route("/")
    def dashboard():
        return render_template("dashboard.html", pagina="dashboard")

    @app.route("/ativos")
    def listar_ativos():

        pesquisa = request.args.get("pesquisa", "").lower()

        ativos_filtrados = ativos

        if pesquisa:

            ativos_filtrados = []

            for ativo in ativos:

                if (
                    pesquisa in ativo["patrimonio"].lower()
                    or pesquisa in ativo["hostname"].lower()
                    or pesquisa in ativo["tipo"].lower()
                    or pesquisa in ativo["sistema"].lower()
                    or pesquisa in ativo["responsavel"].lower()
                ):

                    ativos_filtrados.append(ativo)

        return render_template(
            "ativos.html",
            pagina="ativos",
            ativos=ativos_filtrados,
            pesquisa=pesquisa,
            total_ativos=len(ativos)
        )

    @app.route("/ativos/novo", methods=["GET", "POST"])
    def novo_ativo():
        global proximo_id
        
        if request.method == "POST":
            ativo = {
                "id": proximo_id,
                "patrimonio": request.form.get("patrimonio"),
                "hostname": request.form.get("hostname"),
                "tipo": request.form.get("tipo"),
                "sistema": request.form.get("sistema"),
                "responsavel": request.form.get("responsavel"),
                "status": request.form.get("status"),
                "localizacao": request.form.get("localizacao"),
            }
            
            if not ativo["patrimonio"] or not ativo["hostname"] or not ativo["tipo"] or ativo["tipo"] == "Selecione...":
                return render_template(
                    "form_ativo.html",
                    pagina="ativos",
                    titulo="Novo Ativo",
                    subtitulo="Cadastre as informações completas do ativo de TI",
                    erro="Preencha os campos obrigatórios: patrimônio, hostname e tipo."
                )

            ativos.append(ativo)
            proximo_id += 1
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
        ativo_encontrado = None

        for ativo in ativos:
            if ativo["id"] == id:
                ativo_encontrado = ativo
                break

        if ativo_encontrado is None:
            flash("Ativo não encontrado.", "danger")
            return redirect(url_for("listar_ativos"))

        if request.method == "POST":
            ativo_encontrado["patrimonio"] = request.form.get("patrimonio")
            ativo_encontrado["hostname"] = request.form.get("hostname")
            ativo_encontrado["tipo"] = request.form.get("tipo")
            ativo_encontrado["sistema"] = request.form.get("sistema")
            ativo_encontrado["responsavel"] = request.form.get("responsavel")
            ativo_encontrado["status"] = request.form.get("status")
            ativo_encontrado["localizacao"] = request.form.get("localizacao")

            flash("Ativo atualizado com sucesso!", "success")
            return redirect(url_for("listar_ativos"))

        return render_template(
            "form_ativo.html",
            pagina="ativos",
            titulo="Editar Ativo",
            subtitulo="Altere as informações do ativo selecionado",
            ativo=ativo_encontrado
        )
        
    @app.route("/ativos/<int:id>/excluir")
    def excluir_ativo(id):
        ativo_encontrado = None

        for ativo in ativos:
            if ativo["id"] == id:
                ativo_encontrado = ativo
                break

        if ativo_encontrado is None:
            flash("Ativo não encontrado.", "danger")
            return redirect(url_for("listar_ativos"))

        ativos.remove(ativo_encontrado)

        flash("Ativo excluído com sucesso!", "success")
        return redirect(url_for("listar_ativos"))