<script context=module>
    import { addMessage } from '$lib/messaging/messages.js';
	export async function load({ session }) {
		if ('user' in session) { 
			addMessage('error','You cannot create a new account while logged in.');
			return {
			redirect: '/login',
			status : 301
			};
		}

		return {};

	};
</script>

<script>
import { postRequest } from '$lib/requests';
import Button from '$lib/forms/button.svelte';
import Form from '$lib/forms/form.svelte';
import FormControl from '$lib/forms/formControl.svelte';
import { goto } from '$app/navigation';
import {validateEmail} from '$lib/validateEmail.js';

const inputs = {
	username : null,
	email : null,
	password : null,
	passwordConfirm : null,
};

const submit = async () => {
	const data = {
		username : inputs.username,
		email_address : inputs.email,
		password : inputs.password
	};
	console.log(data);
	if (data.password !== inputs.passwordConfirm) {
		addMessage('danger','Passwords do not match.');
		return;
	}
	if (data.password.length < 8) {
		addMessage('danger','Password must be at least 8 characters.');
		return;
	}
	if (!validateEmail(data.email_address)) {
		addMessage('danger','Invalid email address.');
		inputs.email = '';
		return;
	}


	postRequest({path : '/auth/register', data}).then(()=> {
		addMessage('success','Account created. You may now log in.');
		goto('/login');
	}).catch(err => {
		console.log(err);
		addMessage('danger',err.message);
	});

};	


</script>

<Form>

	<FormControl props={{
		label : 'Username',
		name : 'username',
		type : 'text',
		placeholder : 'Username'
	}}
	bind:value={inputs.username}
	/>

	<FormControl props={{
		label : 'Email',
		name : 'email',
		type : 'email',
		placeholder : 'Email'
	}}
	bind:value={inputs.email}
	/>

	<FormControl props={{
		label : 'Password',
		name : 'password',
		type : 'password',
		placeholder : 'Password'
	}}
	bind:value={inputs.password}
	/>
		
	<FormControl props={{
		label : 'Confirm Password',
		name : 'passwordConfirm',
		type : 'password',
		placeholder : 'Confirm Password'
	}}
	bind:value={inputs.passwordConfirm}
	/>

	<Button props={{
		label : 'Submit',
		type : 'submit',
		value : 'Register',
	}}
	on:click={submit}
	/>

	<button type="submit" class="submit">Submit</button>	

</Form>