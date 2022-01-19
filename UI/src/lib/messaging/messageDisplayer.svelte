<script>
import { createEventDispatcher } from "svelte/internal";

export let message;


const dispatch = createEventDispatcher();

const clicked = (e) => {
    dispatch("click", {
        messageCreated : message.created, 
    });
}; 

</script>

<style>
    .message-box{
        width : 98%;
        margin-bottom: 10px;
        padding : 1px 10px;
        border-radius: 10px;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: center;
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
    .closeButton{
        display : flex;
        align-self: stretch;
        cursor: pointer;
    }
    button{
        cursor: pointer;
        background-color: transparent;
        padding: 0;
        margin: 0;
        border: none;
        border-radius: 30px;
    }
</style>

<div class="{message.type ? message.type : 'success' } message-box">
    <div class=messageText name={message.type + "-message"} >
        <slot>
            <p>{message.text}</p>
        </slot>
    </div>
    <div class=closeButton><button on:click|preventDefault={clicked}>X</button> </div>
   
</div>