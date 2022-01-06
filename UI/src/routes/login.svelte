<script context="module">

	export async function load({ session }) {
		console.log("Login page loaded");
		if (session.user) {
			if (session.user.logging_in){
				session.user.logging_in = false;
			} else {
				addMessage('danger', 'You are already logged in.');
			}
		
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
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';
	import { addMessage} from '$lib/messaging/messages.js'
	import { postRequest } from '$lib/requests.js';
	


	
	const inputs = {
		email_address : null,
		password : null
	};

	// define this here so that the promise from tryLogin
	// can be stored in it, and it can be accessed in the
	// UI for #await block
	let logging_in;
	
	const tryLogin = async () => {
		try{ 
			const loginResponse = await postRequest({
				path: '/auth/login', 
				data: {
					email_address: inputs.email_address,
					password: inputs.password
				}
			});
			return loginResponse;
		} catch (err) {
			console.log(err);
			throw new AuthenticationError();
		}
	
	}

		const handleLogin = async (event) => {
		if (validateEmail(inputs.email_address) && inputs.password.length > 0 ){
			try {

				logging_in = tryLogin();
				console.log(logging_in);
				const { user }  = await logging_in;
				console.log(user);
				console.log("Before Session set");
				user.logging_in = true;
				$session.user =  user;
				addMessage('success', 'Successfully logged in as ' + user.tag);

			} catch(error) {
				if (error instanceof AuthenticationError){
						addMessage('danger', 'Invalid email or password');
						inputs.password = '';
				} else {
					console.log(error);
						addMessage('danger', 'An error occurred');
				}
			}
		} else {
			addMessage('danger', 'Please enter a valid email address');
		}
	};
</script>

<style>
	.container {
		display : flex;
		flex-direction : column;
		justify-content : left;
	}

	.container > * {
		margin-bottom : 0.5rem;
	}

	/*
  	.content {
    	display: grid;
    	grid-template-columns: 20% 80%;
 	   	grid-column-gap: 10px;
		grid-row-gap: 10px;
		margin : 20px;
  	}
  	.login{
		grid-column: 2;
  	}
	*/
</style>
<h3>
		Login
</h3>

<form class='container'>
	<label for="email_address">Email Address</label>
	<input placeholder="Email" name="email_address" id="email_address" type="text" bind:value={inputs.email_address}/>
	<label for="password">Password</label>
	<input placeholder="Password" name="password" id="password" type="password" bind:value={inputs.password}/>

	<button class=login type=submit on:click|preventDefault={handleLogin}>
		Login
	</button>

</form>
	
<button on:click={() => goto('/register')}>
		Register
</button>
