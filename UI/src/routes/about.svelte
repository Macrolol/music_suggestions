<script>
import {session} from '$app/stores';




</script>



<svelte:head>
    <title>About</title>
</svelte:head>

<h1>About</h1>
{#if $session.messages && $session.messages.length > 0}
    <p> Session content: {JSON.stringify($session.messages)}<p>
{/if}
<p>This is the about section</p>