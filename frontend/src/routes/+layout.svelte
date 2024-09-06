<script lang="ts">
	import "../app.css";

	import { logout } from "$lib/utils";
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { account } from "$lib/store";

	onMount(() => {
		const accountSessionStorage = sessionStorage.getItem("account") || null;
		if (accountSessionStorage) account.set(JSON.parse(accountSessionStorage));
		else account.set(null);
	});

	const handleLogout = async () => {
		account.set(null);
		await logout();
	};
</script>

<div class="flex w-full flex-col gap-10">
	<header class="flex justify-center bg-slate-200 p-5 px-10">
		<div class="container">
			<div class="flex justify-between">
				<nav class="flex justify-start gap-10 uppercase">
					<a href="/">home</a>
					<a href="/my/page">my page</a>
					<a href="/my/dashboard">dashboard</a>
					<a href="/community">community</a>
				</nav>
				{#if !$account}
					<button on:click={() => goto("/login/test")}>Login</button>
				{:else}
					<button on:click={handleLogout}>Logout</button>
				{/if}
			</div>
		</div>
	</header>
	<main class="flex justify-center">
		<div class="container px-10">
			<slot />
		</div>
	</main>
</div>
