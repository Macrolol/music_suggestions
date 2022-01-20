<script>
import { createEventDispatcher } from 'svelte';



const dispatch = createEventDispatcher();

const formSubmitted = () =>{
    dispatch('submit', inputs);
}

</script>

<form on:submit={formSubmitted}>
    <div class="inputs-container">
        <slot>Input Fields</slot>
    </div>
</form>

<style>
    .inputs-container {
        display: flex;
        flex-direction: column;
        justify-content: left;
    }
</style>
