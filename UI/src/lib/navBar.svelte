<script>
    import { session } from '$app/stores';



</script>
<nav id=mainNav>
    <a sveltekit:prefetch href="/">Home</a>
    <a sveltekit:prefetch href="/about">About</a>
    <a sveltekit:prefetch href="/suggest">Suggest</a>
    {#if $session.user}
        <a sveltekit:prefetch href="/profile">Profile</a>
        <a sveltekit:prefetch href="/logout">Logout</a>
    {:else}
        <a sveltekit:prefetch href="/login">Login</a> 
    {/if}
</nav>