let valores = [8, 1, 7, 4, 2, 9];

for(var c = 0; c < valores.length; c++){
    console.log('Posição ' + c + ' tem o número ' + valores[c]);
}
console.log('//////////////////////////////');
//novo modo de fazer 
for(let c in valores){
    console.log('Posição ' + c + ' tem o número ' + valores[c]);
} 
console.log('//////////////////////////////');
var pos = valores.indexOf(7);
if (pos == -1){
    console.log('Valor não encontrado!');
}else{
    console.log('Valor na posição ' + pos);
}