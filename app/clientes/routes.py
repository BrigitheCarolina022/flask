from flask import render_template, redirect, flash 
from app.clientes import clientes
import app
from .forms import NewClientesForm, EditClientesFrom


@clientes.route('/create', methods = ['GET', 'POST'])

def crear():
    p = app.models.Cliente()
    form = NewClientesForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        #subir imagen a carpeta / imagenes
        flash("clientes registrado exitosamente")
        return redirect ('/clientes/listar')
    return render_template('new.html',
                           form = form)


@clientes.route('/listar')
def listar():
    #selecionar los clientes
    clientes = app.models.Cliente.query.all()
    return render_template ("list.html", 
                            clientes = clientes)

    
@clientes.route('/editar/<id>',
                 methods = ['GET', 'POST'])
def editar(id):
    p = app.models.Cliente.query.get(id)
    form = EditClientesFrom(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente actualizado')
        return redirect('/Cliente/listar')
    return render_template('new.html', 
                           form=form)


@clientes.route('/eliminar/<id>')
def eliminar(id):
    p = app.models.Cliente.query.get(id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('cliente eliminado')
    return redirect('/cliente/listar')
