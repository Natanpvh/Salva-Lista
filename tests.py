"""jQuery para criar multiplos inputs"""
#$("#teste").click(function () {
    #$("#col-box").append('<input type="text" name="nome" maxlength="100" >');
#});
"""Salva multiplos codigos em uma só linha separado por virgula"""
if form.is_valid():
    # model que vai salvar os valores
    categoria_valor = Categoria()
    # separador
    s = ","
    # dados dos imputs
    valor_nome = request.POST.getlist('nome')
    # valor_nome = ['122', '555', '77']
    cod_pecas = s.join(valor_nome)
    # cod_pecas = 122,555,77
    categoria_valor.nome = cod_pecas
    categoria_valor.save()