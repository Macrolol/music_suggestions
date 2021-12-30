<script context=module>
    import { addMessage } from '$lib/messages/messages.js';
	export async function load({page, fetch, session, stuff}) {
		if ('user' in session) {
            session.user = null;
            addMessage('success','You have been logged out.');
			return {
				redirect: '/',
				status : 301
			};
		}
		return {};
	}
</script>