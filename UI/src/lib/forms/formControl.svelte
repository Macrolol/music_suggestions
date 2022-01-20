<script>

export let props;
export let value = '';
const onInput = (e) => {
  value = e.target.value; 
};

</script>

<style>
    .input-group {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
</style>

<div class=input-group>
    {#if props.label}
        <label for={props.id}>{props.label}</label>
    {/if}
    <input {...props} {value} on:input={onInput}/> 
</div>