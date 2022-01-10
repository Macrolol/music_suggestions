<script>
import { goto } from '$app/navigation';
import { addMessage } from '$lib/messaging/messages.js';


    let input;
    let req = "";

    const submit = () => {
       
    };

</script>



<svelte:head>
    <title>Welcome</title>
</svelte:head>
<h1>Welcome to Music Suggestions</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<input type="text" bind:value={input}/>
<p> {#await req}
    waiting for response
{:then response } 
    {JSON.stringify(response)}
{/await} </p>

<button on:click={submit}>Submit</button>
