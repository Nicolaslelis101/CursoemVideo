function parimpar(n){
    if (n%2==0){
        return 'Par!';
    }else{
        return 'Impar!';
    }
}

function soma(n1=0, n2=0){
    return n1 + n2;
}

let v = function(x){
    return x*2;
} 

function fatorial(n){
    let fat = 1;
    for(let c = n; c >= 1; c--){
        fat *= c;
    }
    return fat;
} 

console.log('Par ou impar: ' + parimpar(223));
console.log('//////////////');
console.log('Soma: ' + soma(2, 5));
console.log('//////////////');
console.log('Dobro: ' + v(7));
console.log('//////////////');
console.log('Fatorial: ' + fatorial(5));
