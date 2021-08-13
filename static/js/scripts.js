    function sumValues(){
    var myval1 = document.getElementById('value1').value;   
    var myval2 = document.getElementById('value2').value;
    var myval3 = document.getElementById('value3').value;
    var myval4 = document.getElementById('value4').value;
    

    // if((myval1 || myval2 || myval3 ||myval4) >5){
    //     alert('Enter valid values')
    //     return false
    // }
    // else{
         mytotal = parseInt(myval1) +parseInt(myval2)+ parseInt(myval3) + parseInt(myval4);
        // if(!isNaN(mytotal)){
        //     alert(mytotal)
        //     document.getElementById('totals').innerHTML = mytotal
        // }
        // else{
        //     alert("Enter values in the required fields")
        // }



        if(((parseInt(myval1))|| (parseInt(myval2))||(parseInt(myval3))||(parseInt(myval4)))< 5){
            alert("Enter valid values")
            return false;
        }

    }
//}
