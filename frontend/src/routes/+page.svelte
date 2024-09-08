<script>
	import { goto } from "$app/navigation";


	import { account } from "$lib/store";

</script>
<main>
<h1>Vitae Aggregate</h1>

{#if !$account}<button class="w-20 h-10  bg-slate-200 mt-5" on:click={() => goto("/login/test")}>Login</button>{:else}
	<button class="w-28 h-10 bg-slate-200 mt-5" on:click={() => goto("/my/dashboard")}>Dashboard
	</button>{/if}

</main>
