<script>
    import Message from "$lib/message.svelte";    
    import { messages } from "$lib/messages.js";

    console.debug($messages);
     

</script>

{#if $messages }
    {#each $messages as message (message)}
        <Message type={message.type}>
            <p>{message.text}</p>
        </Message>
    {/each}
{/if}