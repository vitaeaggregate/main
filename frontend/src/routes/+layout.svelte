<script lang="ts">
	import "../app.css";

	import { logout } from "$lib/utils";
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { account } from "$lib/store";
	import TimeAgo from "javascript-time-ago";
	import { getUnreadNotifications, readNotification } from "$lib/api/commentNotification";
	import BellIcon from "$lib/icons/bell-icon.svelte";
	import type CommentNotification from "$lib/interfaces/member/CommentNotification";
	import CommentNotificationView from "$lib/components/CommentNotificationView.svelte";
	import Button from "$lib/components/Button.svelte";
	import en from "javascript-time-ago/locale/en";


	let commentNotifications: CommentNotification[] | null = null;

	let isNotificationsViewHidden = true;

	onMount(() => {
		TimeAgo.addDefaultLocale(en);
		const accountSessionStorage = sessionStorage.getItem("account") || null;
		if (accountSessionStorage) account.set(JSON.parse(accountSessionStorage));
		else account.set(null);
		loadUnreadNotifications();
		setInterval(loadUnreadNotifications, 5000);
	});

	const loadUnreadNotifications = async () => {
		if (!$account) return;
		const results: CommentNotification[] = await getUnreadNotifications($account.id);
		if (results) commentNotifications = results;
	};

	const handleNotificationsView = () => {
		if (!$account) return;
		if (isNotificationsViewHidden) isNotificationsViewHidden = false;
		else {
			isNotificationsViewHidden = true;
			if (commentNotifications && commentNotifications.length) {
				commentNotifications.forEach(
					async (commentNotification) => await readNotification($account.id, commentNotification.id)
				);
			}
			commentNotifications = null;
		}
	};
</script>

<div class="z-10 flex w-full flex-col gap-10">
	<header class="flex justify-center bg-slate-200 p-5 px-10">
		<div class="container">
			<div class="flex justify-between">
				{#if $account}
					<nav class="relative flex justify-start gap-10">
						<div class="flex items-center gap-3">
							<a href="/my/page">My Page </a>
							<Button on:click={handleNotificationsView}>
								<div class="relative size-6">
									<BellIcon></BellIcon>
									{#if commentNotifications && commentNotifications.length}
										<span
											class="absolute -right-3 -top-2 rounded-full bg-slate-100 px-2 text-sm ring-1"
										>
											{commentNotifications.length}
										</span>
									{/if}
								</div>
							</Button>
						</div>
						<a href="/community">Community</a>
						{#if !isNotificationsViewHidden}
							<div class="item absolute top-full rounded-lg border-2 bg-slate-50 p-5">
								<h3>
									<a on:click={handleNotificationsView} href="/my/notifications">Notifications</a>
								</h3>
								{#if commentNotifications && commentNotifications.length}
									<div role="button" aria-hidden="true" on:click={handleNotificationsView}>
										<CommentNotificationView value={commentNotifications} type="dropdown"
										></CommentNotificationView>
									</div>
								{:else}
									<p>Nothing new for now.</p>
								{/if}
							</div>
						{/if}
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

	<main class="relative -z-10 flex justify-center">
		<div class="container px-10">
			<slot />
		</div>
	</main>
</div>
