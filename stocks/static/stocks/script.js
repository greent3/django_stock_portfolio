

function activateHeader(page){
    document.querySelector(page).classList.add("active");
}



function changeProfitColor(){
    profits = document.querySelectorAll(".profit");
    Array.from(profits).forEach(function(profit){
        
        let newString = String(profit.innerHTML).substring(0, profit.innerHTML.length -3);
        let newnum = parseInt(newString)
        if(newnum > 0){
            profit.classList.add("green")
        }
        else if (newnum < 0){
            profit.classList.add("red")
        }
    });
        
            

}