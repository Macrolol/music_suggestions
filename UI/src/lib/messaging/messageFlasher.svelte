<script>
    import MessageDisplayer from "$lib/messaging/messageDisplayer.svelte";    
    import { messages } from "$lib/messaging/messages.js";

    //console.debug($messages);
    const closeMessage = (e) => {
        //console.debug("closeMessage: ", e);
        for (const [mes, i] of $messages.entries()) {
            if (mes.created === e.messageCreated) {
                $messages.splice(i, 1);
                $messages = $messages;
                break;
            }
        }
    };

</script>
<style>
    .messageContainer{
        padding : 2px;
        margin-top: 10px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

</style>


<div class=messageContainer>
{#if $messages }
    {#each $messages as message (message)}
        <MessageDisplayer {message} on:click={closeMessage}/>
    {/each}
{/if}
</div>