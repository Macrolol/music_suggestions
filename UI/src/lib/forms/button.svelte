
<script>
import {createEventDispatcher} from 'svelte';

export let props;


const dispatch = createEventDispatcher(); 

const handleClick = (event) => {
    dispatch('click', event);    
}

let value = props.value;
let type = props.type;
delete props.type;
delete props.value;

</script>

<style>
button {
    margin-bottom: 10px;
}
</style>




<button type={type} {...props} on:click|preventDefault={handleClick}>
		{value}
</button>