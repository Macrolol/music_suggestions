<script>
import { createEventDispatcher } from "svelte/internal";

export let message;


const dispatch = createEventDispatcher();

const clicked = (e) => {
    dispatch("click", {
        messageId : message.id, 
    });
}; 

</script>

<style>
    .message-box{
        margin-bottom: 10px;
        padding : 5px;
        border-radius: 5px;
    }
    .danger{
        background-color: #f2dede;
        border-color: #ebccd1;
        color: #a94442;
    }
    .success{
        background-color: #dff0d8;
        border-color: #d6e9c6;
        color: #3c763d;
    }
    .info{
        background-color: #d9edf7;
        border-color: #bce8f1;
        color: #31708f;
    }
    .warning{
        background-color: #fcf8e3;
        border-color: #faebcc;
        color: #8a6d3b;
    }
</style>

<div class="{type ? type : 'success' } message-box">
    <slot>
    </slot>
    <button on:click|preventDefault={clicked}>X</button>
</div>