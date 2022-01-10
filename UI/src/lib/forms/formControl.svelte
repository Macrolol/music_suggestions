<script>

export let props;



export let value = '';

let inputValue = '';

$: value = inputValue;

</script>

<style>
    .input-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
</style>

<div class=input-group>
<label for={props.id}>{props.label}</label>
	<input {...props} bind:value={inputValue}/> 
</div>