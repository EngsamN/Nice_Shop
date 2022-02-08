
var updatebtn=document.getElementsByClassName('update-cart')

for(var i =0; i<updatebtn.length;i++){

    updatebtn[i].addEventListener('click',function(){
        var productid=this.dataset.proditals
        var action=this.dataset.action
        console.log('productid',productid,'action',action)
    })
}