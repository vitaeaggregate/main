<script lang="ts">
	import "../app.css";

	import { logout } from "$lib/utils";
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { account } from "$lib/store";
	import { firebaseAuth } from "$lib/configs/firebase";
	import { SvelteToast } from '@zerodevx/svelte-toast'

	const options = {}
	
	onMount(() => {
		const accountSessionStorage = sessionStorage.getItem("account") || null;
		if (accountSessionStorage) account.set(JSON.parse(accountSessionStorage));
		else account.set(null);
	});

	const handleLogout = async () => {
		await firebaseAuth.signOut()
		account.set(null);
		sessionStorage.removeItem("token");
		logout();
	};
</script>

<SvelteToast {options}/>
<div class="flex w-full flex-col gap-10">
	<header class="flex justify-center bg-slate-200 p-5 px-10">
	  <div class="container">
		<div class="flex justify-between">
			{#if $account}
		  <nav class="flex justify-start gap-10">
			<a href="/my/page">My Page</a>
			<a href="/my/dashboard">Dashboard</a>
			<a href="/community">Community</a>
		  </nav>
		{:else}
		<nav></nav>
		  {/if}
		  {#if !$account}
			<button on:click={() => goto("/login/test")}>Login</button>
		  {:else}
			<button on:click={handleLogout}>Logout</button>
		  {/if}
		</div>
	  </div>
	</header>

	<main class="flex justify-center relative">
	  <div class="container px-10">
		<slot />
	  </div>
	</main>
  </div>
