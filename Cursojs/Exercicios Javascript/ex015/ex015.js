function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.length == 0 || fano.value > ano){
        window.alert('ERRO!')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - fano.value 
        res.innerHTML = 'Idade calculada: ' + idade
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked){
            genero = 'Homem'
            if (idade >= 0 && idade < 10){
                //criança
                img.setAttribute('src', 'foto-criança-m.jpg')
            } else if (idade < 21){
                //jovem
                img.setAttribute('src', 'foto-jovem-m.jpg')
            } else if (idade < 50){
                //adulto
                img.setAttribute('src', 'foto-adulto-m.jpg')
            } else {
                //idoso
                img.setAttribute('src', 'foto-idoso-m.jpg')
            }
        } else if (fsex[1].checked){
            genero = 'mulher'
            if (idade >= 0 && idade < 10){
                //criança
                img.setAttribute('src', 'foto-criança-f.jpg')
            } else if (idade < 21){
                //jovem
                img.setAttribute('src', 'foto-jovem-f.jpg')
            } else if (idade < 50){
                //adulto
                img.setAttribute('src', 'foto-adulto-f.jpg')
            } else {
                //idoso
                img.setAttribute('src', 'foto-idoso-f.jpg')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = 'Detectamos ' + genero + ' com ' + idade + ' anos.'
        res.appendChild(img)
    } 
}