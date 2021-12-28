<script>
import { goto } from '$app/navigation';
import { messages } from '$lib/messages.js';


    let input;

    const submit = () => {

        messages.update((list) => {
            const newMessage = {
                'text': 'some message text',
                'type': 'danger'
            }
            list.push(newMessage);
            return list;
        });
    };

</script>



<svelte:head>
    <title>Welcome</title>
</svelte:head>
<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<input type="text" bind:value={input}/>
<p> {input} </p>
<p> {@debug $messages}</p>
<button on:click={submit}>Submit</button>
