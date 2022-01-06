<script context=module>
    import { addMessage } from '$lib/messaging/messages.js';
	export async function load({page, fetch, session, stuff}) {
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
	import { getRequest } from '$lib/requests.js';

	onMount(() => {
		getRequest({ path: 'auth/logout' }).then(() => {
			$session.user = null;
			addMessage('success','You have been logged out.');
			goto('/', {replaceState: true});
		});
	});

</script>
<p> Logging Out </p>