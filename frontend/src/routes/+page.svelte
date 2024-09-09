<script>
	import { goto } from "$app/navigation";

	import { account } from "$lib/store";
</script>

<main>
	<h1>Vitae Aggregate</h1>

	{#if !$account}<button class="mt-5 h-10 w-20 bg-slate-200" on:click={() => goto("/login/test")}
			>Login</button
		>{:else}
		<button class="mt-5 h-10 w-28 bg-slate-200" on:click={() => goto("/my/dashboard")}
			>Dashboard
		</button>{/if}
</main>
