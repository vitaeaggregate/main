<script>
	import { goto } from "$app/navigation";
	import { account } from "$lib/store";
</script>

<main class="grid grid-cols-3 ">
<span class="[writing-mode:vertical-lr] text-7xl">Vitae Aggregate</span>

{#if !$account}<button class="w-20 h-10  bg-slate-200 mt-5" on:click={() => goto("/login/test")}>Login</button>{:else}
	<button class="w-28 h-10 bg-slate-200 mt-5" on:click={() => goto("/my/dashboard")}>Dashboard
	</button>{/if}

</main>
