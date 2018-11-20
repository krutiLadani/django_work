function validateForm(){
	var validate=true;
	var name = document.forms["contactForm"]["name"].value;
	var email = document.forms["contactForm"]["email"].value;
	var address = document.forms["contactForm"]["address"].value;
	var country = document.forms["contactForm"]["country"].value;
	var contactno = document.forms["contactForm"]["contactno"].value;
	var gender = document.forms["contactForm"]["gender"].value;
	var uploadFile = document.forms["contactForm"]["uploadFile"].value;
	var verification = document.forms["contactForm"]["verification"].checked;

	if (name == "") {
		document.getElementById('valMsgName').innerHTML = "Please Enter Name";
		validate=false;		
	}
	else if (!(/^[A-Z a-z]+$/.test(name)) || !(/\S/.test(name))) {
		document.getElementById('valMsgName').innerHTML = "Please Enter Valid name";
		validate=false;		
	}
	else{
		document.getElementById('valMsgName').innerHTML = "";
	}

	if (email == "") {
		document.getElementById('valMsgEmail').innerHTML = "Please Enter E-mail Address";
		validate=false;		
	}	
	else if (!(/\S+@\S+\.\S+/.test(email))) {
		document.getElementById('valMsgEmail').innerHTML = "Please Enter Valid Email Address";
		validate=false;		
	}
	else{
		document.getElementById('valMsgEmail').innerHTML = "";
	}

	if (address == null || !(/\S/.test(address))) {
		document.getElementById('valMsgAddress').innerHTML = "Please Enter Address";
		validate=false;		
	}	
	else{
		document.getElementById('valMsgAddress').innerHTML = "";
	}

	if (country == "") {
		document.getElementById('valMsgCountry').innerHTML = "Please Select Country";
		validate=false;		
	}	
	else{
		document.getElementById('valMsgCountry').innerHTML = "";
	}

	if (contactno == "") {
		document.getElementById('valMsgContactNo').innerHTML = "Please Enter Contact No";
		validate=false;		
	}	
	else if (!(/^\d{10}$/.test(contactno))) {
		document.getElementById('valMsgContactNo').innerHTML = "Please Enter valid Contact";
		validate=false;		
	}	
	else{
		document.getElementById('valMsgContactNo').innerHTML = "";
	}

	if (gender == "") {
		document.getElementById('valMsgGender').innerHTML = "Please Choose Your Gender";
		validate=false;		
	}	
	else{
		document.getElementById('valMsgGender').innerHTML = "";
	}

	if (uploadFile == "") {
		document.getElementById('valMsgFile').innerHTML = "Please Choose File to Upload";
		validate=false;		
	}	
	else{
		document.getElementById('valMsgFile').innerHTML = "";
	}
	if (!verification) {
		document.getElementById('valMsgVerification').innerHTML = "Please Verify Your Self First";
		validate=false;		
	}
	else
	{
		document.getElementById('valMsgVerification').innerHTML = "";		
	}

	if (validate==true) {
		return true;
	}
	else
	{
		return false;
	}
}