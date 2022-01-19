<script context=module>
	import { browser } from '$app/env';
    import { addMessage } from '$lib/messaging/messages.js';
	export async function load({session}) {
		if (! 'user' in session) { 
			addMessage('error','You must be logged in to log out.');
			return {
			redirect: '/login',
			status : 301
			};
		}
		return {}
	};
</script>

<script>
	import { session } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { postRequest } from '$lib/requests.js';

	onMount(() => {
		postRequest({ path: 'auth/logout' }).then(() => {	
			goto('/', {replaceState: true}).then( () => {
				$session.user = null;
				addMessage('success','You have been logged out.');
			});
		})
		.catch(err => {
				console.log(err);
				goto('/', {replaceState: true}).then( () => {
				addMessage('danger','There was a problem logging you out.');
			});
		});
	});

</script>
<p> Logging Out </p>