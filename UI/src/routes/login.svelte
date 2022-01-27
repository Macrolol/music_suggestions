<script context="module">

	export async function load({ session }) {
		console.log("Login page loaded");
		if (session.user) {
			addMessage('danger', 'You are already logged in.');
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
	import { postRequest, RequestError } from '$lib/requests.js';
	import FormControl from '$lib/forms/formControl.svelte';
	import Button from '$lib/forms/button.svelte';
	import Form from '$lib/forms/form.svelte';
	
	const inputs = {
		email_address : '',
		password : ''
	};

	// define this here so that the promise from tryLogin
	// can be stored in it, and it can be accessed in the
	// UI for #await block
	let loggingIn;
	
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
			if (err instanceof RequestError || err.name === 'RequestError') {
				if (err.status === 401){
					throw new AuthenticationError('Invalid email or password');
				}
			}
			console.log(err); //debug
			throw err;
		}
	
	}

		const handleLogin = async (event) => {
		if (validateEmail(inputs.email_address)){
			if (inputs.password.length > 0){
				try {
					loggingIn = tryLogin();
					//console.log(loggingIn); //debug
					const { user }  = await loggingIn;
					console.log(user);
					goto('/').then(() => {
						$session.user = user
						addMessage('success', 'Successfully logged in as ' + user.tag);
					});
					

				} catch(error) {
					if (error instanceof AuthenticationError){
							addMessage('danger', 'Invalid email or password');
							inputs.password = '';
					} else {
						console.log(error); // debug
						addMessage('danger', error.message);
					}
				}
			} else {
				addMessage('danger', 'Please enter a password');
			}
		} else {
			addMessage('danger', 'Please enter a valid email address');
			inputs.email_address = '';
		}
	};
</script>

<svelte:head>
	<title>Login</title>
</svelte:head>

<h3>
		Login
</h3>

<Form>
	
	<FormControl props={{
		label: 'Email Address',
		type: 'email',
		name: 'email_address',
		placeholder : 'Email Address',
	}}
	bind:value={inputs.email_address}
	/>

	<FormControl props={{
		label: 'Password',
		type: 'password',
		name: 'password',
		placeholder : 'Password',
	}}
	bind:value={inputs.password}/>


	<Button
	props={{
		id: 'login-button',
		type: 'submit',
		value : 'Login'
	}}
	on:click={handleLogin}/>

	

</Form>
	
<Button
	props={{
		id: 'register-button',
		type: 'button',
		value : 'Register'
	}}
on:click={() => goto('/register')}/>
