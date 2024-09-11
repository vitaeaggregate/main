<script lang="ts">
	import { getAllNotifications, readNotification } from "$lib/api/commentNotification";
	import { account, checkAccountAndRedirect } from "$lib/store";
	import CommentNotificationComponent from "$lib/components/CommentNotification.svelte";
	import type CommentNotification from "$lib/interfaces/member/CommentNotification";

	let commentNotifications: CommentNotification[] | null = null;

	const loadPage = async () => {
		if (!$account) return;

		commentNotifications = await getAllNotifications($account.id);

		if (!commentNotifications) return;

		for (const commentNotification of commentNotifications) {
			if (commentNotification.is_read === false) {
				commentNotification.is_read = true;
				readNotification($account.id, commentNotification.id);
			}
		}
	};

	checkAccountAndRedirect(loadPage);

	$: if ($account) loadPage;
</script>

<section>
	<h1>Notifications</h1>
	<div>
		{#if commentNotifications}
			<CommentNotificationComponent value={commentNotifications}></CommentNotificationComponent>
		{/if}
	</div>
</section>
