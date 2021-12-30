

<script>
 
    import MessageFlasher from "$lib/messaging/messageFlasher.svelte";
    import NavBar from "$lib/navBar.svelte";
    import { session } from "$app/stores"
   
    

    

</script>
<style>
    .bar {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }
    .container {
        width : 100%;
        display: flex;
        flex-direction: row;
        margin-top: 20px; 
    }
    .left {
        box-sizing: border-box;
        width: 50%;
        height: 100%;
    }
    .right {
        box-sizing: border-box;
        width: 20%;
        height: 100%;
        margin-right: 0px;
        padding: 0px 20px;
        justify-self: right; 
    }

</style>

<div class=bar>
<NavBar/>
{#if $session.user}
<h3>Logged in as: {$session.user.tag}</h3>
{/if}
</div>
<div class=container>
    <div class=left>
        <slot></slot>
    </div>
        
    <div class=right>
    <MessageFlasher/>
    </div>
    

</div>