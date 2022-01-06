<script context=module>
    import { addMessage } from '$lib/messaging/messages.js';
	export async function load({ session }) {
		if (! 'user' in session) { 
			addMessage('error','You must be logged in to log out.');
			return {
			redirect: '/login',
			status : 301
			};
		}
	};
</script>