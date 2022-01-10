
<script>
import {createEventDispatcher} from 'svelte';

export let props;


const dispatch = createEventDispatcher(); 

const handleClick = (event) => {
    dispatch('click', event);    
}
</script>

<style>
button {
    margin-bottom: 10px;
}
</style>




<button type={props.type}  on:click|preventDefault={handleClick}>
		{props.value}
</button>