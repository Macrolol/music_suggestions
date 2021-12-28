<script context="module">

	export async function load({page, fetch, session, stuff}) {
		if ('user' in session) {
			
			return {
				redirect: '/',
				status : 301
			};
		}
		return {};
	}


</script>

<script>
	import { AuthenticationError } from '$lib/errors/AuthenticationError.js';
	import { validateEmail } from '$lib/validateEmail.js';
	import { session } from '$lib/stores';
	import { goto, prefetch } from '$app/navigation';
	
	
	const inputs = {
		email_address : null,
		password : null
	};
	let logging_in;
	
	const tryLogin = async () => {
		const loginResponse = await fetch("/api/login", {
  			method: "POST",
  			headers: {'Content-Type': 'application/json'}, 
 			body: JSON.stringify(inputs)
		});
		if (loginResponse.ok) {
			return await loginResponse.json();
		}
		throw new AuthenticationError(loginResponse.status); 
	}

	const handleLogin = (event) => {
		if (validateEmail(inputs.email_address) && inputs.password.length > 0 ){
			logging_in = tryLogin();
			logging_in.then(
				(userDetails) => {
					$session.user = userDetails;	
					goto('/');
				})
				.catch(
				(error) => {
					inputs.password = '';
				}
			);
		}
	};
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
