
function myFunction() {

  var firstNameInput = document.getElementById("firstName"); //textbox to add first name
  var lastNameInput = document.getElementById("lastName");//textbox to add last name
  var emailInput = document.getElementById("emailInput");//textbox to add email
  
    var table = document.getElementById("myTable");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3).outerHTML="<td><input type='button' value='X' class='delete' onclick='deleteRow(this)'></td>";
  
    //cell4.style = "Button"
  
    //set output text
    cell1.innerHTML = firstNameInput.value;
    cell2.innerHTML = lastNameInput.value;
    cell3.innerHTML = emailInput.value;
    cell4.innerHTML = "X";
  
    //clear input text boxes
    firstNameInput.value = "";
    lastNameInput.value = "";
    emailInput.value = "";



  }  
function deleteRow(r){
  var i = r.parentNode.parentNode.rowIndex;
  document.getElementById("myTable").deleteRow(i);
}
//used for deleting buttons
/*function delete_row(this)
{
 document.getElementById("row"+no+"").outerHTML="";
}*/

function submitForm(){
var TableData = new Array();
    
$('#myTable tr').each(function(row, tr){
    TableData[row]={
        "FirstName" : $(tr).find('td:eq(0)').text()
        , "LastName" :$(tr).find('td:eq(1)').text()
        , "Email" : $(tr).find('td:eq(2)').text()
    }
}); 
	TableData.shift();  // first row is the table header - so remove
	console.log(TableData);
	TableData = JSON.stringify(TableData);
	
	 $.ajax({
    type: "POST",
    url: "/receiptDistribution",
    data: "pTableData=" + TableData,
    success: function(msg){
		window.location.href = msg;

    }
});
	
}