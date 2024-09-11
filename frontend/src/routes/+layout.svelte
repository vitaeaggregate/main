<script lang="ts">
	import "../app.css";

	import { logout } from "$lib/utils";
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { account, commentNotifications } from "$lib/store";
	import { getUnreadNotifications } from "$lib/api/commentNotification";
	import BellIcon from "$lib/icons/bell-icon.svelte";
	import type CommentNotification from "$lib/interfaces/member/CommentNotification";

	onMount(() => {
		const accountSessionStorage = sessionStorage.getItem("account") || null;
		if (accountSessionStorage) account.set(JSON.parse(accountSessionStorage));
		else account.set(null);
	});

	const loadUnreadNotifications = async () => {
		if (!$account) return;
		const results: CommentNotification[] = await getUnreadNotifications($account.id);
		if (results) commentNotifications.set(results);
	};

	$: if ($account) {
		setInterval(loadUnreadNotifications, 2000);
	}
</script>

<div class="flex w-full flex-col gap-10 grow">
	<header class="flex justify-center bg-slate-200 p-5 px-10">
		<div class="container">
			<div class="flex justify-between">
				{#if $account}
					<nav class="flex justify-start gap-10">
						<div class="flex items-center gap-3">
							<a href="/my/page">My Page </a>
							<a href="/my/notifications" class="relative size-5 rounded-full"
								><BellIcon></BellIcon>
								{#if $commentNotifications && $commentNotifications.length}
									<span
										class="absolute -right-4 -top-3 rounded-full bg-slate-100 px-2 text-sm ring-1"
										>{$commentNotifications.length}</span
									>
								{/if}
							</a>
						</div>
						<a href="/my/dashboard">Dashboard</a>
						<a href="/community">Community</a>
					</nav>
				{:else}
					<nav></nav>
				{/if}
				{#if !$account}
					<button on:click={() => goto("/login/test")}>Login</button>
				{:else}
					<button on:click={logout}>Logout</button>
				{/if}
			</div>
		</div>
	</header>

	<main class="relative flex justify-center">
		<div class="container px-10">
			<slot />
		</div>
	</main>
</div>
