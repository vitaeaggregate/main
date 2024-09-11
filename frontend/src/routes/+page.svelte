<script>
	import { goto } from "$app/navigation";
	import { account } from "$lib/store";
	import Logo from "$lib/Logo.png";
  </script>
  
  <main class="flex md:flex-row flex-col items-center px-10">
	<div class="">
	  <h1 class="text-4xl font-bold">Vitae Aggregate</h1>
  
	  {#if !$account}
		<button class="w-20 h-10 bg-slate-200 mt-5" on:click={() => goto("/login/test")}>Login</button>
	  {:else}
		<button class="w-28 h-10 bg-slate-200 mt-5" on:click={() => goto("/my/page")}>My Page</button>
	  {/if}
	</div>
  
	<div class="flex justify-center mt-4 md:mt-8 md:order-first">
	  <img src="{Logo}" alt="Logo" class="" />
	</div>
  </main>