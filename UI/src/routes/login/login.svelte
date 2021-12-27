<script context="module">

	export async function load({page, fetch, session, stuff}) {
		if ('user' in session) {
			
			return {
				redirect: '/',
				status : 301
			}
		}
	}


</script>




<script>
	import { validateEmail } from '$lib/validateEmail.js';
	import { goto, prefetch } from '$app/navigation';
	
	
	const inputs = {
		email_address : null,
		password : null
	};
	
	let loginSuccess = false;
	let logging_in;
	
	const tryLogin = async () => {
		const loginResponse = fetch("/post/data/here", {
  			method: "POST",
  			headers: {'Content-Type': 'application/json'}, 
 			body: JSON.stringify(inputs)
		});
		return await loginAttempt.json();
	}

	const handleLogin = (event) => {
		if (validateEmail(inputs.email_address) && inputs.password.length > 0 ){
			
	}
</script>

<style>
  .content {
    display: grid;
    grid-template-columns: 20% 80%;
    grid-column-gap: 10px;
		margin : 20px;
  }
</style>
<h3>
		Login
</h3>

<form class='content'>
	<label for="email_address">Email Address</label>
	<input name="email_address" id="email_address" type="text" bind:value={inputs.email_address}/>
	<label for="password">Password</label>
	<input name="password" id="pwassword" type="password" bind:value={inputs.password}/>
</form>
<button on:click|preventDefault={handleLogin}>
		Login
</button>

	

<p>
	Email Address is: {inputs.email_address} <br/>
	Password is: {inputs.password}
</p>
<p>
	Login successfull? : {loginSuccess}
</p>