<script>
	import { goto } from "$app/navigation";
	import { account } from "$lib/store";
</script>


<div class="float-left">
	<span class="[writing-mode:vertical-rl] text-8xl h-8">Vitae Aggregate</span>
</div>

<main class="flex flex-col items-center justify-center h-screen ">
	{#if !$account}
	  <button class="w-20 h-10 bg-slate-200 mt-5" on:click={() => goto("/login/test")}>Login</button>
	{:else}
	  <button class="w-28 h-10 bg-slate-200 mt-5" on:click={() => goto("/my/dashboard")}>Dashboard</button>
	{/if}
  </main>
