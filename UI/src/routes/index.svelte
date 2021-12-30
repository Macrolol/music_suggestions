<script>
import { goto } from '$app/navigation';
import { addMessage } from '$lib/messaging/messages.js';


    let input;

    const submit = () => {

        addMessage('success', 'this is the message text');
    };

</script>



<svelte:head>
    <title>Welcome</title>
</svelte:head>
<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<input type="text" bind:value={input}/>
<p> {input} </p>
<button on:click={submit}>Submit</button>
