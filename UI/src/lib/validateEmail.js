const reValidEmail = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ 

// this function returns true if potentialAddress is a valid 
// email address otherwise returns false 
export const validateEmail = (potentialAddress) => {
	let lowercaseString = String(potentialAddress).toLowerCase();
	let matchResult = lowercaseString.match(reValidEmail);
	console.log(`match result : ${matchResult}`);
	return !!matchResult ;
};